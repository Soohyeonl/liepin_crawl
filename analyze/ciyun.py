import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


fenciFileNames = ['DataMining.txt', 'ImageAlgorithm.txt', 'JavaEE.txt',
             'InternetProductManager.txt']


for i in range(4):
    fencilines = open('../data/fenci/' + fenciFileNames[i], 'r', encoding='utf-8').readlines()
    text = ''
    for line in fencilines:
        text += ' ' + line.strip()
    alice_mask = np.array(Image.open("./lib/ciy.png"))
    stopwords = set(STOPWORDS)
    stopwords.add("said")
    wc = WordCloud(
        font_path=r'./lib/simsun.ttc',
        background_color="white",
        width=800,
        height=600)
    wc.generate(text)

    # store to file
    wc.to_file('../result/' + fenciFileNames[i] + ".jpg")