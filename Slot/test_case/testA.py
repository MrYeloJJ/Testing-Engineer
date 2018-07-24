import unittest
from common.Slot_Caps import Slot
from common.Common import Common
from businessView.WebGame import WebGame
from businessView.PlayGame import PlayGame
from businessView.WebRecord import WebRecord


class SlotQ3(unittest.TestCase):
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
        """季度:Slot-2017-Q3,项目:变形金刚,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 1)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testB(self):
        """季度:Slot-2017-Q3,项目:中世纪特权,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 2)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testC(self):
        """季度:Slot-2017-Q3,项目:淘金热,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 3)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testD(self):
        """季度:Slot-2017-Q3,项目:摸金校尉,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 4)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testE(self):
        """季度:Slot-2017-Q3,项目:66路,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 5)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testF(self):
        """季度:Slot-2017-Q3,项目:大秦帝国,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 6)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testG(self):
        """季度:Slot-2017-Q3,项目:阿兹特克,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 7)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testH(self):
        """季度:Slot-2017-Q3,项目:狂欢,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 8)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testI(self):
        """季度:Slot-2017-Q3,项目:指环王,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 9)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testJ(self):
        """季度:Slot-2017-Q3,项目:怪物命运,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 10)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testK(self):
        """季度:Slot-2017-Q3,项目:80天旅行,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 11)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testL(self):
        """季度:Slot-2017-Q3,项目:海盗财富,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 12)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testM(self):
        """季度:Slot-2017-Q3,项目:封神榜,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 13)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testN(self):
        """季度:Slot-2017-Q3,项目:荣耀王者,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 14)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testO(self):
        """季度:Slot-2017-Q3,项目:仙剑,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 15)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testP(self):
        """季度:Slot-2017-Q3,项目:白蛇传,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 16)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testQ(self):
        """季度:Slot-2017-Q3,项目:梦游仙境,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 17)
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
    suite.addTest(SlotQ3("testA"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
