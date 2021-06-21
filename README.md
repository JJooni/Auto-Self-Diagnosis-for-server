# Auto-Self-Diagnosis-for-server
자동 자가진단 메크로 서버전용<br><br>
이 프로그램은 [SaidBySolo님의 auto-self-diagnosis](https://github.com/SaidBySolo/auto-self-diagnosis)를 참고하여 제작하였습니다.<br>
개인 사용 목적으로 제작하였기 때문에 추후 업데이트는 **진행하지 않습니다**.

## 의존성
Google-Chrome 91 이상<br>
Python3<br>
Selenium 3.141.0

## 설치
이 [링크](https://github.com/JJooni/Auto-Self-Diagnosis-for-server/archive/refs/heads/main.zip)를 통해서 설치를 진행할 수 있습니다.<br>
## 실행 
1. info.json에 사용자를 입력합니다.<br>
','를 통해 여러명을 입력할 수 있습니다.<br>

ex<br>
```
{
   "C/P": "서울특별시,서울특별시",
   "SL": "고등학교,고등학교",
   "SN": "ㅁㅁ고등학교,ㅇㅇ고등학교",
   "NM": "홍길동,홍길순",
   "BH": "030101,031212",
   "PD": "1234,4567"
}
```

2. reservationTime.json에 예약 시간을 입력합니다.<br>
시간은 24시간제를 사용합니다.<br>
서버의 위치를 기준으로 시간을 측정하므로 현지 시간으로 입력해야 합니다.<br>

3.
- 
```bash
$ python3 server.py
```
위 명령어로 실행합니다.<br>

- 
```bash
$ nohup python3 server.py
```
위 명령어로 백그라운드에서 실행합니다.

## 기타
필자는 ubuntu 18.04 환경에서 원활하게 동작하였습니다.

## 경고 (Warning)
사용에 대한 모든 책임은 사용자 본인에게 있습니다.<br>
You are responsible for all responsibility for using it.

## LISENSE
This project is licensed under the terms of the [MIT license](https://github.com/JJooni/Auto-Self-Diagnosis-for-server/blob/main/LICENSE).<br>
The binary files of ChromeDriver are licensed under the [BSD-3-Clause](https://github.com/JJooni/Auto-Self-Diagnosis-for-server/blob/main/LICENSE.chromedriver).
