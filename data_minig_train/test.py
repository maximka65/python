import requests
from parsel import Selector
from urllib.parse import urljoin



response = requests.get('https://auto.youla.ru/advert/used/bmw/3_series/prv--310ea6e666593166/').text
response = Selector(text=response)

#'images': [i for i in map(lambda i: i.attrib['src'], response.css('div.PhotoGallery_photoWrapper__3m7yM img'))],

#data = {'params': [{str(i.css('div.AdvertSpecs_label__2JHnS::text').get()): i.css('div.AdvertSpecs_data__xK2Qx::text').get()}
#         for i in response.css('div.AdvertSpecs_row__ljPcX')]}
#data['params'][0]['Год выпуска'] = response.css('div.AdvertSpecs_row__ljPcX a::text').get()

print(response.css('div.AdvertCard_descriptionInner__KnuRi::text').get())

print(1)