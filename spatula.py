#!/usr/bin/python3
import os
import re
import sys
import json
import time
import color
import requests
import mysql.connector

from datetime import datetime
from recipe_scrapers import scrape_me

# User defined modules.
import stdlib
from config import *
from tagger import *


def Scraper(domain):
    # Initialize variables.
    dbPointer = ""
    dbSchema  = ""
    urlNum    = URL_NUM

    PrintEgg()
    PrintMOTD()
    PrintVersion()

    if not stdlib.Directory.Exists(D_IMAGES):
        os.mkdir(D_IMAGES)

    if stdlib.File.Exists(F_LOG):
        with open(F_LOG) as f:
            urlNum = int(f.read())

    dbPointer, dbSchema = dbInit(DB_USERNAME, DB_PASSWORD, DB_HOSTNAME, DB_DATABASE)

    print(f"URL number starting at {str(urlNum)}.")
    print(f"Database credentials: {DB_USERNAME}, {DB_PASSWORD}, {DB_HOSTNAME}, {DB_DATABASE}")
    print("")

    for urlNum in range(urlNum, MAXIMUM_INCREMENT, 1):
        scrapePointer  = ""
        title          = ""
        amount         = ""
        recipeURL      = ""
        cookTime       = ""
        instructions   = ""
        ingredients    = []

        print(f"{domain}/{str(urlNum)}")

        with open(F_LOG, "w") as filePointer:
            filePointer.write(str(urlNum))

        # TODO: Error checking here.
        scrapePointer = scrape_me(f"{domain}/{str(urlNum)}")

        try:
            title = scrapePointer.title()
            cookTime = scrapePointer.total_time()
            amount = scrapePointer.yields()
            ingredients = scrapePointer.ingredients()
            instructions = scrapePointer.instructions()
            recipeURL = scrapePointer.image()
        except:
            print(f"Execption when pulling recipe.\n")
            continue

        if len(title) <= MINIMUM_TITLE_CHARACTERS:
            print(f"{color.bad}Title smaller than {color.title}{MINIMUM_TITLE_CHARACTERS}{color.bad} characters.{color.endc}\n")
            continue
        if not cookTime:
            print(f"{color.bad}Cook length less than minimum of \"{color.title}{MINIMUM_COOK_LENGTH}{color.bad}\".{color.endc}\n")
            continue
        if not amount:
            print(f"{color.bad}Yield equal to \"{color.title}{str(amount)}{color.bad}\", which is too small.{color.endc}\n")
            continue
        for Line in ingredients:
            if len(Line) <= 3:
                print(f"{color.bad}Ingredient line equal to \"{color.title}{str(len(Line))}{color.bad}\".{color.endc}\n")
                continue
        if len(instructions) <= 3:
            print(f"{color.bad}Instruction line equal to \"{color.title}{str(len(instructions))}{color.bad}\".{color.endc}\n")
            continue
        if not recipeURL:
            print(f"{recipeURL} URL is empty.\n")
            continue

        ''' Go through error checking, and then write the data input query.
            Ensure I build the list(s) using \n as the delimiter. This will be
            taken apart as <li>s when PHP processes it. '''
        #FILE_TITLE = re.sub(r'[^a-zA-Z]', '', title)

        image = stdlib.WriteImageURLToFile(recipeURL, urlNum, D_IMAGES, DefaultHashArray)
        if not image:
            print(f"Removed {recipeURL}.\n")
            continue
        image = image.replace(f"{D_IMAGES}/", "")
        print(image)

        title = stdlib.Normalize(title)

        ingredients = ",,".join(ingredients)
        ingredients = stdlib.Normalize(ingredients)

        instructions = stdlib.Normalize(instructions)

        tags = generateTags(title)
        if not tags:
            print(f"No tags found. Skipping.\n")
            #print(f"\t- {color.bad}{len(tags)} tags.{color.endc}\n")
            continue

        # TODO: Change yield to amount in database.
        dbPointer.execute(
            "INSERT INTO\
                 recipe(\
                     recipeTitle,\
                     recipeUploadData,\
                     recipeImage,\
                     recipeTags,\
                     recipeCookTime,\
                     recipeAmount,\
                     recipeIngredients,\
                     recipeInstructions\
                 )\
                 VALUES(\
                     '" + title + "',\
                     '" + str(datetime.date(datetime.now())) + "',\
                     '" + image + "',\
                     '" + tags + "',\
                     '" + str(cookTime) + "',\
                     '" + str(amount) + "',\
                     '" + ingredients + "',\
                     '" + instructions + "'\
                 );"
        )

        dbSchema.commit()
        ''' TODO: Check why I did this. Really, I have no idea. '''
        print(dbPointer, end=''); print("\n")

    with open(F_LOG, "w") as filePointer:
        filePointer.write("0")

def dbInit(username, password, hostname, database):
    try:
        dbSchema = mysql.connector.connect(
            user = username,
            password = password,
            host = hostname,
            database = database
        )
    except mysql.connector.errors.DatabaseError:
        print(f"- {color.bad}Can't connect to database at \"{hostname}\".{color.endc}")
        sys.exit(1)

    return dbSchema.cursor(), dbSchema

def PrintColorfulBar(length):
    print('#', end='')
    for i in range(0, length + 2, 1):
        if (i % 3) == 2:
            print(f"{color.good}={color.endc}", end="")
        elif (i % 3) == 1:
            print(f"{color.warn}={color.endc}", end="")
        else:
            print(f"{color.bad}={color.endc}", end="")
    print('#')

def PrintEgg():
    print("      ████")
    print("    ██░░░░██")
    print("  ██░░░░░░░░██")
    print("  ██░░░░░░░░██")
    print("██░░░░░░░░░░░░██")
    print("██░░░░░░░░░░░░██")
    print("██░░░░░░░░░░░░██")
    print("  ██░░░░░░░░██")
    print("    ████████")
    print("")
def PrintMOTD():
    print(f"{TITLE}: {DESCRIPTION}")
    print(f"rethy.xyz (C) 2023")
    print("")
def PrintVersion():
    print(f"{VERSION}")
    print(f"Past versions can be found at {PROJECT_LINK}")
    print("")