from selenium import webdriver

def before_scenario(context, scenario):
    # Create an instance of the Chrome WebDriver
    context.driver = webdriver.Chrome()

def after_scenario(context, scenario):
    # Close the browser
    context.driver.quit()
