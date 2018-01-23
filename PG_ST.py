import pyautogui as pg
pg. dragTo (200,750, 5)

def m(x,y,n):
    pg.moveTo (x,y,n)

def c(x,y,n,i):
    pg.click(x,y,n,i)

m(200,300,4)
c(1000,400,3,.1)
