import re

import xlrd
from celery import shared_task
from django.db import IntegrityError

from core_part.booksParsing import ExcelParsingError
from core_part.models import Group, Student


@shared_task
def parse_excel_file(file):
    new_group = None
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
                        try:
                            new_group = Group.objects.create(number=currentGroupNumber)
                        except IntegrityError:
                            new_group = Group.objects.get(number=currentGroupNumber)
                        break
        else:
            if new_group is None:
                return ExcelParsingError
            else:
                new_student = Student.objects.create(lastName=row[1], firstName=row[2], middleName=row[3], ticketNumber=row[4], studentGroup=new_group)
    #write_dict_to_file(dict)
    return None