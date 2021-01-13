import pytest

from test_cases.case import Case
from common.data import DataReader

case = Case()
data_reader = DataReader("test_user_data.xls")


# def setup_module(module):
# 	case.set_env(get_env)


@pytest.mark.parametrize("case_data", data_reader.read_excel_data("login"))
def test_login_normal(case_data, env):
	case.set_env(env)
	r = case.run_case(case_data)
	assert r.status_code == 200
	assert r.json()["status"] == 0
	assert case_data[-1] in r.json()["msg"]


if __name__ == '__main__':
	pytest.main(["-v", "--env", "test", "test_user.py"])
