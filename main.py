from selenium import webdriver
import time


PROMISED_UPLOAD = 35
PROMISED_DOWNLOAD = 65
CHROME_DRIVER_PATH = "c:\selenium chrome driver\chromedriver.exe"
TWITTER_EMAIL = "email"
TWITTER__PASSWORD = "password"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url='https://www.speedtest.net/')
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(75)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"download:{self.down}")
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(f"upload:{self.up}")

    def tweet_at_provider(self):
        self.driver.get(url="https://www.twitter.com")
        time.sleep(3)
        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span')
        login.click()
        time.sleep(3)
        email_field = self.driver.find_element_by_name('session[username_or_email]')
        email_field.click()
        email_field.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        password_field = self.driver.find_element_by_name('session[password]')
        password_field.click()
        password_field.send_keys(TWITTER__PASSWORD)
        time.sleep(4)
        secondary_login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        secondary_login_button.click()
        time.sleep(6)
        tweet_compose = f"Hey @isp_provider tech your internet download speed is {self.down} and upload speed is {self.up} please fix this"
        tweet_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_field.click()
        tweet_field.send_keys(tweet_compose)
        time.sleep(4)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()


bot = InternetSpeedTwitterBot(driver_path=CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()



