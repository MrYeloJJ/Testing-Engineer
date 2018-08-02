import time
import logging.config
from common.Common import Common
from common.Slot_Caps import Slot
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class WebGame(Common):
    # 选择语言相关元素
    element_language = (By.XPATH, "//input[@readonly='readonly']")
    simplified_chinese = (By.XPATH, "//span[contains(text(), '简体中文')]")
    # simplified_chinese = (By.XPATH, "//li[@class='el-select-dropdown__item']")

    # 登录相关元素
    login_button = (By.XPATH, "//button[@class='el-button login-btn bg el-button--default el-popover__reference']")
    free_button = (By.XPATH, "//button[@class='el-button el-button--success']")
    username = (By.XPATH, "//input[@placeholder='请输入任意用户名']")
    password = (By.XPATH, "//input[@placeholder='请输入密码']")
    blizzmi_user = "bx0342"
    blizzmi_pass = "123456"
    again_login_button = (By.XPATH, "//span[contains(text(), '登录或创建新用户')]")
    check_login_name = (By.XPATH, "//p/span[@class='el-tooltip item']")

    # 进入游戏前准备相关元素
    text_box = (By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div/input")
    search_button = (By.XPATH, "//i[@class='search-font']")
    element_tiger = (By.XPATH, "//span[contains(text(), '老虎机')]")
    game_name = (By.XPATH, "//span[contains(text(), '激情世界杯')]")

    # 进入被测大厅
    def get_fungaming(self):
        logging.info("==========进入被测大厅==========")
        self.browser.get("https://lobby.fg.blizzmi.cn/")
        self.browser.implicitly_wait(2)

    # 检查被测大厅标题，返回：TRUE/FALSE
    def check_game_hall(self):
        logging.info("==========检查被测大厅标题==========")
        try:
            title = self.browser.title
            assert title == "乐游 — 乐趣无限 共赢财富"
        except AssertionError:
            time.sleep(1)
            logging.error("Game hall title FALSE!")
            self.get_screen_shot("Game hall title FALSE")
            return False
        else:
            logging.info("Game hall title TRUE!")
            return True

    # 多语言选择简体中文
    def select_language(self):
        logging.info("==========select_language==========")
        try:
            self.get_element(*self.element_language).click()
            # self.get_elements(*self.simplified_chinese)[4].click()
            text = self.get_element(*self.simplified_chinese).text
        except NoSuchElementException:
            logging.error("Select Language NoSuchElementException!")
            self.get_screen_shot("Select Language NoSuchElementException")
            raise
        else:
            logging.info("Select Language %s success!" % text)
            self.browser.find_element(*self.simplified_chinese).click()
            return text

    # 检查多语言选择是否正确
    def check_language(self):
        logging.info("==========检查多语言选择是否正确==========")
        try:
            text = self.select_language()
            assert text == "简体中文"
        except AssertionError:
            logging.error("Select Language %s FALSE!" % text)
            self.get_screen_shot("Select Language FALSE")
            return False
        else:
            logging.info("Select Language %s TRUE!" % text)
            return True

    # 选择非免转/免转
    def select_free_rotation(self, select=1):
        logging.info("==========选择非免转/免转==========")
        try:
            if select == 0:
                logging.info("选择免转")
                self.get_elements(*self.free_button)[1].click()
            elif select == 1:
                logging.info("选择非免转")
                self.get_elements(*self.free_button)[2].click()
        except NoSuchElementException:
            logging.error("select_free_rotation NoSuchElementException!")
            self.get_screen_shot("select_free_rotation NoSuchElementException")
            raise
        except TimeoutException:
            logging.error("select_free_rotation TimeoutException!")
            self.get_screen_shot("select_free_rotation TimeoutException")
            raise

    # 登录大厅用户名
    def login_user(self):
        logging.info("==========登录大厅用户名==========")
        try:
            logging.info("开始登录")
            logging_button = self.get_element(*self.login_button)
            logging_button.click()

            self.select_free_rotation()

            logging.info("输入用户名-密码")
            user_box = self.get_element(*self.username)
            user_box.send_keys(self.blizzmi_user)
            logging.info("UserName is: %s" % self.blizzmi_user)

            pass_box = self.get_element(*self.password)
            pass_box.send_keys(self.blizzmi_pass)
            logging.info("PassWord is: %s" % self.blizzmi_pass)

            logging.info("点击登录按钮")
            self.get_element(*self.again_login_button).click()
        except NoSuchElementException:
            logging.error("login_user NoSuchElementException!")
            self.get_screen_shot("login_user NoSuchElementException")
            raise
        except TimeoutException:
            logging.error("login_user TimeoutException!")
            self.get_screen_shot("login_user TimeoutException")
            raise

    # 检查登录状态，成功返回TRUE，反之FALSE
    def check_login_status(self):
        logging.info("==========检查登录状态==========")
        try:
            username = self.get_elements(*self.again_login_button)[0].text
            assert username == self.blizzmi_user
        except AssertionError:
            logging.error("login Fail!")
            self.get_screen_shot("login Fail")
            return False
        else:
            logging.info("login success!")
            return True

    # 切换老虎机标签页
    def select_tiger(self):
        logging.info("==========切换老虎机标签页==========")
        try:
            self.get_element(*self.element_tiger).click()
        except NoSuchElementException:
            logging.error("select_tiger NoSuchElementException!")
            self.get_screen_shot("select_tiger NoSuchElementException")
            raise

    # 大厅搜索游戏项目
    def lookup_game(self, game_name):
        logging.info("==========大厅搜索游戏项目==========")
        try:
            text_box = self.get_element(*self.text_box)
            text_box.click()
            text_box.clear()
            text_box.send_keys(game_name)
            logging.info("Look Up Game %s" % game_name)
            self.get_element(*self.search_button).click()
        except NoSuchElementException:
            logging.error("Look Up Game NoSuchElementException!")
            self.get_screen_shot("Look Up Game NoSuchElementException")
            raise

    # 选择游戏项目
    def select_we_game(self, game_name):
        logging.info("==========选择游戏项目==========")
        try:
            self.browser.find_elements_by_xpath("//span[contains(text(), '" + game_name + "')]")[3].click()
        except NoSuchElementException:
            logging.error("Game Name NoSuchElementException!")
            self.get_screen_shot("Game Name NoSuchElementException")
            raise
        else:
            logging.info("to Game %s success!" % game_name)

    def all_agg(self, game_name):
        logging.info("==========游戏正在初始化······==========")
        self.get_fungaming()
        self.check_game_hall()
        self.select_language()
        self.check_language()
        self.login_user()
        self.check_login_status()
        self.select_tiger()
        self.lookup_game(game_name)
        self.select_we_game(game_name)
        self.switch_tab_game()
        logging.info("==========加载成功，正在进入游戏······==========")


if __name__ == '__main__':
    browser = Slot.browser()
    wg = WebGame(browser)
    wg.get_fungaming()
    wg.check_game_hall()
    wg.select_language()
    wg.check_language()
    wg.login_user()
    wg.check_login_status()
    wg.select_tiger()
    wg.lookup_game("船长宝藏")
    wg.select_we_game("船长宝藏")
    # browser.close()
