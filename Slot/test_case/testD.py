import unittest
from common.Slot_Caps import Slot
from common.Common import Common
from businessView.WebGame import WebGame
from businessView.PlayGame import PlayGame
from businessView.WebRecord import WebRecord


class SlotQ2(unittest.TestCase):
    def setUp(self):
        self.browser = Slot.browser()
        self.com = Common(self.browser)
        self.wg = WebGame(self.browser)
        self.pg = PlayGame(self.browser)
        self.wr = WebRecord(self.browser)
        self.csv = "../data/game_list.csv"

    def tearDown(self):
        self.browser.quit()

    def testA(self):
        """季度:Slot-2018-Q2,项目:黄金右脚,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 81)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testB(self):
        """季度:Slot-2018-Q2,项目:人猿泰山,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 82)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testC(self):
        """季度:Slot-2018-Q2,项目:世界杯吉祥物,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 83)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testD(self):
        """季度:Slot-2018-Q2,项目:金球争霸,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 84)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testE(self):
        """季度:Slot-2018-Q2,项目:潘帕斯雄鹰,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 85)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testF(self):
        """季度:Slot-2018-Q2,项目:群星闪耀,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 86)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testG(self):
        """季度:Slot-2018-Q2,项目:激情世界杯,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 87)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testH(self):
        """季度:Slot-2018-Q2,项目:船长宝藏,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 88)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testI(self):
        """季度:Slot-2018-Q2,项目:金靴争霸,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 89)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testJ(self):
        """季度:Slot-2018-Q2,项目:激情球迷,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 90)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(SlotQ2("testB"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
