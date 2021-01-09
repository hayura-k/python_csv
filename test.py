import csv

lst = []
with open('data.csv', 'r') as csv_file:
  reader = csv.reader(csv_file)
  lst = [r for r in reader]

a = [5,999]

for row in lst:
  print(row)
  if row[0] == '2':
    row[0], row[1] = a[0], a[1]
