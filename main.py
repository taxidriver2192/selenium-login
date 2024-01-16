from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def find_element_with_retry(driver, xpath, retries=3, delay=1):
    for i in range(retries):
        try:
            element = driver.find_element(By.XPATH, xpath)
            return element
        except NoSuchElementException:
            print(f"Attempt {i+1} of {retries} failed. Retrying in {delay} second(s)...")
            time.sleep(delay)
    print(f"Failed to find element after {retries} attempts.")
    return None

def tryLoginSelenium(base_url, driver):
    driver.get(base_url)
    # Find the link and click on it

    # Close the modal by clicking on the accept button
    accept_button = find_element_with_retry(driver, '//*[@id="acceptButton"]')
    accept_button.click()


    link = driver.find_element(By.XPATH, '//*[@id="account-settings-list"]/li[1]/a/span')
    link.click()

    email = "your_email@example.com"  # Replace with your test email
    password = "your_password"        # Replace with your test password

    email_input = driver.find_element(By.NAME, "borsen-login-email")
    password_input = driver.find_element(By.NAME, "borsen-login-password")

    email_input.send_keys(email)
    password_input.send_keys(password)

    # Click the submit button
    submit_button = driver.find_element(By.ID, "submitLogin")
    submit_button.click()

    try:
        driver.find_element(By.ID, "login")
    except NoSuchElementException:
        print("Login successful")
    else:
        print("Login failed")

def main():
    driver = webdriver.Chrome()

    base_url = "https://lusc.borops.net"
    tryLoginSelenium(base_url, driver)

    # driver.quit()

if __name__ == "__main__":
    main()
