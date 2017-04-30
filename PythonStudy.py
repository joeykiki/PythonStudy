#encoding:utf-8

Add_Comment={}    #初始化列表，键是词典中字符串，值是出现的次数

with open('/home/kiki/文档/太空旅客.txt','r') as Comment_file:
    C = Comment_file.read()   #打开太空旅客评论文件
    Comment_file.close()

def Read(path):     #读取特定路径txt文档中每一行字符串
    with open(path,'r') as file:
        return file.readlines()
    file.close()

import re

FinalTxt = '/home/kiki/文档/result.txt'   #结果文件路径

def Count(path):      #统计词典中词语出现的频率
    Dict_file = Read(path)
    for line in Dict_file:
        line = line.strip('\n')
        n = re.findall(line,C)    #正则表达式匹配字符串
        Add_Comment[line] = len(n)
        with open(FinalTxt, 'w') as writeFile:
            for line in Add_Comment:
                writeFile.write(line)
                writeFile.write(' ')
                writeFile.write(str(Add_Comment[line]))
                writeFile.write('\n')
            writeFile.close()


Count('/home/kiki/下载/我的资源/week2Python基础语言讲解/作业/词典/角色/男主角.txt')






