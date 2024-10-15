from repository.repository_base import RepositoryBase

# Implementation for uploading an artifact into the S3 repository.
class NexusRepository(RepositoryBase):
    def __init__(self, url: str):
        super().__init__('Nexus', url)

    def publis_artifact(self, artifact_path: str):
        print(f"Artifact: {artifact_path} successfully published to {self.repository_type}: {self.url}")