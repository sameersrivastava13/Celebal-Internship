from selenium import webdriver
import bs4


options = webdriver.ChromeOptions()
driver = webdriver.Chrome("./chromedriver")


def get_corona_detail():
    url = "https://www.mohfw.gov.in/"

    li = ("blue", "green", "red", "orange")
    l2 = ("Active Cases", "Cured / Discharged", "Deaths", "Migrated")
    all_details = ""
    for i in range(4):
        driver.get(url)
        for job in driver.find_elements_by_class_name("site-stats-count"):
            bs = bs4.BeautifulSoup(job.get_attribute("innerHTML"), "html.parser")
            info = bs.find_all("li", class_="bg-" + str(li[i]))
            for j in info:
                data = j.find("strong").get_text()
                all_details += l2[i] + " : " + data + "\n"
    print(all_details)


get_corona_detail()
