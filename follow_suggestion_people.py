def follow_suggested_people(driver,time,random):
    try:
        driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div').click()
    except:
        pass
    time.sleep(4)

    follows =  driver.find_elements_by_class_name('sqdOP.L3NKy.y3zKF')

    for follow in follows:
        follow.click()
        time.sleep(random.randint(5, 7) )