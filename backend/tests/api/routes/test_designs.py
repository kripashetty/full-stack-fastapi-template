import uuid

from fastapi.testclient import TestClient
from sqlmodel import Session

from app import crud
from app.core.config import settings
from app.models import DesignStatus
from tests.utils.design import create_design_with_status, create_random_design
from tests.utils.user import authentication_token_from_email
from tests.utils.utils import random_email


def _superuser_id(db: Session) -> uuid.UUID:
    superuser = crud.get_user_by_email(session=db, email=settings.FIRST_SUPERUSER)
    assert superuser and superuser.id
    return superuser.id


def test_create_design(
    client: TestClient, normal_user_token_headers: dict[str, str]
) -> None:
    data = {"title": "API Gateway Design", "description": "Edge routing proposal"}
    response = client.post(
        f"{settings.API_V1_STR}/designs/",
        headers=normal_user_token_headers,
        json=data,
    )
    assert response.status_code == 201
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert content["status"] == DesignStatus.DRAFT.value
    assert "id" in content
    assert "owner_id" in content


def test_read_design(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    design = create_random_design(db)
    response = client.get(
        f"{settings.API_V1_STR}/designs/{design.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == design.title
    assert content["description"] == design.description
    assert content["id"] == str(design.id)
    assert content["owner_id"] == str(design.owner_id)
    assert content["status"] == design.status.value


def test_read_design_not_found(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/designs/{uuid.uuid4()}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Design not found"


def test_read_design_not_enough_permissions(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    design = create_random_design(db)
    response = client.get(
        f"{settings.API_V1_STR}/designs/{design.id}",
        headers=normal_user_token_headers,
    )
    assert response.status_code == 403
    content = response.json()
    assert content["detail"] == "Not enough permissions"


def test_read_designs_as_engineer(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    create_random_design(db)
    create_random_design(db)
    response = client.get(
        f"{settings.API_V1_STR}/designs/",
        headers=normal_user_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["count"] == 0
    assert content["data"] == []


def test_read_designs_as_superuser(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    create_random_design(db)
    create_random_design(db)
    response = client.get(
        f"{settings.API_V1_STR}/designs/",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert len(content["data"]) >= 2


def test_update_design(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    design = create_random_design(db, owner_id=_superuser_id(db))
    data = {"title": "Updated title", "description": "Updated description"}
    response = client.put(
        f"{settings.API_V1_STR}/designs/{design.id}",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert content["id"] == str(design.id)
    assert content["owner_id"] == str(design.owner_id)


def test_update_design_not_found(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    data = {"title": "Updated title", "description": "Updated description"}
    response = client.put(
        f"{settings.API_V1_STR}/designs/{uuid.uuid4()}",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Design not found"


def test_update_design_not_enough_permissions(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    design = create_random_design(db)
    data = {"title": "Updated title", "description": "Updated description"}
    response = client.put(
        f"{settings.API_V1_STR}/designs/{design.id}",
        headers=normal_user_token_headers,
        json=data,
    )
    assert response.status_code == 403
    content = response.json()
    assert content["detail"] == "Not enough permissions"


def test_update_approved_design(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    design = create_design_with_status(
        db, status=DesignStatus.APPROVED, owner_id=_superuser_id(db)
    )
    data = {"title": "Updated title", "description": "Updated description"}
    response = client.put(
        f"{settings.API_V1_STR}/designs/{design.id}",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 400
    content = response.json()
    assert content["detail"] == "Only draft designs can be modified"


def test_delete_design(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    design = create_random_design(db, owner_id=_superuser_id(db))
    response = client.delete(
        f"{settings.API_V1_STR}/designs/{design.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["message"] == "Design deleted successfully"


def test_delete_design_not_found(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    response = client.delete(
        f"{settings.API_V1_STR}/designs/{uuid.uuid4()}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Design not found"


def test_delete_design_not_enough_permissions(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    design = create_random_design(db)
    response = client.delete(
        f"{settings.API_V1_STR}/designs/{design.id}",
        headers=normal_user_token_headers,
    )
    assert response.status_code == 403
    content = response.json()
    assert content["detail"] == "Not enough permissions"


def test_delete_non_draft_design(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    design = create_design_with_status(
        db, status=DesignStatus.IN_REVIEW, owner_id=_superuser_id(db)
    )
    response = client.delete(
        f"{settings.API_V1_STR}/designs/{design.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 400
    content = response.json()
    assert content["detail"] == "Only draft designs can be modified"


def test_engineer_lists_only_own_designs(
    client: TestClient, db: Session
) -> None:
    email = random_email()
    headers = authentication_token_from_email(client=client, email=email, db=db)
    user = crud.get_user_by_email(session=db, email=email)
    assert user and user.id

    own_design = create_random_design(db, owner_id=user.id)
    create_random_design(db)

    response = client.get(
        f"{settings.API_V1_STR}/designs/",
        headers=headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["count"] == 1
    assert len(content["data"]) == 1
    assert content["data"][0]["id"] == str(own_design.id)
