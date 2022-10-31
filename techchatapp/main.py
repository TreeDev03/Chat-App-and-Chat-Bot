import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

background = input("Do you want to run the bot in the background(yes or no): ").lower()
username = input("Enter your username: ")
password = input("Enter your password: ")
room_name = input("Enter the room name: ")
time_interval = float(input("Enter a time interval for each message: "))
messages = input("Each messages to send separated by a coma: ").split(",")


print("Bot in progress...")

chop = webdriver.ChromeOptions()
print(list)
time.sleep(1)

driver = webdriver.Chrome(options=chop)
driver.maximize_window()
driver.get("http://127.0.0.1:8000/")
signin = driver.find_element(By.XPATH, """/html/body/nav/div[2]/a[1]""")
signin.click()
time.sleep(1)
user_input = driver.find_element(By.XPATH, """/html/body/form/div[1]/input""")
user_input.click()
user_input.send_keys(username)
time.sleep(1)
pass_input = driver.find_element(By.XPATH, """/html/body/form/div[2]/input""")
pass_input.click()
pass_input.send_keys(password)
time.sleep(1)
login_in = driver.find_element(By.XPATH, """/html/body/form/button""")
login_in.click()
time.sleep(1)
chat_room = driver.find_element(By.CSS_SELECTOR, f'[href="/rooms/{room_name}/"]')
chat_room.click()
time.sleep(1)
chat_bot = driver.find_element(By.XPATH, """//*[@id="chat-message-input"]""")
chat_bot.click()

for i in messages:
    chat_bot.send_keys(i)
    submit = driver.find_element(By.XPATH, """//*[@id="chat-message-submit"]""")
    submit.click()
    time.sleep(time_interval)

