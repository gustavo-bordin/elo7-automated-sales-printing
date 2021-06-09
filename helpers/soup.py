from bs4 import BeautifulSoup

def create_soup_obj(page_content):
    return BeautifulSoup(page_content, "html.parser")