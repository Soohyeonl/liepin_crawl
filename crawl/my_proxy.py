import requests
import re
from bs4 import BeautifulSoup
from crawl.user_agent import get_user_agent


def my_proxy(paegn, testurl):
    k_proxy = 'https://www.kuaidaili.com/free/inha/{}/'
    kurl = k_proxy.format(paegn)
    page = requests.get(url=kurl, headers={"User-Agent": get_user_agent()})

    soup = BeautifulSoup(page.text, "html.parser")
    ips = [i.text for i in soup.select('.table > tbody:nth-child(2) > tr')]
    ip = []
    port = []
    protocal = []
    proxys = []
    print(ips)

    for item in ips:
        ip.append(re.search(r'\d+\.\d+\.\d+\.\d+', item).group())
        port.append(re.search(r'\d+\.\d+\.\d+\.\d+\s([0-9]+)\s', item).group(1))
        protocal.append(re.search(r'http|https|HTTP|HTTPS', item).group())
    print(ip)
    print(port)
    print(protocal)

    for i in range(len(ip)):
        urlpp = protocal[i] + '://' + ip[i] + ':' + port[i]
        try:
            response = requests.get(testurl, proxies={protocal[i]: urlpp}, timeout=1)
            if response.status_code == 200:
                proxy = {protocal[i]: urlpp}
                proxys.append(proxy)
        except Exception as e:
            pass

    return proxys
