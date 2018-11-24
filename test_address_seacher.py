import unittest


class AddressSeacher:
    def search(self, postal_code):
        return "岩手県八幡平市大更"


class TestAddressSeacher(unittest.TestCase):
    def test_岩手県八幡平市大更の地名を郵便番号から取得できる(self):
        address_sercher = AddressSeacher()

        actual = address_sercher.search(postal_code="0287111")

        self.assertEqual("岩手県八幡平市大更", actual)


if __name__ == "__main__":
    unittest.main()
