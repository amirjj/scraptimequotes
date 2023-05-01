import json

import xlsxwriter


def json_to_csv(source_path):
    """
    read all json files and write all contents in a csv file
    """
    q_dict = dict()
    key = 0
    for file in source_path.glob("*.json"):
        with open(file, "r", encoding='utf-8') as fp:
            data = json.load(fp)
            q_dict[key] = {
                'q': data['q'],
                'owner': data['owner']
            }
            key += 1

    workbook = xlsxwriter.Workbook('output.xlsx')
    worksheet = workbook.add_worksheet()
    for key in q_dict:

        worksheet.write(key, 0, q_dict[key]['q'])
        worksheet.write(key, 1, q_dict[key]['owner'])

    workbook.close()


def merge_all_files(source_path):
    for file in source_path.glob("*.json"):
        with open(file, "r") as fp:
            data = fp.readlines()
            print(data)
