import os
import time
from common.config import Config
from common.send_email import send_email
import pytest


def main(env):
    cf = Config()
    report_dir = cf.get_node_value("runtime", "report_dir")
    now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    report_name = os.path.join(report_dir, 'report_' + now + '.html')
    # pytest.main(["-q", "test_cases", "--env", f"{env}", "--html=" + report_name])
    pytest.main(["-q", "test_cases", "--env", f"{env}", f"--alluredir={report_dir}/allure_report"])
    # send_email(report_name)


if __name__ == '__main__':
    main("test")

