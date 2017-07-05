import webbrowser
import time

i = 1
print("This program started on " + time.ctime())
while (i < 4):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    i += 1

