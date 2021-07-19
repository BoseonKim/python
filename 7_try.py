#1.8 예외처리

try:
    print(1)
    a=10/0
    print(a)
except ZeroDivisionError:
    print("0으로 나누면 안됩니다")
print("안녕")

try:
    print(1)
    a=10/0
    print(a)
except IndexError:
    print("Index Error")
except ZeroDivisionError:
    print("0으로 나누면 안됩니다")
print("안녕")


a_list=[]
try:
    print(1)
    a_list[100]
    print(a)
except IndexError:
    print("Index Error")
except ZeroDivisionError:
    print("0으로 나누면 안됩니다")
print("안녕")

#---------------------------------------------------------

class Naver:
    def crawl(self):
        print("네이버 크롤링")

class Twitter:
    def crawl(self):
        print("트위터 크롤링")

class Yahoo:
    def crawl(self):
        print("야후 크롤링")

crawl_target_list=[Naver(),Twitter(),Yahoo()]


class Naver:
    def crawl(self):
        print("네이버 크롤링")

class Twitter:
    def crawl(self):
        a=0/0
        print("트위터 크롤링")

class Yahoo:
    def crawl(self):
        print("야후 크롤링")

result_list=[]
for site in crawl_target_list:
    try:
        result=site.crawl()
    except Exception:
        print("나한테 에러가 났다고 문자를 보냈다")
    else:
        result_list.append(result)

