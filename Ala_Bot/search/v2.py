import requests
from bs4 import BeautifulSoup

page_link = "https://vk.com"
user_headers = "mozilla/5.0 (symbianos/9.4; u; series60/5.0 nokia5800d-1/21.0.025; profile/midp-2.1 configuration/cldc-1.1 ) applewebkit/413 (khtml, like gecko) safari/413"
list_link = []


def if_parser(page_start, el):
    if "/" in el[0]:
        return page_start + el
    elif "http" in el:
        return el
    else:
        return page_start


def parser_every(page_ev, head_ev):
    response = requests.get(page_ev, headers={"user-agent": head_ev})
    return response.text


def all_date(list_l, list_o, page_start, count_l=0):
    while True:
        if count_l == len(list_o):
            break
        obj = list_o[count_l]
        try:
            elem = obj.attrs["href"].strip(" ")
        except KeyError:
            elem = "/"
        list_l.append(if_parser(page_start, elem))
        count_l = count_l + 1


def parser(list_links, page, head, count, count_l=0, count_ex=1):
    while int(count) > 0:
        if count_ex == count_l:
            count_ex = len(list_links)
            count = count - 1
        html = parser_every(page, head)
        soup = BeautifulSoup(html, "lxml")
        object_all = soup.find_all("a")
        all_date(list_links, object_all, page)
        page = list_links[count_l]
        count_l = count_l + 1


def print_for(list_l):
    links = set(list_l)
    for l in links:
        print(l)


def other():
    response = requests.get("https://www.dns-shop.ru/product/2645e72c6fca1b80/igrovaa-konsol-playstation-5/",
                            headers={"user-agent": user_headers})
    html = response.text
    print(html)
    soup = BeautifulSoup(html,"lxml")



other()
