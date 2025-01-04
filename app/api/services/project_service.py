from app.db.models import ProjectModel


class ProjectService:
    @staticmethod
    async def create_project(project_data, created_by):
        return await ProjectModel.create_project(
            project_data.name, project_data.description, created_by
        )

    @staticmethod
    async def get_projects():
        return await ProjectModel.get_projects()

    @staticmethod
    async def get_project(project_id):
        return await ProjectModel.get_project(project_id)

    @staticmethod
    async def delete_project(project_id):
        return await ProjectModel.delete_project(project_id)
