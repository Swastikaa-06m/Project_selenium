import pytest

from utils.driver_factory import create_driver
from utils.screenshot_helper import capture_screenshot


@pytest.fixture
def driver(request):
    """Create a WebDriver for each test and capture failures."""

    browser = create_driver()

    yield browser

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        capture_screenshot(
            browser,
            f"FAILED_{request.node.name}"
        )

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Store the test result so the driver fixture can detect failures."""

    outcome = yield

    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)