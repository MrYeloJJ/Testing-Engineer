import os
import time
import unittest
import logging.config
from BSTestRunner import BSTestRunner


class Run(object):
    def __init__(self):
        self.test_dir = "../test_case/"
        self.report_dir = "../report/"
        self.title = "Slot Test Report"
        self.last = "_report.html"
        self.description = "用例执行情况"

    def run(self):
        logging.info("==========测试报告加载中···==========")
        """
        discover(start_dir, pattern = "test*.py, top_level_dir = None) 方法的使用
        start_dir 要测试的模块名或测试用例目录
        pattern = "test*.py   表示用例文件名的匹配原则。此处匹配文件名以"test*"开头的.py类型文件，*表示任意多个字符
        top_level_dir = None  测试模块的顶层目录，如果没有，默认为None
        """
        discover = unittest.defaultTestLoader.discover(self.test_dir, pattern="test*.py")

        # times = time.strftime("%Y-%m-%d %H_%M_%S")
        times = time.strftime("%Y-%m-%d")

        v = 1.0
        report_path = self.report_dir + self.title + " V" + str(round(v, 1)) + " " + times + self.last

        while True:
            is_exists = os.path.exists(report_path)
            if is_exists:
                v += 0.1
                report_path = self.report_dir + self.title + " V" + str(round(v, 1)) + " " + times + self.last
            else:
                break

        with open(report_path, "wb") as fp:
            runner = BSTestRunner(stream=fp, title=self.title, description=self.description)
            logging.info("start run testcase...")
            runner.run(discover)
            # fp.close()    # 使用with方法不需要关闭文件


if __name__ == '__main__':
    run = Run()
    run.run()
