# 문제코드
# dmopc15c7p2

# 문제명
# World Count(단어 수 세기)

# 입력
# 소문자와 공백으로 구성된 한 줄의 텍스트다.

# 출력
# 입력된 라인의 단어 수를  출력한다.

# 문제에 필요한 로직
# 단어수 = '' + 1

# 1. 문자열은 작은따옴표로 감싼다.
# 2. .count() 메소드를 사용한다.
# 3. 문자열에 있는 단어개수 = 띄어쓰기 + 1 이다.
# 4. 따라서 ''.count + 1 을 한다.


# 'this is a string with a few words'.count('') + 1


line = input()
total_words = line.count(' ') + 1

print(total_words)
