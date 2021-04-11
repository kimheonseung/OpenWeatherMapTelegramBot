# OpenWeatherMapTelegramBot

## OpenWeatherMap API와 Telegram Bot API 사용하여 메세지 전송
- Telegram Bot 구독한 사용자들에게 특정 지역의 날씨정보 반환
- 현재 구로 날씨만 일방적으로 제공
  
- 사용 : crontab에 등록하여 매일 특정 시간에 python 명령어로 해당 스크립트 실행

```python

# 지역을 변경하려면 145, 146 line에 변경하려는 지역 위도, 경도 수정
guro_lat = '37.485385187270985'
guro_lon = '126.90141558277708'

# 135 line OpenWeatherMApAPI 발급 키 입력
api_key = 'OpenWeatherMapAPIKey'

# 180 line 텔레그램 봇 발급 키
my_token = '텔레그램봇키'
  
  

# 전송 메세지 예시  
  
  
  
## 2021년 04월 10일 날씨 정보입니다.



# 현재 맑음

온도 (체감) : 7.07℃  (4.62℃ )
어제보다 1.18˚ 높아요

맑음 예상
최저 / 최고 : 7.07℃ / 16.1℃
아침 (체감) : 9.59℃ (8.7℃)
낮 (체감) : 15.14℃ (13.57℃)
저녁 (체감) : 14.15℃ (12.48℃)
밤 (체감) : 12.01℃ (8.7℃)
강수확률 : 0.0%
예상 강수량 : 0mm
습도 : 57%
풍속 : 3.6m/s
구름 : 0%
현재 강수량 : 0mm
============================


# 08시 (맑음)

온도 (체감) : 8.78℃  (7.66℃ )
습도 : 49%
풍속 : 2.13m/s
구름 : 0%
강수량 : 0mm
============================

# 09시 (맑음)

온도 (체감) : 10.75℃  (9.03℃ )
습도 : 44%
풍속 : 2.16m/s
구름 : 0%
강수량 : 0mm
============================

# 10시 (맑음)

온도 (체감) : 12.72℃  (11.09℃ )
습도 : 40%
풍속 : 2.12m/s
구름 : 0%
강수량 : 0mm
============================

# 12시 (맑음)

온도 (체감) : 15.14℃  (13.57℃ )
습도 : 33%
풍속 : 2.8m/s
구름 : 0%
강수량 : 0mm
============================

# 14시 (맑음)

온도 (체감) : 16.1℃  (14.5℃ )
습도 : 28%
풍속 : 4.03m/s
구름 : 2%
강수량 : 0mm
============================

# 16시 (맑음)

온도 (체감) : 15.74℃  (14.05℃ )
습도 : 26%
풍속 : 4.21m/s
구름 : 5%
강수량 : 0mm
============================


# 04월 11일 12시 (약간의 구름이 낀 하늘)

최저 / 최고 : 10.5℃ / 20.26℃
아침 (체감) : 10.5℃ (8.88℃)
낮 (체감) : 18.3℃ (16.79℃)
저녁 (체감) : 18.93℃ (17.58℃)
밤 (체감) : 16.39℃ (8.88℃)
강수확률 : 0.0%
강수량 : 0mm
습도 : 23%
풍속 : 0.82m/s
구름 : 20%

============================

# 04월 12일 12시 (실 비)

최저 / 최고 : 12.85℃ / 18.27℃
아침 (체감) : 13.36℃ (11.82℃)
낮 (체감) : 18.27℃ (16.83℃)
저녁 (체감) : 13.8℃ (12.99℃)
밤 (체감) : 12.85℃ (11.82℃)
강수확률 : 100.0%
강수량 : 3.14mm
습도 : 26%
풍속 : 3.01m/s
구름 : 100%

============================

# 04월 13일 12시 (보통 비)

최저 / 최고 : 11.4℃ / 16.79℃
아침 (체감) : 12.43℃ (12.16℃)
낮 (체감) : 16.34℃ (15.62℃)
저녁 (체감) : 15.05℃ (13.47℃)
밤 (체감) : 11.4℃ (12.16℃)
강수확률 : 100.0%
강수량 : 14.02mm
습도 : 61%
풍속 : 5.43m/s
구름 : 74%

============================

# 04월 14일 12시 (실 비)

최저 / 최고 : 8.07℃ / 14.35℃
아침 (체감) : 8.12℃ (8.12℃)
낮 (체감) : 13.77℃ (11.99℃)
저녁 (체감) : 12.35℃ (10.87℃)
밤 (체감) : 11.37℃ (8.12℃)
강수확률 : 39.0%
강수량 : 1.2mm
습도 : 30%
풍속 : 1.49m/s
구름 : 3%

============================

# 04월 15일 12시 (실 비)

최저 / 최고 : 7.97℃ / 14.89℃
아침 (체감) : 7.97℃ (7.07℃)
낮 (체감) : 13.62℃ (12.03℃)
저녁 (체감) : 12.78℃ (11.16℃)
밤 (체감) : 10.92℃ (7.07℃)
강수확률 : 37.0%
강수량 : 2.07mm
습도 : 38%
풍속 : 1.27m/s
구름 : 5%

============================

# 04월 16일 12시 (맑음)

최저 / 최고 : 9.05℃ / 15.38℃
아침 (체감) : 9.05℃ (8.51℃)
낮 (체감) : 15.03℃ (13.53℃)
저녁 (체감) : 13.82℃ (12.64℃)
밤 (체감) : 12.23℃ (8.51℃)
강수확률 : 0.0%
강수량 : 0mm
습도 : 36%
풍속 : 3.83m/s
구름 : 0%

============================

# 04월 17일 12시 (약간의 구름이 낀 하늘)

최저 / 최고 : 10.15℃ / 20.66℃
아침 (체감) : 10.15℃ (9.13℃)
낮 (체감) : 18.14℃ (16.95℃)
저녁 (체감) : 19.34℃ (18.09℃)
밤 (체감) : 16.84℃ (9.13℃)
강수확률 : 0.0%
강수량 : 0mm
습도 : 36%
풍속 : 0.83m/s
구름 : 11%

============================
```