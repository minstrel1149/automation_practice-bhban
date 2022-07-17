# 책 프로그램 대신 가급적이면 pyautogui를 사용하는 것에 익숙해지기
import pyautogui as pag
import pyperclip

pag.position()
pag.size()
pag.moveTo(400, 800, duration=0.5)
pag.click()
pag.scroll(-500, x=500, y=500)
pag.moveTo(1400, 500, duration=0.1); pag.dragTo(400, 200, duration=0.5)
pag.pixel(1200, 600)
pag.pixel(pag.position()[0], pag.position()[1])
# 한글은 입력이 안되어서 책 파일 활용 필요 "import pywinmacro as pw"
# 혹은 pyperclip과 같이 활용(pyperclip.copy('안녕'); pag.hotkey('ctrl', 'v'))
pag.click(pag.position()); pag.write('Hello', 0.25); pag.write(['backspace'], 0.5)
pyperclip.copy('안녕'); pag.click(pag.position()); pag.hotkey('ctrl', 'v')