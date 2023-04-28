import yaml
import requests

path  = "./"
config_file = path + 'config.yml'
with open(config_file, 'rb') as f:
    config = yaml.safe_load(f)
f.close()

def get_oxr_rates():
    # base currency is USD
    app_id = config['oxr_id']
    symbols = 'HKD,SGD,RMB,AUD,TWD,KRW,JPY,EUR,GBP,THB'

    oxr_url = f'https://openexchangerates.org/api/latest.json?app_id={app_id}&symbols={symbols}'

    response = requests.get(oxr_url)
    xe = response.json()
    rates = xe['rates']
    return rates

if __name__ == '__main__':
    rates = get_oxr_rates()
    print(rates)

    HKD = rates['HKD']
    print(HKD)
