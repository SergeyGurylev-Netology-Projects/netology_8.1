import sys
import requests

base_url = 'https://akabab.github.io/superhero-api/api/'

if __name__ == '__main__':
    uri = 'all.json'
    response = requests.get(base_url+uri)
    if not response.ok:
        print(f'Request error {response.status_code}: {response.reason}')
        sys.exit()

    downloaded_heroes_list = response.json()
    desired_heroes_list = ['Hulk', 'Captain America', 'Thanos'] # список анализируемых героев
    smartest_hero = {'name': 'Smartest hero not found', 'intelligence': None} # результат - кто самый умный

    desired_heroes_list = [n.lower() for n in desired_heroes_list]

    for hero in downloaded_heroes_list:
        if hero['name'].lower() in desired_heroes_list:
            hero_intelligence = hero['powerstats']['intelligence']
            if smartest_hero['intelligence'] is None or hero_intelligence>smartest_hero['intelligence']:
                smartest_hero['name'] = hero['name']
                smartest_hero['intelligence'] = hero_intelligence

    if smartest_hero['intelligence'] is None:
        print(smartest_hero['name'])
    else:
        print(f'Smartest hero is {smartest_hero["name"]} with intelligence {smartest_hero["intelligence"]}')
