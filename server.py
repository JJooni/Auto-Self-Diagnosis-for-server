import datetime
import json
import os
import re
import sys
import time

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.select import Select

def diagnosis(CP, SL, SN, NM, BH, PD):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("disable-gpu")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")

        if getattr(sys, "frozen", False):
            chromedriver_path = os.path.join(sys._MEIPASS, "./chromedriver")
            driver = webdriver.Chrome(chromedriver_path, options=options)
        else:
            driver = webdriver.Chrome("./chromedriver", options=options)

        driver.get("https://hcs.eduro.go.kr/#/loginHome")
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()

        time.sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="WriteInfoForm"]/table/tbody/tr[1]/td/button'
        ).click()
        time.sleep(0.5)
        Select(
            driver.find_element_by_xpath(
                '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select'
            )
        ).select_by_visible_text(CP)
        time.sleep(0.5)
        Select(
            driver.find_element_by_xpath(
                '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select'
            )
        ).select_by_visible_text(SL)
        time.sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[1]/input'
        ).send_keys(SN)
        time.sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button'
        ).click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > ul"
        ).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="softBoardListLayer"]/div[2]/div[2]/input'
        ).click()

        time.sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="WriteInfoForm"]/table/tbody/tr[2]/td/input'
        ).send_keys(NM)
        time.sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="WriteInfoForm"]/table/tbody/tr[3]/td/input'
        ).send_keys(BH)
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

        time.sleep(2)
        driver.find_element_by_id('password').click()

        # time.sleep(0.5)
        # driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

        #print(list(PD))
        time.sleep(1)

        for i in list(PD):
            time.sleep(0.5)
            driver.find_element_by_css_selector(f'[aria-label="{i}"]').click()

        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

        time.sleep(2)
        driver.find_element_by_css_selector(
            "#container > div > section.memberWrap > div:nth-child(2) > ul > li > a > em"
        ).click()

        try:
            alert = driver.switch_to.alert
            message = alert.text
            left_time = re.findall(r"약(\d)분", message)[0]
            alert.accept()
        except NoAlertPresentException:
            pass
        else:
            print(left_time)
            time.sleep(int(left_time) * 60)
            driver.find_element_by_css_selector(
                "#container > div > section.memberWrap > div:nth-child(2) > ul > li > a > em"
                    # "#container > div:nth-child(1) > section.memberWrap > div:nth-child(2) > ul > li > a > button"
            ).click()

        time.sleep(2)

        for i in range(1, 4):
            time.sleep(0.5)
            driver.find_element_by_css_selector(
                f"#container > div.subpage > div > div:nth-child(2) > div.survey_question > dl:nth-child({i}) > dd > ul > li:nth-child(1) > label"
            ).click()

        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
        time.sleep(2.0)

        print(time.strftime('%x %X ', time.localtime(time.time())) + NM + ' - 완료')
    except Exception as e:
        print(e)
        print(time.strftime('%x %X ', time.localtime(time.time())) + '오류 발생 : 프로그램 초기화')
        diagnosis(CP, SL, SN, NM, BH, PD)
    finally:
        driver.quit()
        r.close()

reserveTime = '07 00 00'

if __name__ == "__main__":
    while True:
        nowTime = time.strftime('%H %M %S', time.localtime(time.time()))
        Today = time.strftime('%a', time.localtime(time.time()))

        if Today != 'Sat' and Today != 'Sun':
            if reserveTime == nowTime:
                with open("./info.json", "r", encoding="utf-8") as r:
                    info = json.load(r)
                CP = info['C/P'].split(',')
                SL = info['SL'].split(',')
                SN = info['SN'].split(',')
                NM = info['NM'].split(',')
                BH = info['BH'].split(',')
                PD = info['PD'].split(',')

                for i in range(0, len(CP)):
                    print(time.strftime('%x %X ', time.localtime(time.time())) + NM[i] + ' - 자가진단 시작')
                    diagnosis(CP[i], SL[i], SN[i], NM[i], BH[i], PD[i])
                time.sleep(1)