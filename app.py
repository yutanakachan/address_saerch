from address_seacher import AddressSeacher


def main():
    # ユーザーからの郵便番号を受け取る
    # 郵便番号を使って地名をとってくる
    # #地名をプリントする

    postal_code = input("郵便番号を入力してください例1110074　入力:")
    address_sercher = AddressSeacher()
    location = address_sercher.search(postal_code)
    print(location)



if __name__ == "__main__":
    main()
