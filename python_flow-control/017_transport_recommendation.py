# [problem]
# 거리(km, 실수)를 입력받아 두 줄로 출력하시오.
# 거리: {거리}km
# 추천 교통수단: {교통수단}
# 추천 기준:

# 2km 미만: 도보
# 2km 이상 5km 미만: 자전거
# 5km 이상 20km 미만: 버스
# 20km 이상: 지하철

# 예시:
# 입력: 8.5 → 출력: 거리: 8.5km\n추천 교통수단: 버스
# 입력: 1.5 → 출력: 거리: 1.5km\n추천 교통수단: 도보
# 입력: 25.0 → 출력: 거리: 25.0km\n추천 교통수단: 지하철


# 사용자로부터 거리를 입력받기
distance = float(input())

# 거리가 2km 이상인지, 2km 이상 5km 미만인지, 5km 이상 20km 미만인지, 20km 이상인지 판별
if 2.0 > distance:
    # 거리가 2km 미만인 경우 "도보" 저장
    transport = "도보"

elif 2.0 <= distance < 5.0:
    # 거리가 2km 이상 5km 미만일 경우 "자전거" 저장
    transport = "자전거"

elif 5.0 <= distance < 20.0:    
    # 거리가 5km 이상 20km 미만일 경우 "버스" 저장
    transport = "버스"
    
elif 20.0 <= distance:
    # 거리가 20km 이상일 경우 "지하철" 저장
    transport = "지하철"

# 최종결과 출력
print(f"거리: {distance}km\n추천 교통수단: {transport}")