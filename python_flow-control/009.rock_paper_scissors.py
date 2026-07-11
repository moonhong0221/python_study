# [problem]
# 컴퓨터는 항상 바위를 냅니다. 
# 사용자가 낸 값을 입력받아 아래 형식으로 3줄을 출력하시오.
# 컴퓨터: 바위
# 나: {사용자}
# 결과: {결과}

# 결과 기준:
#   사용자가 바위면 비겼습니다
#   사용자가 가위면 졌습니다
#   사용자가 보면 이겼습니다
#   그 외 입력은 잘못된 입력입니다


# computer변수에 "바위"를 저장
computer = "바위"

# 사용자로 부터 입력값 입력 받기
user =  input()

# 입력값이 "바위", "가위", "보"인지 판별
if user == "바위":
    # "바위"이면 "비겼습니다"를 result변수에 저장 후 결과 출력
    result = "비겼습니다"
    print(f"컴퓨터: {computer}\n나: {user}\n결과: {result}")
     
elif user == "가위":     
    # "가위"이면 "졌습니다"를 result변수에 저장 후 결과 출력 
    result = "졌습니다" 
    print(f"컴퓨터: {computer}\n나: {user}\n결과: {result}")

elif user == "보":    
    # "보"이면 "이겼습니다"를 result변수에 저장 후 결과 출력
    result = "이겼습니다"
    print(f"컴퓨터: {computer}\n나: {user}\n결과: {result}")
    
else:    
    # 그 외이면 "잘못된 입력입니다"를 출력  
    print("잘못된 입력입니다")
