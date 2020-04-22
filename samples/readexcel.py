import os
import xlrd

current_path = os.path.dirname(__name__)
excel_path = os.path.join(current_path, '../element_info_datas/elements.xlsx')


workbook = xlrd.open_workbook(excel_path)

sheet = workbook.sheet_by_name('login_page')
value = sheet.cell_value(1, 0)
print(value)
row_count = sheet.nrows

element_infos = {}

for i in range(1, row_count):
    element_info = {'element_name': sheet.cell_value(i, 1), 'locator_type': sheet.cell_value(i, 2),
                    'locator_value': sheet.cell_value(i, 3), 'timeout': sheet.cell_value(i, 4)}
    element_infos[sheet.cell_value(i, 0)] = element_info

print(element_infos)
'''        self.username_input_box = {'element_name': '用户名输入框',
                                   'locator_type': 'XPATH',
                                   'locator_value': '//input[@name="account"]',
                                   'timeout': 3}'''