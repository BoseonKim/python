#1.3 함수(function)
#1.3.2 정의/호출 구조
#1.3.2.1 정의하는 방법
def f(wow_x):
    result=wow_x+2
    return result

#1.3.2.2 호출하는 방법
print(f(5))
a=f(1)

#------------------------------------------------------------------------

#1.3.3 default arguments
def wow_f(x,y):
    return x+y

wow_f(3,2)
wow_f(x=3,y=2)
print(wow_f(3,2))

def wow_f(x,y,const=0.1):
    return (x+y)*const

print(wow_f(3,5))
print(wow_f(3,5,0.2))

#------------------------------------------------------------------------

#1.3.4 Return 관련 주의사항
def f(x,y):
    return x+y
print(f(3,4))
a=f(3,4)
# 변수에 저장해야함

#------------------------------------------------------------------------

#1.3.5 함수의 4가지 유형
#input O / output O
def calculate_sum(x,y):
    return x+y

result=calculate_sum(1,2)
print(result)

#input O /output X
def save_data_in_database(x):
    print(x, "를 데이터베이스에 저장하겠습니다")
    print("저장완료 되었습니다")

result=save_data_in_database(3)
print(result)

type(None)

#input X / output O
def get_pi():
    return 3.141592

result=get_pi()
print(result)

#input X / output X
"""
def get_current_time():
    print(time.time(())
"""

#------------------------------------------------------------------------

#1.3.6 함수의 cascading
#func1(func2)
def get_my_lucky_number():
    return 7

def my_sum(x,y):
    return x+y

my_sum(get_my_lucky_number(),5)

lucky_number=get_my_lucky_number()
my_sum(lucky_number,5)
print(my_sum(lucky_number,5))

#1.3.7 함수를 쓰는 이유
#pseudo code
#캡슐화






#------------------------------------------------------------------------
