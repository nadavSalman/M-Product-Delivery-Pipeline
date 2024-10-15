from repository.repository_base import RepositoryBase

# Implementation for uploading an artifact into the Artifactory repository.
class ArtifactoryRepository(RepositoryBase):
    def __init__(self, url: str):
        super().__init__('Artifactory', url)

    def publis_artifact(self, artifact_path: str):
        print(f"Artifact: {artifact_path} successfully published to {self.repository_type}: {self.url}")