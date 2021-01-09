import csv
import os

with open('ranking.csv', 'r') as csv_file:
  reader = csv.DictReader(csv_file)
  print(reader)
  rows = []
  for row in reader:
    rows.append(row)
    print(row)

  print(rows)

  with open('ranking.csv', 'w') as csv_file:
    print('helo')
    fieldnames = ['NAME', 'COUNT']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
      print(row)
      new_count = int(row['COUNT']) + 1
      writer.writerow({'NAME':row['NAME'], 'COUNT':new_count})
