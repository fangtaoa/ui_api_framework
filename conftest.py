import pytest


def pytest_addoption(parser):
	parser.addoption(
		"--env", action="store", default="test", help="set env"
	)


@pytest.fixture(scope="session")
def env(request):
	"""获取测试环境参数"""
	return request.config.getoption("--env")
