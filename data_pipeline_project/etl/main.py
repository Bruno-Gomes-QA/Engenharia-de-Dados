import os
from dotenv import load_dotenv
from extract.appsheet import AppSheetExtractor

load_dotenv('.env.appsheet')

API_URL = os.getenv('APPSHEET_API_URL')
print(API_URL)
APPSHEET_API_KEY = os.getenv('APPSHEET_API_KEY')
APP_ID = os.getenv('APPSHEET_APP_ID')
TABLE_NAME = 'Produtos'

appsheet_extractor = AppSheetExtractor(API_URL, APPSHEET_API_KEY, APP_ID)
appsheet_extractor.extract(TABLE_NAME)