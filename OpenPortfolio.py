from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def login_and_navigate_to_portfolio(username, password):
    # Set up Chrome driver
    driver = webdriver.Chrome()

    # Navigate to the first website
    driver.get("https://itrade.mtbsecurities.com/")

    # Wait for the login page to load
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "InternalLoginUser_UserName")))
    except TimeoutException:
        print("Timed out waiting for login page to load")
        driver.quit()
        return None

    # Enter username
    username_input = driver.find_element(By.ID, "InternalLoginUser_UserName")
    username_input.send_keys(username)

    # Enter password
    password_input = driver.find_element(By.ID, "InternalLoginUser_Password")
    password_input.send_keys(password)

    # Click the login button
    login_button = driver.find_element(By.ID, "InternalLoginUser_btnAdminLogin")
    login_button.click()

    # Wait for the portfolio button to be present and click it
    try:
        portfolio_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "AdminMainContent_btnPortfolio")))
        portfolio_button.click()
    except TimeoutException:
        print("Timed out waiting for portfolio button to be present")
        driver.quit()
        return None

    return driver

def login_to_bullbd(email, bullbd_password, driver):
    # Open a new tab
    driver.execute_script("window.open('', '_blank');")

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[1])

    # Navigate to the BullBD login page using the existing driver
    driver.get("https://bullbd.com/login")

    # Wait for the password input field to be present
    try:
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"][aria-label="Password"]'))
        )
    except TimeoutException:
        print("Timed out waiting for password input field to be present")
        return None

    # Type the email
    email_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Email"]')
    email_input.send_keys(email)

    # Type the password
    password_input.send_keys(bullbd_password)

    # Click the login button using the provided XPath
    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main/main/div/div[2]/div/div/div/form/div/button/span[2]')
    login_button.click()

    # Perform any additional actions or clicks if needed

    return driver

def click_elements_with_delay(driver):
    # Wait for the first element to be present and click it
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main/main/div/div[2]/div').click()

    # Wait for the second element to be present and click it
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main/main/div/div[2]/div/div[2]/div[2]/div[2]').click()

    # Wait for the third element to be present and click it
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main/main/div/div[3]/div/div/div[5]/div/div[1]/div/div/div[3]/div/div[1]/div[1]/span').click()

    # Wait for the fourth element to be present and click it
    time.sleep(2)
    driver.find_element(By.XPATH, '//div[@class="q-tab__label" and text()="Adv chart"]').click()

# Example usage:
main_driver = login_and_navigate_to_portfolio("72228", "Mtbs@1204")

# Continue with other actions on the portfolio page or perform checks on 'main_driver'

# Example usage for BullBD login using the same driver
bullbd_driver = login_to_bullbd("riponsarkar21@gmail.com", "12345678", main_driver)

# Click on elements with a 2-second delay
click_elements_with_delay(bullbd_driver)

# Continue with other actions on the BullBD website or perform checks on 'bullbd_driver'
