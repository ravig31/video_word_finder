import numpy as np
import win32gui, win32ui, win32con
import pyautogui

h = 0
w = 0
hwnd = None

class WindowCapture:   

    def __init__(self, window_name=None):

        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()

        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception("Window not found: {}".format(window_name))

        #window size and location: [x, y, width, height]
        rect = win32gui.GetWindowRect(self.hwnd)
        x_cord = rect[0]
        y_cord = rect[1]
        self.w = rect[2] - x_cord
        self.h = rect[3] - y_cord
    
    def get_screenshot(self):
    
        #gets image data from windows API
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (0,0), win32con.SRCCOPY)

        #saves the screen capture
        # dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h,self.w,4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        return img

# for x in pyautogui.getAllWindows():  
#     print(x.title)