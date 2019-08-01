import random

HP = 50
count = 0

while HP > 0:
    lucky = random.randint(1,10)
    if lucky >= 9:
        damage = random.randint(15,20)
        print(str(lucky) + " :hogeは会心の一撃をあたえた。fooに " + str(damage) + "のダメージ")
    elif lucky >= 3:
        damage = random.randint(1,10)
        print(str(lucky) + " :hogeはfooに " + str(damage) + " のダメージをあたえた")
    else:
        damage = 0
        print("miss")
    HP -= damage
    count += 1
print("fooを倒した")
print("hogeは" + str(count) + "回の攻撃でfooを倒した")
amazonaws
