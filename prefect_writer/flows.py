"""This is an example flows module"""
from prefect import flow

from prefect_writer.blocks import WriterBlock
from prefect_writer.tasks import (
    goodbye_prefect_writer,
    hello_prefect_writer,
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    WriterBlock.seed_value_for_example()
    block = WriterBlock.load("sample-block")

    print(hello_prefect_writer())
    print(f"The block's value: {block.value}")
    print(goodbye_prefect_writer())
    return "Done"


if __name__ == "__main__":
    hello_and_goodbye()
