"""
获取详情页链接
"""
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

from crawl.my_proxy import my_proxy
from crawl.user_agent import get_user_agent


def get_all_http(main_url, outFileName):
    def find_href(tag):
        return ('data-param' in tag.parent.attrs) and tag.parent.attrs['data-param'] == 'city'

    proxy_num = 1
    myproxy = my_proxy(proxy_num, "https://www.liepin.com/zhaopin/?key=图像算法工程师")
    now_proxy_ = 0
    max_proxy_ = len(myproxy)


    main_page = requests.get(url=main_url, headers={"User-Agent": get_user_agent(),
                                                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'},
                             proxies=myproxy[now_proxy_])
    now_proxy_ += 1

    if now_proxy_ == max_proxy_ - 1:
        proxy_num += 1
        myproxy = my_proxy(proxy_num, "https://www.liepin.com/zhaopin/?key=图像算法工程师")
        max_proxy_ = len(myproxy)
        now_proxy_ = 0

    main_bspage = BeautifulSoup(main_page.text, 'html.parser')
    main_links = [('https://www.liepin.com' + item['href']) for item in main_bspage.find_all(find_href)]
    while len(main_links) == 0:
        main_page = requests.get(url=main_url, headers={"User-Agent": get_user_agent(),
                                                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'},
                                 proxies=myproxy[now_proxy_])
        now_proxy_ += 1

        if now_proxy_ == max_proxy_ - 1:
            proxy_num += 1
            myproxy = my_proxy(proxy_num, "https://www.liepin.com/zhaopin/?key=图像算法工程师")
            max_proxy_ = len(myproxy)
            now_proxy_ = 0

        main_bspage = BeautifulSoup(main_page.text, 'html.parser')
        main_links = [('https://www.liepin.com' + item['href']) for item in main_bspage.find_all(find_href)]

    main_links.pop()

    print(main_links)

    out = open(outFileName, 'w', encoding='utf-8')
    linknum = 0

    for link in main_links:
        for i in range(0, 10):
            url_page = link + '&curPage=' + str(i)
            if urlopen(url_page).status != 200:
                break
            link_page = requests.get(url=url_page, headers={"User-Agent": get_user_agent()},
                                     proxies=myproxy[now_proxy_])
            print(myproxy[now_proxy_])
            now_proxy_ += 1

            if now_proxy_ == max_proxy_ - 1:
                proxy_num += 1
                myproxy = my_proxy(proxy_num, link + '&curPage=' + str(i + 1))
                max_proxy_ = len(myproxy)
                now_proxy_ = 0

            detail_bspage = BeautifulSoup(link_page.text, 'html.parser')
            detail_links = [(item['href'] if item['href'][0] != '/' else 'https://www.liepin.com' + item['href']) for
                            item
                            in detail_bspage.select('.job-info h3 a')]
            for aLink in detail_links:
                linknum += 1
                out.write(aLink + '\n')
                if linknum >= 1000:
                    break
            if linknum >= 1000:
                break
        if linknum >= 1000:
            break

    out.close()
