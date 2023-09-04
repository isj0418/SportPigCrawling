import time
from selenium import webdriver  # selenium 패키지에서 webdriver 모듈을 가져온다 -> 웹 브라우저 제어
# selenium 패키지에서 by 모듈을 가져온다 -> 웹 요소를 식별
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# 웹 드라이버를 자동으로 다운로드 및 설치하는 데 사용되는 ChromeDriverManager 클래스를 가져옵니다.

options = webdriver.ChromeOptions()
# : Chrome 웹 브라우저의 옵션을 설정하기 위해 ChromeOptions 객체를 생성합니다.
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# Chrome 브라우저의 로깅을 비활성화하기 위해 "enable-logging" 스위치를 제외한 옵션을 설정합니다.
driver = webdriver.Chrome(options=options)
# 이전에 설정한 옵션을 사용하여 Chrome 웹 드라이버를 생성합니다. 옵션설정하고 Chrome 웹 드라이버를 사용한다 .
try:
    driver.get('https://comic.naver.com/webtoon/detail?titleId=769209&no=84')
    print('test 9:45')
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    # 순더대로 u_cbox_list -> comments -> u_nick
    u_cbox_list = driver.find_element(by=By.CLASS_NAME, value='u_cbox_list')
    # find_element 메서드를 사용하여 by와 같이 요소를 식별해서 가져올수 있다 .
    comments = driver.find_elements(
        by=By.CLASS_NAME, value='u_cbox_comment_box')
    print(type(comments))

    #03naverweb.py문서 result리스트, pathcsv변수에 ~~.csv

    result = []
    path = './data/navercm.txt'
    cmFile = open(path, mode='w', encoding='utf-8')
    for i in range(len(comments)):
        u_nick = comments[i].find_element(
            By.CLASS_NAME, value='u_cbox_nick').text
        u_content = comments[i].find_element(
            By.CLASS_NAME, value='u_cbox_contents').text
        u_recomm = comments[i].find_element(
            By.CLASS_NAME, value='u_cbox_cnt_recomm').text
        u_date = comments[i].find_element(
            By.CLASS_NAME, value='u_cbox_date').text
        print('닉네임:{} 댓글:{} 추천수:{} 날짜:{}'.format(
            u_nick, u_content, u_recomm, u_date))
    print(file_contents)
except Exception as ex:
    print('에러이유', ex)

print('-'*70)
print()