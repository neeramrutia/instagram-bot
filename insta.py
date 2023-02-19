# CHROME_DRIVER_PATH = '/usr/bin/chromedriver'
# SIMILAR_ACCOUNT = "kobebryant"
# USERNAME = 'te.ster1849'
# USERNAME = 'qw_ertyuiop8758'
# USERNAME = 'tester2053'
# PASSWORD = 'testingaccount'



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from sheet import createsheet
import pandas as pd
import csv

# usernames and passwords:
chrome_driver_path = '/usr/bin/chromedriver'
SIMILAR_ACCOUNT = 'kobebryant'
# USERNAME = 'tester2053'
# PASSWORD = 'testingaccount'


class InstaFollower:
    USERNAME = ''
    PASSWORD = ''
    def __init__(self, path, username,password):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.followers=[]
        self.following=[]
        self.notfollowingback=[]
        self.USERNAME=username
        print(self.USERNAME)
        self.PASSWORD=password
        print(self.PASSWORD)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.click()
        username.send_keys(self.USERNAME)
        time.sleep(1)

        password.click()
        password.send_keys(self.PASSWORD)
        time.sleep(1)

        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(3)
        # scrolling through followers list: not working methods
        # modal = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        # not working
        # person.send_keys(Keys.DOWN)  not working
        # person.send_keys(Keys.PAGE_DOWN)  not working
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") not working

        
        fBody  = self.driver.find_element(By.XPATH,"//div[@class='_aano']")
        scroll = 0
        while scroll < 1: # scroll
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            time.sleep(2)
            scroll += 1
    def follow(self):
        try:
            list_of_followers = self.driver.find_elements(By.CSS_SELECTOR, 'button')
            print(type(list_of_followers))
            for item in list_of_followers:
                print(item.text)
                if item.text == "Follow":
                    print("click")
                    item.click()
                    time.sleep(random.randint(1, 2))
                    # list_of_followers.append(self.driver.find_elements(By.CSS_SELECTOR, 'button'))

        except Exception as e:
            print(e) 
    def unfollow(self):
        self.driver.get(f"https://www.instagram.com/{self.USERNAME}/following/")  
        # scrolling through following list
        time.sleep(3)
        fBody  = self.driver.find_element(By.XPATH,"//div[@class='_aano']")
        scroll = 0
        while scroll < 1: # scroll
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            time.sleep(2)
            scroll += 1
        try:
            list_of_followings = self.driver.find_elements(By.CSS_SELECTOR, 'button')
            print(type(list_of_followings))
            for item in list_of_followings:
                print(item.text)
                if item.text == "Following":
                    print("click")
                    item.click()
                    time.sleep(random.randint(1, 2))
                    un=self.driver.find_element(By.XPATH, "//button[normalize-space()='Unfollow']")
                    un.click()
                    # list_of_followings.append(self.driver.find_elements(By.CSS_SELECTOR, 'button'))
        except Exception as e:
            print(e)   
    def converting (self, nameList):
        IGuserName = "\n".join(nameList)
        return IGuserName          
    def followerlist(self):
        self.driver.get(f"https://www.instagram.com/{self.USERNAME}/followers/")
        time.sleep(2)
        # copy the xpath of scrollbar
        scroll_box= self.driver.find_element(By.XPATH,"//div[@class='_aano']")

        # list follower name
        #print(f"{line} Scroll Buttom  Done!!! {line}")
        scroll=0
        while scroll<500:
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', scroll_box)
            # time.sleep(2)
            scroll += 1
            links = scroll_box.find_elements(By.TAG_NAME, 'a')
        time.sleep(2)
        self.followers = [name.text for name in links if name.text != '']
        print(self.followers)
        #not working
        #self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button").click()
        # self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button").click()

        
    def followinglist(self):
        self.driver.get(f"https://www.instagram.com/{self.USERNAME}/following/")
        time.sleep(2)
        scroll_box= self.driver.find_element(By.XPATH,"//div[@class='_aano']")
        scroll=0
        while scroll<1000:
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', scroll_box)
            # time.sleep(2)
            scroll += 1
            links = scroll_box.find_elements(By.TAG_NAME, 'a')
        time.sleep(2)
        self.following = [name.text for name in links if name.text != '']
        print(self.following)

    def not_following_back(self):
        for user in self.following:
            if user not in self.followers:
                self.notfollowingback.append(user)
        print(self.notfollowingback)


    def sendmessage(self):
        self.followinglist()
        print(self.following)
        for user in self.following:
            self.driver.get(f"https://www.instagram.com/{user}/")
            time.sleep(2)
            message=self.driver.find_element(By.XPATH, "//div[@role='button'][normalize-space()='Message']")
            message.click()
            time.sleep(3)
            mes=self.driver.find_element(By.XPATH, "//textarea[@placeholder='Message...']")
            my_message="hi"
            mes.send_keys(my_message)
            mes.send_keys(Keys.ENTER)
            time.sleep(2)

    def createcsv(self):
        with open('/home/neer/Desktop/testing/data.csv',mode='w') as data:
            wr=csv.writer(data)
            d=["insta-id" , "status"]
            wr.writerow(d)
            for i in self.followers:
                d1=[i,"follower"]
                wr.writerow(d1)
            for i in self.following:
                d1=[i,"following"]
                wr.writerow(d1)
            for i in self.notfollowingback:
                d1=[i,"not following back"]
                wr.writerow(d1)  

    def erasecsvdata(self):
        f=open('/home/neer/Desktop/testing/data.csv',mode='w')
        f.truncate()
        f.close()                  


bot = InstaFollower(chrome_driver_path,'tester2053','testingaccount')


bot.login()
bot.find_followers()
bot.follow()
bot.unfollow()


bot.login()
bot.followerlist()
bot.followinglist()
bot.not_following_back()
bot.sendmessage()
bot.createcsv()