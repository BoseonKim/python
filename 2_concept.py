#1.1 변수 (Variable)
#1.1.1 간단한 컴퓨터 구조와 램(RAM)
#1.1.2 변수 할당하기
a=1
my_first_number=1

#1.1.3 변수를 쓰는 이유
#재활용성
print(1)
print(2)

target=3
target=10-12

#------------------------------------------------------------------------

#2.2 자료형
#2.2.1 숫자형(Integer, float)

"""
자료형
: RAM에서 변수를 저장하는 형식
: 컴퓨터가 추후에 변수관련 연산을 할 때 용이하게 해줌
: 클래스 (Class)
"""

# 숫자(Integer, float)
a=1
b=2.3
c=-5

#C언어의 경우
"""
int a=1
float b=3.2
"""

#------------------------------------------------------------------------

#2.2.2 리스트(list)
#2.2.2.1 list가 필요한 이유
a=90
b=30
c=60
#변수가 여러개 필요할 경우->학급과 같이 관리해야 될 때
class_score=[90,30,60]
#class_score=list([90,30,60])
type(class_score)
class_score=[1,2,[1,2]]

#2.2.2.2 indexing
#0부터 시작하는 이유
#-1 indexing
#"범위" 인덱싱
class_score[1]
class_score[2]
class_score[-1]
class_score[-2]
class_score[0:2]
type(class_score[1])
type(class_score[0:1])
class_score[:1]
class_score[1:]
class_score[:]
class_score[-2:]

#2.2.2.3 다차원 리스트
[[1,2],[1,2,3]]
"""
[
    [1,2],
    [1,2,3],
]
"""

#------------------------------------------------------------------------

#2.2.3 튜플(tuple)
a=(1,2)
type(a)
a[1]

a=[1,2]
a[0]=3
a
a=(1,2)
#a[0]=3

#튜플과 리스트는 다르다. immutable vs mutable

#------------------------------------------------------------------------

#2.2.3 문자열(string)
#문자열=스트링(string)=문자열 스트링(string)

a="안녕하세요"

#2.2.4.1 indexing
a[0]
a[-1]
a[:-2]

#------------------------------------------------------------------------

#2.2.5 딕셔너리(dict)
my_dict={123:456, "my_key":1000}
my_dict=dict(my_value=456, my_key=1000)

#2.2.5.1 메모리에 저장되는 방식
#Hashtable

#2.2.5.2 리스트와의 차이
#2.2.5.2.1 key, value pair
#2.2.5.2.2 Find operation 속도
company_list=["삼성전자", "현대차"]
price_list=[10,90]

company_price_list=[["삼성전자",10],["현대차",90]]

stock_dict={"삼성전자":10, "현대차":90}
stock_dict["삼성전자"]
stock_dict["삼성전자"]=20
stock_dict["하이닉스"]=100
print(stock_dict)

#------------------------------------------------------------------------

#2.2.6 집합(set)
#Hash
a={1,2,3,1}
# a={1,2,3}으로 저장된다

my_list=[1,2,3,4,4]
#my_list=[1,2,3,4,4]
my_new_set=set(my_list)
#my_new_set={1,2,3,4}

#list,dict,set과 같이 1개 이상의 데이터를 담고 있는 자료형을 iterable한 자료형이라고 한다.

#------------------------------------------------------------------------

#2.2.7 불(Bool, Boolean)
a=1
a="abc"
a=True
b=False
#True, False는 예약어임
type(a)

#2.2.7.1 with and, or
3+2
print(True and False)
print(True and True)
print(False and False)
print(True or False)
print(False or False)

print(True and True or False)

#2.2.7.2 bool로 받아드려야 하는 낯선 구문들
a=2
print(a<1)
c=a>1
print(c)
a<=1
c=a==3
a!=3
a>1 or a<0
















