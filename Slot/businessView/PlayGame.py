import time
import logging.config
from common.Common import Common
from common.Slot_Caps import Slot
from businessView.WebGame import WebGame


class PlayGame(Common):

    # 等待加载完成
    def loading_pass(self):
        logging.info("==========···等待加载···==========")
        self.wait_for_loading_view_showing()

        self.wait_for_loading_bar_completed()

        self.wait_for_loading_view_dispear()
        logging.info("==========···加载完成···==========")

    # Spin前按钮及滚轴状态
    def spin_first(self):
        logging.info("==========Spin前按钮及滚轴状态==========")
        try:
            assert self.start_btn_visible() is True
            assert self.start_btn_touchable() is True
            assert str(self.start_btn_status()) == "stopped"
            assert self.slot_machine_rolling() is False
        except AssertionError:
            logging.error("Spin first game AssertionError!")
            self.get_screen_shot("Spin first game AssertionError")
            raise

    # 点击Spin按钮
    def spin(self):
        logging.info("==========点击Spin按钮==========")
        self.start_btn_click()
        time.sleep(0.8)

    # Spin后按钮及滚轴状态
    def spin_after(self):
        logging.info("==========Spin后按钮及滚轴状态==========")
        try:
            assert str(self.start_btn_status()) == "playing"
            assert self.slot_machine_rolling() is True
        except AssertionError:
            logging.error("Spin after game AssertionError!")
            self.get_screen_shot("Spin after game AssertionError")
            raise
        else:
            time.sleep(6)

    # 执行spin方法
    def execute_wait_lading(self):
        logging.info("==========集合wait_loading方法==========")
        self.loading_pass()
        logging.info("==========集合spin方法==========")
        self.spin_first()
        self.spin()
        self.spin_after()


if __name__ == '__main__':
    browser = Slot.browser()
    pg = PlayGame(browser)
    wg = WebGame(browser)
    wg.all_agg("激情世界杯")
    pg.execute_wait_lading()
