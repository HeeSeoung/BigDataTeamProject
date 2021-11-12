import requests
import pandas as pd
from datetime import datetime

# OTP코드를 메시지로 받습니다.
rsp = requests.get('https://web-production.lime.bike/api/rider/v1/login?phone=%2B821086094104')

# 핸드폰으로 입력받은 OTP코드를 login_code에 입력합니다.
headers = {'Content-Type': 'application/json'}
data = '{"login_code": "187268", "phone": "+821086094104"}'
response = requests.post('https://web-production.lime.bike/api/rider/v1/login', headers=headers, data=data)

# 입력받은 쿠키와 토큰값을 설정하고 전동킥보드 정보를 요청합니다.
rsp_token = response.json().get('token')
rsp_cookie = response.cookies.get('_limebike-web_session')

cookies = {'_limebike-web_session': f'{rsp_cookie}'}
headers = {'authorization': f'{rsp_token}'}

# TODO 어떤 위치를 중심으로 받아올지 zoom 설정은 어떻게할지 논의 필요
params = (
    ('ne_lat', '37.5'),
    ('ne_lng', '127.1'),
    ('sw_lat', '37.4'),
    ('sw_lng', '127.0'),
    ('user_latitude', '37.5172'),
    ('user_longitude', '127.0473'),
    ('zoom', '16'),
)

now = datetime.now()
lime_data = requests.get('https://web-production.lime.bike/api/rider/v1/views/map', headers=headers, params=params, cookies=cookies)
mobility = lime_data.json()
df_bike = pd.DataFrame(data=mobility['data']['attributes']['bikes'])
temp = []
for i in df_bike['attributes']:
    temp.append(i)
df = pd.DataFrame(data=temp)
date = [now for _ in range(len(df))]
df.insert(0, 'id', df_bike['id'])
df.insert(3, 'collect_time', now)