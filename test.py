from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='chromedriver.exe')
driver.set_window_size(1920, 1080)
driver.get("http://10.245.0.225/uf/login/login.jsp")
WebDriverWait(driver, 20, 0.5).until(
        EC.presence_of_element_located((By.ID, 'loginbtn')))
driver.find_element_by_id('username').send_keys('qinxd15')
driver.find_element_by_id('password').send_keys('lh31415926!')
driver.find_element_by_id('loginbtn').click()
WebDriverWait(driver,20,0.5).until(
        EC.presence_of_element_located((By.ID, 'AppFavorite')))
driver.find_element_by_id('AppFavorite').click()
WebDriverWait(driver,20,0.5).until(
        EC.presence_of_element_located((By.ID, 'appid_30401')))
driver.find_element_by_id('appid_30401').click()
driver.switch_to.window(driver.window_handles[-1])
driver.set_window_size(1920, 1080)
WebDriverWait(driver,20,0.5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div > div.sidebar-container.has-logo > div.el-scrollbar > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div:nth-child(4) > a')))
driver.find_element_by_css_selector('#app > div > div.sidebar-container.has-logo > div.el-scrollbar > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div:nth-child(4) > a').click()
WebDriverWait(driver,20,0.5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div > div.main-container > section > div > button')))
for i in range(3):
        print('processing rule ' + str(i+1))
        # 点击新增按钮
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > button').click()
        WebDriverWait(driver,20,0.5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > div > button:nth-child(2)')))
        # 填充源主机ip地址
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input').send_keys('17.17.39.20')

        # 填充目标主机ip地址
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(3) > div > div > div > input').send_keys('10.126.0.210')

        # 填充源主机所属系统
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div:nth-child(1) > div > div > div > input').send_keys('开源DevOps')

        # 填充目标主机所属系统
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div:nth-child(3) > div > div > div > input').send_keys('代码开源平台')

        # 填充源系统业务负责人
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input').send_keys('秦晓东')

        # 填充目标系统业务负责人
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(3) > div > div > div > input').send_keys('张璇')

        # 填充源负责人联系电话
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div:nth-child(1) > div > div > div > input').send_keys('13261187241')

        # 填充目标负责人联系电话
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div:nth-child(3) > div > div > div > input').send_keys('18845678900')

        # 填充目的端口
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(7) > div:nth-child(1) > div > div > div > input').send_keys('22,80,443')

        # 填充宽带需求
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(1) > div > div > div > input').send_keys('最大带宽')

        # 填充数据交互内容
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(3) > div > div > div > input').send_keys('接口互访')

        # 点选源主机所属机房
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > div.el-input.el-input--suffix > input').click()

        time.sleep(2)
        # 查找总部运营域动态元素并点击
        flag = True
        while(flag):
                menus = []
                while(len(menus) <= 1):
                        menus = re.findall('cascader-menu-\d*-0-0', driver.page_source)
                for menus_index in range(len(menus)):
                        try:
                                driver.find_element_by_xpath('//*[@id="'+menus[menus_index]+'"]').click()
                                flag = False
                                break
                        except:
                                pass
                
        # 指定选择项 0：其他， 1：郑州， 2：廊坊
        chosen_item = 2 
        # 查找源主机总部运营域动态子元素并点击
        flag = True
        while(flag):
                sub_items = []
                while(len(sub_items) == 0):
                        sub_items=re.findall('cascader-menu-\d*-1-'+str(chosen_item), driver.page_source)
                for sub_items_index in range(len(sub_items)):
                        try:       
                                driver.find_element_by_xpath('//*[@id="'+sub_items[sub_items_index]+'"]').click()
                                flag = False
                                break
                        except:
                                pass
        # 点选目标主机所属机房
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(3) > div > div > div > div > input').click()
        time.sleep(2)
        # 点击总部运营域动态元素
        flag = True
        while(flag):
                for menus_index in range(len(menus)):
                        try:
                                driver.find_element_by_xpath('//*[@id="'+menus[menus_index]+'"]').click()
                                flag = False
                                break
                        except:
                                pass
        # 指定选择项 0：其他， 1：郑州， 2：廊坊
        chosen_item = 2
        # driver.save_screenshot('screen_shot.png')
        # 查找目标主机总部运营域动态子元素并点击
        flag = True
        while(flag):
                sub_items = []
                while(len(sub_items) == 0):
                        sub_items=re.findall('cascader-menu-\d*-1-'+str(chosen_item),driver.page_source)

                for sub_items_index in range(len(sub_items)):
                        try:       
                                driver.find_element_by_xpath('//*[@id="'+sub_items[sub_items_index]+'"]').click()
                                flag = False
                                break
                        except:
                                pass
                
        # driver.save_screenshot('screen_shot1.png')
        # driver.implicitly_wait(5)
        # 点击源主机所属区域
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(6) > div:nth-child(1) > div > div > div > div > input').click()

        time.sleep(2)
        # 选择子区域： 1：核心区， 2:用户访问区， 3：大数据区， 4：DMZ区， 5：测试区， 6：管理维护区， 7：外部系统接口区，8其他
        chosen_item = 2
        flag = True
        while(flag):
                for item_index in range(5, 20):
                        try:
                                driver.find_element_by_xpath('/html/body/div[' + str(item_index) + ']/div[1]/div[1]/ul/li[' + str(chosen_item) + ']') .click()
                                flag = False
                                break
                        except:
                                pass


        # 点击目标主机所属区域
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(6) > div:nth-child(3) > div > div > div > div > input').click()

        time.sleep(2)
        # 选择子区域： 1：核心区， 2:用户访问区， 3：大数据区， 4：DMZ区， 5：测试区， 6：管理维护区， 7：外部系统接口区，8其他
        chosen_item = 1
        flag = True
        while(flag):
                for item_index in range(5, 20):
                        try:
                                driver.find_element_by_xpath('/html/body/div[' + str(item_index) + ']/div[1]/div[1]/ul/li[' + str(chosen_item) + ']').click()
                                flag = False
                                break
                        except:
                                pass
        # 点击协议
        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(7) > div:nth-child(3) > div > div > div > div > input').click()

        time.sleep(2)
        # 选择协议 1：tcp, 2: udp
        chosen_item = 2
        flag = True
        while(flag):
                for item_index in range(5, 20):
                        try:
                                driver.find_element_by_xpath('/html/body/div[' + str(item_index)+ ']/div[1]/div[1]/ul/li[' + str(chosen_item) + ']').click()
                                flag = False
                                break
                        except:
                                pass

        # driver.save_screenshot('screen_shot2.png')
        #点击保存

        driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > div > button:nth-child(2)').click()

        # driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > div.el-input.el-input--suffix > input').send_keys(Keys.ARROW_RIGHT)


        # driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > div.el-input.el-input--suffix > input').send_keys(Keys.ARROW_DOWN)
        # driver.find_element_by_css_selector('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > div.el-input.el-input--suffix > input').send_keys(Keys.RETURN)
        # driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/ul/li/span').click()

        # driver.find_element_by_css_selector(".pan:nth-child(2) .imgover").click()
        # driver.switch_to.window(driver.window_handles[-1])
# driver.set_window_size(1920, 1080)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/button[2]').click()
time.sleep(5)
# driver.save_screenshot('screen_shot3.png')
# content = client.page_source.encode('utf-8')
# print (content)
driver.quit()