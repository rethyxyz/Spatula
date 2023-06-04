#!/usr/bin/python3
import spatula

from config import *

def main():
    for domain in DOMAINS:
        spatula.Scraper(domain)

if __name__ == "__main__":
    main()