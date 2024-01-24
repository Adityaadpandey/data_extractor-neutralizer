import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.options import Options
import time

def download_transcript(youtube_link):
    options = Options()
    options.headless = True  # Set to True if you don't want to see the browser window

    # Provide the directory path where geckodriver is located
    geckodriver_directory = 'C:/Users/adity/test/geckodriver.exe'  # Replace with the actual directory path
    os.environ['PATH'] += os.pathsep + geckodriver_directory

    driver = webdriver.Firefox(options=options)

    try:
        driver.get('https://tactiq.io/tools/youtube-transcript#youtube-form-link')
        time.sleep(2)  # Allow time for the page to load

        # Find the input field and paste the YouTube link
        input_field = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, "yt-2"))
        )

        input_field.send_keys(youtube_link)

        # Submit the form
        input_field.send_keys(Keys.RETURN)

        # Wait for the transcript to load (adjust the sleep duration as needed)
        time.sleep(5)
        try:
            # Find the download button and click it
            download_button = driver.find_element(By.ID, "download")
            download_button.click()
            # Wait for the download to complete (adjust the sleep duration as needed)
            time.sleep(3)
        except:
            pass        

    finally:
        driver.quit()

if __name__ == "__main__":
    # input_file = input("Enter the file path containing YouTube links: ")
    input_file = "video_links.txt"

    with open(input_file, 'r') as file:
        youtube_links = file.read().splitlines()

    for link in youtube_links:
        download_transcript(link)

    print("Transcripts downloaded successfully.")
