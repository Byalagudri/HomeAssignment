import pytest

@pytest.fixture(scope="session")
def default_log_file():
    return "logs/bs_log.txt"

@pytest.fixture(scope="session")
def default_threshold():
    return 25.0