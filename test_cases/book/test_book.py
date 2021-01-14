import os
import shutil

import pytest

from test_cases.book.base_book_case import BaseBookCase


case = BaseBookCase()


def setup_module():
	pass


@pytest.mark.parametrize("case_data", case.get_runnable_cases())
def test_book(case_data, env):
	case.set_env(env)
	r = case.run_book_case(case_data)
	assert r.status_code == 200
	# assert r.json()["status"] == 0
	# assert r.json()["msg"] in case_data["except_result"]


def teardown_module():
	case.clean()


if __name__ == '__main__':
	file_name = os.path.basename(__file__)
	pytest.main(["-v", "--env", "test", f"{file_name}"])
