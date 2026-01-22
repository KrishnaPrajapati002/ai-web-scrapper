"""captcha_solver.py"""
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import time

def solve_captcha(url):
    """Solving Captcha"""
    options = Options()
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    solver = RecaptchaSolver(driver=driver)

    driver.get(url)
    time.sleep(3)

    try:
        iframe = driver.find_element(By.XPATH, '//iframe[contains(@src,"recaptcha")]')
        solver.click_recaptcha_v2(iframe=iframe)
        print("CAPTCHA_SOLVED")
        driver.quit()
        return 0
    except Exception:
        print("NO_RECAPTCHA_FOUND")
        driver.quit()
        return 0   # important: still return success

if __name__ == "__main__":
    solve_captcha(sys.argv[1])






# """ 
# test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

# options = Options()

# options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
# options.add_argument("--window-size=1920,1080")

# options.add_argument(f'--user-agent={test_ua}')

# options.add_argument('--no-sandbox')
# options.add_argument("--disable-extensions")

# test_driver = webdriver.Chrome(options=options)

# solver = RecaptchaSolver(driver=test_driver)

# test_driver.get('https://www.google.com/recaptcha/api2/demo')

# recaptcha_iframe = test_driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')

# solver.click_recaptcha_v2(iframe=recaptcha_iframe)
# """