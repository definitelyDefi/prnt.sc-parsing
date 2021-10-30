
import requests,random, string, logging
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import threading
import os


headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36' }

if 'log.log':
    logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
else:
    logging.basicConfig(filename='log.log', filemode='w', format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


bad_url = 'https://i.imgur.com'
def main_func(count):
    counter = 0
    while counter != count:
        strin = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(6))
        url_excample = f'https://prnt.sc/{strin}'
        print('[INFO] Proccessing: ',url_excample)
        request = Request(url_excample, headers=headers)
        page = urlopen(request).read()

        soup = BeautifulSoup(page, 'html.parser')
        try:
            url = soup.find('img', id='screenshot-image')['src']

        except Exception as ex:
            print('[Error] Screenshot corrupted1111.')
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

def run_threads():
    name_of_loops = int(input('write number of loops: '))
    thread1 = threading.Thread(target=main_func,args=([name_of_loops]))  
    thread2 = threading.Thread(target=main_func,args=([name_of_loops]))
    thread3 = threading.Thread(target=main_func,args=([name_of_loops]))
    thread4 = threading.Thread(target=main_func,args=([name_of_loops]))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()


path = 'img'
isExist = os.path.exists(path)


if not isExist:
    os.makedirs(path)
run_threads()


# thread3 = threading.Thread(
#    target=print_squares, args=("thread3", [11, 12, 13, 14, 15]))

    
        

# url != '//st.prntscr.com/2021/10/22/2139/img/0_173a7b_211be8ff.png' and 






