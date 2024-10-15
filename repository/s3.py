from repository.repository_base import RepositoryBase

# Implementation for uploading an artifact into the Nexus repository.
class S3Repository(RepositoryBase):
    def __init__(self, url: str):
        super().__init__('S3', url)

    def publis_artifact(self, artifact_path: str):
        print(f"Artifact: {artifact_path} successfully published to {self.repository_type}: {self.url}")
