import pyautogui
import keyboard
import time
 
def cautare_google():
    if pyautogui.locateOnScreen("lab5.png", confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen("lab5.png", confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(3)
        pyautogui.write("http://youtube.com")
        pyautogui.press('enter')
        time.sleep(3)
 
    if pyautogui.locateOnScreen("yt.png", confidence=0.7) != None:
        camp_yt = pyautogui.locateOnScreen("yt.png", confidence=0.7)
        pyautogui.click(camp_yt)
        time.sleep(3)
        pyautogui.write("zona it")
        pyautogui.press('enter')
        time.sleep(3)

    if pyautogui.locateOnScreen("img.png", confidence=0.7) != None:
        camp_img = pyautogui.locateOnScreen("img.png", confidence=0.7)
        pyautogui.click(camp_img)
        time.sleep(3)
 
    if pyautogui.locateOnScreen("sub.png", confidence=0.7) != None:
        camp_sub = pyautogui.locateOnScreen("sub.png", confidence=0.7)
        pyautogui.click(camp_sub)
        time.sleep(3)

    if pyautogui.locateOnScreen("video.png", confidence=0.7) != None:
        camp_video = pyautogui.locateOnScreen("video.png", confidence=0.7)
        pyautogui.click(camp_video)
        time.sleep(3)

    if pyautogui.locateOnScreen("video1.png", confidence=0.7) != None:
        camp_videoclipuri = pyautogui.locateOnScreen("video1.png", confidence=0.7)
        pyautogui.click(camp_videoclipuri)
        time.sleep(3)

    if pyautogui.locateOnScreen("img2.png", confidence=0.7) != None:
        camp_img2 = pyautogui.locateOnScreen("img2.png", confidence=0.7)
        pyautogui.click(camp_img2)
        time.sleep(3)

    if pyautogui.locateOnScreen("back.png", confidence=0.7) != None:
        camp_back = pyautogui.locateOnScreen("back.png", confidence=0.7)
        pyautogui.click(camp_back)
        time.sleep(3)

    if pyautogui.locateOnScreen("img3.png", confidence=0.7) != None:
        camp_img3 = pyautogui.locateOnScreen("img3.png", confidence=0.7)
        pyautogui.click(camp_img3)
        time.sleep(3)
 
    
time.sleep(3)
cautare_google()


