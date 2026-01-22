"""scrape.py"""

import subprocess
import sys
import time
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service

def solve_captcha_external(url):
    result = subprocess.run(
        [r"venv_captcha\Scripts\python.exe","captcha_solver.py",url], 
        stdout= subprocess.PIPE,
        stderr= subprocess.PIPE,
        text=True
    )
    print("Captcha solver stdout:\n", result.stdout)
    print("Captcha solver stderr:\n", result.stderr)


    if result.returncode !=0:
        print("Captcha solver failed, continuing without solve....")

def scrape_website(website):
    """Scraping website function"""
    print("Launching browser.....")

    solve_captcha_external(website)

    chrome_driver_path="./chromedriver.exe "
    #"""for basic chrome"""
    # options = webdriver.ChromeOptions()
    #"""for other browsers"""
    brave_path = r"C:\Users\hp\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"
    options = webdriver.ChromeOptions()
    options.binary_location = brave_path

    driver = webdriver.Chrome(service = Service(chrome_driver_path), options = options)

    try:
        driver.get(website)
        print("page loaded....")
        html = driver.page_source
        time.sleep(5)

        return html
    finally:
        driver.quit()
