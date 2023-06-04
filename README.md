# Spatula          

          ████  
        ██░░░░██  
      ██░░░░░░░░██
      ██░░░░░░░░██
    ██░░░░░░░░░░░░██
    ██░░░░░░░░░░░░██
    ██░░░░░░░░░░░░██
      ██░░░░░░░░██
        ████████

## Requirements
- mysql_connector_repackaged==0.3.1
- Pillow==9.3.0
- recipe_scrapers==14.24.0
- requests==2.25.1

## Operating Systems
Linux x64/x86 is required.

## Source Files
### main.py
`main.py` is the main file you will run when executing Spatula. Run the following in your terminal: `python3 main.py`

### config.py
`config.py` contains the main variable declarations. This is where you should make your changes. `config.py` controls (most) internal scraping processes. Here are the following options you can set:
- D_IMAGES
    - This is the directory that hold the images Spatula will download. Paths to these images will be placed in the database that link up to the recipe ID.
- F_LOG
    - This file simply holds a single number. This number is the last incremented recipe ID so Spatula can keep track of scraping history in case of program failure/closure. This file is created automatically on first run.
- DB_USERNAME
- DB_PASSWORD
- DB_HOSTNAME
- DB_DATABASE
- MINIMUM_TITLE_CHARACTERS
    - This is the minimum number of characters a title can be before the recipe is skipped. It's not recommended to go below 3, as the quality of the recipe is likely low.
- MINIMUM_COOK_LENGTH
    - This is the minimum time a recipe can be prepared. It's not recommended to go below 1, as a zero or below usually denotes poor quality/attention to detail when making the recipe article.
- MAXIMUM_INCREMENT
    - This is the maximum number a recipe website will have recipes scraped to. The default is 1000000, but any number is okay here, as long as there are recipes to scrape.
- URL_NUM
    - This is the number your scraper will start at. The default is set to 1. After the first time Spatula is run, this number will no longer be used using your F_LOG file is removed.
- DOMAINS
    - This array contains websites that have numbers denoting recipes. Recipe websites in here should only contain the URL up to the number.
    - Examples:
        - https://www.bigoven.com/recipe
        - https://cookpad.com/us/recipes
    - Do not put a slash at the end of the URL.
- DefaultHashArray
    - Any default hashes for images should be placed here in MD5 format. This way, if a downloaded image matching a hash in the array is encountered, the recipe will be skipped.

#### spatula.py
`spatula.py` contains the recipe scraping portion of Spatula.
`spatula.py` secondarily runs initialization tasks, such as creating files and directories according to variable content imported from `config.py`.

#### color.py
`color.py` contains color declarations.

#### stdlib.py
`stdlib.py` contains few standard wrapper functions, such as File.Exists() and WriteImageURLToFile(). It isn't much as of now, but it will grow in the future where needed.

#### tagger.py
`tagger.py` decides what category/categories a recipe should be in.
Admittedly, it's very primitive at the moment, only looking at the title as a means to determine weather or not a recipe should be a member of a category. This is very limited, as you do have titles such as "Beer Batter", which in the past would end up going in the "Drinks" category. This has been subverted by using exemption keywords, which stops certain title strings - such as "beer batter" - from being included in certain categories. It is over-engineered, and frankly underpreforming, but it does the job, albeit with many recipes being skipped due to the title limitation.
`tagger.py` needs work.

#### database.sql
`database.sql` contains all SQL code you need to setup a Spatula database.
You can freely modify the category names and titles where you see fit, though defaults are provided. Your changes will have to be reflected in `spatula.py`.

## TODO
- [ ] Work on README.md, specifically style and orgainzation
- [ ] Test URLs in `sitelist.md`