#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pywinmacro as pw
import pyautogui
import time


class LikeBot:
    def __init__(self, like_button_filename, red_like_button_filename):
        # ���ƿ� ��ư ���� �̸��� �����մϴ�.
        self.like_button = like_button_filename
        self.red_like_button = red_like_button_filename
        # ���� ���̽��� �����մϴ�.
        self.querry ="https://www.instagram.com/explore/tags/"
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        self.options.add_argument("--window-size=1024,768")
        # ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)

    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

    # �������� ���ΰ�ħ�մϴ�.
    def refresh(self):
        pw.key_press_once("f5")

    # ��ũ������ �����ϴ� �Լ��Դϴ�.
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # �ν�Ÿ�׷� �α��� �Լ��Դϴ�.
    def login(self, id, ps):
        # �α��� �������� �̵��մϴ�.
        self.driver.get("https://www.instagram.com/accounts/login")
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(5)
        # �� Ű�� �� �� ������ ���̵� �Է�â���� �̵��մϴ�.
        pw.key_press_once("tab")
        # ���̵� �Է��մϴ�.
        pw.typing(id)
        # �� Ű�� �� �� ���� ��й�ȣ �Է�â���� �̵��մϴ�.
        pw.key_press_once("tab")
        # ��й�ȣ�� �Է��մϴ�.
        pw.typing(ps)
        # ����Ű�� ���� �α����� �õ��մϴ�.
        pw.key_press_once("enter")
        # �ε��� �Ϸ�Ǳ���� ����� ��ٷ��ݴϴ�.
        time.sleep(10)

    # �ν�Ÿ�׷����� �±׸� �˻��ϴ� �Լ��Դϴ�.
    def search_tag(self, tag):
        self.driver.get(self.querry + tag)
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(5)

    # �±� �˻� ȭ�鿡�� ������ ������ �ϳ� �����ϴ� �Լ��Դϴ�.
    def select_picture(self):
        # �� Ű�� ������ ���� �������� �̵��ϴ� ������ ����մϴ�.
        # �˻� ����� ���÷� ������ '���� �ؽ��±�' ������ �Ź� �ٸ��Ƿ�
        # ù ��° ������ ������ �Ź� �ٸ� ȸ���� ���� ������ �մϴ�.
        # ���� ù ��� ������ ����� �˳��ϰ� ���� �����ô�.
        for i in range(20):
            pw.key_press_once("tab")
        pw.key_press_once("enter")
        # ��� ��ٸ��ϴ�.
        time.sleep(5)

    # ���ƿ� ��ư�� ã�Ƽ� ������ �Լ��Դϴ�.
    def press_like(self):
        # ȭ�鿡�� ���ƿ��ư�� ã���ϴ�.
        find = find_on_screen(self.like_button)
        # ȭ�鿡�� ���ƿ� ��ư�� ã�� �� ���� ��츦 ó���մϴ�.
        if not find:
            # �̹� ���ƿ並 ���� ���� ��Ʈ�� �� ��� �ƹ��͵� ���� �ʰ� �Ѿ�ϴ�.
            if find_on_screen(self.red_like_button):
                return True
            # ȭ�鿡�� ��Ʈ�� ã�� �� ���� ��� ���� �޽����� False�� return�մϴ�.
            else:
                return False
        # ���ƿ� ��ư�� ã������ �������ϴ�.
        pw.click(find)
        # �ε��� �ɸ� ���� ������ 1�ʰ� ��ٷ� �ݴϴ�.
        time.sleep(1)
        return True

    # �˻�������� ���ƴٴϸ� ������ ���ƿ並 �����ϴ�.
    # num���� �� ���� �Խù��� ���ƿ並 �������� �����ݴϴ�.
    # -1�� �Է��ϸ� ����ڰ� ���� �����ϱ� ������ ������ ����մϴ�.
    def press_like_buttons(self, num):
        # �ݺ� ȸ���� �����ϱ� ���� �����Դϴ�.
        count = num
        # count �� 0�� �ɶ����� �ݺ��մϴ�.
        while count != 0:
            # ī��Ʈ�� �� ���� ��Ƴ����ϴ�.
            # num�� -1�� ��� ��� 0���� �۾����⸸ �ϰ� 0�� ������ �����Ƿ� ������ ����˴ϴ�.
            count -= 1
            # ���ƿ� ��ư�� ã�� Ŭ���� �õ��մϴ�.
            # self.press_like() �Լ��� Ŭ���� �õ��ϰ� ���ÿ� �������θ� �����ϹǷ� if�� �ȿ� �־��ݴϴ�.
            if not self.press_like():
                # ȭ�鿡�� ���ƿ� ��ư�� ã�� ���� ������ ��� �����޽����� ����ϰ� �����մϴ�.
                print("Cannot find like button. Please check " + self.like_button + " file.")
                exit(1)
            # ���ƿ� ��ư Ŭ���� ���������� ���� �Խù��� �Ѿ�ϴ�. ������ ȭ��ǥ��ư�� ������ �˴ϴ�.
            pw.key_press_once("right_arrow")
            # �ε��� ���� 5�ʰ��� ��ٸ��ϴ�.
            time.sleep(5)

    # �ڵ� ����ȭ�� ���� �ڱⰡ �˾Ƽ� �ν�Ÿ �α����ϰ�, �˻��ϰ�, ���ƿ䵵 �� ������ �޼��带 ����ô�.
    def insta_jungdok(self, tag, num=100):
        # �±׵� �˻��ϰ�
        self.search_tag(tag)
        # ���� �� ���� ������ ����
        self.select_picture()
        # ���ƿ並 �����鼭 ������ �� �� �ѱ�ϴ�.
        self.press_like_buttons(num)


# �̹����� �Է¹޾� ȭ�鿡�� ��ġ�� Ž���մϴ�.
# ȭ�鿡�� �̹����� �߰ߵ��� ���� ��� False�� �����մϴ�.
def find_on_screen(filename):
    a = pyautogui.locateCenterOnScreen(filename)
    if not a:
        return False
    else:
        return a[0], a[1]
