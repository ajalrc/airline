import os
import pathlib
import unittest
from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()#this func takes 
#a file and gets its url to open in the browser.
driver = webdriver.Chrome()#this allow us to run and simulate interaction
#the interaction with the chrome. This is seperate from the google chrome
#but the google does make it available.
class WebpageTests(unittest.TestCase):
    def test_title(self):#here we are making sure that the title of the page
# is Counter that we assigned before.
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title,"Counter")
    def test_increse(self):
        driver.get(file_uri("counter.html"))
        increase=driver.find_element_by_id("increase")
        increase.click()#here I am simulating the user pressing the button
        self.assertEqual(driver.find_element_by_tag_name("h1").text,"1")#
 #get me what is inside h1 tag and compare.
    def test_decrese(self):
        driver.get(file_uri("counter.html"))
        decrease=driver.find_element_by_id("decrease")
        decrease.click()#this simualate the user pressing decrement button
        self.assertEqual(driver.find_element_by_tag_name("h1").text,"-1")
    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        increase=driver.find_element_by_id("increase")
        for i in range(100):#simulate pressing button multiple times.
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text,"100")

if __name__=="__main__":
    unittest.main()