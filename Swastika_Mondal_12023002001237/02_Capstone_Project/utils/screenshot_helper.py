from pathlib import Path
from datetime import datetime


def capture_screenshot(driver, name):
    """Capture a timestamped screenshot in the screenshots folder."""

    screenshot_dir = Path(__file__).resolve().parent.parent / "screenshots"
    screenshot_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = screenshot_dir / f"{name}_{timestamp}.png"

    driver.save_screenshot(str(file_path))

    return file_path