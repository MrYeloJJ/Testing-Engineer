# coding=utf-8
import csv
import time
import xlrd
import logging.config
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from common.Slot_Caps import Slot
from baseView.BaseView import BaseView


class Common(BaseView):

    # 切换游戏标签页
    def switch_tab_game(self):
        logging.info("==========切换游戏标签页==========")
        try:
            time.sleep(1)
            handle = self.browser.window_handles[-1]
            self.browser.switch_to.window(handle)
        except Exception:
            logging.info("切换游戏标签页 %s Fail!" % self.browser.window_handles)
            self.get_screen_shot("切换游戏标签页 Fail")
            raise

    #
    #
    # ---------------------------------------------------载入场景-------------------------------------------------------
    #
    #

    # 等待进入加载场景
    def wait_for_loading_view_showing(self):
        logging.info("==========等待进入加载场景==========")
        times = 30
        logging.info("设置等在时间 %s 秒" % times)
        start_time = datetime.now()
        logging.info("开始时间: %s" % start_time)
        while True:
            try:
                self.browser.execute_script(
                    "var loading = " + self.add_script + "UIManager.instance.getWindowByName(" +
                    self.add_script + "window.Loading.FUILoadingView.URL, " + self.add_script +
                    "UIManager.instance.commonView);return loading.isShowing;"
                )
                break
            except Exception:
                end_time = datetime.now()
                logging.info("结束时间: %s" % end_time)
                cost_time = (end_time - start_time).seconds
                logging.info("超时时间: %s" % cost_time)

                if cost_time > times:
                    # print("等待" + str(times) + "秒，不会进入loading场景！")
                    logging.error("Wait %s time,不会进入loading场景 Fail!" % str(times))
                    self.get_screen_shot("Wait %s time,不会进入loading场景 Fail" % str(times))
                    raise

    # 载入场景 进度条数值, [tuple: 0]
    def loading_view_progress_bar_value(self):
        logging.info("==========载入场景 进度条数值==========")
        try:
            value = self.browser.execute_script(
                "var loading = " + self.add_script + "UIManager.instance.getWindowByName(" + self.add_script +
                "window.Loading.FUILoadingView.URL, " + self.add_script +
                "UIManager.instance.commonView);return loading.contentPane.m_progressBar.value;"
            )
            return value
        except Exception:
            raise

    # 等待加载完成
    def wait_for_loading_bar_completed(self):
        logging.info("==========等待加载完成==========")
        times = 30
        logging.info("设置等在时间 %s 秒" % times)
        start_time = datetime.now()
        logging.info("开始时间: %s" % start_time)
        while True:
            bar_value = self.loading_view_progress_bar_value()

            end_time = datetime.now()
            logging.info("结束时间: %s" % end_time)
            cost_time = (end_time - start_time).seconds
            logging.info("超时时间: %s" % cost_time)

            if bar_value == 100:
                logging.info("加载进度: %s" % bar_value)
                break
            else:
                if cost_time > times:
                    try:
                        assert bar_value == 100
                        logging.info("加载进度: %s" % bar_value)
                    except AssertionError:
                        # print("等待" + str(times) + "秒，进度条未到100%！")
                        logging.error("Wait %s time,进度条未到100 Fail!" % str(times))
                        self.get_screen_shot("Wait %s time,进度条未到100 Fail" % str(times))
                        raise

    # 载入场景消失, [tuple: None]
    def loading_view_dispear(self):
        logging.info("==========载入场景消失==========")
        try:
            dispear = self.browser.execute_script(
                "return " + self.add_script + "UIManager.instance.getWindowByName(" +
                self.add_script + "window.Loading.FUILoadingView.URL, " + self.add_script +
                "UIManager.instance.commonView);"
            )
            return dispear
        except Exception:
            raise

    # 等待加载场景消失
    def wait_for_loading_view_dispear(self):
        logging.info("==========等待加载场景消失==========")
        times = 30
        logging.info("设置等在时间 %s 秒" % times)
        start_time = datetime.now()
        logging.info("开始时间: %s" % start_time)
        while True:
            try:
                # self.loading_view_dispear()
                self.browser.execute_script(
                    "return " + self.add_script + "UIManager.instance.getWindowByName(" +
                    self.add_script + "window.Loading.FUILoadingView.URL, " + self.add_script +
                    "UIManager.instance.commonView);"
                )
                break
            except Exception:
                end_time = datetime.now()
                logging.info("结束时间: %s" % end_time)
                cost_time = (end_time - start_time).seconds
                logging.info("超时时间: %s" % cost_time)

                if cost_time > times:
                    # print("等待" + str(times) + "秒，loading场景不会消失！")
                    logging.error("Wait %s time,loading场景不会消失 Fail!" % str(times))
                    self.get_screen_shot("Wait %s time,loading场景不会消失 Fail" % str(times))
                    raise

    #
    #
    # ---------------------------------------------------旋转按钮 及 旋转状态-------------------------------------------
    #
    #

    # 显示旋转按钮, [tuple: True, False]
    def start_btn_visible(self):
        logging.info("==========显示旋转按钮==========")
        try:
            final_visible = self.browser.execute_script(
                "return " + self.add_script +
                "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_startBtn.finalVisible;"
            )
            logging.info("return 显示旋转按钮 %s" % final_visible)
            return final_visible
        except Exception:
            raise

    # 旋转按钮可点击否, [tuple: True, False]
    def start_btn_touchable(self):
        logging.info("==========旋转按钮可点击否==========")
        try:
            touchable = self.browser.execute_script(
                "return " + self.add_script +
                "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_startBtn.touchable;"
            )
            logging.info("return 旋转按钮可点击否 %s" % touchable)
            return touchable
        except Exception:
            logging.error("start_btn_touchable Fail!")
            self.get_screen_shot("start_btn_touchable Fail")
            raise

    # 点击旋转按钮, [tuple: True, False]
    def start_btn_click(self):
        logging.info("==========点击旋转按钮==========")
        try:
            click = self.browser.execute_script(
                "return " + self.add_script +
                "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_startBtn.displayObject.event('click');"
            )
            logging.info("点击旋转按钮")
            return click
        except Exception:
            logging.error("start_btn_click Fail!")
            self.get_screen_shot("start_btn_click Fail")
            raise

    # 旋转按钮状态, [str: stopped, playing]
    def start_btn_status(self):
        logging.info("==========旋转按钮状态==========")
        try:
            status = self.browser.execute_script(
                "return " + self.add_script +
                "UIManager.instance.commonView.contentPane.m_gamblingBarViewL.m_startBtn.m_autoGameCtl.selectedPage;"
            )
            logging.info("return 旋转按钮状态 %s" % status)
            return status
        except Exception:
            logging.error("start_btn_status Fail!")
            self.get_screen_shot("start_btn_status Fail")
            raise

    # 滚轴滚动状态, [tuple: True, False]
    def slot_machine_rolling(self):
        logging.info("==========滚轴滚动状态==========")
        try:
            rolling = self.browser.execute_script(
                "return " + self.add_script + "UIManager.instance.mainView.slotMachine.isRolling;"
            )
            logging.info("return 滚轴滚动状态 %s" % rolling)
            return rolling
        except Exception:
            logging.error("slot_machine_rolling Fail!")
            self.get_screen_shot("slot_machine_rolling Fail")
            raise

    #
    #
    # ---------------------------------------------------左侧菜单-------------------------------------------------------
    #
    #

    """
    # 显示左侧主菜单, [tuple: True, False]
    def main_menu_btn_visible(self):
        try:
            final_visible = self.browser.execute_script(
                "return " + self.add_script +
                "UIManager.instance.commonView.contentPane.m_mainMenuL.m_mainMenuBtn.finalVisible;"
            )
            return final_visible
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 左侧主菜单展开状态, [str: retractL, expandLPC, retractP, expandPPC] expandLPC：横展， retractL：横叠， expandPPC：竖展， retractP：竖叠
    def main_menu_expand(self):
        try:
            expand = self.browser.execute_script(
                "return " + self.add_script +
                "UIManager.instance.commonView.contentPane.m_mainMenuL.m_expandCtl.selectedPage;"
            )
            return expand
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 整个左侧菜单可否点击, [tuple: True, False]
    def main_menu_touchable(self):
        try:
            touchable = self.browser.execute_script(
                "return " + self.add_script +
                "UIManager.instance.commonView.contentPane.m_mainMenuL.touchable;"
            )
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击左侧主菜单按钮, [tuple: True, False]
    def main_menu_btn_click(self):
        try:
            click = self.browser.execute_script(
                "return " + self.add_script +
                "UIManager.instance.commonView.contentPane.m_mainMenuL.m_mainMenuBtn.displayObject.event('click');"
            )
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 显示游戏记录按钮, [tuple: True, False]
    def game_record_btn_enable(self):
        try:
            enable = self.browser.execute_script(
                "return " + self.add_script +
                "UIManager.instance.commonView.contentPane.m_mainMenuL.m_gameRecordBtn.enabled;"
            )
            return enable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 游戏记录按钮可点击否, [tuple: True, False]
    def game_record_btn_touchable(self):
        try:
            touchable = self.browser.execute_script(
                "return " + self.add_script +
                "UIManager.instance.commonView.contentPane.m_mainMenuL.m_gameRecordBtn.touchable;"
            )
            return touchable
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    # 点击游戏记录按钮, [tuple: True, False]
    def game_record_btn_click(self):
        try:
            click = self.browser.execute_script(
                "return " + self.add_script +
                "UIManager.instance.commonView.contentPane.m_mainMenuL.m_gameRecordBtn.displayObject.event('click');"
            )
            return click
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise
    """

    #
    #
    # ---------------------------------------------------数据与标签页---------------------------------------------------
    #
    #

    # 封装XlSX数据文件
    @staticmethod
    def get_game_list():
        logging.info("==========获取XlSX-游戏名称数据==========")
        path = "../data/Game_list.xlsx"
        open_file = xlrd.open_workbook(path)
        read = open_file.sheet_by_name("Sheet1")
        game_list = []
        for row in range(read.nrows):
            game_name = read.row_values(row)
            game_list.append(game_name)
        logging.info("返回整个游戏名称数组")
        return game_list

    # 封装CSV数据文件
    @staticmethod
    def get_csv_data(csv_file, line):
        logging.info("==========获取CSV-游戏名称数据==========")
        with open(csv_file, "r", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    logging.info("根据索引返回单个游戏名称")
                    return row

    # 关闭除大厅外全部标签页
    def close_all_tab(self):
        logging.info("==========关闭除大厅外全部标签页==========")
        try:
            while 1 < len(self.browser.window_handles):
                time.sleep(1)
                self.browser.switch_to.window(self.browser.window_handles[-1])
                self.browser.close()

            self.browser.switch_to.window(self.browser.window_handles[0])
        except Exception:
            logging.error("Close Tab Fail!")
            self.get_screen_shot("Close Tab Fail")
            raise


if __name__ == '__main__':
    browser = Slot.browser()
    com = Common(browser)
    csv_file = "../data/game_list.csv"
    data = com.get_csv_data("../data/game_list.csv", 80)
    print(data)
