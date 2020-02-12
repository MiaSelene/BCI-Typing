import pyautogui
#dimensions to be added
click = ''
lr = ''
ud = ''
enter = ''
space = ''
locking_mechanism = ''

keys = ['qwertzuiop',
        'asdfghjkl',
        'yxcvbnm'
        ]
current_row = 0
current_letter = 'q'
while True:
    posx, posy = pyautogui.position()
    if posx**2 + posy**2 < 3:
        break
    if int(6*max(0,(posy/800) - 0.5)) != current_row:
        current_row = int(6*max(0,(posy/800) - 0.5))
    if keys[current_row][int(len(keys[current_row])*(posx / 1440))] != current_letter:
        current_letter = keys[current_row][int(len(keys[current_row])*(posx / 1440))]
        pyautogui.typewrite(current_letter)
