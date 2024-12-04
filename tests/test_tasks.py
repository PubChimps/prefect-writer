from prefect import flow

from prefect_writer.tasks import (
    goodbye_prefect_writer,
    hello_prefect_writer,
)


def test_hello_prefect_writer():
    @flow
    def test_flow():
        return hello_prefect_writer()

    result = test_flow()
    assert result == "Hello, prefect-writer!"


def goodbye_hello_prefect_writer():
    @flow
    def test_flow():
        return goodbye_prefect_writer()

    result = test_flow()
    assert result == "Goodbye, prefect-writer!"
