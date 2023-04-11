# 문제코드
# ccc13j1

# 문제명
# Next In Line(다음줄)

# 입력
# 정수가 한 줄에 하나씩 두 개의 정수가 입력된다.

# 출력
# 입력된 두 정수의 차를 더한 z값을 출력한다.  

# Sample Input 1
# 12
# 15

# Sample Output 1
# 18

# Sample Input 2
# 10
# 10

# Sample Output 2
# 10


x = int(input())
y = int(input())

print ( y + (y - x) )