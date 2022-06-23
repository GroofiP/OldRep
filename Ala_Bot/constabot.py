# search/v1.py
PATH_LINK = {
    "citi_link_main":
        [
            "product_data__gtm-js",
            "https://www.citilink.ru/search/?text=%D0%9A%D0%BE%D0%BD%D1%81%D0%BE%D0%BB%D1%8C+ps+5"
        ],
}
PATH_SEARCH = {
    "dns":
        [
            "product-card-top__buy",
            "Купить",
            ["https://www.dns-shop.ru/product/2645e72c6fca1b80/igrovaa-konsol-playstation-5/",
             "https://www.dns-shop.ru/product/44f657d4ac493332/igrovaa-konsol-playstation-5-digital-edition/"]
        ],
    "citi_link":
        [
            "ProductCardLayout__product-description",
            "В корзину",
            ["https://www.citilink.ru/product/igrovaya-konsol-playstation-5-ps719398707-belyi-chernyi-1476353/",
             "https://www.citilink.ru/product/igrovaya-konsol-playstation-5-ps719398707-belyi-1438618/",
             "https://www.citilink.ru/product/igrovaya-konsol-playstation-5-digital-edition-ps719398806-belyi-1438620/", ]
        ],
    # "m.video":
    #     [
    #         "product-price",
    #         "₽",
    #         ["https://www.mvideo.ru/products/geimpad-sony-playstation-5-dualsense-cfi-zct1w-40074732",
    #          "https://www.mvideo.ru/products/igrovaya-konsol-sony-playstation-5-40073270",
    #          "https://www.mvideo.ru/products/igrovaya-konsol-sony-playstation-5-digital-edition-40074203",
    #          "https://www.mvideo.ru/products/geimpad-sony-playstation-5-dualsense-cfi-zct1w-40074732"]
    #     ],
    "eldorado":
        [
            "buyBox",
            "Добавить в корзину",
            ["https://www.eldorado.ru/cat/detail/igrovaya-pristavka-sony-playstation-5/", ]
        ],
}


# template.py
TEXT_START = 'Ну привет. Как тебя зовут? Хотя без разницы, если не заешь что делать вводи /help'
TEXT_HELP = "/search для заветного поиска по твоим сайтам!\n" \
            "/search_link для подсчета товара в ситилинк"

if __name__ == '__main__':
    pass

