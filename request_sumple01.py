import requests

岩手県八幡平市大更の情報をrequestsモジュールを使って取得してね。
response = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111")

print(response)

print(response.text)
# 引っ張ってくる

別の郵便番号で試す。
response = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=1130007")

以下コンソールにて
# import requests
# response = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111")
# print(response.text)
# {
# 	"message": null,
# 	"results": [
# 		{
# 			"address1": "岩手県",
# 			"address2": "八幡平市",
# 			"address3": "大更",
# 			"kana1": "ｲﾜﾃｹﾝ",
# 			"kana2": "ﾊﾁﾏﾝﾀｲｼ",
# 			"kana3": "ｵｵﾌﾞｹ",
# 			"prefcode": "3",
# 			"zipcode": "0287111"
# 		}
# 	],
# 	"status": 200
# }
# date = response.json()
# type(date)
# <class 'dict'>

# print(date["results"][0]["address1"])
# 岩手県
