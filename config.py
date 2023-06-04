
# Directories.
D_IMAGES    = "/mnt/hgfs/Spatula/images"
# Files.
F_LOG       = "/mnt/hgfs/Spatula/URLNumber"

DB_USERNAME = ""
DB_PASSWORD = ""
DB_HOSTNAME = "localhost"
DB_DATABASE = "spatula"

# Maximum / Minimums.
MINIMUM_TITLE_CHARACTERS = 3
MINIMUM_COOK_LENGTH      = 1
MAXIMUM_INCREMENT        = 1000000
URL_NUM                  = 1

# Provide the Domain to scrape up until the start of the incremental number in
# URL.
DOMAINS = [
    "https://www.bigoven.com/recipe",
    "https://cookpad.com/us/recipes"
]

# TODO: Capitalize this.
DefaultHashArray = [
    "348e23011e734c1b43d2b65394359c3e",
    "0d735afddc9f4d5cf134bfcf3841afc7",
    "b6403adc9831bea0022a0bfa8ba476ca",
    "5f9e9e05cd6f4381be93173a654d305e",
    "c5f8b282a5ae8e88ef44298fee9c7237",
    "2c3858d4403bb1ac461cf6b7c1416c18",
    "15a28ec14af068846b02edcb8c8ec2f8",
    "2c372f4e750594710313826988885533",
    "4b0b51eba97af3c47367028f3fc79e72"
]

# Build information.
TITLE = "Spatula"
DESCRIPTION = "An incremental recipe scraper"
PROJECT_LINK = "https://rethy.xyz/Projects/Spatula"
VERSION = "v1.0 - First release"