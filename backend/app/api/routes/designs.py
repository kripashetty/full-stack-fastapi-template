import uuid
from typing import Any

from fastapi import APIRouter, HTTPException, status
from sqlmodel import col, func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import (
    Design,
    DesignCreate,
    DesignPublic,
    DesignsPublic,
    DesignStatus,
    DesignUpdate,
    Message,
)

router = APIRouter(prefix="/designs", tags=["designs"])


def _get_design_or_404(session: SessionDep, design_id: uuid.UUID) -> Design:
    design = session.get(Design, design_id)
    if not design:
        raise HTTPException(status_code=404, detail="Design not found")
    return design


def _assert_can_read(design: Design, current_user: CurrentUser) -> None:
    if not current_user.is_superuser and design.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")


def _assert_can_modify_draft(design: Design, current_user: CurrentUser) -> None:
    if design.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    if design.status != DesignStatus.DRAFT:
        raise HTTPException(
            status_code=400, detail="Only draft designs can be modified"
        )


@router.get("/", response_model=DesignsPublic)
def read_designs(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve designs.
    """
    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Design)
        count = session.exec(count_statement).one()
        statement = (
            select(Design)
            .order_by(col(Design.created_at).desc())
            .offset(skip)
            .limit(limit)
        )
        designs = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(Design)
            .where(Design.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Design)
            .where(Design.owner_id == current_user.id)
            .order_by(col(Design.created_at).desc())
            .offset(skip)
            .limit(limit)
        )
        designs = session.exec(statement).all()

    designs_public = [DesignPublic.model_validate(design) for design in designs]
    return DesignsPublic(data=designs_public, count=count)


@router.get("/{id}", response_model=DesignPublic)
def read_design(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Any:
    """
    Get design by ID.
    """
    design = _get_design_or_404(session, id)
    _assert_can_read(design, current_user)
    return design


@router.post("/", response_model=DesignPublic, status_code=status.HTTP_201_CREATED)
def create_design(
    *, session: SessionDep, current_user: CurrentUser, design_in: DesignCreate
) -> Any:
    """
    Create new design.
    """
    design = Design.model_validate(
        design_in,
        update={"owner_id": current_user.id, "status": DesignStatus.DRAFT},
    )
    session.add(design)
    session.commit()
    session.refresh(design)
    return design


@router.put("/{id}", response_model=DesignPublic)
def update_design(
    *,
    session: SessionDep,
    current_user: CurrentUser,
    id: uuid.UUID,
    design_in: DesignUpdate,
) -> Any:
    """
    Update a draft design.
    """
    design = _get_design_or_404(session, id)
    _assert_can_modify_draft(design, current_user)
    update_dict = design_in.model_dump(exclude_unset=True)
    design.sqlmodel_update(update_dict)
    session.add(design)
    session.commit()
    session.refresh(design)
    return design


@router.delete("/{id}")
def delete_design(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Message:
    """
    Delete a draft design.
    """
    design = _get_design_or_404(session, id)
    _assert_can_modify_draft(design, current_user)
    session.delete(design)
    session.commit()
    return Message(message="Design deleted successfully")
