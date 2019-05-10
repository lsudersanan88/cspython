"""
exercise_06  Scraping and Saving

Write a class that scrapes and saves the HTML of a URL (as a plain text file). If the URL to be scraped has been saved, it should
be opened from the saved file and returned without making a new web request.

This class will be named "ScrapeSaver" and has 3 definitions:

 1) an __init__ function that accepts a base_url to scrape and a save_location, both are strings
    * The base URL should be of the format "http://www.uniprot.org/uniprot/{}.fasta" where each item to be scraped
       will replace the {} in the base url ( this is done with base_url.format(item) )
    * The save location is the folder path where the text scraped will be saved

 2) a "retrieve" function that accepts a single argument, the name to be scraped. EX: 'P69892'
    * The retrieve definition should first check if the item to be scraped has already been scraped and saved
       to the save_location.
    * If it exists, then this function should read the file and return the contents without
       making a new web requests.
    * If the save does not exist, then the url should be scraped and saved as a string in a plain text file.

 3) a __str__ function that returns a list of files in the save_location


"""
import os
import urllib.request as ur

class ScrapeSaver:

    def __init__(self, base_url, save_location):
        return

    def retrieve(self, item):
        return

    def __str__(self):
        return


if __name__ == '__main__':
    """
    Here is where the Scrape_Saver class is tested.
    """

    url = "http://www.uniprot.org/uniprot/{}.fasta"
    save_dir = 'data/'
    ss = ScrapeSaver(url, save_dir)

    item = 'P69892'
    print(ss.retrieve(item))  # if the item is downloaded to the 'data/' folder, no web request should be made