# Auto-Self-Diagnosis-for-server

## 의존성
google-chrome 91 이상<br>
python3

## 설치
이 ["링크"]를 통해서 설치를 진행할 수 있습니다.<br>
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
``` bash
python3 server.py
```
위 명령어로 실행합니다.

## 기타
필자는 ubuntu 18.04 환경에서 원활하게 동작하였습니다.

## LISENSE
This project is licensed under the terms of the [MIT license]("https://").<br>
The binary files of ChromeDriver are licensed under the [BSD-3-Clause]("https://").<br>
