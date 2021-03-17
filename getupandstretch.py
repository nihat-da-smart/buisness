import webbrowser
import time
breaksmax=6
currentbreaks=0
while currentbreaks<breaksmax:
    time.sleep(3600)
    webbrowser.open("https://www.youtube.com/watch?app=desktop&v=xTaoCl1rAdQ")
    currentbreaks = int(currentbreaks)+1

