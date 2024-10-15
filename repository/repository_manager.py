from repository.repository_base import RepositoryBase


class RepositoryManager:
    def __init__(self,repository:RepositoryBase):
        self.repository = repository

    def publis_artifact(self, artifact_path: str):
        self.repository.publis_artifact(artifact_path)