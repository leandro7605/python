import random
eins = random.randint(1,6)
counter = 0
while counter < 30:
  print(eins)
  counter = counter +1 #entferne die +1 um dem würfel unendlich zu werfen. Wird python crashen!!!
  print("Anzahl der geworfenen Würfel: ", counter)

  
