import time
import logging.config
from datetime import datetime
from common.Common import Common
from common.Slot_Caps import Slot
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from businessView.WebGame import WebGame
from businessView.PlayGame import PlayGame


class WebRecord(Common):
    # 游戏记录相关元素
    query_button = (By.XPATH, "//button[contains(@class, '--primary')]")

    # 启动新的标签页
    def start_web_record(self):
        logging.info("==========启动新的标签页==========")
        try:
            js = "window.open('https://static.fg.blizzmi.cn/we_token')"
            self.browser.execute_script(js)
            self.browser.implicitly_wait(2)
        except Exception:
            logging.error("Start Record Fail!")
            self.get_screen_shot("Start Record Fail")
            raise

    # 检查游戏记录标题
    def check_record_title(self):
        logging.info("==========检查游戏记录标题==========")
        try:
            title = self.browser.title
            assert title == "游戏详情"
        except AssertionError:
            logging.error("Check record title Fail!")
            self.get_screen_shot("Check record title Fail")
            raise

    # 切换Web游戏记录标签页
    def switch_tab_web(self):
        logging.info("==========切换Web游戏记录标签页==========")
        try:
            time.sleep(1)
            handle = self.browser.window_handles[-1]
            self.browser.switch_to.window(handle)
        except Exception:
            logging.error("切换Web游戏记录标签页 %s Fail!" % self.browser.window_handles)
            self.get_screen_shot("切换Web游戏记录标签页 Fail")
            raise

    # 点击查询按钮
    def click_query_button(self):
        logging.info("==========点击查询按钮==========")
        try:
            self.browser.find_element(*self.query_button).click()
        except NoSuchElementException:
            logging.error("Click query button Fail!")
            self.get_screen_shot("Click query button Fail")
            raise

    # 检查是否有最新记录且显示在第一行位置
    def new_record(self, game_name):
        logging.info("==========检查是否有最新记录且显示在第一行位置==========")
        times = 40
        logging.info("设置等在时间 %s 秒" % times)
        start_time = datetime.now()
        logging.info("开始时间: %s" % start_time)
        while True:
            try:
                game_element = self.browser.find_elements_by_xpath("//div[text()='" + game_name + "']")
                if len(game_element) == 0:
                    one_game = self.browser.find_element_by_xpath("//div[text()='" + game_name + "']").text
                    assert one_game == game_name
                else:
                    game_text = game_element[0].text
                    assert game_text == game_name

                end_time = datetime.now()
                cost_time = (end_time - start_time).seconds
                logging.info("%s 秒找到最新记录" % cost_time)
                return True
            except AssertionError and NoSuchElementException:
                end_time = datetime.now()
                logging.info("结束时间: %s" % end_time)
                cost_time = (end_time - start_time).seconds
                logging.info("超时时间: %s" % cost_time)
                if cost_time <= times:
                    self.click_query_button()
                else:
                    logging.error("No latest record!")
                    self.get_screen_shot("No latest record")
                    return False

    # 打开游戏记录
    def open_record(self):
        logging.info("==========打开游戏记录==========")
        self.start_web_record()
        self.switch_tab_web()
        self.check_record_title()
        self.click_query_button()


if __name__ == '__main__':
    browser = Slot.browser()
    wg = WebGame(browser)
    pg = PlayGame(browser)
    wr = WebRecord(browser)
    wg.all_agg("激情世界杯")
    pg.execute_wait_lading()
    wr.open_record()
