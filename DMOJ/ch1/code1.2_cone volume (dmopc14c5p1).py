# 문제코드
# dmopc14c5p1

# 문제명
# Cone Volume(원뿔 부피)

# 입력
# 첫 번째 줄에 반지름이 입력된다.
# 두 번째 줄에 높이가 입력된다.

# 출력
# 원뿔의 반지름을 출력한다. (10^-2)

# 문제에 필요한 로직
# 원뿔 부피 = PI * r**2 * h / 3 
# math 모듈을 통해 pi를 불러 온다.

import math 

r = int(input())
h = int(input())

print( math.pi * r**2 * h / 3)

