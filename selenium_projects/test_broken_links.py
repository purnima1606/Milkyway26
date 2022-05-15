from selenium.webdriver import Chrome
from requests import request

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/links.html")
links = driver.find_elements_by_xpath("//a")
urls = [ ]
broken_links = [ ]
def test_broken():
    for link in links:
        urls.append((link.text, link.get_attribute("href")))

    for url in urls:
        response = request("GET", url[1])
        if response.status_code != 200:
            broken_links.append(url)

    with open('broken_links.txt', 'w') as f:
        for item in broken_links:
            f.write(":".join(item))
            f.write("\n")


# collecting ... collected 1 item
#
# test_broken_links.py::test_broken PASSED                                 [100%]
#
# ============================= 1 passed in 26.99s ==============================
# Process finished with exit code 0
