import unittest

from address_seacher import AddressSeacher


class TestAddressSeacher(unittest.TestCase):
    def test_岩手県八幡平市大更の地名を郵便番号から取得できる(self):
        address_sercher = AddressSeacher()

        actual = address_sercher.search(postal_code="0287111")

        self.assertEqual("岩手県八幡平市大更", actual)

    def test_東京都練馬区豊玉南の地名を郵便番号から取得できる(self):
        address_sercher = AddressSeacher()

        actual = address_sercher.search(postal_code="1760014")

        self.assertEqual("東京都練馬区豊玉南", actual)

    def test_存在しない郵便番号が入力されたらエラーメッセージを表示する(self):
        address_searcher = AddressSeacher()
        actual = address_searcher.search(postal_code="1234567")

        expected = "該当するデータは見つかりませんでした。検索ワードを変えて再検索してください。"

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
