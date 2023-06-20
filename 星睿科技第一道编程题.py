import requests
import csv
from bs4 import BeautifulSoup

# 定义要爬取的网页链接
url = "https://iftp.chinamoney.com.cn/english/bdInfo/"

# 定义查询条件
params = {
    "BondType": "TreasuryBond",
    "IssueYear": "2023"
}

# 发起HTTP GET请求，并传递查询条件
response = requests.get(url, params=params)

# 解析HTML内容
soup = BeautifulSoup(response.content, "html.parser")

# 查找表格数据
table = soup.find("table")

# 提取表格的列名
header = [th.text.strip() for th in table.find_all("th")]

# 提取表格的行数据
rows = []
for tr in table.find_all("tr"):
    row = [td.text.strip() for td in tr.find_all("td")]
    if row:
        rows.append(row)

# 将数据保存为CSV文件
filename = "bond_data.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(rows)

print(f"数据已保存到 {filename}")
