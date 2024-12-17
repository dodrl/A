my_name='yewon'
my_age=20
deed=False
print("hello my name is",my_name)
print("and my age is", my_age, "yearS ald")
it='uhyun is poop'
print("I think", it)
iu='love you'
print("but i", iu , 'uhyun!!')

d='my dad'
s='smoking'
print('to',d,)
print('dad, stop',s)

def say_hello():
    print("hello how r u")
say_hello()
print("hello would")

def say_bye():
    print("bye bye")

say_bye()
print("would")

def say_hello(user_name):
    print("hello",user_name,"how a u?")

say_hello("uhyun")
say_hello("amy")
say_hello("mom")

def say_hello(user_name, user_age):
    print("hello",user_name)
    print('Are you', user_age, "years old?")
say_hello("yewon", 20)
say_hello("mom",47)
say_hello("dad", 48)

def tax_calculator(money):
    print(money*0.35)
tax_calculator(120000)
tax_calculator(17000)
tax_calculator(200000)
tax_calculator(35000)
tax_calculator(9292229)

t = "윤석열"
p = "김건희"
j = "울 쥴리가 원하면 진행시켜. 오빠 한다면 하는놈이야(한남아님) 좋아 빠르게 가!"
print(p,"는 말했다 오빠 나 계란말이이가 먹고싶어 ",t + "는 말했다 ",j,"!!!!")

def institution(assemblyman,개새끼):
    print("우와" , assemblyman, "이다!")
    print(개새끼)
institution("이재명","찢어!!")
institution("박원순", "킁킁!!!")

def say_hello(user_name="anonymous"):
    print("hello",user_name)
say_hello("yewon")
say_hello()

def plus(a=0,b=0):
    print(a + b)
plus(1,2)
plus()

def minus(a=0,b=0):
    print(a - b)
minus(2,6)
minus()

def multiplication(a=0,b=1):
    print(a * b)
multiplication(7,4)
multiplication()

def division(a=0,b=1):
    print(a / b)
division(9,3)
division()

def power_of(a=0,b=1):
    print(a**b)
power_of(4,2)
power_of()
# 0.35를 곱한값이 리턴돼서 기능을 수행하는 함수

def tax_clac(money):
    return money * 0.35
    
def pay_tax(tax):
    print("thank you for paying", tax)

to_pay = tax_clac(150000000)
pay_tax(to_pay)

name="yewon"
age=20
eyes="black"

print(f"my name is {name} and my age is {age}, i have {eyes}eyes")
#f뒤에는 반드시 "" 를 넣고 변수는 {} 를 쓴다

def make_juice(fruit):
    return f"{fruit} + 🥤"
def add_ice(juice):
    return f"{juice} + 🧊"
def add_sugar(iced_juice):
    return f"{iced_juice} + 🍬"
d= make_juice("🍎") #=🍎 + 🥤
p= add_ice(d) #=🍎 + 🥤 + 🧊
t= add_sugar(p) #=🍎 + 🥤 + 🧊 + 🍬
print(t)

# f는 변수를 간단히 문자롷 표현하기위한 한가지 방법이며 f를 사용하지 않아도 가능하지만 간단히 하귀위함
# def make_juice(앙):
#     return 앙 + "🥤"
# def add_ice(음):
#     return 음+"+🧊"
# def add_suugar(어):
#     return 어+"+🍬"
# t= make_juice("🍎+")
# p= add_ice(t)
# a=add_sugar(p)
# print(a)