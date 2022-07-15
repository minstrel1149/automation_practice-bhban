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
import time
import pyperclip


class NewsBot:
    def __init__(self):
        # ���� ���̽��� �����մϴ�.
        self.querry ="https://www.google.com/search?tbm=nws&q="
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        self.options.add_argument("--window-size=1600,900")
        # ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        # ������ ������ ������ ������ ����ϴ�.
        self.news_list = []
        self.news_text = ""
        # �ϴ� Ʈ���� �α���ȭ������ ���ϴ�.

    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

    # �˻��� �ǽ��մϴ�.
    def search(self, keyword):
        self.driver.get(self.querry + keyword)
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(3)

    # �������� ���ΰ�ħ�մϴ�.
    def refresh(self):
        pw.key_press_once("f5")

    # �������� ��� ������ �����ϰ� Ŭ�����忡 �����մϴ�.
    def copy_all(self):
        pw.ctrl_a()
        # �� �� �������� �� �� ���� �ֽ��ϴ�. �ѱ����� �ټ��� �����ݽô�.
        time.sleep(1)
        pw.ctrl_c()
        time.sleep(1)
        pw.ctrl_c()
        time.sleep(1)
        pw.ctrl_c()

    # �������� ��� ������ ������ ���� ��縸 �̾Ƴ��� �Լ��Դϴ�.
    def scrap_news(self):
        # �ϴ� �������� ��� ���빰�� �����մϴ�.
        self.copy_all()
        # ���� ����Ʈ�� �ʱ�ȭ�մϴ�.
        self.news_list = []
        # �ؽ�Ʈ�� Ŭ�����忡�� ������ ��Ʈ������ �� �ɴϴ�.
        self.news_text = pyperclip.paste()
        # �� �پ� �ɰ��ݴϴ�.
        splt = self.news_text.split("\n")

        # ���� ������ �̹��� ����, ������, �Խ� �ð�, ���� ��� ������ ������ �����˴ϴ�.
        # ���빰�� �� �پ� �����鼭 ������ ������ ���ô�.

        # ���ڵ��� �� �پ� �ҷ��ɴϴ�.
        for i, line in enumerate(splt):
            # ���̰� �ʹ� ª�� ���� �ǳʶݴϴ�. ������ ���ɼ��� Ů�ϴ�.
            if len(line.strip()) < 3:
                continue
            # ������ �ۼ� ������ �˷��ִ� ���ڰ� �����ϸ� ���� 3�� ���� �̾ƿ� �ϳ��� ���� �ݴϴ�.
            elif line.strip()[-3:] in "�� ��  �� ��  �� ��  �ð� ��  �� ��  �� ��":
                new_news = "\n".join(splt[i - 3:i])
                # ������� ������ news_list�� �����մϴ�.
                self.news_list.append(new_news)

    # ���� ��縦 ���ۿ��� �˻��� ��, ����Ʈ�� �ٵ�� �Լ��Դϴ�.
    def news_crawler(self, keyword):
        self.search(keyword)
        self.scrap_news()

    # ��ũ������ �����ϴ� �Լ��Դϴ�.
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # Ʈ���� �������� �����ϴ� �޼����Դϴ�.
    def go_to_twitter(self):
        # Ʈ���� Ȩ�������� �̵��մϴ�.
        self.driver.get("http://twitter.com/login")
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(2)

    # Ʈ���� Ȩ���� �̵��ϴ� �޼����Դϴ�.
    def twitter_home(self):
        self.driver.get("https://twitter.com/home")
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(2)

    # �α����� �����ϴ� �޼����Դϴ�.
    def login(self, id, ps):
        self.go_to_twitter()
        # ���̵� �Է��մϴ�.
        pw.typing(id)
        # tab Ű�� �����ݽô�. ��κ��� ����Ʈ���� ��ȣâ���� �̵��մϴ�.
        pw.key_press_once("tab")
        # ��й�ȣ�� ���� �Է��մϴ�.
        pw.typing(ps)
        # ����Ű�� �����ݴϴ�. ��κ��� ����Ʈ���� �α����� ����˴ϴ�.
        pw.key_press_once("enter")
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(5)

    # Ʈ���Ϳ� ���� �ø��� �Լ��Դϴ�.
    def tweet(self, text, interval):
        # ���� ���� �ۼ��ϱ� ���� �ۼ� ���� �������� �̵��մϴ�.
        self.driver.get("https://twitter.com/intent/tweet")
        time.sleep(2)
        # Ŀ���� �⺻������ �Է�â�� �� �ֽ��ϴ�. Ʈ�� ������ �Է��մϴ�.
        pw.type_in(text)
        time.sleep(1)
        # ��Ʈ�� Ű�� ����Ű�� ������ Ʈ���� �Էµ˴ϴ�.
        pw.key_on("control")
        pw.key_on("enter")
        pw.key_off("control")
        pw.key_off("enter")

        # �ε� �ɶ����� �� �� ��ٸ��ϴ�.
        time.sleep(interval)

    # ��ũ���� ��� ������ Ʈ���Ϳ� �ø��� �Լ��Դϴ�.
    # 15�� �������� ������ �ø��ϴ�. �ð� ������ �ٲٰ� ������ �Լ��� ȣ���� �� �ð��� �ʴ����� �Է��մϴ�.
    # �ؽ��±׸� �Է��� ��� �Բ� �����մϴ�.
    def tweet_all(self, hashtags="", interval=15):
        for el in self.news_list:
            self.tweet(el.strip() + " " + hashtags, interval)

    # ���ۿ��� ������ �˻��ϰ�,
    # Ʈ���Ϳ� �ڵ����� �α��� �� ��,
    # �ܾ�� ��� ������ ���ε���� �ϴ� �Լ��Դϴ�.
    # 15�� �������� ������ �ø��ϴ�. �ð� ������ �ٲٰ� ������ �Լ��� ȣ���� �� �ð��� �ʴ����� �Է��մϴ�.
    # �ؽ��±׸� �Է��� ��� �Բ� �����մϴ�.
    def tweet_all_news(self, keyword, hashtags="", interval=15):
        self.news_crawler(keyword)
        self.twitter_home()
        self.tweet_all(hashtags, interval)
        time.sleep(interval)
