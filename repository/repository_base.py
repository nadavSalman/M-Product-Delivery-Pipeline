class RepositoryBase:
    def __init__(self,repository_type:str,url:str):
        self.repository_type = repository_type
        self.url = url

    def publis_artifact(self, artifact_path: str):
        pass