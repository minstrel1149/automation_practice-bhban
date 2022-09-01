import pyautogui as pag

position = pag.position()
pag_color = pag.color(position[0], position[1])

print(f'Your mouse position is {position}')
print(f'Color is {pag_color}')