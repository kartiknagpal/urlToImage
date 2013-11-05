#!/usr/bin/env python2

import web
from pyhotshot import screenshot
from selenium import webdriver
#import xml.etree.ElementTree as ET

# tree = ET.parse('acess_key.xml')
# root = tree.getroot()

urls = (
    '/urltoimg', 'get_screenshot'
)

app = web.application(urls, globals())

driver = webdriver.PhantomJS()

def my_loadhook():
    #print "my load hook"
    driver = webdriver.PhantomJS()


class get_screenshot:
    def GET(self):
        data_input = web.input()
        screenshot(data_input['url'], driver)
        web.header("Content-Type", "images/png") # Set the Header
        return open('screen.png',"rb").read() # Notice 'rb' for reading images

if __name__ == '__main__':
    app.run()
    app.add_processor(web.loadhook(my_loadhook))
    