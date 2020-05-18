class RecipeExtractor():
    def get_ingredients(self):
        pass
        
    def get_instructions(self):
        pass 
    
    def get_images(self):
        pass
    
    def get_prep_time(self):
        pass 
    
    def get_cooking_time(self):
        pass
    
    def get_num_servings(self):
        pass 

    def get_difficulty(self):
        pass
    
    def get_tags(self):
        pass
    
    def get_links_for_recipes(page):
        pass
    
    def _is_valid_page(self):
        pass
    
    def collect_recipe_urls(ref_pages, database):
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        for page in ref_pages:
            driver.get(page)
            page_content = driver.page_source
            links = get_links_for_recipes(BeautifulSoup(page_content))
            database.update(links)

        return database
    
    
    def collect_recipe_master_data(database, img_download_path=Path('images')): 
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        master_data = {'name': [], 'ingredients': [], 'instructions': [], 'images': [],
                       'prep_time': [], 'cooking_time': [], 'num_servings': [],
                       'difficulty': [], 'tags': [], 'url': []}

        for ix, r in tqdm(database.iterrows(), total=len(database)):
            name = r.loc['recipe_name']
            url = r.loc['recipe_url']
            driver.get(url)
            page_content = BeautifulSoup(driver.page_source)
            
            if not self._is_valid_page(page_content):
                continue

            # Obtain master data
            master_data['name'].append(name)
            master_data['url'].append(url)
            master_data['ingredients'].append(get_ingredients(page_content))
            master_data['instructions'].append(get_instructions(page_content))
            master_data['images'].append(get_images(page_content, img_download_path, name.lower()))
            master_data['cooking_time'].append(get_cooking_time(page_content))
            master_data['difficulty'].append(get_difficulty(page_content))
            master_data['tags'].append(get_tags(page_content))

        master_data_df = pd.DataFrame(master_data)

    return master_data_df