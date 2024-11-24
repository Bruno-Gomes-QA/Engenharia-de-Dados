import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.APPSHEET_API_KEY = os.getenv('APPSHEET_API_KEY')
        self.API_URL = os.getenv('APPSHEET_API_URL')
        self.APP_ID = os.getenv('APPSHEET_APP_ID')
        self.TABLE_NAMES = os.getenv('TABLE_NAMES', 'Produtos').split(',')

    def validate(self):
        if not all([self.APPSHEET_API_KEY, self.API_URL, self.APP_ID, self.TABLE_NAMES]):
            raise ValueError('Missing environment variables')

config = Config()
config.validate()