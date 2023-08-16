"""A Google Cloud Python Pulumi program"""

import pulumi
import pulumi_gcp as gcp


class DockerArtifactRegistry:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def get(self):
        return gcp.artifactregistry.Repository(
            resource_name=self.name,
            description=self.description,
            docker_config=gcp.artifactregistry.RepositoryDockerConfigArgs(
                immutable_tags=False
            ),
            format="DOCKER",
            location="australia-southeast2",
            repository_id=self.name,
        )
