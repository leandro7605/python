law = input("bist du in einen Land wo man ab 18 volljährig bist?")

if law == "nein": 
    print("Danke fürs antworten hab eine schöhne kindheit!")
if law == "ja":
    monthBirthday = input("In welchen monat bist du geboren? Bitte antworte in einen Zahlenwert.")
    monthCurrent = input("Welchen monat haben wir gerade? Bitte wieder in einen Zahlenwert antworten.")
    ageCheck = int(monthCurrent) - int(monthBirthday)
if ageCheck < 1:
    print("Glückwunsch du bist 18 seit " + str(ageCheck) + "monaten.")
    horrormovie = input("Siehst du dir gernen Horrorfilme ab 18 an?")
    if horrormovie == "ja":
        print("Toll! Was ist dein Lieblings Horrorfilm?")
    elif horrormovie == "nein":
        print("Schade lass uns weiter mit der umfrage machen.")
if ageCheck > 1:
    print ("Du bist noch zu jung komm in " + str(ageCheck) +  " monaten zurück")

