import webbrowser
import time
import random
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

    
print("bitte beantworte alle fragen in sekunden")
gesamtZeit = input("Wie lange möchtest du Arbeiten? :")
arbeitsZeit = input("Wie lange möchtest du arbeiten bevor eine pause beginnt? :")
pausenLänge = input("Wie lange soll eine pause dauern? :")
while d < int(gesamtZeit):
  if c ==0:
      time.sleep(int(arbeitsZeit))
      d += int(arbeitsZeit)
      f += int(arbeitsZeit)
      print("Du hast schon seit " + str(f) + " Sekunden gearbeitet")
      c = 1
      if c == 1:
          webbrowser.open_new("https://www.youtube.com/watch?v=CAwiyQTA4s0")
          e += 1
          print("Das ist deine " + str(e) + " Pause")
          frage = input("Möchtest du das Warmup spielen? :")
          if frage == "ja":
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
                time.sleep(int(pausenLänge))
                c = 0
                d += int(pausenLänge)
            elif b == 1:
                print("Du hast gewonnen!")
                time.sleep(int(pausenLänge))
                c = 0
                time.sleep(int(pausenLänge))
                d += int(pausenLänge)
            else:
                print("Error")
                time.sleep(int(pausenLänge))
                c = 0
                d += int(pausenLänge)
          else:    
             time.sleep(int(pausenLänge))
             c = 0
             d += int(pausenLänge)
          
print("Arbeit beendet!")
