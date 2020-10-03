import os
from dotenv import load_dotenv
from WebScreenshot import WebScreenshot

def screenshot_url(url):
    screenshotter = WebScreenshot(os.getenv("DRIVER_PATH"))
    uri = screenshotter.get_screenshot_uri(url)

    return uri

if __name__ == "__main__":
    load_dotenv()
    screenshot_url("https://www.example.com/")