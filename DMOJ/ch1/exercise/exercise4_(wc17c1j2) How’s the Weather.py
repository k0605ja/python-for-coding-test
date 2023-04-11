# 문제코드
# wc18c1j2

# 문제명
# An Honest Day's Work

# 입력
# 정수로 섭씨온도(C)가 입력 된다. 

# 출력
# 입력된 섭씨온도를 화씨온도로 변환하여 출력한다. 

# Sample Input
# 20

# Sample Output
# 68

# 문제에 필요한 로직
# 섭씨온도(C) = 5 / 9 * (F - 32)
# 화씨온도(F) = C + 32 * (9 / 5)

c = int(input())

# print( c + 32 * 9 / 5 )
print( c * 9 / 5 + 32 )



