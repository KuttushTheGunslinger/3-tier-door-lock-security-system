from openpyxl import load_workbook

i = 0

wb2 = load_workbook('personal_data.xlsx')
ws2 = wb2.active

n = input('Enter your name: ')

for cell in ws2['A']:
    if cell.value is not None:
        if n in cell.value:
            r = cell.row

r1 = 'B' + str(r)

while i < 3:
    p = input('Enter your current password: ')
    if p == ws2[r1].value:
        p1 = input('Enter your new password: ')
        ws2[r1] = p1
        break

    else:
        print('Incorrect password')
        i += 1

wb2.save(filename='personal_data.xlsx')
wb2.close()
