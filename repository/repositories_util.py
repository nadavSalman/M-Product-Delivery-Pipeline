from repository.repository_base import RepositoryBase
from repository.artifactory import ArtifactoryRepository
from repository.nexus import NexusRepository
from repository.s3 import S3Repository


class RepositoryFactory:
    def __init__(self):
        # Attribute to hold the mapping of repository types to classes
        self.repository_classes = {
            'artifactory': ArtifactoryRepository,
            'nexus': NexusRepository,
            's3': S3Repository,
        }

    def create_repository(self, repository_type: str, url: str) -> RepositoryBase:

        # Normalize the repository type (case insensitive)
        repo_class = self.repository_classes.get(repository_type.lower())

        if not repo_class:
            raise ValueError(f"Unknown repository type: {repository_type}")

        return repo_class(url)

    # Method to get all supported repository types.
    def get_supported_repository_types(self) -> list:
        return list(self.repository_classes.keys())