
from selenium import webdriver as wd
from time import sleep
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys as Keys

driver = ""
class rootsd():

    def __init__(self,e_mail="girilmedi@gmail.com",password="girilmedi"):
        self.password = password
        self.e_mail = e_mail

        self.password = "******"
        self.e_mail = "*******@gmail.com"
       
        daata = [self.e_mail,self.password]

        self.selenium_go(daata)


    global scripts
    
    def scripts(data,driver):
        
        g = 1
        for a in data:
            print(a)
            driver.get("{}".format(a))
            sleep(7)


            try:
                driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[29]/div/div").click()
                
            except:
                driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[27]/div/div").click()
           
            
            print("Yorum yapma butonu bulundu.")
            # /html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[27]/div/div
            # /html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[27]/div/div
            sleep(7)

            
            driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[9]/iframe"))
            sleep(4)
            
            driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div/div/div[1]/div[4]/div[2]/div[1]/div/div/div[2]").click()
            driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div/div/div[1]/div[4]/div[2]/div[2]/div/div/span[5]").click()
            #.CrAOse-hSRGPd
            #/html/body/div[1]/c-wiz/div/div/div/div/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/g-bubble/span/span
            #/html/body/div[1]/c-wiz/div/div/div/div/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/g-bubble/span/span
            sleep(2)

            #for i in range(0 , 5):
                #driver.find_element_by_class_name(" NMm5M").send_keys("\ue004")
            #driver.find_element_by_class_name(" NMm5M").send_keys("\ue007")

        
          
            sleep(4)
            driver.find_element_by_class_name("review-text").send_keys("Gördüğüm en güzel hizmet.")
            sleep(0.2)
            #chat1.send_keys("Burası gerçekten çok hoşuma gitti, hizmetiniz için çok teşekkür ederim ve herkese tavsiye ederim.")
            sleep(2)
            driver.find_element_by_xpath("/html/body/div/c-wiz/div/div/div/div/div[2]/div[2]/div/div[2]/button/div/div").click()
            print("Yorum gönderildi.")
            sleep(6)
            g+=1

  
    def selenium_go(self,ddata):
        email_data = ddata[0]
        password_data = ddata[1]

        #driver = webdriver.Firefox()
       
        
        with open("maps_list.txt", "r") as f:
            data = [url.strip() for url in f.read().split("=en")]

        # her birini en diline ayarlamak.
        def_data = list()
        for link in data:
            link = str(link) + "=en"
            def_data.append(link)

     
        
        driver = wd.Chrome()
        d = 1
        driver.get("https://accounts.google.com/signin/v2/identifier?hl=tr&continue=https%3A%2F%2Fwww.google.com.tr%2Fmaps&service=local&flowName=GlifWebSignIn&flowEntry=AddSession")
        
        sleep(3)
        a = driver.find_element_by_xpath("//*[@id='identifierId']")
        a.send_keys(email_data)
        sleep(0.5)
        go_btn = driver.find_element_by_class_name("VfPpkd-vQzf8d")

        go_btn.click()
        sleep(2)
        b = driver.find_element_by_name("password")
        b.send_keys(password_data)
        sleep(0.5)
        go_btn = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
        go_btn.click()

        sleep(5)
        scripts(def_data,driver)


    


rootsd()



