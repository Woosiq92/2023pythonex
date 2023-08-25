# 1. 월을 입력받아 계절 표시하기 

month = int(input('월을 입력하세요 : '))

if month >= 3 and month <= 5 :
    print('%d월은 봄입니다.' % month)

if month >= 6 and month <= 8 :
    print('%d월은 여름입니다.' % month)

if month >= 9 and month <= 11 :
    print('%d월은 가을입니다.' % month)

if month == 12 or month == 1 or month == 2 :
    print('%d월은 겨울입니다.' % month)
  
# 2. 4의 배수인지, 5의 배수인지 판별

num = int(input('숫자를 입력하세요 : '))
result = '4의 배수도 5의 배수도 아니다.'

if num%4 == 0 :
    result = '4의 배수이다'    
if num%5 == 0 :
    result = '5의 배수이다'
if num%4 == 0 and num%5 == 0 :
    result = '4의 배수이면서 5의 배수이다.'

print('%d은(는) %s' % (num, result))


# 3. 모음/ 자음 판변하기 

char = input('영어 알파벳을 입력하세요 : ')

char2 = char.upper()

if char2 == 'A' or char2 == 'E' or char2 == 'I' or char2 == 'O' or char2 == 'U' :
    print('%s은(는) 모음이다.' % char)
else :
    print('%s은(는) 자음이다.' % char)
