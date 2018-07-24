import logging
import logging.config
from selenium import webdriver

CON_LOG = "../config/log.conf"
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


class Slot(object):
    @staticmethod
    def browser():
        logging.info("==========browser==========")
        browser = webdriver.Firefox()
        return browser


if __name__ == '__main__':
    Slot.browser()
