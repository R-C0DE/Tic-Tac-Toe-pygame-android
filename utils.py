#https://youtu.be/Ven-pqwk3ec
from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
# import webdriver
from selenium import webdriver
 
# create webdriver object
driver = webdriver.Firefox()
 
 
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
 
# get element
element = driver.find_element_by_id("gsc-i-id1")
 
# send keys
element.send_keys("Arrays")

#https://www.andressevilla.com/running-chromedriver-with-python-selenium-on-heroku/

 

def valid_number(ctr):
    mini=0
    maxi=100
    try:
        number=int(ctr)
    except:
        return False
    return mini <= number <= maxi
print(valid_number('444'))
import time
import random
def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Fire in the hole!!') 
countdown(10)
class whac_a_mole:
    def __init__(self, speed=2, highscore=0):
        self.score=highscore
    def play(self):
        while True:
            direction=randint(0,3)
            if direction==0:
                str1="w"
            elif direction==1:
                str1="s"
            elif direction==2:
                str1="a"
            elif direction==3:
                str1="d"
            print(str1)
            guess=input("Enter 'W', 'A', 'S' or 'D' :")
            guess.lower()
            
            while t>1:
                if mole=='up':
                    guess=input("Enter 'W', 'A', 'S' or 'D' :")
                    if guess==str1:
                        strfinal="_____you wacked it..._____"
                        return strfinal
                    else:
                        break
                time.sleep(0.)
            else:
                mole="down"

                    
            #if guess
    
    
