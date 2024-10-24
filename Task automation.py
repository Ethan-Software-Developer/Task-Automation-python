from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Function to log in to GitHub
def automate_github_login(username, password):
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    try:
        # Open the GitHub login page
        driver.get("https://github.com/login")

        # Wait for the page to load
        time.sleep(2)

        # Find the username and password fields and the login button
        username_field = driver.find_element(By.ID, "login_field")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.NAME, "commit")

        # Enter username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click the login button
        login_button.click()

        # Wait for a while to see the result
        time.sleep(5)

        # Optionally, you can verify if the login was successful
        print("Login attempted. Check the browser.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    username = "your_username"  # Replace with your actual GitHub username
    password = "your_password"    # Replace with your actual GitHub password

    automate_github_login(username, password)
