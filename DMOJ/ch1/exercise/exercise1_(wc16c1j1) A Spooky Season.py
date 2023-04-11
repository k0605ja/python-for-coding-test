# 문제코드
# wc16c1j1

# 문제명
# A Spooky Season(무시무시한 계절)

# 입력
# 정수 S가 입력 된다. (5 < s < 20)

# 출력
# 주어진 수 만큼 o를 출력한다. (Spooky 형태)

# Sample Input
# 5

# Sample Output
# spoooooky

# 문제에 필요한 로직
# 1. 정수를 입력 받기 위해 input() 메소드를 int()로 형변환한다.
# 2. 문자열을 + 연산자를 사용해서 연결해서 요구하는 형태대로 출력되도록 한다.
# 3. 입력된 수를 문자 o와 곱하여 출력한다.  


S = int(input())

print('sp' + 'o' * S + 'ky') 