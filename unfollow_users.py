def unfollow_users(driver,time,random):
    driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a").click()
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()

    # this section will scrolls the pop-up windows
    fBody = driver.find_element_by_xpath("//div[@class='isgrP']")
    scroll = 0
    while scroll < 2:  # scroll 5 times
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        time.sleep(random.randint(7, 10))
        scroll += 1

    fList = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
    # section end here.

    # this section will unfollow the user
    buttons = driver.find_elements_by_class_name("sqdOP")
    buttons = buttons[1:len(buttons)]

    for button in buttons:
        driver.execute_script("arguments[0].click();", button)
        time.sleep(random.randint(3, 6))
        driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]").click()
        time.sleep(random.randint(8, 10))