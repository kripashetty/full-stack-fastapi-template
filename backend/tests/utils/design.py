import uuid

from sqlmodel import Session

from app import crud
from app.models import Design, DesignCreate, DesignStatus
from tests.utils.user import create_random_user
from tests.utils.utils import random_lower_string


def create_random_design(db: Session, *, owner_id: uuid.UUID | None = None) -> Design:
    if owner_id is None:
        user = create_random_user(db)
        owner_id = user.id
    assert owner_id is not None
    title = random_lower_string()
    description = random_lower_string()
    design_in = DesignCreate(title=title, description=description)
    return crud.create_design(session=db, design_in=design_in, owner_id=owner_id)


def create_design_with_status(
    db: Session, *, status: DesignStatus, owner_id: uuid.UUID | None = None
) -> Design:
    design = create_random_design(db, owner_id=owner_id)
    design.status = status
    db.add(design)
    db.commit()
    db.refresh(design)
    return design
