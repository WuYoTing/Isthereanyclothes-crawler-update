# Isthereanyclothes-crawler-update

Base on old version of Isthereanyclothes

## Installation

Use Request,Beautiful Soup,Selenium to crawl data.

1. install dependencies.

```bash
pipenv install
```

2. Set up .env

```bash 
Crawler_DB_IP=""         //Your Database Ip 
Crawler_DB_Name=""       //Your Database Name
Crawler_DB_User=""       //Your Database User Name
Crawler_DB_Password=""   //Your Database User Password

TG_BOT=""                //Telegram Bot Token
TG_TO=""                 //Telegram Recever Id
```

3. Run isthereanyclothes_crawler.py

## offical api analysis

| offical           | local                   |  
| ----------------- |:----------------------- |
| l1GoodsCd         | prod number             |
| goodsNm           | prod name               |
|                   | sex                     |
| dtlExp            | about                   | 
| materialInfo      | material                |
| termLimitSalesEndMsg| limited_price_date      |
|                   | category                |
| dispL2GoodsKey    | main_image_url          |
| fixed format      | size_url                | 
| newFlg            | is_new_good             |
| onlineLimitFlg    | is_online_only          |
| specialSizeFlg(?) | is_set                  | 
| termLimitSalesEndMsg   | is_limited_time         |
| discountFlg       | is_price_down           |
| Share & Publish   | can_modify              |

