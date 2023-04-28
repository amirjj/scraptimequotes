import pathlib


URL = 'https://www.time.ir/'

QUOTE_XPATH = '//*[@id="ctl00_cphTop_Sampa_Web_View_BrainyQuoteUI_RandomQuoteControl20cphTop_3735_lblQuoteText"]'
QUOTE_XPATH = '//*[@id="ctl00_cphTop_Sampa_Web_View_BrainyQuoteUI_RandomQuoteControl20cphTop_3735_lblQuoteText"]'

QUOTE_OWNER_XPATH = '//*[@id="ctl00_cphTop_Sampa_Web_View_BrainyQuoteUI_RandomQuoteControl20cphTop_3735_hplAuthor"]'
SLEEP_TIME = 6
OUTPUT_PATH = pathlib.Path.cwd().joinpath('output')
