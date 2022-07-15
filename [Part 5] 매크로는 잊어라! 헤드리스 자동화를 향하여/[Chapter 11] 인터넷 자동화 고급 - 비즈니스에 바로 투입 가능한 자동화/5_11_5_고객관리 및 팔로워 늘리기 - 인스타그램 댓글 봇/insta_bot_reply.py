#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random


class ReplyBot:
    def __init__(self, replyfile):
        # ���� ���̽��� �����մϴ�.
        self.querry ="https://www.instagram.com/explore/tags/"
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� ��帮���� ����մϴ�. �ּ��� �����ϸ� ��帮���� �۾��� ����˴ϴ�.
        # self.options.add_argument("headless")
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        self.options.add_argument("--window-size=1024,768")
        # ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        # ��� ������ ���� ������ �ҷ��ɴϴ�. ���ڵ��� utf8�� �ƴϸ� �ٲ��ּ���.
        self.replyfile = open(replyfile, encoding="utf8")
        # ��� ���� ����Ʈ�� ����ϴ�.
        self.replylist = self.replyfile.read().split("\n")

    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

    # ��ũ������ �����ϴ� �Լ��Դϴ�.
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # �ν�Ÿ�׷� �α��� �Լ��Դϴ�.
    def login(self, id, ps):
        # �α��� �������� �̵��մϴ�.
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        # �ε��� ���� 5�� ���� ��ٷ� �ݴϴ�.
        time.sleep(5)
        # ID, PS �Է� ��Ҵ� <input> �±��Դϴ�. ��Ҹ� ã���ݽô�.
        input_field = self.driver.find_elements_by_tag_name("input")
        # ù ��° ��Ұ� ���̵��Դϴ�. ���̵� �Է��մϴ�.
        input_field[0].send_keys(id)
        # ��й�ȣ �Է� ��Ҵ� �� ��°�Դϴ�. ��й�ȣ�� �Է��մϴ�.
        input_field[1].send_keys(ps)
        # ����Ű�� �ļ� �α����� �������մϴ�.
        input_field[1].send_keys(Keys.RETURN)
        # 10�� ���� ��ٷ� �ݴϴ�.
        time.sleep(5)

    # �ν�Ÿ�׷����� �±׸� �˻��ϴ� �Լ��Դϴ�.
    def search_tag(self, tag):
        self.driver.get(self.querry + tag)
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(5)

    # �±� �˻� ȭ�鿡�� �ֱٿ� �Խõ� ù ��° ������ ��� Ŭ���մϴ�.
    def select_picture(self):
        # �ֱ� ������ xpath�� �Ʒ��� �����ϴ�.
        recent_picture_xpath = '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]'
        # �ֱ� ������ ��Ҹ� �����ɴϴ�.
        recent_picture = self.driver.find_element_by_xpath(recent_picture_xpath)
        # �ֱ� ������ Ŭ���մϴ�.
        recent_picture.click()

    # �˻�������� ���ƴٴϸ� ������ ���ƿ並 ������ ��۵� ��ϴ�.
    # num���� �� ���� �Խù��� ���ƿ� ���� �Է��մϴ�.
    # -1�� �Է��ϸ� ����ڰ� ���� �����ϱ� ������ ������ ����մϴ�.
    def press_like_and_reply(self, num):
        # �ݺ� ȸ���� �����ϱ� ���� �����Դϴ�.
        count = num
        # count �� 1���� ���̸鼭, 0�� �ɶ����� �ݺ��մϴ�.
        # num�� -1�� ��� ��� 0���� �۾����⸸ �ϰ� 0�� ������ �����Ƿ� ������ ����˴ϴ�.
        while count != 0:
            # ���ƿ� ��ư�� �±׸� ���� ã��� ����ϴ�. ���ƿ� ��ư�� <svg> �±׷� ������� �ִµ�
            # �� ȭ�鿡 <svg> �±׸� ���� �ִ� ��ư�� �� �� ���� �ƴմϴ�.
            # �׷��Ƿ� �ϴ� <svg> �±׸� ���� ��Ҹ� ���� ����ɴϴ�.
            svg = self.driver.find_elements_by_tag_name("svg")
            # <svg> �±״� ���ο� aria-label �̶�� �̸��� ��Ʈ����Ʈ�� ���� �ֽ��ϴ�.
            # �� ��Ʈ����Ʈ�� '���ƿ�' �� svg��Ҹ� ã�Ƴ� Ŭ���սô�.
            # for ������ �ϴ� svg �±׵��� ������ �ҷ��ɴϴ�.
            for el in svg:
                # �±� ������ aria-label ��Ʈ����Ʈ�� ���ƿ� �� ��츸 ��Ƴ��ϴ�.
                # �̹� ���ƿ䰡 ������ �ִ� ��� ��Ʈ����Ʈ ���� "���ƿ� ���" �� ����˴ϴ�.
                # ���� �� ����� �̹� ���ƿ並 ���� �� �Խù��� �ǳʶ� �� �ִٴ� ������ �����ϴ�.
                # �̹� ���ƿ並 ���� �Խù��� �ǳʶݴϴ�.
                if el.get_attribute("aria-label") == "���ƿ� ���":
                    break
                # ���ƿ� ��ư�� ã���ϴ�.
                if el.get_attribute("aria-label") == "���ƿ�":
                    # ���ƿ� ��ư�� Ŭ���մϴ�.
                    el.click()
                    # ������ ���� ��ٷ� �ݴϴ�.
                    time.sleep(5)
                    # ��� ���� �� �������� �ϳ��� �̾Ƽ� ����� �޾��ݽô�.
                    # ������ ���� �� �� �� �õ��մϴ�.
                    # �������ؼ� 3���̸� �˴ϴ�.
                    # �̷��� try except���� ���� ���°� ������ ���� ���� ���ƾ� �� �ڵ� ����Դϴ�.
                    try:
                        self.send_reply(random.choice(self.replylist))
                    except:
                        time.sleep(5)
                        try:
                            self.send_reply(random.choice(self.replylist))
                        except:
                            time.sleep(5)
                            self.send_reply(random.choice(self.replylist))
                    # ī��Ʈ�� �� ���� ��Ƴ����ϴ�.
                    count -= 1
                    break
            # ���� �Խù��� �Ѿ�ô�. ���� ��ư���� link text�� "����"���� ����Ǿ� �ֽ��ϴ�. ��Ҹ� ã���ϴ�.
            next_button = self.driver.find_element_by_link_text("����")
            # Ŭ���մϴ�.
            next_button.click()
            # ����� �� �� ���� �ΰ� �޾ƾ� �մϴ�. �� �׷��� �ν�Ÿ ������� ��� ���� �ߴ� ������ �ݴϴ�.
            time.sleep(30)

    # ����� ����� �Լ��Դϴ�.
    def send_reply(self, text):
        # ��� �Է�â�� <textarea> ��� �±׷� �Ǿ� �ֽ��ϴ�.
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys(text + Keys.RETURN)

    # �ڵ� ����ȭ�� ���� �ڱⰡ �˾Ƽ� �ν�Ÿ �α����ϰ�, �˻��ϰ�, ��۵� �� �ٴ�
    def insta_jungdok(self, tag, num=100):
        # �±׵� �˻��ϰ�
        self.search_tag(tag)
        # ���� �� ���� ������ ����
        self.select_picture()
        # ���ƿ並 ������, ����� �޸鼭 ������ �� �徿 �Ѱ��ݴϴ�.
        self.press_like_and_reply(num)
