import os
import color
import hashlib
import requests

from PIL import Image

class Directory:
    def Exists(path):
        # Do proper handling here.
        return os.path.isdir(path)
class File:
    def Exists(path):
        # Do proper handling here.
        return os.path.isfile(path)

def Normalize(string):
    return string\
        .replace("\n", ",,")\
        .replace("\r", ",,")\
        .replace("'", "")

# Generic.
class Item:
    def Exists(path):
        # Do proper handling here.
        return os.path.exists(path)

def WriteImageURLToFile(imageURL, URLNumber, imageDirectory, defaultHashes):
    # TODO: Hash file content from web so I don't have to save then remove.
    imageBinary = requests.get(imageURL)
    if not imageBinary:
        print(f"{color.bad}No image data received/invalid URL.{color.endc}")
        return False

    # Check if the file already exists in the images directory.
    while os.path.isfile(imageDirectory + "/" + str(URLNumber) + ".jpg"):
        URLNumber += 1
    imagePath = imageDirectory + "/" + str(URLNumber) + ".jpg"

    with open(imagePath, "wb") as filePointer:
        filePointer.write(imageBinary.content)

    # Setup image buffer.
    imageBuffer = Image.open(imagePath)
    # Define image height and width from object information.
    imageHeight, imageWidth = imageBuffer.size
    with open(imagePath, "rb") as filePointer:
        content = filePointer.read()

    # Setup the hash using the hash library.
    md5Hash = hashlib.md5()
    md5Hash.update(content)
    imageHash = md5Hash.hexdigest()

    # Check if image is a default/placeholder image. In other words, does the
    # recipe have an image that's valuable to use?
    if imageHash in defaultHashes:
        print(f"Default image hash. Skipping.")
        os.remove(imagePath)
        return False

    # Image resize ratios.
    if imageWidth > 3200:
        ratio = 4
    elif imageWidth > 1600:
        ratio = 2
    elif imageWidth > 1200:
        ratio = 1.5
    elif imageWidth <= 250:
        print(f"Image width {imageWidth} less than than 250.")
        os.remove(imagePath)
        return False

    try:
        if ratio:
            imageWidth = int(imageWidth / ratio)
            imageHeight = int(imageHeight / ratio)

            imageBuffer.resize((imageWidth, imageHeight))
            imageBuffer.save(imagePath)
    except UnboundLocalError:
        pass

    #print(f"{color.warn}Width: {str(imageWidth)}{color.endc}")
    #print(f"{color.warn}Height: {str(imageHeight)}{color.endc}")

    return imagePath

def CleanFractions(str):
    return str\
        .replace("½", "1/2")\
        .replace("¼", "1/4")\
        .replace("¾", "3/4")\
        .replace("⅓", "1/3")\
        .replace("⅔", "2/3")\
        .replace("⅕", "1/5")\
        .replace("⅖", "2/5")\
        .replace("⅗", "3/5")\
        .replace("⅘", "4/5")\
        .replace("⅙", "1/6")\
        .replace("⅚", "5/6")\
        .replace("⅛", "1/8")\
        .replace("⅜", "3/8")\
        .replace("⅝", "5/8")\
        .replace("⅞", "7/8")