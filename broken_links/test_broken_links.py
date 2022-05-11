from selenium.webdriver import Chrome
from requests import request

driver = Chrome("chromedriver")
driver.get(r"C:\Users\RAGHAVENDRA\Downloads\links.html")
links = driver.find_elements_by_xpath("//a")
urls = [ ]
broken_links = [ ]
for link in links:
    urls.append((link.text, link.get_attribute("href")))
print(urls)

for url in urls:
    response = request("GET", url[1])
    if response.status_code != 200:
        broken_links.append(url)

with open('broken_links.txt', 'w') as f:
    for item in broken_links:
        f.write(":".join(item))
        f.write("\n")