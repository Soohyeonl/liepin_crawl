import jieba
from wordcloud import WordCloud


# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open('./lib/chinesestoptxt.txt', encoding='UTF-8').readlines()]
    return stopwords


cutFileNames = ['./cut/DataMining.txt', './cut/ImageAlgorithm.txt', './cut/JavaEE.txt',
                './cut/InternetProductManager.txt']

fenciFileNames = ['DataMining.txt', 'ImageAlgorithm.txt', 'JavaEE.txt',
                  'InternetProductManager.txt']

# 给出文档路径
for i in range(4):
    filename = cutFileNames[i]
    inputs = open(filename, 'r', encoding='UTF-8')

    # 将输出结果写入ou.txt中

    # 对文档中的每一行进行中文分词
    jieba.load_userdict("./lib/user_dict.txt")
    text = ''
    for line in inputs.readlines():
        text += ' ' + line.strip()
    sentence_depart = jieba.cut(text)
    # 创建一个停用词列表
    stopwords = stopwordslist()
    # 输出结果为outstr
    outstr = ''
    word_dict = {}
    word_list = ''
    # 去停用词
    for word in sentence_depart:
        if len(word) > 1 and not word in stopwords:
            if word != '\t':
                word_list = word_list + ' ' + word
                if word_dict.get(word):
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
                outstr += word
                outstr += " "
    inputs.close()

    sort_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    print(sort_words[0:101])
    print(str(i + 1) + "删除停用词和分词成功！！！")

    wc = WordCloud(
        background_color="white",
        max_words=500,
        font_path='./lib/simsun.ttc',
        min_font_size=15,
        max_font_size=50,
        width=800,
        height=600
    )

    wc.generate(word_list[0:1000])
    wc.to_file(fenciFileNames[i] + '.png')
