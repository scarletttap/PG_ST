import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What's your fave food?")

answer = pg.prompt ("Enter you fave food.")

if answer == "chicken nugs":
    speak.Speak("I love nuggets")
elif answer == "ice cream":
    speak.Speak ("thats really cool. Your cool like ice cream")
elif answer == "rutabega":
    speak.Speak ("sick nasty")
elif answer == "bacon":
    speak.Speak ("Youre not vegan! Oh my gawd you are killing pigs you monster")
else:
    speak.Speak("Your favorite food is" + answer)

speak.Speak ("What youtuber do you want to watch")

video = pg.prompt ("Enter your youtuber below.")

speak.Speak ("Ok lets go find some" + video + "videos on youtube.")

wb.open ("https://www.youtube.com/results?search_query=" + video)

             
