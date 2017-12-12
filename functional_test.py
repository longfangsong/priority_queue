import unittest
from selenium.webdriver import Chrome
from time import sleep
# now I use chrome so this can be also a demo
# if want it be a test only, consider using Phantom.js etc.

class TestDefault(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.browser = Chrome()
        self.now_task = 0


    def add_task(self,task_name):
        # 用户点击了左下角的图标
        self.browser.find_element_by_id('functions-button').click()
        sleep(1)
        # 他点击了新建按钮
        self.browser.find_element_by_id('new-item-button').click()
        sleep(1)
        # 有个对话框出现了，用户输入了这个任务的名字
        self.browser.find_elements_by_class_name('modal')[self.now_task].find_element_by_tag_name('input').send_keys(task_name)
        sleep(1)
        # 用户点击了确定
        self.browser.find_elements_by_class_name('modal')[self.now_task].find_elements_by_tag_name('button')[1].click()
        sleep(1)

    def test_default(self):
        # 用户打开了浏览器/App
        self.browser.get('http://localhost:8080/#/')
        sleep(1)
        # 用户发现屏幕上有App的名称
        self.assertIn('优先队列', self.browser.find_element_by_id('title').text)
        # 用户发现屏幕上有“现在要做的事”，现在还不需要做什么事
        self.assertIn('还没有要做的事……', self.browser.find_element_by_id('now-should-do').text)
        # 用户发现屏幕底部可以用来切换页面
        self.assertIn('目前任务', self.browser.find_elements_by_class_name('q-tab')[0].text)
        self.assertIn('任务列表', self.browser.find_elements_by_class_name('q-tab')[1].text)

        # 用户切换到了任务列表
        self.browser.find_elements_by_class_name('q-tab')[1].click()
        sleep(1)
        # 用户发现任务列表空空如也
        self.assertFalse(self.browser.find_elements_by_class_name('task'))

        # 用户决定添加一项任务
        self.add_task('Task 1')
        # 任务出现在了任务列表中
        self.assertIn('Task 1', self.browser.find_element_by_class_name('tasks').text)
        # 用户又添加了几项任务
        self.add_task('Task 2')
        self.assertIn('Task 2', self.browser.find_element_by_class_name('tasks').text)
        self.add_task('Task 3')
        self.assertIn('Task 3', self.browser.find_element_by_class_name('tasks').text)
        self.add_task('Task 4')
        self.assertIn('Task 3', self.browser.find_element_by_class_name('tasks').text)

        # 用户回到了目前任务的页面
        self.browser.find_elements_by_class_name('q-tab')[0].click()
        sleep(1)
        # 页面上现在有要做的事了
        self.assertIn('Task 1', self.browser.find_element_by_id('now-should-do').text)

        # 用户想要重新排列代办事项，他先进入了列表页
        self.browser.find_elements_by_class_name('q-tab')[1].click()
        sleep(1)
        # 用户点击了左下角的图标
        self.browser.find_element_by_id('functions-button').click()
        sleep(1)
        # 他点击了编辑按钮
        self.browser.find_element_by_id('edit-order-button').click()
        sleep(1)
        # 他将Task2拖拽到了第一个，Task4拖拽到了第二个
        # 此处需要手动干预测试……
        # Action Chains don't currently work on Mac.（F**k）
        sleep(30)
        # 他回到了目前任务的页面
        self.browser.find_elements_by_class_name('q-tab')[0].click()
        sleep(1)
        # 页面上要做的事更新了
        self.assertIn('Task 2', self.browser.find_element_by_id('now-should-do').text)

        # 用户已经完成Task 2了
        self.browser.find_element_by_id('task-finish').click()
        sleep(1)
        # 现在目前要做的是Task 4
        self.assertIn('Task 4', self.browser.find_element_by_id('now-should-do').text)

        # 用户想要删除所有排列代办事项，他先进入了列表页
        self.browser.find_elements_by_class_name('q-tab')[1].click()
        sleep(1)
        # 用户点击了左下角的图标
        self.browser.find_element_by_id('functions-button').click()
        sleep(1)
        # 他点击了删除按钮
        self.browser.find_element_by_id('delete-button').click()
        sleep(1)
        # 他点击了每个项目的删除按钮（应该有三个项目）
        self.browser.find_element_by_class_name('delete-item').click()
        sleep(1)
        self.browser.find_element_by_class_name('delete-item').click()
        sleep(1)
        self.browser.find_element_by_class_name('delete-item').click()
        sleep(1)
        # 用户发现任务列表又空空如也了
        self.assertFalse(self.browser.find_elements_by_class_name('task'))

if __name__ == '__main__':
    unittest.main()
