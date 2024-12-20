import pytest
from prefect.testing.standard_test_suites import BlockStandardTestSuite

from prefect_writer.credentials import WriterCredentials


@pytest.mark.parametrize("block", [WriterCredentials])
class TestAllBlocksAdhereToStandards(BlockStandardTestSuite):
    @pytest.fixture
    def block(self, block):
        return block