
import requests,random, string, logging
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36' }

if 'log.log':
    logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
else:
    logging.basicConfig(filename='log.log', filemode='w', format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


counter = 0
bad_url = 'https://i.imgur.com'

while counter < 2000:
    strin = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(6))
    url_excample = f'https://prnt.sc/{strin}'
    print('[INFO] Proccessing: ',url_excample)
    request = Request(url_excample, headers=headers)
    page = urlopen(request).read()

    soup = BeautifulSoup(page, 'html.parser')
    try:
        url = soup.find('img', id='screenshot-image')['src']

    except Exception as ex:
        print('[Error] Screenshot corrupted.')
        # counter += 1  
        continue
    
    format = url[-3]+url[-2]+url[-1]
    if format == 'peg':
        format = 'j'+format
    try:
        with open(fr"img\{strin}.{format}", "wb") as f:
            r = requests.get(url,headers=headers)
            img = r.content
            f.write(img)
            print('[INFO] Done: ',url)
            logging.info(url_excample)
            counter += 1
    except Exception as ex:
        print('[Error] Screenshot corrupted.')
        counter += 1  
        continue
   
    
        

# url != '//st.prntscr.com/2021/10/22/2139/img/0_173a7b_211be8ff.png' and 






