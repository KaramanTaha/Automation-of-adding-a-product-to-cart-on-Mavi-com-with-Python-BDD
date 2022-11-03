import time
import selenium
from behave import *
from selenium import webdriver


@given('User is on homepage')
def launchHomePage(context):
    context.driver = webdriver.Chrome(executable_path="T:\seleniumWebrivers\chromedriver.exe")
    context.driver.maximize_window()
    context.driver.get("https://www.mavi.com/")


@when('Choose cookie settings')
def cookieSettings(context):
    context.driver.find_element_by_xpath("//a[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection']").click()
    time.sleep(2)



@when('Click the search box and type "sweatshirt"')
def searchBox(context):
    context.driver.find_element_by_xpath("//button[@class='header__menu--search-button pw-search-present']//span[@class='header__menu--search-placeholder'][normalize-space()='Arama Yap']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//input[@class='input input-search pw-search-input pw-autocomplete-active']").send_keys("sweatshirt")
    time.sleep(2)



@when('Click search button')
def searchButton(context):
    context.driver.find_element_by_xpath("//button[@class='inputBox__search-logo pw-search-submit']//*[name()='svg']").click()
    time.sleep(2)

@when('Click on size filter')
def sizeFilter(context):
    context.driver.find_element_by_xpath("//div[contains(@data-filter-code,'size')]").click()
    time.sleep(2)



@when('Apply size filter as XL')
def applySizeFilter(context):
    context.driver.find_element_by_xpath("//span[contains(text(),'XL')]").click()
    time.sleep(2)



@when('Click on the Fit filter')
def fitFilter(context):
    context.driver.find_element_by_xpath("//span[contains(@class,'text')][contains(text(),'Fit/Kalıp')]").click()
    time.sleep(2)



@when('Apply fit filter as Oversize')
def applyFitFilter(context):
    context.driver.find_element_by_xpath("//span[contains(text(),'Oversize')]").click()
    time.sleep(2)


@when('Click on any product')
def aProduct(context):
    context.driver.find_element_by_xpath("//h3[contains(text(),'Mavi Pro Kapüşonlu Sweatshirt')]").click()



@when('Click on size selection')
def sizeFilter(context):
    context.driver.find_element_by_xpath("//div[@id='size-length']//div[contains(@class,'dropdown-button size:full type:border-8 mobile-type: color:white style:')]").click()



@when('Choose size as XL')
def applySizeFilter(context):
    context.driver.find_element_by_xpath("//ul[@class='size-list size-dropdown']//span[@class='number status:blue'][normalize-space()='XL']").click()



@when('Click the Add to Cart button')
def addToCartButton(context):
    context.driver.find_element_by_xpath("//button[@class='button button-add-to-cart pdp-add-to-cart add-to-cart dark js-add-to-cart add-to-cart-pdp']").click()
    time.sleep(10)



@when('Click the My Cart button')
def myCartButton(context):
    context.driver.find_element_by_xpath("//li[@class='header__menu--basket basket--full js-basket-icon']//a//*[name()='svg']").click()
    time.sleep(5)



@then('Check that the product is in the cart')
def checkProduct(context):
    status = context.driver.find_element_by_css_selector("span[class='name']").is_displayed()
    assert status is True


@then('Close browser')
def closeBrowser(context):
    context.driver.quit()

