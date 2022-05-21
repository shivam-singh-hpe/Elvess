import os
import sys
import pytest

root_dir = os.path.dirname(__file__)
sys.path.append(root_dir)
sys.path.append(os.path.join(root_dir, "tests"))


def pytest_addoption(parser):
    parser.addoption(
        "--tvt", action="store", default="type1", help="my option: type1 or type2"
    )
    parser.addoption("--access_key", help="AWS Access Key Id")
    parser.addoption("--access_secret", help="AWS Access Secret Key")
    parser.addoption("--access_role", help="AWS ROLE")
    parser.addoption("--session_token", help="AWS SESSION TOKEN")


@pytest.fixture
def test_vault_token_opt(request):
    return request.config.getoption("--tvt")


@pytest.fixture
def access_key_opt(request):
    return request.config.getoption("--access_key")


@pytest.fixture
def access_secret_opt(request):
    return request.config.getoption("--access_secret")


@pytest.fixture
def access_role_opt(request):
    return request.config.getoption("--access_role")

@pytest.fixture
def session_token_opt(request):
    return request.config.getoption("--session_token")