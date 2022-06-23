from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from constabot import PATH_SEARCH, PATH_LINK
from service import search_try, search_if_else


def search_ps5_link(update, context):
    driver = webdriver.Firefox()
    for k, v in PATH_LINK.items():
        driver.get(v[1])
        try:
            results = driver.find_elements_by_class_name(v[0])
        except NoSuchElementException:
            update.message.reply_text(f"Там капча! Идем дальше!")
            driver.quit()
            return
        if len(results) > 19:
            update.message.reply_text(f"Вот по этой ссылки добавился товар, наверное оно: {v[1]}")
        else:
            update.message.reply_text(f"По этой ссылке ничего: {v[1]}\n"
                                      f"В сити линке не добавляли товар")
    driver.quit()


def search_ps5(update, context):
    driver = webdriver.Firefox()
    for k, v in PATH_SEARCH.items():
        for item in v[2]:
            driver.get(item)
            result = search_try(driver, update, k, v[0], item)
            if isinstance(result, list):
                continue
            search_if_else(update, result, k, v[1], item)
        update.message.reply_text(f"К сожалению в {k} больше не какой инфы")
    update.message.reply_text(f"Пока что так обстоят дела. Заходи ещё!")
    driver.quit()


if __name__ == '__main__':
    pass
