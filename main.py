import time
import os
import pyscreenshot as ImageGrab
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def take_screenshot():
    if not os.path.exists("screenshots"):
        os.mkdir("screenshots")
    print("Taking screenshot...")

    image_name = f"screenshot-{str(datetime.now())}"
    screenshot = ImageGrab.grab()

    image_name = image_name.replace(":", "")
    filepathloc = f"./screenshots/{image_name}.png"

    screenshot.save(filepathloc)

    print("Screenshot taken...")

    return filepathloc

def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(take_screenshot, 'interval', seconds=5)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == '__main__':
    main()
