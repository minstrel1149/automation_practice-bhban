#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class ImgCrawler:
    def __init__(self, out_dir):
        # ���� ���̽��� �����մϴ�.
        self.querry ="https://www.google.co.in/search?tbm=isch&q="
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� ��帮���� ����մϴ�. �ּ��� �����ϸ� ��帮���� �۾��� ����˴ϴ�.
        # self.options.add_argument("headless")
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        self.options.add_argument("--window-size=1024,768")
        # ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        # ������� ������ ���͸��� ����մϴ�.
        self.out_dir = out_dir

    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

    # ��ũ������ �����ϴ� �Լ��Դϴ�.
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # Ű���带 ���� �̹������� �˻��ϴ� �Լ��Դϴ�.
    def search_image(self, keyword):
        self.driver.get(self.querry + keyword)
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(5)

    # �̹��� �˻� ȭ�鿡�� ù ��° �̹����� Ŭ���� �̸����� â�� ���� �Լ��Դϴ�.
    def select_picture(self):
        # ���� �˻��� �̹������� <img> �±׷� ������ �ֽ��ϴ�. �� �� �� ���� �±׸� �������ô�.
        picture_element = self.driver.find_element_by_tag_name("img")
        # Ŭ���մϴ�. Ȯ�� �̹��� â�� ��̴ϴ�.
        picture_element.click()
        # 5�� ��ٸ��ϴ�.
        time.sleep(5)

    # �̹��� �˻�â�� Ȯ�뼦�� ���� ���¿��� �̹����� �����ϰ�, ���� �������� �Ѿ�� �Լ��Դϴ�.
    def crawl_one_image(self):
        # Ȯ��� �̹������� �̹��� ��Ҹ� �̾ƿɴϴ�.
        # �� ����� xpath�� '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img' �Դϴ�.
        img_xpath = '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img'
        # �̹��� ��Ҹ� �����ɴϴ�.
        image_element = self.driver.find_element_by_xpath(img_xpath)
        # �̹������� ���� ��ó ��ũ�� �̾Ƴ��ϴ�.
        image_url = image_element.get_attribute("src")
        # �̹����� �� â�� ���� �ҷ��ͼ� �۾��սô�.
        # ����̹� �� ���� ���ϴ�.
        self.driver.execute_script("window.open('');")
        # �� ���� driver.window_handles �ȿ� ����Ʈ�� ����˴ϴ�.
        # ���߿� �߰��� ���ϼ��� ����Ʈ�� �ڿ� �߰��˴ϴ�.
        # ����Ʈ�� �� ���� ���� �����ɴϴ�.
        new_tab = self.driver.window_handles[-1]
        # �� ������ �̵��մϴ�.
        self.driver.switch_to.window(new_tab)
        # �̹��� ��ũ�� �̵��մϴ�.
        self.driver.get(image_url)
        # �ε� �Ǳ���� �� ��ٸ��ϴ�.
        time.sleep(5)
        # ū �̹����� â�� �� �ֽ��ϴ�. �� â���� �̹��� �±׸� �ܾ�ɽô�.
        image = self.driver.find_element_by_tag_name("img")
        # �̹����� �����մϴ�.
        image.screenshot(self.out_dir + "/" + str(time.time()) + ".png")
        # �� ���� �������� �� ���� �ݾ��ݴϴ�.
        self.driver.close()
        # ���� ������ ���ƿɴϴ�.
        self.driver.switch_to.window(self.driver.window_handles[0])

    # ���� �̹����� �Ѿ�� �Լ��Դϴ�.
    def next_image(self):
        # ���� �̹����� �Ѿ�� ���� ���� ��ư�� ã���ϴ�.
        # �� ��ư�� xpath�� '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[1]/a[2]/div' �Դϴ�.
        button_xpath = '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[1]/a[2]/div'
        # ��ư ��Ҹ� �����ɽô�.
        next_button = self.driver.find_element_by_xpath(button_xpath)
        # ��ư�� ���� ���� �̹����� �Ѿ�ϴ�.
        next_button.click()
        # �ε��� ���� ��� ��ٸ��ϴ�.
        time.sleep(2)

    # �ڵ� ����ȭ�� ���� �ڱⰡ �˾Ƽ� ���� �˻��ϰ�, �̹��� ũ�Ѹ��ϴ� �Լ��� ����ϴ�.
    def crawl_images(self, keyword, num=100):
        # �̹��� �˻��� �����մϴ�.
        self.search_image(keyword)
        # ù ��° �̹����� ���� Ȯ��â�� �մϴ�.
        self.select_picture()
        # num �� ��ŭ �ݺ��ϸ� �̹����� �����մϴ�.
        for i in range(num):
            # �̹����� �����ϰ�
            self.crawl_one_image()
            # ���� �̹����� �Ѿ�ϴ�.
            self.next_image()
