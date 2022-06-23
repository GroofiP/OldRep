from selenium.common.exceptions import NoSuchElementException


def search_try(dri, up, name_link, link_reg, link_item):
    try:
        results = dri.find_element_by_class_name(link_reg)
        return results
    except NoSuchElementException:
        if "m.video" == name_link:
            try:
                results = dri.find_element_by_tag_name("mvideoru-product-details-card")
                return results
            except NoSuchElementException:
                pass
        up.message.reply_text(f"Короче соснули мы! Там капча! Хз чо делать. Давай потом поговорим."
                              f"Гребанный {name_link}\n {link_item}")
        return []


def search_if_else(up, results, name_link, link_search, link_item):
    if link_search in results.text:
        up.message.reply_text(f"Поздравляю кое что нашли по ссылке в {name_link}: {link_item} ")
    else:
        up.message.reply_text(f"По этой ссылке ничего: {link_item} ")
