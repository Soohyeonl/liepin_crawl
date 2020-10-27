from crawl.get_detail import get_detail
from crawl.get_http import get_all_http
from crawl.my_proxy import my_proxy

urlAll = [
    "https://www.liepin.com/zhaopin/?key=数据挖掘",
    "https://www.liepin.com/zhaopin/?key=图像算法工程师",
    "https://www.liepin.com/zhaopin/?key=java后端", "https://www.liepin.com/zhaopin/?key=互联网产品经理"
]

httpFileNames = ['./http/DataMining.txt', './http/ImageAlgorithm.txt', './http/JavaEE.txt',
                './http/InternetProductManager.txt']

detailFileNames = ['../data/detail/DataMining.txt', '../data/detail/ImageAlgorithm.txt', '../data/detail/JavaEE.txt',
             '../data/detail/InternetProductManager.txt']


for i in range(1, 4):
    get_all_http(urlAll[i], httpFileNames[i])
    link_in = open(httpFileNames[i], 'r', encoding='utf-8').readlines()
    outDetail = open(detailFileNames[i], 'w', encoding='utf-8')

    proxy_num = 1
    myproxy = my_proxy(proxy_num, "https://www.liepin.com/zhaopin/?key=图像算法工程师")
    now_proxy_ = 0
    max_proxy_ = len(myproxy)
    for link in link_in:
        get_detail(link, myproxy[now_proxy_], outDetail)
        now_proxy_ += 1
        if now_proxy_ == max_proxy_ - 1:
            proxy_num += 1
            myproxy = my_proxy(proxy_num, link + '&curPage=' + str(i + 1))
            max_proxy_ = len(myproxy)
            now_proxy_ = 0


