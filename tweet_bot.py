from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class tweet_bot:


	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot = webdriver.Chrome("E:/chromedriver")    # make sure to download chromedriver


	def log_in(self):
  
  
		bot = self.bot
		bot.get('https://twitter.com/login')              # get the twitter login page
		time.sleep(3)                                     # give time to load the page elements
    
    # uncheck the remember me check box
    
		bot.find_element_by_class_name("remember").click() 
    # find the username textbox using thier tag name, class name,Xpath. here i used css_selector function
		username = bot.find_element_by_css_selector('input[placeholder="Phone, email or username"]')
	  # find the password textbox to enter the password 
    password = bot.find_element_by_css_selector('input.js-password-field')
		username.send_keys(self.username)
		password.send_keys(self.password)
		bot.find_element_by_tag_name('button').click()
		time.sleep(3)
    
    # alternate method to hit enter after entering password insted of clicking login button 
    ## bot.send_keys(Keys.RETURN)


	def like_tweet(self,hashtag):
  
  
		bot = self.bot
		bot.get("https://twitter.com/search?q='+hashtag+'&src=typd") 
   
   # scroll down the page for more tweets 
   
    for i in range(1,3):
					bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
					time.sleep(2)
          # since we want multiple tweet use -- find_elements_by_class_name function
					tweets= bot.find_elements_by_class_name("tweet")
					links = [elem.get_attribute('data-permalink-path') for elem in tweets]
          
          # the last element in links list is none so ignore it
          
					for link in links[0:-1]:                 
						bot.get('https://twitter.com'+link)
						time.sleep(2)
						try:
            # try to hit the like button
            
							bot.find_element_by_class_name("HeartAnimation").click()
							time.sleep(10)
						except Exception as ex:
							time.sleep(15)


enter= tweet_bot('mail_id', 'password')
enter.log_in()
enter.like_tweet('page_you_like')


