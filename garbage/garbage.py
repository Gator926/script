import datetime
import os
import shutil

# 获取文件列表
files = os.listdir()
importFile = ['garbage.txt', 'garbage.bat', 'garbage.py']            # 不删除的文件列表

# 将重要文件从列表中删除
for eachFile in importFile:
    if eachFile in files:
        files.remove(eachFile)

# 若无garbage.txt文件, 则新建该文件
if 'garbage.txt' not in os.listdir():

    # 创建garbage.txt文件
    file = open('garbage.txt', 'w', encoding='utf-8')
    jsonString = '{"date":"2017-08-08", "files":[{"restTime": "30", "file": '+str(files)+'}]}'
    file.write(jsonString)
    file.close()

# 如果有文件则执行相应操作
else:
    file = open('garbage.txt', 'r', encoding='utf-8')
    data = eval(file.readlines()[0])                                 # 获取文本内容
    file.close()                                                     # 关闭文本文件
    txtDate = datetime.datetime.strptime(data['date'], "%Y-%m-%d")   # 文本时间
    today = datetime.datetime.today()                                # 今日时间
    todayDate = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
    dateDiff = (todayDate - txtDate).days                            # 天数差

    filesJsonList = []                                               # 构造新的json列表
    # 根据操作files字典
    for eachRestDay in data["files"]:
        eachRestDay["restTime"] = eval(eachRestDay["restTime"]) - dateDiff
        newJsonString = {"restTime": str(eachRestDay["restTime"]), "file": eachRestDay["file"]}

        # 若文件到期则删除文件
        if eachRestDay["restTime"] < 0:
            for eachDeleteFile in eachRestDay["file"]:
                files.remove(eachDeleteFile)
                if os.path.isdir(eachDeleteFile):
                    shutil.rmtree(eachDeleteFile)
                else:
                    os.remove(eachDeleteFile)
        else:
            for eachSpecivalFile in eachRestDay["file"]:
                files.remove(eachSpecivalFile)
            filesJsonList.append(newJsonString)

    # 当日新删除的文件
    if len(files) != 0:
        newFileJsonDict = {"restTime": "30", "file": files}
        filesJsonList.append(newFileJsonDict)                        # 将当日新删除的文件加入json列表中

    # 待存储的内容
    newJsonString = '{"date":"'+str(datetime.date.today())+'", "files":'+str(filesJsonList)+'}'
    file = open('garbage.txt', 'w', encoding='utf-8')
    file.write(newJsonString)
    file.close()
