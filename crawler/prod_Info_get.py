import datetime
import random

import requests
from bs4 import BeautifulSoup

from global_vars import user_agent_list
from sql_connector.sql_connector import sql_connector


def get_prod_info(prod_url, table_name, prod_sex):
    now = datetime.datetime.now()
    # currently cant get category
    prod_category = ""
    prod_number = prod_url.split("/")[-1]

    if table_name == "gu_clothes":
        prod_api = "https://www.gu-global.com/tw/store/ApiGetProductInfo.do?format=json&product=" \
                   + prod_number
        prod_size_url = "https://www.gu-global.com/tw/store/support/size/" + prod_number + \
                        "_size.html"
    elif table_name == "uniqlo_clothes":
        prod_api = "https://www.uniqlo.com/tw/store/ApiGetProductInfo.do?format=json&product=" \
                   + prod_number
        prod_size_url = "https://www.uniqlo.com/tw/store/support/size/" + prod_number + \
                        "_size.html"
    headers = {
        'user-agent': random.choice(user_agent_list),
        "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    man_index_res = requests.get(
        prod_api, headers=headers
    ).json()

    if table_name == "gu":
        prod_size_url = "https://www.gu-global.com/tw/store/support/size/" + prod_number + \
                        "_size.html"
    elif table_name == "uniqlo":
        prod_size_url = "https://www.uniqlo.com/tw/store/support/size/" + prod_number + \
                        "_size.html"
    else:
        prod_size_url = ""

    sql_connector(prod_sex, prod_category, prod_name, int(prod_price), prod_number, prod_about,
                  prod_material, prod_url, prod_main_image_url, prod_size_url, prod_is_newgood,
                  prod_is_onlineonly, prod_is_set, prod_is_limitedtime, prod_is_pricedown,
                  prod_can_modify, prod_limited_price_date, prod_get_time, table_name)
