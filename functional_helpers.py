def user_login(driver, email, password):
    driver.find_element_by_xpath("//span[contains(text(),'Zaloguj się')]").click()
    driver.find_element_by_xpath("//div[@class='col-md-6']//input[@name='email']").send_keys(email)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//button[@id='submit-login']").click()
