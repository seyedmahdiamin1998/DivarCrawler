## Divar Crawler
Divar Crawler is a project to crawl data from the Diver website. In this project, I focus on extracting **car ad** data from **Mashhad** city.

> Divar is an Iranian Farsi classified ads and E-commerce mobile app, and an online platform for users in Iran sections devoted to real estate, vehicles, goods, community service, Industrial equipment, and jobs.
website: [https://divar.ir/s/mashhad/auto]

![Screenshot](.//assets//img//divar.JPG)

___

## Intallation

```
$ pip install -r requirements.txt
```
___

## Run it
```
$ cd divar
$ scrapy crawl mashhad -o results.json
```
___

## result example
```
{
    "name": "مگان ۹۰ اتومات  ۲۰۰۰",
    "category": "car",
    "model": "Renault Megan-ir 2000cc", 
    "vehicleTransmission": "automatic",
    "productionDate": "۱۳۹۰",
    "url": "https://divar.ir/v/%D9%85%DA%AF%D8%A7%D9%86-%DB%B9%DB%B0-%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA-%DB%B2%DB%B0%DB%B0%DB%B0_%D8%B3%D9%88%D8%A7%D8%B1%DB%8C-%D9%88-%D9%88%D8%A7%D9%86%D8%AA_%D9%85%D8%B4%D9%87%D8%AF_%D9%85%DB%8C%D8%AF%D8%A7%D9%86-%D8%B9%D8%AF%D9%84-%D8%AE%D9%85%DB%8C%D9%86%DB%8C_%D8%AF%DB%8C%D9%88%D8%A7%D8%B1/wYjjbp-M", "mileageFromOdometer": 180000,
    "knownVehicleDamages": "intact",
    "priceCurrency": "IRR", 
    "price": "8700000000.0", 
    "color": "خاکستری", 
    "brand": "Renault", 
    "description": "مگان موتور ۲۰۰۰ اتومات \nفول سه پرده بدون پارگی \nمانیتور بزرگ فابریک \nبدون رنگ شدگی \nکارکرد واقعی تک‌ برگ سند\nتزیینات و تو دوزی تمیز در حد \nموتوری و گیربکس به شرط مکانیک \nدوربین و سنسور عقب \n۴ حلقه لاستیک نو خارجی\nقابل معاوضه با خودرو \nادرس نمایشگاه مشهد نبش خرمشهر ۸ \nاتو گالری مهتاب"
}

```
___
## License
This project is licensed under the terms of the MIT license.