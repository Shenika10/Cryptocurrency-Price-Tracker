from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://coinmarketcap.com")
time.sleep(5)
rows = driver.find_elements(By.TAG_NAME, "tr")

file = open("crypto_prices.csv", "w", newline="")
writer = csv.writer(file)

writer.writerow(["Coin Name", "Symbol", "Price", "Market Cap"])

print("Number of rows found:", len(rows))
print(rows[0])
print(type(rows[0]))
for row in rows[2:12]:
    bitcoin_data = row.text.split("\n")

    coin_name = bitcoin_data[1]
    symbol = bitcoin_data[2]
    price = bitcoin_data[4]
    market_cap = bitcoin_data[6]

    writer.writerow([coin_name, symbol, price, market_cap])

    print("\n==============================")
    print("Coin Name  :", coin_name)
    print("Symbol     :", symbol)
    print("Price      :", price)
    print("Market Cap :", market_cap)
file.close()

input("Press Enter to close the browser...")
driver.quit()