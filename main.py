import requests
from random import *
from time import sleep


headers = {'Host': 'seumedu.kr',
           'Connection': 'keep-alive',
           'Accept': '*/*',
           'Origin': 'http://seumedu.kr',
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Referer': 'http://seumedu.kr/study/study.html?no=35143&num=4',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
           'Cookie': 'PHPSESSID=user session id'}

target_url = "https://seumedu.kr/study/jindo_check.php"
# appendents = "no=35143&num=2&log_num=1%2C&cl_start_time=1560825333&cl_start_check=1560825333"
# no=35143&num=3&log_num=1%2C&cl_start_time=1560933073&cl_start_check=1560933062

# r = requests.session()
num = ''
start_epoch = 1561077334
for x in range(1,13):
    num = num+str(x)+','
    sleep(1)
    start_epoch = start_epoch + randint(60, 360)
    base_epoch = 1561076943
    appendents = {
        'no': '35143',
        'num': '8',  # 차시
        'log_num': num,  # 차시내부 챕터, 1,2,3,
        'cl_start_time': start_epoch,
        'cl_start_check': base_epoch
    }
    print(appendents)
    response = requests.post(url=target_url, data=appendents, headers=headers,
                             cookies=dict(PHPSESSID='user session id'))