from json import load

from core import auto_sell
from utils import logger

if __name__ == '__main__':
    with open('settings.json', 'r', encoding='utf-8-sig') as file:
        settings_json: dict = load(file)

    API_KEY: str = settings_json['api_key']
    API_SECRET: str = settings_json['api_secret']
    API_PASS_PHRASE: str = settings_json['api_pass_phrase']
    START_SALE_TIME: int = int(str(settings_json['start_sale_time'])[:10])
    THREADS: int = int(settings_json['threads'])
    REQUESTS_COUNT: int = int(settings_json['requests_count'])
    ENDPOINT_URL: str = settings_json['endpoint_url']
    PROXY_STR: str | None = settings_json['proxy']

    if not PROXY_STR:
        PROXY_STR: None = None

    token_from: str = input('Enter Token From Name: ').lower()
    token_to: str = input('Enter Token To Name: ').lower()
    print('')

    auto_sell(api_key=API_KEY,
              api_secret=API_SECRET,
              api_pass_phrase=API_PASS_PHRASE,
              token_from=token_from,
              token_to=token_to,
              start_sale_time=START_SALE_TIME,
              threads=THREADS,
              requests_count=REQUESTS_COUNT,
              endpoint_url=ENDPOINT_URL,
              proxy_str=PROXY_STR)

    logger.success(f'The Work Was Successfully Completed')
    input('\nPress Enter To Exit..')
