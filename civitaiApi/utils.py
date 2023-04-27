"""

search_creators (username : str, limit : int = 100, page : int = 1)
Searching creators by username

"""

import requests, json
from .constants import API_URL
from .models import Creator, Model

def get_creators(limit : int = 100, page : int = 1) -> list[Creator]:
    creators = requests.post(API_URL + 'creators', {
        limit : limit,
        page : page
    })

    creators = json.loads(creators.text).get('items')
    result = list()

    for creator in creators:
        c = Creator(creator['link'], creator['username'], creator.get('modelCount'))
        result.append(c)

    return result

def get_models(username : str, types) -> list[Model]:
    query = f'username={username}&types={types}'
    models = requests.get(API_URL + 'models?' + query)

    models = json.loads(models.text)

    if type(models) == list:
        raise Exception(models)

    models = models.get('items')
    result = list()

    for model in models:
        m = Model(
            model.get('name'), 
            model.get('description'), 
            model.get('type'),
            model.get('nsfw'),
            )

        result.append(m)

    return result