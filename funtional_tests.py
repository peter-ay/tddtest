from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(
            executable_path=r'D:\Peter\sourcecode\python\geckodriver.exe')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 一个很酷的在线代办应用
        # 应用首页
        self.browser.get('http://localhost:8000')

        # 网页的标题
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    # unittest.main(warnings='ignore')
    unittest.main()
