import time
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def generate_random_string(length):
    """Genera una cadena aleatoria de letras y dígitos."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def main():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = '/usr/bin/google-chrome' 

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get('https://temp-mail.org/es/')
        time.sleep(8)  


        email_element = driver.find_element("id", "mail")
        email_text = email_element.get_attribute('value')

        driver.execute_script("window.open('https://www.instagram.com/accounts/emailsignup/', 'new window')")
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)

        email_input = driver.find_element("name", "emailOrPhone")
        full_name_input = driver.find_element("name", "fullName")
        username_input = driver.find_element("name", "username")
        password_input = driver.find_element("name", "password")

        random_full_name = generate_random_string(10)  
        random_username = generate_random_string(8)
        random_password = generate_random_string(12)  

        email_input.send_keys(email_text)
        full_name_input.send_keys(random_full_name)
        username_input.send_keys(random_username)
        password_input.send_keys(random_password)

        
        print(f"Email: {email_text}")
        print(f"Full Name: {random_full_name}")
        print(f"Username: {random_username}")
        print(f"Password: {random_password}")

       
        input("Press Enter to close the browser...")
        driver.quit()

    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()

if __name__ == "__main__":
    main()
