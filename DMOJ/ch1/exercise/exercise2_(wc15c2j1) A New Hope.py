# 문제코드
# wc15c2j1

# 문제명
# A New Hope(새로운 희망)

# 입력
# 정수 N이 입력 된다. (1 < s < 5)

# 출력
# 주어진 수 만큼 far을 출력한다.
# far 문자가 2번 이상 출력 되면 ,로 연결된다.

# Sample Input 1
# 1

# Sample Output 1
# A long time ago in a galaxy far away...

# Sample Input 2
# 4

# Sample Output 2
# A long time ago in a galaxy far, far, far, far away...


# 문제 풀이 로직1
# if문을 사용하지 않고 far, 문구는 n-1만큼 출력된다는 규칙을 찾는다.

# 1. 정수 N을 입력 받고 정수로 형변환한다.
# 2. N = 1이면 쉼표 없이 far을 출력한다.
# 3. N >=2이면 쉼표를 포함한 far,을 N-1만큼 출력한다.
# 4. 따라서 문자열 far, 에 입력받은 N-1만큼 곱하여 출력한다.
# 5. 연산자 우선순위는 *가 먼저 계산되므로 N-1 계산을 괄호로 감싸 우선으로 계산되도록 처리한다.
# 6. 따라서 'far, ' * (N-1) 코드를 작성한다. 



# N = int(input())  

# print('A long time ago in a galaxy ' + 'far, ' * (N-1) + 'far away...')


# 문제 풀이 로직 2
# 변수 값을 변경하는 방법을 선택한다. (시간 효율도가 더 높다.)

# 2. 'far, ' * n-1 만큼 곱한 값을 연결하여 값을 출력할 변수값을 변경한다.
# 3. 뒤에 이어질 문구 'far away...'를 연결하고 저장한다.


num_far = int(input())
result = 'A long time ago in a galaxy ' 

result = result + 'far, ' * (num_far - 1) 
result = result + 'far away...'

print(result)