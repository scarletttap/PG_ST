import pyautogui as pg
import time
import webbrowser

points = 0

#Question goes here
answer = pg.prompt(
"""
What food would you eat?

a) acai bowl
b) ice cream
c) Cheeseburger

"""
     )
pg.alert("You chose " + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
    
#Question goes here
answer = pg.prompt(
"""
Which activity would you do?

a) dance around your room
b) soccer!
c) cry alone in your room to sad music

"""
     )
pg.alert("You chose " + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

    #Question goes here
answer = pg.prompt(
"""
Whats your favorite makeup product?

a) concealer, you keep it natural
b) A blinding highlight, ya girl loves a glow
c) black eyeliner to define those eyes.

"""
     )
pg.alert("You chose " + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

#Question goes here
answer = pg.prompt(
"""
Whats your favorite thing to wear?

a) cute ripped jeans and a basic tee.
b) highwaisted jeans and a colorful tank.
c) A deep v neck shirt and calvin klein joggers.

"""
     )
pg.alert("You chose " + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
    
#Question goes here
answer = pg.prompt(
"""
Whats your favorite drink?

a) a fresh G&T smoothie
b) TEA
c) Water! Hydrate or die!!

"""
     )
pg.alert("You chose " + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
    
#Question goes here
answer = pg.prompt(
"""
What is your chosen accessory?

a) a couple dainty rings
b) hoop earrings
c) headphones, music gets me through the day.

"""
     )
pg.alert("You chose " + answer)

#Answers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
# End of Survey
pg.alert ("Ok, here's what friend you are...")
#Neeley is first
if points < 9:
    pg.alert (" You are Neeley!")
    webbrowser.open ("http://www.lovethispic.com/uploaded_images/118954-Blonde-On-The-Beach.jpg")          
#Mercy is second
elif points >=9 and points <=14 :
    pg.alert (" You are Mercy! ")
#Kendall is last
elif points >19:
    pg.alert (" You are Kendall!")
    webbrowser.open ("https://i.pinimg.com/736x/17/f3/de/17f3de0e3f7a4df4710153d39833be50--teenage-outfits-adidas-brand.jpg")

