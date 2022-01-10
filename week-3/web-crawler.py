import urllib.request
import json

# get response
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with urllib.request.urlopen(url) as response:
   html = response.read()

# Convert from JSON to Python (dict)
json_object = json.loads(html)
# results List
results = json_object["result"]["results"]

# return 景點名稱,區域,經度,緯度,第一張圖檔網址 format Function
def analyzeData(data):
    # 景點名稱
    stitle = data["stitle"]
    # 區域
    address = data["address"]
    district = address[address.find("區")-2:address.find("區")+1]
    # 經度
    longitude = data["longitude"]
    # 緯度
    latitude = data["latitude"]
    # 第一張圖檔網址
    files = data["file"].lower()
    img = files[:files.find(".jpg")+4]
    return f"{stitle},{district},{longitude},{latitude},{img}"

with open("data.csv", "w") as f:
    for result in results:
        f.write(analyzeData(result)+"\n")