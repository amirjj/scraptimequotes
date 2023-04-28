import datetime
import time
import json
from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from util import merge_all_files


def fetch_q():
    driver = webdriver.Chrome()
    driver.get(URL)
    time.sleep(SLEEP_TIME)
    q = driver.find_element(By.XPATH, QUOTE_XPATH).text
    q_owner = driver.find_element(By.XPATH, QUOTE_OWNER_XPATH).text
    driver.close()

    q_dict = dict()
    q_dict['q'] = q
    q_dict['owner'] = q_owner

    return q_dict


def save_as_json(q_dict):
    # print(q_dict)
    ts = datetime.datetime.now()
    filename = ts.strftime("%Y%m%d%H%M%S") + ".json"
    filepath = OUTPUT_PATH.joinpath(filename)
    with open(filepath, 'a+', encoding='utf-8') as fp:
        json.dump(q_dict, fp)


def run():
    while True:
        q_dict = fetch_q()
        save_as_json(q_dict)


def test_json_print():
    with open(OUTPUT_PATH.joinpath('20230428140951.json'), encoding='utf-8') as fp:
        data = json.load(fp)
        print(data['q'])
        print(data['owner'])
        print("_______________________")


if __name__ == '__main__':
    run()
    # test_json_print()
    # merge_all_files(OUTPUT_PATH)
