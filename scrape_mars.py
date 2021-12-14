import pandas as pd
from splinter import Browser, browser
from webdriver_manager.chrome import ChromeDriverManager 

def scrape_start(): 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    newstitle, newspara = mars_news(browser)

    dataset = {
        "newstitle": newstitle,
        "newspara": newspara,
        "featured_image_url": featured_image_url(browser),
        "mars_facts": mars_facts(),
        "hemispheres": hemispheres(browser)
    }
    browser.quit()
    return dataset


def scrape_part1(browser): 
# Part 1
# Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

    browser.visit('https://redplanetscience.com/')
    newstitle =  browser.find_by_css('div.content_title').text,
    newstitle
    newspara = browser.find_by_css('div.article_teaser_body').text
    newspara

    return newstitle, newspara


def scrape_part2(browser):
# Part 2
# JPL Mars Space Images - Featured Image
# Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).
#  Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
# Make sure to find the image url to the full size `.jpg` image.
# Make sure to save a complete url string for this image.

    browser.visit('https://spaceimages-mars.com/')
    browser.find_by_tag('button')[1].click()
    featured_image_url = browser.find_by_css('img.fancybox-image')['src']
    featured_image_url

    return featured_image_url


def scrape_part3(browser):
# Part 3
# Mars Facts
#  Visit the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# Use Pandas to convert the data to a HTML table string.

    mars_facts = pd.read_html('https://galaxyfacts-mars.com/', index_col=0,header=0)[0].to_html(classes='table table-striped')
    mars_facts 
    
    return mars_facts


def scrape_part4(browser): 
# Part 4 
# Mars Hemispheres
# Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


    browser.visit('https://marshemispheres.com/')
    hemispheres = []

    for i in range(4):
            hemisphere = {}
            browser.find_by_css('a.itemLink h3')[i].click()
            hemisphere['title'] = browser.find_by_tag('h2').text
            hemisphere['url'] = browser.find_by_text('Sample')['href']
            hemispheres.append(hemisphere)
            browser.back()
    browser.quit()
    hemispheres
    return hemispheres