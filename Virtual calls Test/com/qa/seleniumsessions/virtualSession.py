from selenium import webdriver


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
for x in range(1,6):


    driver = webdriver.Chrome('/Users/adeel/Documents/Virtual calls Test/webdrivers/chromedriver 2')

    driver.get('https://dev-live.tame.events/session/6OUNjADdP')
    driver.implicitly_wait(25000)
    driver.find_element_by_name('email').send_keys(f'attendee{x}@gmail.com')
    driver.find_element_by_class_name('dxemHy').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/span[2]').click()
# driver.quit()

# import time
# from selenium import webdriver
# import os

# chrome_options = webdriver.ChromeOptions()
#
# chrome_options.add_argument('--headless')
#
# driver = webdriver.Chrome('/Users/adeel/PycharmProjects/VideoCaliingTest/webdrivers/chromedriver 2', chrome_options=chrome_options)
#
# time.sleep(10)
# driver.get('https://youtube.com')
# print(driver.title)
#
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='search']").send_keys("Guido van Rossum")
#
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='search-icon-legacy']").submit()
#
# time.sleep(3)
# print(driver.title)
# list = []
# for x in range(1, 11):
#     list.append('driver')
#     print(list)
# for x in range(1,11):
#     list.append(x)
#     print(list)
    # driver1 = f"driver{x}"
    # f'{driver1}{x}' = webdriver.Chrome('/Users/adeel/PycharmProjects/VideoCaliingTest/webdrivers/chromedriver 2')
    # f'{driver1}{x}'.maximize_window()