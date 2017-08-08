import datetime
import os

# 获取文件列表
files = os.listdir()
importFile = ['garbage.txt','garbage.bat','garbage.py']

# 若无garbage.txt文件, 则新建该文件
if 'garbage.txt' not in files:

    # 将重要文件从列表中删除
    for eachFile in importFile:
        files.remove(eachFile)

    # 创建garbage.txt文件
    file = open('garbage.txt', 'w')
    jsonString = '{"date":"2017-07-8", "files":[{"restTime": "30", "file": '+files+']}]}'
    file.write()
    file.close()

# 如果有文件则执行相应操作
else:
    pass