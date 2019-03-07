import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 声明浏览器对象
# option = webdriver.ChromeOptions()
# option.binary_location=r'C:\Users\73573\AppData\Local\Google\Chrome\Application\chrome.exe'
browser = webdriver.Chrome()
try:
    browser.get('http://www.baidu.com')
    input=browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser,10)
    wait.until(expected_conditions.presence_of_all_elements_located((By.ID,'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()



# 单个元素
browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first,input_second,input_third)
browser.close()
'''或者'''
input_first = browser.find_element(By.ID,'q')
print(input_first)

# 多个元素
'''
find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
'''

# 元素交互操作
browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
input_first = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_elements_by_class_name('btn-search')
button.click()

# 交互动作
browser = webdriver.Chrome()
url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('frameResult')
source=browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()

# 执行JavaScript
browser = webdriver.Chrome()
browser.get('http://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')

# 获取元素信息
# 获取属性
browser = webdriver.Chrome()
browser.get('http://www.zhihu.com/explore')
browser.get(url)
logo=browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))
# 获取文本值
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)
# 获取ID、位置、标签名、大小
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)

# Frame
browser = webdriver.Chrome()
url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('frameResult')
source=browser.find_element_by_css_selector('#draggable')
print(source)
try:
    logo=browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO LOGO')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)

# 等待
# 隐式等待
browser = webdriver.Chrome()
browser.implicitly_wait(10)     # 隐式等待
browser.get('http://www.zhihu.com/explore')
input=browser.find_element_by_id('zh-top-link-logo')
print(input)

# 显示等待
browser = webdriver.Chrome()
browser.get('http://www.taobao.com/')
wait=WebDriverWait(browser,10)
input = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
print(input,button)
'''
常用显示等待条件
title_is    标题是某内容
title_contains  标题包含某内容
presence_of_element_located     元素加载出，传入定位元素，如（By.ID,'p'）
visibility_of_element_located   元素课件，传入定位元组
visibility_of   可见，传入元素对象
presence_of_all_elements_located    所有元素加载出
text_to_be_present_in_element   某个元素文本包含某文字
text_to_be_present_in_element_value     某个元素值包含某文字
frame_to_be_availiable_and_switch_to_it     frame加载并切换
invisibility_of_element_located     元素不可见
element_to_be_clickable     元素克点击
staleness_of    判断一个元素是否仍在DOM，可判断页面是否已经刷新
element_to_be_selected  元素可选择，传元素对象
element_located_to_be_selected  元素可选择，传入定位元组
element_selection_state_to_be   传入元素对象以及状态，相等返回True，否则返回False
element_located_selection_state_to_be   传入定位元组以及状态，相等返回True，否则返回False
alert_is_present    是否出现Alert
'''

# 前进和倒退
browser = webdriver.Chrome()
browser.get('http://www.taobao.com/')
browser.get('http://www.baidu.com/')
browser.get('http://www.sina.com/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()

# Cookies
browser = webdriver.Chrome()
browser.get('http://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())

# 选项卡管理
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('http://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('http://www.sina.com')

# 异常处理
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
browser.find_element_by_id('hello')

# 捕获异常
browser = webdriver.Chrome()
try:
    browser.get('http://www.baidu.com/')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()