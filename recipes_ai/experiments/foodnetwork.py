from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
from pathlib import Path


PAGES_TO_SEARCH_FOR_LINKS = {
    'foodnetwork': ['https://foodnetwork.co.uk/recipes/',
                    'https://foodnetwork.co.uk/roast-chicken-recipes/',
                    'https://foodnetwork.co.uk/healthy-family-dinners/',
                    'https://foodnetwork.co.uk/vegetarian-food/',
                    'https://foodnetwork.co.uk/pasta-bake-recipes/',
                    'https://foodnetwork.co.uk/recipes/lemon-blueberry-ricotta-buttermilk-pancakes-blueberry-cassis-relish-and-blueberry-maple/',
                    'https://foodnetwork.co.uk/best-ever-weeknight-pork-chop-recipes/',
                    'https://foodnetwork.co.uk/chocolate-cake-recipe-collection/',
                    'https://foodnetwork.co.uk/new-year-occasion/',
                    'https://foodnetwork.co.uk/50-ways-sweet-potatoes/',
                    'https://foodnetwork.co.uk/italian-family-dinners/'
                   ]
}

def get_ingredients_foodnetwork(page):
    ingredients = []
    for ingredient in page.findAll('div', attrs={'class':'ingredient'}):
        ingredients.append(ingredient.text)
    return ingredients

def get_instructions_foodnetwork(page):
    instructions = []
    div = page.find('div', attrs={'class':'recipe-text'})
    for ele in div:
        if ele.name == 'p':
            instructions.append(ele.text)
    return instructions


def get_images_foodnetwork(page, download_path=Path('.'), image_name='image.jpg'):
    images = []
    image_name = image_name if len(image_name.split('.')) > 1 else image_name + '.jpg'
    counter = 1
    for div in page.findAll('picture'):
        for ele in div:
            if ele.name == 'img':
                name = image_name.split('.')[0] + '_' + str(counter) + '.' + image_name.split('.')[1]
                urllib.request.urlretrieve(ele.attrs['srcset'], Path(download_path / name))
                images.append(ele.attrs['srcset'])
                counter += 1
        return images

    
def get_cooking_time_foodnetwork(page):
    cooking_time = None
    ul = page.find('ul', attrs={'class':'recipe-head'})
    for li in ul:
        if hasattr(li, 'text') and li.next_element.text == 'Cooking Time':
            cooking_time = li.find_next('strong').text
    return cooking_time


def get_difficulty_foodnetwork(page):
    difficulty = None
    ul = page.find('ul', attrs={'class':'recipe-head'})
    for li in ul:
        if hasattr(li, 'text') and li.next_element.text == 'Difficulty':
            difficulty = li.find_next('strong').text
    return difficulty

def get_recipe_name_foodnetwork(page):
    difficulty = None
    section = page.find('section', attrs={'class':'article-head'})
    h1 = page.find('h1')
    return h1.text

def get_tags_foodnetwork(page):
    tags = []
    div = page.find('div', attrs={'class':'tags'})
    for a in div.findAll('a'):
        tags.append(a.text)
    return tags

def get_links_for_recipes_foodnetwork(page):
    recipe_links = {}
    for card in page.findAll('a', attrs={'class':'card-link'}):
        if card.name == 'a':
            recipe_links[card.attrs['title']] = "https://foodnetwork.co.uk" + card.attrs['href']
    return recipe_links

def recipe_url_db_foodnetwork(ref_pages, database):
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    for page in ref_pages:
        driver.get(page)
        page_content = driver.page_source
        links = get_links_for_recipes_foodnetwork(BeautifulSoup(page_content))
        database.update(links)
    
    return database