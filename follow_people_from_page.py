def follow_people_from_page(driver,time,random):
    driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div/span[2]').click()

    searchbox = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    page_name = input("Enter the page name from where you want to follow people : \n")
    searchbox.send_keys(page_name)
    driver.find_element_by_class_name('Ap253').click()
    time.sleep(3)

    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()

    fBody = driver.find_element_by_xpath("//div[@class='isgrP']")
    scroll = 0
    while scroll < 5:  # scroll 5 times
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        time.sleep(random.randint(7, 10))
        scroll += 1

    fList = driver.find_elements_by_xpath("//div[@class='isgrP']//li")

    followers = driver.find_elements_by_class_name('sqdOP')
    print(len(followers))
    count = 0
    for follower in followers:
        if follower.text == 'Follow':
            follower.click()
            time.sleep(random.randint(7, 10))
        else:
            print("ignored")
            pass
        count = count + 1
        print(count)