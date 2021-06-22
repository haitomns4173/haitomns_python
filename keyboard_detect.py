import keyboard  
while True: 
    try:  
        if keyboard.is_pressed('esc'):  
            print('You Pressed A Key!')
            break  
    except:
        break 