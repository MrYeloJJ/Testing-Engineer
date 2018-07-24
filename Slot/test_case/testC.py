import unittest
from common.Slot_Caps import Slot
from common.Common import Common
from businessView.WebGame import WebGame
from businessView.PlayGame import PlayGame
from businessView.WebRecord import WebRecord


class SlotQ1(unittest.TestCase):
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
        """季度:Slot-2018-Q1,项目:湛蓝深海,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 66)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testB(self):
        """季度:Slot-2018-Q1,项目:哥谭魅影猫女,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 67)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testC(self):
        """季度:Slot-2018-Q1,项目:招财进宝,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 68)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testD(self):
        """季度:Slot-2018-Q1,项目:十二生肖,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 69)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testE(self):
        """季度:Slot-2018-Q1,项目:捕鱼达人,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 70)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testF(self):
        """季度:Slot-2018-Q1,项目:愤怒的小鸟,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 71)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testG(self):
        """季度:Slot-2018-Q1,项目:十二星座,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 72)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testH(self):
        """季度:Slot-2018-Q1,项目:角斗士,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 73)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testI(self):
        """季度:Slot-2018-Q1,项目:恭贺新春,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 74)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testJ(self):
        """季度:Slot-2018-Q1,项目:埃及女王,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 75)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testK(self):
        """季度:Slot-2018-Q1,项目:金狗旺财,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 76)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testL(self):
        """季度:Slot-2018-Q1,项目:闹元宵,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 77)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testM(self):
        """季度:Slot-2018-Q1,项目:森林舞会,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 78)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testN(self):
        """季度:Slot-2018-Q1,项目:神雕侠侣,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 79)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testO(self):
        """季度:Slot-2018-Q1,项目:抢红包,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 80)
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
    suite.addTest(SlotQ1("testB"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
