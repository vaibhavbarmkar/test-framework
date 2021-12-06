from dotenv import load_dotenv
import pytest,pytest_html
from src.common.driver import Driver
import os
from datetime import datetime
import logging
import logging.config


logging.config.fileConfig('./configurations/config.ini')
objectLoadDriver = Driver()
now = datetime.now()
current_time = now.strftime("%d_%m_%Y_%H_%M_%S")


@pytest.fixture(scope="session")
def driver_get(request):
    logging.info("inside driver_get fixture")
    driver = objectLoadDriver.load_driver()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    yield
    driver.close()
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    try :
        outcome = yield
        rep = outcome.get_result()
        if rep.when == 'call' and (rep.failed or rep.skipped):
            driver = objectLoadDriver.get_driver_obj()
            extra = getattr(rep, "extra", [])
            file_name = (rep.nodeid.replace("::","_") + ".png").split("/")[1]
            report_dir = os.getcwd() + os.getenv("REPORTDIR") + current_time + "/"
            if os.path.isdir(report_dir) is False:
                os.mkdir(report_dir)
            filepath = os.path.join(report_dir,file_name)
            driver.get_screenshot_as_file(filepath)
            html = '<div><img src="%s" alt="screenshot" style="width:600px;height:300px;" onclick="window.open(this.src)" align="right"/></div>'  %file_name
            extra.append(pytest_html.extras.html(html))
            rep.extra = extra
    except Exception as e:
        raise e

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    load_dotenv()
    config.option.htmlpath = os.getcwd() + os.getenv("REPORTDIR") + current_time + "/report.html"
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "Github  Suite"


def pytest_runtest_setup(item):
    logging.info("===============")
    logging.info("Starting test case" + item.originalname)


def pytest_runtest_teardown(item):
    logging.info("Completing test case" + item.originalname)
    logging.info("===============")


