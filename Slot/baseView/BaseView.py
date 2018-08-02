import os
import time
import logging.config
from common.Slot_Caps import Slot
from selenium.webdriver.support.ui import WebDriverWait


class BaseView(object):
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 3, 0.5)
        self.add_script = "window.frames[0].frames."  # 需要可视化需改为 "window.frames[0].frames."

    # 定位单个元素
    def get_element(self, *loc):
        logging.info("==========find_element==========")
        element = self.wait.until(lambda x: x.find_element(*loc))
        return element

    # 定位一组元素
    def get_elements(self, *loc):
        logging.info("==========find_elements==========")
        elements = self.wait.until(lambda x: x.find_elements(*loc))
        return elements

    # 设置全屏
    def horizontal_screen(self):
        logging.info("==========horizontal_screen==========")
        # self.browser.set_window_size(width=1136, height=660)
        self.browser.maximize_window()

    # 设置竖屏游戏
    def vertical_screen(self):
        self.browser.set_window_size(width=370, height=660)

    # 返回屏幕大小
    def get_window_size(self):
        logging.info("==========get_window_size==========")
        return self.browser.get_window_size()

    # 通过xy坐标滑动屏幕
    def swipe(self, start_x, start_y, end_x, end_y, duration):
        logging.info("==========swipe==========")
        return self.browser.swipe(start_x, start_y, end_x, end_y, duration)

    # 获取时间戳
    def get_time(self):
        logging.info("==========get_Time==========")
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    # 截图
    def get_screen_shot(self, module):
        logging.info("==========get_screen_shot==========")
        times = self.get_time()
        image_file = os.path.dirname(os.path.dirname(__file__)) + "/screenshots/%s_%s.png" % (module, times)
        logging.info("get %s screenshots" % module)
        self.browser.get_screenshot_as_file(image_file)


if __name__ == '__main__':
    browser = Slot.browser()
    bv = BaseView(browser)
    bv.get_time()
