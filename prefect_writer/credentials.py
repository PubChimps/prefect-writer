"""Module containing credentials for interacting with Writer"""
from prefect.blocks.core import Block
from pydantic import Field, SecretStr

from writerai import AsyncWriter


class WriterCredentials(Block):
    """
    Credentials block for credential use across Writer tasks and flows.

    Attributes:
        api_key: [Writer API KEY](
            https://dev.writer.com/api-guides/quickstart#generate-a-new-api-key)

    Examples:
        Load stored Writer credentials:
        ```python
        from prefect_writer import WriterCredentials

        writer_credentials = WriterCredentials.load("BLOCK_NAME")
        ```
    """  # noqa

    _block_type_name = "Writer Credentials"

    api_key: SecretStr = Field(
        default=..., title="API Key", description="API key from Writer."
    )

    def get_writer(self):
        """
        Returns api_key for Writer object
        """
        return AsyncWriter(
            api_key=self.api_key.get_secret_value(),
        )
