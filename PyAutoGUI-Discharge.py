import pyautogui
import pywinauto
import pygetwindow as gw
import pyperclip
import time
import os
import cv2
import pandas as pd
os.chdir(r"C:\Users\CHowitt01\OneDrive - States of Guernsey\Desktop\test")

"""
A program that uses screen shots and mouse/keyboard commands to automate a GUI (protected HTML).

"""

def Click_Button(path):
    buttonlocation  = pyautogui.locateOnScreen(path)
    buttonx, buttony = pyautogui.center(buttonlocation)
    pyautogui.click(buttonx, buttony)

def Enter_Record(URN):
    pyperclip.copy(URN)
    time.sleep(4)
    Click_Button('home.PNG')
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1)
    for i in range(0, 11):
        pyautogui.hotkey('shift', 'tab',pause= 0.3)
    time.sleep(1)    
    pyautogui.press('enter')
    time.sleep(10)
    
def Enter_Value(value):
    pyperclip.copy(value)
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    
def Activate_Window(window_title):
    hwnd = gw.getWindowsWithTitle(window_title)
    if hwnd != []:
        try:
            hwnd[0].activate()
        except:
            hwnd[0].minimize()
            hwnd[0].maximize()
            
def Enter_Episode(episode_number):
    Activate_Window("TrakCare")
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'f')
    pyperclip.copy(episode_number)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    Activate_Window("TrakCare")
    pyautogui.hotkey('ctrl', 'enter')
    
def Discharge():
    time.sleep(5)
    Click_Button("EpisodeEdit.PNG")
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.write("D")
    pyautogui.press('tab')
    pyautogui.write("NC001")
    pyautogui.press('tab')
    pyautogui.press('tab')
 
Enter_Record("12345")
Enter_Episode("123456789")
Discharge()


# test if image is on screen

import pyautogui

if pyautogui.locateOnScreen("EpisodeEdit.png", grayscale=True, confidence=0.5) != None:
    print("Image detected!")
