import webbrowser
import time
a = 0
b = 0
while b < 5:
  if a ==0:
      time.sleep(5400)
      a = 1
      if a == 1:
          webbrowser.open_new("https://www.youtube.com/watch?v=CAwiyQTA4s0")
          time.sleep(450)
          a = 0
          b += 1

