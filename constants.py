from pymongo import MongoClient

block_explorer= 'https://blocks.bitcoin.org.hk/tx/'
satwatch= ""
dca = ""

currencylist = {'hkd':'$','cny': '￥','usd':'$','eur':'€'}
core_currency = "HKD"


mongo_url = 'mongodb://localhost:27017'
client = MongoClient('localhost', port=27017)
# Create a new database
db = client["bahkbot"] 

# db = client.bahkbot
dbname = 'bahkbot'

# Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017")  # Replace with your MongoDB connection string



