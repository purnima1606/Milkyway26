

class facebook_login():
	clk_email = ("id", email)
	clk_password=("id", "Password")
	clk_login = ("id", "")
	
	def enter_text(self,username ):
		self.driver.find_element(*self.clk_email).send_keys(username)
	def click_login(self, ):
		self.driver.find_element(*clk_login).click()