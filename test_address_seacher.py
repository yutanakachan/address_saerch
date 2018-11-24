import unittest

import requests

class AddressSeacher:
    def search(self, postal_code):
        url = "http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111"

        response = requests.get(url)
        都道府県 = response.json()["results"][0]["address1"]
        市区町村 = response.json()["results"][0]["address2"]
        町域 = response.json()["results"][0]["address3"]
        return f"{都道府県}{市区町村}{町域}"


class TestAddressSeacher(unittest.TestCase):
    def test_岩手県八幡平市大更の地名を郵便番号から取得できる(self):
        address_sercher = AddressSeacher()

        actual = address_sercher.search(postal_code="0287111")

        self.assertEqual("岩手県八幡平市大更", actual)

    def test_東京都練馬区豊玉南の地名を郵便番号から取得できる(self):
        address_sercher = AddressSeacher()

        actual = address_sercher.search(postal_code="1760014")

        self.assertEqual("東京都練馬区豊玉南", actual)









if __name__ == "__main__":
    unittest.main()
