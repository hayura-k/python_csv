import csv

print('=====================================')
print('こんにちは。あなたの名前はなんですか？')
print('=====================================\n')

name = input()

print('=====================================')
print('{}さん。どこのレストランが好きですか？'. format(name))
print('=====================================\n')

restaurant = input()

print('=====================================')
print('{}さん。ありがとうございました。'. format(name))
print('=====================================\n')

with open('ranking.csv', 'w') as csv_file:
  fieldnames = ['NAME', 'COUNT']
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({'NAME':restaurant, 'COUNT':1})

print('=====================================')
print('こんにちは。あなたの名前はなんですか？')
print('=====================================\n')

name = input()

while True:
  with open('ranking.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
      print('=====================================')
      print('私のお勧めのレストランは、{}です。'. format(row['NAME']))
      print('このレストランは好きですか？[y/n]')
      print('=====================================')


  choice = input()
  # if choice == 'y':
    #csvファイルに+1

  # if #全てのレストランにnoと答えた場合 :
  break

print('=====================================')
print('{}さん。どこのレストランが好きですか？'. format(name))
print('=====================================\n')

restaurant = input()

print('=====================================')
print('{}さん。ありがとうございました。'. format(name))
print('=====================================\n')
