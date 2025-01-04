from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.project import ProjectCreate, ProjectResponse
from app.api.security.auth import get_current_user, check_admin_role
from app.api.services.project_service import ProjectService

router = APIRouter(prefix="/projects")


@router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(
    project: ProjectCreate, current_user: dict = Depends(check_admin_role)
):
    return await ProjectService.create_project(project, current_user["username"])


@router.get("/", response_model=List[ProjectResponse])
async def get_projects(current_user: dict = Depends(get_current_user)):
    return await ProjectService.get_projects()


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(project_id: str, current_user: dict = Depends(get_current_user)):
    project = await ProjectService.get_project(project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )
    return project


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: str, current_user: dict = Depends(check_admin_role)
):
    deleted = await ProjectService.delete_project(project_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )
