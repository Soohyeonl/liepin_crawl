import re

detailFileNames = ['../data/detail/DataMining.txt', '../data/detail/ImageAlgorithm.txt', '../data/detail/JavaEE.txt',
             '../data/detail/InternetProductManager.txt']
cutFileNames = ['./cut/DataMining.txt', './cut/ImageAlgorithm.txt', './cut/JavaEE.txt',
             './cut/InternetProductManager.txt']

for i in range(4):
    fin = open(detailFileNames[i], 'r', encoding='utf-8')
    out = open(cutFileNames[i], 'w', encoding='utf-8')

    lines = fin.readlines()

    for line in lines:
        if re.search(r'(任职.?.?.?([\s\S]+))', line) is not None:
            txt = re.search(r'任职.?.?.?([\s\S]+)', line).group(1)
        elif re.search(r'(要求.?([\s\S]+))', line) is not None:
            txt = re.search(r'要求.?([\s\S]+)', line).group(1)
        else:
            txt = line
        xuqiu = re.sub(r'；|。|-|;', '\n', re.sub(r'(\d.)|\s+', '', txt))
        out.write(xuqiu + '\n\n')

    fin.close()
    out.close()