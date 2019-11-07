import csv
from django.shortcuts import render
from table.models import Field, FilePath


FilePath.set_path('phones.csv')
CSV_FILENAME = FilePath.get_path()
COLUMNS = [
    {'name': 'id', 'width': 1},
    {'name': 'name', 'width': 3},
    {'name': 'price', 'width': 2},
    {'name': 'release_date', 'width': 2},
    {'name': 'lte_exists', 'width': 1},
]


def table_view(request):
    template = 'table.html'
    with open(CSV_FILENAME, 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        columns = []
        fields = Field.objects.order_by('serial_number')
        for f in fields:
            columns.append({'name': f.name, 'width': f.width})

        context = {
            'columns': columns,
            'table': table,
            'csv_file': CSV_FILENAME
        }
        result = render(request, template, context)
    return result
