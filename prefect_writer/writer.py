"""Tasks and flows for prompting Writer models"""

import asyncio
from typing import Dict

from prefect import get_run_logger, task

from prefect_writer.credentials import WriterCredentials


@task(
    name="Prompt Writer model",
    description="Send message to Writer model and get response",
    retries=0,
)
async def prompt_writer_model(
    model_name: str,
    prompt_content: str,
    prompt_role: str,
    writer_credentials: WriterCredentials,
) -> Dict:
    """
    Send message to Writer model and get response.

    Args:
        model_name: The model you would like to use in Writer.
        prompt_content: The prompt you would like to send to Writer.
        prompt_role: The role of the message (e.g. user or assistant).
        writer_credentials: The credentials to authenticate.

    Returns:
        The response from the Writer API.

    Examples:
        Prompt a Writer model in Prefect
    ```python
    import asyncio

    from prefect import flow
    from prefect_writer.credentials import WriterCredentials
    from prefect_writer.writer import prompt_writer_model

    @flow
    async def example_flow():
        writer_credentials = WriterCredentials(
            api_key="my-api-key",
        )
        result = await prompt_writer_model(
            model_name="palmyra-x-004",
            prompt_content="Write a poem about Python",
            prompt_role="user",
            writer_credentials=writer_credentials,
        )

        print(result)
        return result

    asyncio.run(example_flow())
    ```
    """
    if not prompt_content:
        raise ValueError("A prompt must be provided to send to Writer.")
   
    async with writer_credentials.get_writer() as writer_client:
        return await writer_client.chat.chat(
                model=model_name,
                messages=[{"content":prompt_content, "role":prompt_role}],
        )

