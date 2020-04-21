from configparser import ConfigParser
import openpyxl

def getConfig():
    cfg = ConfigParser()
    cfg.read('config.ini', encoding='utf-8')

    username = cfg['DEFAULT']['username']
    password = cfg['DEFAULT']['password']
    rules_file = cfg['DEFAULT']['rules_file']
    return username, password, rules_file

def getRules(rules_file):
    workbook=openpyxl.load_workbook(rules_file) 
    ws=workbook.active
    rules=list()
    row_index = 2
    while(ws.cell(row = row_index, column = 1).value is not None):
        rule = dict()
        for i in range(1, 17):
            rule[ws.cell(row = 1, column = i).value] = ws.cell(row = row_index, column = i).value
        rules.append(rule)
        row_index += 1
    return rules


def main():
    wo_username, wo_password, rules_file = getConfig()
    print(wo_username)
    print(wo_password)
    rules = getRules(rules_file)
    print('done!')

    


if __name__ == '__main__':
    main()