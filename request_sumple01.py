import requests

岩手県八幡平市大更の情報をrequestsモジュールを使って取得してね。
response = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111")

print(response)

print(response.text)
# 引っ張ってくる

別の郵便番号で試す。
response = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=1130007")
