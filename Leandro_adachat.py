print("Wie heißt du?")
username = input()
print("Hallo, " + username)
print("möchtest du meinen namen hören? Bitte antworte nur mit ja oder nein.")
antwort = input()
if antwort == "ja":
  print("Mein name lautet Ada")
elif antwort == "nein":
    print("ok, :(")
else:
      print("falsche antwort bitte versuche es erneut.")
      antwort = input()
      if antwort == "ja":
        print("Mein name lautet Ada")
      elif antwort == "nein":
           print("ok, :(")
print("Wie alt bist du?")
alter = input()
print("Du siehst echt jung aus für " + alter)
print("Hat dir das gespräch mit Ada gefallen?")
frage = input()
if frage == "ja":
  print("Das freut mich ich hoffe wir können bald wieder reden.")
else:
    print("Das tut mir leid bitte leite alle beschwerden an Leandro damit er mich verbessern kann, danke!")
