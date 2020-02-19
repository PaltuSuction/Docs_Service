import json
import re

import xlrd
from django.shortcuts import render

class ExcelParsingError(Exception):
    def __init__(self, text):
        self.txt = 'Ошибка парсинга данных: не удалось считать номер группы.'

def parse_excel_file(file):
    dict = {}
    currentGroupNumber = ''
    book = xlrd.open_workbook(file_contents=file.read())
    #TODO: Выбирается только конкретный лист конкретного файла, исправить.
    sheet = book.sheet_by_name('GR63 ПОСЛЕДНИЕ') #Выбор листа по индексу
    for rownumber in range(1, sheet.nrows, 1):
        row = sheet.row_values(rownumber)
        if row[0] == '':
            for cell in row:
                if cell != '':
                    if re.fullmatch(r'\d{4}',str(int(cell))):
                        currentGroupNumber = str(int(cell))
                        #dict['groupNumber'] = currentGroupNumber
                        dict[currentGroupNumber] = {}
                        break
        else:
            if currentGroupNumber == '':
                return ExcelParsingError
            else:
                #Номер студенческого билета - ключ к остальным данным.
                dict[currentGroupNumber][row[4]] = {
                    'lastName': row[1],
                    'firstName': row[2],
                    'middleName': row[3],

                }
                '''dict[currentGroupNumber]['lastName'] = row[1]
                dict[currentGroupNumber]['firstName'] = row[2]
                dict[currentGroupNumber]['middleName'] = row[3]
                dict[currentGroupNumber]['ticketNumber'] = row[4]'''
    write_dict_to_file(dict)
    return None

def write_dict_to_file(dict):
    with open('Testing_files/file_to_write/test_writing_file.json', 'a') as file:
       """ file.write('Группа {}: {} {} {} ; Номер студенческого: {}\n'.format(dict['groupNumber'], dict['lastName'],
                                                                          dict['firstName'], dict['middleName'],
                                                                          dict['ticketNumber']))"""
       json.dump(dict, file, ensure_ascii=False, indent=2)