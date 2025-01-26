from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def scrape_google_results(query):
    driver = webdriver.Chrome(executable_path="path/to/chromedriver")
    driver.maximize_window()

    try:
        driver.get("https://www.google.com")
        time.sleep(2)

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

        results = driver.find_elements(By.CSS_SELECTOR, ".tF2Cxc")

        scraped_data = []
        for result in results:
            title_element = result.find_element(By.TAG_NAME, "h3")
            link_element = result.find_element(By.CSS_SELECTOR, ".yuRUbf a")
            description_element = result.find_element(By.CSS_SELECTOR, ".VwiC3b")

            title = title_element.text
            link = link_element.get_attribute("href")
            description = description_element.text

            scraped_data.append({
                "title": title,
                "link": link,
                "description": description
            })

        
        for idx, data in enumerate(scraped_data, start=1):
            print(f"Result {idx}:")
            print(f"Title: {data['title']}")
            print(f"Link: {data['link']}")
            print(f"Description: {data['description']}\n")
        
        return scraped_data

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()


if __name__ == "__main__":
    query = "Python Selenium tutorial"
    scrape_google_results(query)
