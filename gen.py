
import requests,random, string, time, logging
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


# url_excample = 'https://prnt.sc/hpycu1' #--> hpycu1 is changing and can be both int and str literals

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36' }
options = Options()
options.headless = True
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"   
counter = 0

if 'log.log':
    logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
else:
    logging.basicConfig(filename='log.log', filemode='w', format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
 
while counter < 400:
    
    strin = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(6))
    url_excample = f'https://prnt.sc/{strin}'
    logging.info(url_excample)
    driver = webdriver.Chrome(desired_capabilities=caps,options=options)
    driver.get(url_excample)
    time.sleep(3)
    page_source = driver.page_source
    with open('test.html', 'w+', encoding='utf-8') as output_file:
        output_file.write(page_source)

    driver.quit()

    with open('test.html', 'r', encoding='utf-8') as output_file:
        soup = BeautifulSoup(output_file, 'html.parser')
    try:
        dom = etree.HTML(str(soup))
        day = dom.xpath('//*[@id="screenshot-image"]/@src')
        try:
            url = day[0]
            format = url[-3]+url[-2]+url[-1]
            r = requests.get(url,headers=headers)
            img = r.content

            with open(fr"img\{strin}.{format}", "wb") as f:
                f.write(img)

            counter += 1

        except Exception as ex:
            print(ex)
            counter += 1

            continue
    except Exception as ex:
            print(ex)
            continue
    


