 from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the webpage
url = 'https://www.walmart.com/search?q=airpods+pro+2nd+generation'  # Replace with the URL of the page you want to scrape
driver.get(url)

# Find elements containing product names and prices
product_elements = driver.find_elements(By.CSS_SELECTOR, 'CSS_SELECTOR_FOR_PRODUCT')  # Replace with the actual CSS selector
price_elements = driver.find_elements(By.CSS_SELECTOR, 'CSS_SELECTOR_FOR_PRICE')  # Replace with the actual CSS selector

# Extract and print the product names and prices
products = []
for product_element, price_element in zip(product_elements, price_elements):
    product_name = product_element.text
    product_price = price_element.text
    products.append({'name': product_name, 'price': product_price})

# Print the scraped products
for product in products:
    print(f"Product Name: {product['name']}, Product Price: {product['price']}")

# Close the WebDriver
driver.quit()
