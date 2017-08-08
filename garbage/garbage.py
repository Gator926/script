import datetime
import os

# 获取文件列表
files = os.listdir()
importFile = ['garbage.txt', 'garbage.bat', 'garbage.py']    # 不删除的文件列表

# 若无garbage.txt文件, 则新建该文件
if 'garbage.txt' not in files:

    # 将重要文件从列表中删除
    for eachFile in importFile:
        if eachFile in files:
            files.remove(eachFile)

    # 创建garbage.txt文件
    file = open('garbage.txt', 'w', encoding='utf-8')
    jsonString = '{"date":"2017-07-8", "files":[{"restTime": "30", "file": '+str(files)+'}]}'
    file.write(jsonString)
    file.close()

# 如果有文件则执行相应操作
else:
    file = open('garbage.txt', 'r')
    data = eval(file.readlines()[0])                                 # 获取文本内容
    txtDate = datetime.datetime.strptime(data['date'], "%Y-%m-%d")   # 文本时间
    today = datetime.datetime.today()                                # 今日时间
    todayDate = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
    dateDiff = (todayDate - txtDate).days                            # 天数差

    # 根据操作files字典
    for eachRestDay in data['files']:
        pass