import cv2
import jieba
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import os
from PIL import Image
# jieba.setLogLevel(jieba.logging.INFO) #决定jieba是否要输出日志，注释掉则输出，不注释掉就不输出
# file = open(r'C:\Users\75464\Desktop\潮起不落文章.txt', encoding="UTF-8")#使用时替换路径即可。记得对应该文件的编码模式
# file_context = file.read()
# words2 = jieba.lcut_for_search(file_context)  # 搜索引擎模式
# data2 = {}#把data2初始化为字典
# for chara in words2:
#     if len(chara) < 2:
#         continue#排除单字词
#     if chara in data2:
#         data2[chara] += 1#如果data2中已有该词，则+1
#     else:
#         data2[chara] = 1
# data2 = sorted(data2.items()#item包含了键和值，用值排序
#                , key=lambda x: x[1],#x指键、x[1]指键值，使用键值排序
#                reverse=True)# 排序，顺便把字典变成列表
# data2=data2[1:]
# print(data2)
# data2=pd.DataFrame(data2)#转化成DataFrame,方便导出excel
# data2.to_excel('D:/test.xlsx') # 如果生成excel，可以用to_excel，此处可以填入你要存放数据表的位置


file1 = open(r'C:\Users\75464\Desktop\潮起不落文章.txt', encoding="UTF-8").read()
# name_list = ["1"]
for i in range(100):
    wordcloud = WordCloud(
        background_color='white',  # 背景颜色，根据图片背景设置，默认为黑色
        # mask = backgroup_Image, #笼罩图
        font_path='C:\Windows\Fonts\STZHONGS.TTF',  # 若有中文需要设置才会显示中文
        # font_path='C:/Windows/Fonts/simkai.ttf',
        width=2350,
        height=1000,
        margin=10,
        stopwords=['图片','a','the','Q','BY','I','Part','and','锐锴','家烁','炫箐','泓毅','红衣'],#屏蔽词，用来屏蔽一些文章出现的人名
        #prefer_horizontal=0.9,
        min_font_size=8,
        max_words=500,
        relative_scaling=1,
        colormap="tab20c",).generate(file1)# generate 可以对全部文本进行自动分词
    # 参数 width，height，margin分别对应宽度像素，长度像素，边缘空白处
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    # 保存图片：默认为此代码保存的路径
    wordcloud.to_file('meterial.jpg')


# for i in range(100):
#     name_list.append(str(i+1))
#     wordcloud = WordCloud(
#         background_color='white',  # 背景颜色，根据图片背景设置，默认为黑色
#         # mask = backgroup_Image, #笼罩图
#         font_path='C:\Windows\Fonts\STZHONGS.TTF',  # 若有中文需要设置才会显示中文
#         # font_path='C:/Windows/Fonts/simkai.ttf',
#         width=400,
#         height=600,
#         margin=10,
#         stopwords=['图片', 'a', 'the', 'Q', 'BY', 'I', 'Part', 'and', ],
#         # prefer_horizontal=0.9,
#         min_font_size=8,
#         max_words=500,
#         relative_scaling=0.9,
#         colormap="tab20c", ).generate(file1)  # generate 可以对全部文本进行自动分词
#
#     # 指定图片保存路径
#     figure_save_path = "files_fig_many"#这里创建了一个文件夹，如果依次创建不同文件夹，可以用name_list[i]
#     if not os.path.exists(figure_save_path):
#         os.makedirs(figure_save_path) # 如果不存在目录figure_save_path，则创建
# #    plt.savefig(os.path.join(figure_save_path , name_list[i]))#分别命名图片
# #     wordcloud=Image.open(r"D:\pythonProject\词频分析\files_fig_many")
#     plt.imshow(wordcloud)
#     plt.axis('off')
#     plt.savefig(r"D:\pythonProject\词频分析\files_fig_many" + name_list[i] + ".png")
#     plt.show()
#
#
#     print(i)
#     # plt.show()



# # 保存图片：默认为此代码保存的路径
#wordcloud.to_file('meterial.jpg')
