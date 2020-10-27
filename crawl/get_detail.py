import requests
from bs4 import BeautifulSoup

from crawl.user_agent import get_user_agent


def get_detail(url, proxy, outer):  # proxy,
    print(url)
    try:
        rs = requests.session()
        rs.keep_alive = False
        pages = rs.get(url=url, headers={"User-Agent": get_user_agent(),
                                         'Host': 'www.liepin.com',
                                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
                                         },
                       proxies=proxy,
                       timeout=3)
        if pages.status_code == 200:
            rss_page = BeautifulSoup(pages.text, 'html.parser')
            rss = rss_page.select(
                'div.job-item:nth-child(3) > div:nth-child(2)')  # div.job-item:nth-child(3) > div:nth-child(2)
            if len(rss) != 0:
                if rss[0] is not None:
                    if rss[0].text is not None:
                        outer.write(rss[0].text.strip() + '\n')
                        print(rss[0].text.strip())
                        return True
    except Exception as e:
        pass
