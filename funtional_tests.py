from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(
            # executable_path=r'D:\Peter\sourcecode\python\geckodriver.exe'
        )
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 一个很酷的在线代办应用
        # 应用首页
        self.browser.get('http://localhost:8000')

        # 网页的标题都有to do
        self.assertIn('To-Do', self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To Do',header_text)

        #app ask she to make a to do list
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')


        #she input Buy peacock feathers
        #and she love make fly
        inputbox.send_keys('Buy peacock feathers')

        #she enter 'Enter' key and the page refreash
        #the list show "1:Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)

        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text=='1:Buy peacock feathers' for row in rows)
        )

        


        self.fail('Finish the test!')


if __name__ == '__main__':
    # unittest.main(warnings='ignore')
    unittest.main()
