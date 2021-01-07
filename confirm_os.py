import csv
import os
print(os.path.exists('ranking.csv'))

with open('ranking.csv', 'r') as csv_file:
  reader = csv.DictReader(csv_file)
  for row in reader:
    new_count = int(row['COUNT']) + 1
    with open('ranking.csv', 'w') as csv_file:
      fieldnames = ['NAME', 'COUNT']
      writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerow({'NAME':row['NAME'], 'COUNT':new_count})
