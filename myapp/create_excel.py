import pandas as pd
import itertools
from myapp.models import Region  # Replace 'myapp' with the name of your Django app

def create_excel(data):
    keys = list(data.keys())
    first_key = keys[0]
    second_key = keys[1]

    table_width = 5

    df1 = pd.DataFrame(data[first_key])
    df2 = pd.DataFrame(data[second_key])

    columns_to_sum = ['comunidad', 'primer nivel', 'segundo nivel', 'centros']

    df1['Total'] = df1[columns_to_sum].sum(axis=1)
    df2['Total'] = df2[columns_to_sum].sum(axis=1)

    excel_file = 'myapp/output.xlsx'

    initial_cords = [1, 1]
    gap = 1

    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        df1.to_excel(writer, sheet_name='Septiembre', index=False, startrow=initial_cords[0], startcol=initial_cords[1])
        df2.to_excel(writer, sheet_name='Septiembre', index=False, startrow=initial_cords[0], startcol=initial_cords[1] + table_width + gap)

        workbook = writer.book
        worksheet = writer.sheets['Septiembre']
        worksheet.write_string(initial_cords[0] - 1, 0 + initial_cords[1] + int(table_width / 2), first_key)
        worksheet.write_string(initial_cords[0] - 1, 0 + initial_cords[1] + int(table_width / 2) + table_width + gap, second_key)

    writer._save()

def fetch_data_from_database():
    regions = Region.objects.all()
    data = {region.name: {
        'comunidad': region.comunidad,
        'primer nivel': region.primer_nivel,
        'segundo nivel': region.segundo_nivel,
        'centros': region.centros,
    } for region in regions}
    return data

if __name__ == "__main__":
    data = fetch_data_from_database()
    create_excel(data)
