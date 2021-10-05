
import requests
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


# url_excample = 'https://prnt.sc/hpycu1' #--> hpycu1 is changing and can be both int and str literals
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36' }
options = Options()
options.headless = False
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"   
counter = 0

while counter < 100:
    import random
    import string
    a = random.choice(string.ascii_letters.lower())
    a1 = random.choice(string.ascii_letters.lower())
    a2 = random.choice(string.ascii_letters.lower())
    a3 = random.choice(string.ascii_letters.lower())
    a4 = random.choice(string.ascii_letters.lower())
    a5 = random.choice(string.ascii_letters.lower())
    url_excample = f'https://prnt.sc/{a+a1+a2+a3+a4+a5}'
    print(url_excample)
    driver = webdriver.Chrome(desired_capabilities=caps,options=options)
    driver.get(url_excample)
    time.sleep(3)
    page_source = driver.page_source
    with open('test.html', 'w+', encoding='utf-8') as output_file:
        output_file.write(page_source)

    driver.quit()

    with open('test.html', 'r', encoding='utf-8') as output_file:
        soup = BeautifulSoup(output_file, 'html.parser')

    dom = etree.HTML(str(soup))
    day = dom.xpath('//*[@id="screenshot-image"]/@src')
    try:
        url = day[0]
        format = url[-3]+url[-2]+url[-1]
        r = requests.get(url,headers=headers)
        img = r.content

        with open(f"random_image_{counter}.{format}", "wb") as f:
            f.write(img)

        counter += 1

    except Exception as ex:
        print(ex)
        counter += 1

        continue
    


