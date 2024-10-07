import random
a = 0
b = 0
geheim =int(random.randint(1,100))
print("Errate meine geheimzahl und gewinne mein gold!")
while a < 7 and b < 1:
    print("Rate!")
    antwort =int(input())
    a += 1
    if antwort < geheim:
        print("Zu niedrig, du Landratte!")
    elif antwort > geheim:
        print("Zu hoch!")
    else:
        b += 1
if a == 7:
    print("Game over!")
elif b == 1:
    print("Du hast gewonnen!")
else:
    print("Error")
    
