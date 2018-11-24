from address_seacher import AddressSeacher


def main():
    # ユーザーからの郵便番号を受け取る
    postal_code = input("郵便番号を入力してください例1110074　入力:")
    # 郵便番号を使って地名をとってくる
    address_sercher = AddressSeacher()

    location = address_sercher.search(postal_code)
    # #地名をプリントする
    print(location)


if __name__ == "__main__":
    main()
