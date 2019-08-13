###文字列
"""
a = '''<html>hogehoge \n
foobar</html>'''
print (a)
"""

###数値
"""
x = 3
x += 10
print (x)
"""

###文字列
"""
y = "あああ\n"
y += "いいい"
print (y)
"""

###フォーマット
"""name = "basil"
score = 95.2
print("name: {0}, score: {1}" .format(name, score))
print("name: {0:>s}\nscore: {1:>.3f}" .format(name, score))
print("name: {0:>15s}\nscore: {1:>15.3f}" .format(name, score))
"""

###if文
"""
score = int(input("score? "))

if score > 80:
    print("Great")
elif score > 50:
    print("Good")
elif score > 30:
    print("Bad")
else:
    print("so so...")

print("Good" if score > 60 else "soso...")
"""

###while
"""
i = 0
while i < 35:
#    print(i)
    i += 1
    if i == 15:
#        break
        continue
    print(i)
else:
    print("end")
"""

###for 変数 in データ集合
"""
i = 0
for i in range(30):
#    print(i)
    i += 1
    if i == 15:
        continue
    print(i)
else:
    print("end")
"""

###関数 def

def say_hi(name, age):
#    print("hi {0}, {1}".format(name, age))
    print("hello {0}\n {1:7}才".format(name, age))
say_hi("sato", 20)
say_hi("tanaka", 30)
say_hi(age = 40, name = "hogeo")
