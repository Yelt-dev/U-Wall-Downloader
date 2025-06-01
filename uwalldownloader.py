import os
import requests
from datetime import datetime
from plyer import notification
import time
import json
from dotenv import load_dotenv

load_dotenv()

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
CATEGORY = os.getenv("CATEGORY")
ORIENTATION = "landscape"
WIDTH = 2160
HEIGHT = 1440
DOWNLOAD_FOLDER = os.getenv("DOWNLOAD_FOLDER")
LOG_FILE = "downloaded.json"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Check for internet connection
def has_internet_connection(max_attempts=15, wait=5):
    test_url = "https://google.com"
    for attempt in range(1, max_attempts + 1):
        try:
            print(f"Checking internet connection (Attempt {attempt})...")
            response = requests.get(test_url, timeout=5)
            if response.status_code == 200:
                print("Internet connection confirmed.")
                return True
        except requests.RequestException:
            time.sleep(wait)
    print("No internet connection after multiple attempts.")
    return False

# Load download log
def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

# Save download log
def save_log(log):
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=4)

# Download image
def download_image():
    if not has_internet_connection():
        notification.notify(
            title="No Internet Connection",
            message="Could not download the image. Please check your connection.",
            app_name="Unsplash Downloader",
            timeout=5
        )
        return

    log = load_log()
    file_name = f"{DOWNLOAD_FOLDER}/{datetime.now().strftime('%Y-%m-%d')}.jpg"
    
    if os.path.exists(file_name):
        print("Today's image is already downloaded.")
        return

    url = f"https://api.unsplash.com/photos/random?query={CATEGORY}&orientation={ORIENTATION}&client_id={UNSPLASH_ACCESS_KEY}&w={WIDTH}&h={HEIGHT}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        image_url = data["urls"]["full"]
        image_id = data["id"]

        if image_id in log:
            print("This image has already been downloaded before.")
            return

        img_data = requests.get(image_url).content
        with open(file_name, "wb") as img_file:
            img_file.write(img_data)

        log[image_id] = {
            "file": file_name,
            "date": datetime.now().strftime('%Y-%m-%d'),
            "url": image_url
        }

        save_log(log)

        print(f"Image saved to: {file_name}")

        notification.notify(
            title="Image Downloaded",
            message="A new image from Unsplash has been saved.",
            app_name="Unsplash Downloader",
            timeout=5
        )

    except Exception as e:
        print(f"Error downloading image: {e}")
        notification.notify(
            title="Download Error",
            message=str(e),
            app_name="Unsplash Downloader",
            timeout=5
        )

# Run the script
download_image()
