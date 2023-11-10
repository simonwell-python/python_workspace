from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import base64
import requests
from fake_useragent import UserAgent


options = Options()
options.add_argument("--disable-notifications")

# user-agent
# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
ua = UserAgent()
print("user-agent：" + ua.random)


chrome = webdriver.Chrome("./chromedriver", chrome_options=options)
wait = WebDriverWait(chrome, 10)  # 等待載入10s
chrome.get("https://agri.pks.com.tw/Default.aspx?ReturnUrl=%2fmember.aspx")


def login():
    # 輸入帳號
    acount = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_Login1_UserName"]'))
    )
    acount.send_keys("F226349902")
    # 輸入密碼
    pwd = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_Login1_Password"]'))
    )
    pwd.send_keys("Qq-86305635")
    # 點擊登入
    submit = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_Login1_LoginButton"]'))
    )
    # 點選登入按鈕
    submit.click()
    logined_action()


def logined_action():
    chrome.get("https://agri.pks.com.tw/member.aspx")
    time.sleep(1)
    # 找出線上學習系統
    findElearnSys = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_Repeater4_ctl02_HL"]')
        )
    )
    # 找出線上學習系統href
    findElearnSysUrl = findElearnSys.get_attribute("href")
    print("找出線上學習系統href: " + findElearnSysUrl)
    elearning_system(findElearnSysUrl)


def elearning_system(findElearnSysUrl):
    # 跳轉 農金保經公司線上學習系統
    chrome.get(findElearnSysUrl)
    time.sleep(10)
    print("滑鼠mouse over 待完成活動 顯示其他下拉選單")
    # 滑鼠mouse over 待完成活動 顯示其他下拉選單
    toDolist = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[7]/div[1]/div/div[13]")
        )
    )
    ActionChains(chrome).move_to_element(toDolist).perform()
   
    time.sleep(2)
    
    # 閱讀
    print("找出閱讀元素")
    readName = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[7]/div[1]/div/div[13]/ul/li[4]")
        )
    ).click()
    
    class_action()


def class_action():
    print("跑到class_action")
    
    time.sleep(2)
    
    print("滑鼠mouse over 第一個課程")
    # 滑鼠mouse over 第一個課程
    mouse_over_firstClass = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[7]/div[3]/div/div/div/div[2]/div[3]/div/div[2]/div/div[4]/div[6]/table/tbody/tr/div/div[1]")
        )
    )
    ActionChains(chrome).move_to_element(mouse_over_firstClass).perform()

    time.sleep(2)
    
    #點擊 第一個課程
    print("點擊 第一個課程")
    firstClass = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[7]/div[3]/div/div/div/div[2]/div[3]/div/div[2]/div/div[4]/div[6]/table/tbody/tr/div/div[1]")
        )
    ).click()
    homepage()
    
    
def homepage():
    #進入 jomepage
    print("進入 homepage")
    #chrome.get("https://learn-afib.com.tw/eHRD/Homepage.html")



login()
