from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver.exe")
driver.get("https://www.monsterindia.com/")
sleep(5)

driver.find_element_by_id("SE_home_autocomplete").click()
sleep(1)
driver.find_element_by_id("SE_home_autocomplete").send_keys("python")
sleep(1)
driver.find_element_by_xpath("//strong[text()='Python']").click()
sleep(2)
driver.find_element_by_xpath("//input[@value='Search']").click()
sleep(2)
driver.find_element_by_xpath("//div[@class='job-tittle']/h3/a").click()
sleep(5)
handles = driver.window_handles

driver.switch_to.window(handles[1])



driver.find_element_by_xpath("//i[@class='mqfi-star-empty']").click()
driver.implicitly_wait(10)

# driver.find_element_by_xpath("//span[@class='apply-panel']/a/button[1]").click()
# driver.find_element_by_xpath("//div[@id='stickyApply']/div/div/div/div/div/span/a/button[1]").click()
sleep(2)


