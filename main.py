import self as self
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


desired_caps = dict(
    platformName='Android',
    platformVersion='7.0',
    automationName='uiautomator2',
    deviceName = '6AGDU18112000071',
    #deviceName='6AGDU18112000071',
    app='/home/enock/Downloads/app-debug-1.apk',
    #appActivityWait = 'WelcomeActivity',
    #appActivity = 'MainActivity',
    autoGrantPermissions = True
)

options = ['radioButton','radioButton1','radioButton2']
self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

for i in options:
    self.driver.implicitly_wait(720)
    if i=='radioButton1' or i=='radioButton2':
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Open").click()
        self.driver.find_element(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()
    self.driver.find_element(MobileBy.ID,i).click()
    self.driver.find_element(MobileBy.ID,"switch1").click()
    self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Open").click()
    self.driver.find_element(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]").click()
    self.driver.find_element(MobileBy.ID,"startButton").click()
    self.driver.implicitly_wait(30)
    self.driver.find_element(MobileBy.ID,"http_test").click()
    #self.driver.find_element(MobileBy.ID,"sites").click()
    for x in range(2,16):
        try:
            self.driver.find_element(MobileBy.ID,"sites").click()
            self.driver.implicitly_wait(360)
            self.driver.find_element(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[{}]".format(x)).click()
            self.driver.implicitly_wait(10)
        except:
            continue
    self.driver.find_element(MobileBy.ID,"video_test").click()
    self.driver.find_element(MobileBy.ID,"buttonStart").click()
    self.driver.implicitly_wait(30)

self.driver.quit()
