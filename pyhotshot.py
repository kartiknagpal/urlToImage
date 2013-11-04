import time

def screenshot(url, driver):
    driver.set_window_size(1024, 768) # optional
    driver.get(url)
    driver.save_screenshot('screen.png') # save a screenshot to disk
    #time.sleep(10)



if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.PhantomJS()
    screenshot("https://www.google.com/",driver)