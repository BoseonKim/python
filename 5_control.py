#1.5 제어문
#1.5.1 if

a=1
if a<5:
    print("야호")
    print("야호")
else:
    print("틀림")
    print("틀림2")

#boolean condition 예시
title="삼성전자 오늘 오를까요?"
a="삼성전자2" in title
print(a)

if "삼성전자" in title:
    print("나한테 이메일을 보낸다")
else:
    print("무시한다")
print(3)

#elif
a=7
if a>10:
    print("a는 10보다 크다")
elif a>5 and a<=10:
    print("a는 5보다 크고 10보다 작다")
elif a>1 and a<=5:
    print("a는 1보다 크고 5보다 작거나 같다")
else:
    print("a는 1보다 작다")

#------------------------------------------------------------------------

#1.6 반복문
#1.6.1 for
a=[1,2,4,5]
for i in a:
    print(i)
    print("룰루")
print(1)

#0부터 99까지 숫자 출력하기
for i in range(5):
    print(i)
    print("랄라")

#50부터 99까지 숫자 출력하기
for i in range(50,55):
    print(i)
    print("헤헤")

#50부터 99까지 짝수 출력하기
for i in range(50,55,2):
    print(i)

#------------------------------------------------------------------------

#1.6.1.2 break/continue
#1.6.1.2.1 break
for i in range(10):
    if i==5:
        break
    else:
        print(i)

for i in range(10):
    print(i)
    if i==5:
        break

#1.6.1.2.2 continue
for i in range(10):
    if i==5:
        continue
    print(i)

for i in range(10):
    if i<5:
        continue
    print(i)

for i in range(10):
    print(i)
    if i<5:
        continue
    elif i==7:
        break

#1.6.1.3 list comprehension
my_list=[]
for i in range(1,11):
    my_list.append(i)

print(my_list)

[wow_tmp for wow_tmp in range(1,11)]

#------------------------------------------------------------------------

#1.6.2 while
#for랑 비슷한데, for에서와 같이 "리스트와 같은 형식의 자료형"이 반드시 필요한 것은 아님
#내부 구문에서 "비교연산"에서 사용되는 변수의 값을 변경하는 로직이 있어야함

#1.6.2.1 for 예제를 while로 바꾸기
a=0
while a<5:
    print(a)
    a=a+1
print("ㅋㅋ")


a=0
while a<=5 or a>2:
    a=a+1
    if a==3:
        continue
    if a==10:
        break
    print(a)

for i in range(1,11,2):
    print(i)

i=1
while i<11:
    if i%2==1:
        print(i)
    i=i+1

#1.6.2.2 while True:
#break와 함께 쓰임
    
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
