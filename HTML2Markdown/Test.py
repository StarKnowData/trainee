#!/usr/bin/python
#coding:utf-8

# from . import markdown_libs

from markdown_libs import html2text
import codecs
from markdownify import markdownify as md
from bs4 import BeautifulSoup

# /Users/lw/Desktop/大数据/Runoob/Python2/www.runoob.com/python
filepath = '/Users/lw/Desktop/大数据/Runoob/Python2/www.runoob.com/python/python-basic-syntax.html'
# file = codecs.open(filepath, 'r',encoding='utf-8', errors='ignore')                   #以读方式打开文件
file = codecs.open(filepath, 'r',encoding='utf-8', errors='ignore')                   #以读方式打开文件
lines = list()

lines = file.readlines()


# open('cdays-4-result.txt', 'w').write('%s' % '\n'.join(result)) #保存入结果文件


soup = BeautifulSoup(str(lines).decode('unicode_escape').encode('utf-8').replace("', u'",''),"html.parser")

articleIntro = soup.find_all('div',class_='article-intro');

#print articleIntro[0]

#print articleIntro

# print articleIntro[0]
print md(str(articleIntro[0])).strip().replace("""', u\"""",'').replace("""", u'""",'');