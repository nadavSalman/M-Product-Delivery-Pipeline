import unittest
from repository.repositories_util import RepositoryFactory
from repository.artifactory import ArtifactoryRepository

class TestRepositoryFactory(unittest.TestCase):

    def setUp(self):
        self.factory = RepositoryFactory()

    def test_create_artifactory_repository(self):
        repository = self.factory.create_repository('artifactory', 'https://artifactory.example.com/repository/my-app-releases')
        self.assertIsInstance(repository, ArtifactoryRepository, "Expected ArtifactoryRepository object")

    def test_invalid_repository_type(self):
        with self.assertRaises(ValueError):
            self.factory.create_repository('invalid_type', 'https://example.com')

if __name__ == '__main__':
    unittest.main()