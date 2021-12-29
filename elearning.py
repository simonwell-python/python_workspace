from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import ddddocr
import time
import base64
import requests


options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome("./chromedriver", chrome_options=options)
wait = WebDriverWait(chrome, 10)  # 等待載入10s
chrome.get("https://elearning.tii.org.tw/moodle/courserecord/index.php")
# 找出登入位置
chrome.find_element_by_xpath(
    "/html/body/div/div/div/table/tbody/tr[1]/td/h1/b/a[2]"
).click()


def login():
    chrome.get("https://edu.tii.org.tw/home/mpage/login")
    # 輸入帳號
    input = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
    )
    input.send_keys("chuqiu")
    # 輸入密碼
    input = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
    input.send_keys("349902qq")

    # 下載驗證碼圖像
    img_base64 = chrome.execute_script(
        """
        var ele = arguments[0];
        var cnv = document.createElement('canvas');
        cnv.width = ele.width+90; cnv.height = ele.height+30;
        cnv.getContext('2d').drawImage(ele, 0, 0);
        return cnv.toDataURL('image/jpeg').substring(22);    
        """,
        chrome.find_element_by_xpath('//*[@id="captcha_img"]'),
    )

    with open("captcha_img.png", "wb") as image:
        image.write(base64.b64decode(img_base64))

    file = {"file": open("captcha_img.png", "rb")}  # 下載下來的一般驗證碼(Normal Captcha)圖片

    ocr = ddddocr.DdddOcr()
    with open("captcha_img.png", "rb") as f:
        img_bytes = f.read()
        res = ocr.classification(img_bytes)
        print(res)
        # 輸入驗證碼
        input = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="captcha_code"]'))
        )
        input.send_keys(res)
        # 點擊登入
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="loginform"]/div/div[6]/button')
            )
        )
        # 點選登入按鈕
        submit.click()
        logined_action()


def logined_action():
    chrome.get("https://edu.tii.org.tw/home/mpage/myinfo")
    time.sleep(1)
    # 找出數位學習
    chrome.find_element_by_xpath('//*[@id="right_block"]/div/div/a[1]').click()
    unFinished_training()


def unFinished_training():
    chrome.get("https://elearning.tii.org.tw/moodle/courserecord/index.php")
    # 法尊課程(未完訓)
    # chrome.find_element_by_xpath('//*[@id="region-main"]/div/div[3]/button[2]').click()
    time.sleep(4)
    # 課程名稱第一個
    chrome.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]/a').click()
    verification_check_user()


def verification_check_user():
    chrome.get(
        "https://elearning.tii.org.tw/moodle/courserecord/verification_check_user.php?id=40137"
    )
    time.sleep(4)

    # 先取得Label文字是什麼
    q1 = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="question1"]/label',
            )
        )
    )
    q11 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="q1"]')))
    q2 = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="question2"]/label',
            )
        )
    )
    q22 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="q2"]')))

    ###### 找出q1是屬於哪種問題 ######
    if q1.text == "出生日期(yyyy-mm-dd)":
        print("q1:出生日期(yyyy-mm-dd)")
        q11.send_keys("19860913")

    elif q1.text == "身分證號":
        print("q1:身分證號")
        q11.send_keys("F226349902")

    elif q1.text == "喜歡的季節:":
        print("q1:喜歡的季節")
        s1 = Select(q11)
        s1.select_by_visible_text("秋")

    elif q1.text == "喜歡的運動:":
        print("q1:喜歡的運動")
        s1 = Select(q11)
        s1.select_by_visible_text("室內")

    elif q1.text == "喜歡的動物:":
        print("q1:喜歡的動物")
        s1 = Select(q11)
        s1.select_by_visible_text("水裡游的")

    elif q1.text == "選擇生肖:":
        print("q1:選擇生肖")
        s1 = Select(q11)
        s1.select_by_visible_text("虎")

    ###### 找出q2是屬於哪種問題 ######

    if q2.text == "出生日期(yyyy-mm-dd)":
        print("q2:出生日期(yyyy-mm-dd)")
        q22.send_keys("19860913")

    elif q2.text == "身分證號":
        print("q2:身分證號")
        q22.send_keys("F226349902")

    elif q2.text == "喜歡的季節:":
        print("q2:喜歡的季節")
        s2 = Select(q22)
        s2.select_by_visible_text("秋")

    elif q2.text == "喜歡的運動:":
        print("q2:喜歡的運動")
        s2 = Select(q22)
        s2.select_by_visible_text("室內")

    elif q2.text == "喜歡的動物:":
        print("q2:喜歡的動物")
        s2 = Select(q22)
        s2.select_by_visible_text("水裡游的")

    elif q2.text == "選擇生肖:":
        print("q2:選擇生肖")
        s2 = Select(q22)
        s2.select_by_visible_text("虎")

    time.sleep(2)
    # 點擊確定
    confirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnCheck"]')))
    confirm.click()
    main_video_View()


def main_video_View():
    print("main_video_View")


login()
