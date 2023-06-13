from datetime import datetime
import os, requests, csv, time

URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
def get_data(timeout = 1):
    response = requests.get(URL).json()
        
    price = response['bpi']['USD']['rate_float']
    date = datetime.now()

    return ({
        'date': date,
        'price': price,
        'timeout': timeout,
    })

def exchange(target, amount):
    price = get_data()['price']

    if target == 'USD':
        print(amount / price, 'BTC') 
    elif target == 'BTC':
        print(amount * price, 'USD') 

def harvest(timeout: int):
    filename = str(datetime.now().date()) + '.csv'

    data = read_data(filename)
    try:
        while True:
            print('TIMEOUT', len(data))
            time.sleep(timeout)

            data.append(get_data(timeout))    
    except KeyboardInterrupt:
        write_data(filename, data)

def read_data(filename):
    data = []
    try:
        # 'data/2023-06-11'
        with open(f'data/{filename}', 'r') as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)
    except (FileNotFoundError, FileExistsError):
        pass
    else: 
        print('ELSE')
        temp = []
        for item in data:
            temp.append({
                'date': item[0],
                'price': item[1],
                'timeout': item[2],
            })
        data = temp
    finally:
        return data
    
def write_data(filename: str, data: list):
    os.chdir('In_Clasa/data') # schimbam directorul
    print(f'Scriem fisierul {filename}')

    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file) 

        for item in data:
            csv_writer.writerow(item.values())
    os.chdir('..')

