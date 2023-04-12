from time import sleep

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class InstaFollower:
    def __init__(self):
        Chrome_Dev_path = "E:\Python Udemy\Day 48\Chrome Dev Tools\chromedriver.exe"
        driver = Service(Chrome_Dev_path)
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=driver, options=option)

    def login(self):
        email = "mamun.kfz@gmail.com"
        passd = "testing@464"
        url=" https://www.instagram.com/"
        self.browser.get(url)
        sleep(2)
        username=self.browser.find_element(By.NAME,"username")
        username.send_keys(email)

        passed = self.browser.find_element(By.NAME, "password")
        passed.send_keys(passd)
        sleep(1)
        passed.send_keys(Keys.ENTER)
    def find_followers(self):
        sleep(10)
        url="https://www.instagram.com/chefsteps/"
        self.browser.get(url)
        print("processing")
        sleep(5)
        follower_list=self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/ul/li[2]/a')
                                                #'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a')
        sleep(1)
        follower_list.click()
        sleep(2)
        modal = self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')

        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

            sleep(2)

    def follow(self):
        print("Clicking follow")
        # create list of all the follower elements
        followers_list = self.browser.find_elements(By.CSS_SELECTOR, '._acan _acap _acas _aj1-')
        # loop through each follower in follower list
        for follower in followers_list:
            try:
                follower.click()
                sleep(1)
            # if sometimes we click on following instead of follow, so instagram displays pop up to confirm unfollow
            except ElementClickInterceptedException:
                # click on cancel
                self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]').click()
                sleep(2)





Obj_insta=InstaFollower()
Obj_insta.login()
Obj_insta.find_followers()

Obj_insta.follow()


