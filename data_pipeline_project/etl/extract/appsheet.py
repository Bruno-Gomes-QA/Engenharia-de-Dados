import requests


class AppSheetExtractor:
    def __init__(self, api_url, api_key, app_id, logger):
        self.api_url = api_url
        self.api_key = api_key
        self.app_id = app_id
        self.logger = logger

    def extract(self, table_name):
        endpoint = f'{self.api_url}/{self.app_id}/tables/{table_name}/Action'

        headers = {
            'Content-Type': 'application/json',
            'ApplicationAccessKey': self.api_key,
        }

        payload = {
            'Action': 'Find',
            'Properties': {'Locale': 'pt-BR', 'Timezone': 'America/Sao_Paulo'},
            'Rows': [],
        }
        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            self.logger.info(
                f'Data extracted successfully from {table_name}'
            )
            return data
        except Exception as err:
            self.logger.error(
                f'Failed to extract data from {table_name}: {err}'
            )
            raise ValueError(err)
