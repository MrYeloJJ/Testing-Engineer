import unittest
from common.Slot_Caps import Slot
from common.Common import Common
from businessView.WebGame import WebGame
from businessView.PlayGame import PlayGame
from businessView.WebRecord import WebRecord


class SlotQ4(unittest.TestCase):
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
        """季度:Slot-2017-Q4,项目:瑞狗迎春,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 18)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testB(self):
        """季度:Slot-2017-Q4,项目:女校橄榄球,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 19)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testC(self):
        """季度:Slot-2017-Q3,项目:武圣关云长,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 20)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testD(self):
        """季度:Slot-2017-Q4,项目:刺客信条,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 21)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testE(self):
        """季度:Slot-2017-Q4,项目:古墓丽影,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 22)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testF(self):
        """季度:Slot-2017-Q4,项目:希腊传说,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 23)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testG(self):
        """季度:Slot-2017-Q4,项目:吸血鬼与狼人,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 24)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testH(self):
        """季度:Slot-2017-Q4,项目:梦幻西游,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 25)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testI(self):
        """季度:Slot-2017-Q4,项目:女校足球部,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 26)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testJ(self):
        """季度:Slot-2017-Q4,项目:女校剑道部,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 27)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testK(self):
        """季度:Slot-2017-Q4,项目:绿野仙踪,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 28)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testL(self):
        """季度:Slot-2017-Q4,项目:剑侠情缘,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 29)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testM(self):
        """季度:Slot-2017-Q4,项目:格斗之王,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 30)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testN(self):
        """季度:Slot-2017-Q4,项目:埃菲尔,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 31)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testO(self):
        """季度:Slot-2017-Q4,项目:性感女神,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 32)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testP(self):
        """季度:Slot-2017-Q4,项目:功夫熊猫,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 33)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testQ(self):
        """季度:Slot-2017-Q4,项目:植物大战僵尸,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 34)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testR(self):
        """季度:Slot-2017-Q4,项目:阿凡达,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 35)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testS(self):
        """季度:Slot-2017-Q4,项目:新年符号,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 36)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testT(self):
        """季度:Slot-2017-Q4,项目:守望英雄,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 37)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testU(self):
        """季度:Slot-2017-Q4,项目:世界末日,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 38)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testV(self):
        """季度:Slot-2017-Q4,项目:现代战争,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 39)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testW(self):
        """季度:Slot-2017-Q4,项目:甜水绿洲,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 40)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testX(self):
        """季度:Slot-2017-Q4,项目:加勒比海盗,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 41)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testY(self):
        """季度:Slot-2017-Q4,项目:侏罗纪,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 42)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testZ(self):
        """季度:Slot-2017-Q4,项目:玛雅,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 43)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAA(self):
        """季度:Slot-2017-Q4,项目:印第安,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 44)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAB(self):
        """季度:Slot-2017-Q4,项目:神秘东方,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 45)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAC(self):
        """季度:Slot-2017-Q4,项目:红楼梦,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 46)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAD(self):
        """季度:Slot-2017-Q4,项目:富饶农场,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 47)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAE(self):
        """季度:Slot-2017-Q4,项目:哪吒闹海,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 48)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAF(self):
        """季度:Slot-2017-Q4,项目:金瓶梅,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 49)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAG(self):
        """季度:Slot-2017-Q4,项目:武松打虎,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 50)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAH(self):
        """季度:Slot-2017-Q4,项目:黑珍珠号,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 51)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAI(self):
        """季度:Slot-2017-Q4,项目:七夕情缘,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 52)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAJ(self):
        """季度:Slot-2017-Q4,项目:四大美女,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 53)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAK(self):
        """季度:Slot-2017-Q4,项目:女校游泳队,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 54)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAL(self):
        """季度:Slot-2017-Q4,项目:女校啦啦队,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 55)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAM(self):
        """季度:Slot-2017-Q4,项目:女校体操队,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 56)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAN(self):
        """季度:Slot-2017-Q4,项目:钻石之恋,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 57)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAO(self):
        """季度:Slot-2017-Q4,项目:鸟叔,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 58)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAP(self):
        """季度:Slot-2017-Q4,项目:天龙八部,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 59)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAQ(self):
        """季度:Slot-2017-Q4,项目:鹿鼎记,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 60)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAR(self):
        """季度:Slot-2017-Q4,项目:笑傲江湖,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 61)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAS(self):
        """季度:Slot-2017-Q4,项目:幸运水果机,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 62)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAT(self):
        """季度:Slot-2017-Q4,项目:众神之王,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 63)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAU(self):
        """季度:Slot-2017-Q4,项目:红粉女郎,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 64)
        self.wg.all_agg(",".join(data))
        self.pg.execute_wait_lading()
        self.wr.open_record()
        try:
            self.assertTrue(self.wr.new_record(",".join(data)))
        except AssertionError:
            raise

    def testAV(self):
        """季度:Slot-2017-Q4,项目:灌篮高手,环境:PRO,用例:游戏能正常运行"""
        data = self.com.get_csv_data(self.csv, 65)
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
    suite.addTest(SlotQ4("testB"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
