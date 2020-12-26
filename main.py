from selenium import webdriver
import time
import pandas as pd

# driver
chromedriver_path = 'C:\Program Files (x86)/chromedriver.exe'
webdriver = webdriver.Chrome(chromedriver_path)
#webdriver.get("https://www.frewsburgcsd.org/site/Default.aspx?PageID=328") # Frewsburg
#webdriver.get("https://www.swcsk12.org/Page/1469") # Southwestern
#webdriver.get("https://www.randolphcsd.org/site/Default.aspx?PageID=31") # Randolph
webdriver.get("https://www.jpsny.org/Page/4475") # Jamestown High School
# lists
teacher_names = []
teacher_emails = []

#alert_button = webdriver.find_element_by_css_selector("#onscreenalert-ctrl-gotit")
#alert_button.click()
#time.sleep(1)

# search
search = webdriver.find_element_by_css_selector("#txtJobTitle")
search.send_keys("teacher")
# Frewsburg
#search_button = webdriver.find_element_by_css_selector("#module-content-3296 > div > div.ui-widget-detail.searchdiv.directory-filter > div.floatright.marginleft.miniright > a")
# Southwestern
#search_button = webdriver.find_element_by_css_selector("#module-content-1732 > div > div.ui-widget-detail.searchdiv.directory-filter > div.floatright.marginleft.miniright > a")
# Randolph
#search_button = webdriver.find_element_by_css_selector("#module-content-3201 > div > div.ui-widget-detail.searchdiv.directory-filter > div.floatright.marginleft.miniright > a")
# Jamestown High School
search_button = webdriver.find_element_by_css_selector("#module-content-4871 > div > div.ui-widget-detail.searchdiv.directory-filter > div.floatright.marginleft.miniright > a")
search_button.click()

# Get number of pages

pages = webdriver.find_elements_by_css_selector("#ui-paging-container")

page_number = 2
for i in pages:
    page_number += 1

print(page_number)
# loop over the list and append items to list
for i in range(2, 6):
    print(i)
    time.sleep(1)
    teachers = webdriver.find_elements_by_class_name("staff")
    print(teachers)
    for teacher in teachers:
        teacher_name = teacher.find_element_by_class_name("staffname")
        teacher_email = teacher.find_element_by_class_name("staffemail")

        teacher_names.append(teacher_name.text)
        teacher_emails.append(teacher_email.text)

    # Lincoln
    #page_button = webdriver.find_element_by_xpath(f"//*[@id='ui-paging-container']/ul/li[{i}]/a")
    # Frewsburg
    #page_button = webdriver.find_element_by_css_selector(f"#ui-paging-container > ul > li:nth-child({i}) > a")
    # Southwestern
    page_button = webdriver.find_element_by_css_selector(f"#ui-paging-container > ul > li:nth-child({i}) > a")
    page_button.click()
    time.sleep(2)

teachers = webdriver.find_elements_by_class_name("staff")
for teacher in teachers:
    teacher_name = teacher.find_element_by_class_name("staffname")
    teacher_email = teacher.find_element_by_class_name("staffemail")

    teacher_names.append(teacher_name.text)
    teacher_emails.append(teacher_email.text)

n = 0
for i in teacher_names:
    n += 1


# Save data to excel sheet
df = pd.DataFrame({'Name': teacher_names, 'Email': teacher_emails})

writer = pd.ExcelWriter('Jamestown.xlsx')

df.to_excel(writer, sheet_name="Jamestown High School", index=False)

writer.save()

print(f"\nThere are {n} teachers")









