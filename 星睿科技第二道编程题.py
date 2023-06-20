import csv
import requests

# 下载测试数据到本地
url = "https://edidata.oss-cn-beijing.aliyuncs.com/fyx_chinamoney.csv"
filename = "test_data.csv"
response = requests.get(url)
with open(filename, "wb") as file:
    file.write(response.content)

# 读取测试数据并拆分为多个数组
batch_size = 80
data = []
with open(filename, "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)
        if len(data) == batch_size:
            print(data)
            data = []

# 打印剩余的数据（如果有）
if data:
    print(data)
