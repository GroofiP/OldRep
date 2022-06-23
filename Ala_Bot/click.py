from selenium import webdriver


def click_form(update, context):
    driver = webdriver.Firefox()
    item = "https://www.dns-shop.ru/product/5bcf683849e23330/kompaktnaa-mys-provodnaa-ritmix-rom-111-cernyj/"
    driver.get(item)
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector('button.buy-btn').click()
    driver.get("https://www.dns-shop.ru/order/begin/")
    driver.find_element_by_css_selector('button.buy-button').click()
    driver.find_element_by_css_selector('a.base-login-button__link').click()
    # driver.quit()
