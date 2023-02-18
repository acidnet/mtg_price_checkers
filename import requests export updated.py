import requests
import json
import time
import pandas as pd
import datetime

def get_price_info():
    # List of cards to retrieve pricing information for
    card_list = ['Lightning Bolt', 'Tarmogoyf', 'Snapcaster Mage', 'Dockside Extortionist', 'Atraxa, Praetors Voice' ]
    
    # Create an empty DataFrame to store the data
    df = pd.DataFrame(columns=['Card Name', 'Price (USD)', 'Date & Time'])

    while True:
        for i, card_name in enumerate(card_list):
            # Send an HTTP GET request to the Scryfall API
            response = requests.get(f'https://api.scryfall.com/cards/named?exact={card_name}')

            # Parse the JSON response
            data = json.loads(response.text)

            # Extract the pricing information
            price = data['prices']['usd']
            date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(f'The price of {card_name} is ${price} as of {date_time}.')

            # Add the data to the DataFrame
            new_data = {'Card Name': [card_name], 'Price (USD)': [price], 'Date & Time': [date_time]}
            df = pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)
        
            # Add a 100 millisecond delay between each request
            time.sleep(0.1)
        
        # Save the DataFrame to an Excel file
        df.to_excel('card_prices.xlsx', index=False)

        # Add a 1 hour delay after each iteration of the loop
        time.sleep(60 * 60)

get_price_info()