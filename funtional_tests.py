from selenium import webdriver

browser=webdriver.Firefox(executable_path=r'D:\Peter\sourcecode\python\geckodriver.exe')
browser.get('http://localhost:8000')

assert 'Django' in browser.title