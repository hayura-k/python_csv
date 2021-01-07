import csv
import os

print('=====================================')
print('こんにちは。あなたの名前はなんですか？')
print('=====================================\n')

name = input()

# csvがあるかの場合わけ
if os.path.exists('ranking.csv'):
  while True:
    with open('ranking.csv', 'r') as csv_file:
      reader = csv.DictReader(csv_file)
      for row in reader:
        print('=====================================')
        print('私のお勧めのレストランは、{}です。'. format(row['NAME']))
        print('このレストランは好きですか？[y/n]')
        print('=====================================')

        choice = input()
        if choice == ('y' or 'yes'):
          row['COUNT'] = int(row['COUNT']) +1
          # with open('ranking.csv', 'a') as csv_file:
          #   #csvファイルに+1
          #   writer = csv.DictWriter(csv_file)
          #   writer.writerow({'COUNT':new_count})
    break

      # if #全てのレストランにnoと答えた場合 :



# csv上のレストランを聞き終わった後
print('=====================================')
print('{}さん。どこのレストランが好きですか？'. format(name))
print('=====================================\n')

restaurant = input()

print('=====================================')
print('{}さん。ありがとうございました。'. format(name))
print('=====================================\n')


if os.path.exists('ranking.csv'):
  with open('ranking.csv', 'a') as csv_file:
    fieldnames = ['NAME', 'COUNT']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writerow({'NAME':restaurant,'COUNT':1})
else:
  with open('ranking.csv', 'w') as csv_file:
    fieldnames = ['NAME', 'COUNT']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'NAME':restaurant, 'COUNT':1})
