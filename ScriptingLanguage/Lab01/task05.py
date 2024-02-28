import datetime
inputDate = input("Podaj date: ").split("-")
date = datetime.date(int(inputDate[0]), int(inputDate[1]), int(inputDate[2]))

actualDate = datetime.date.today()
days = actualDate - date
print(days)

# 2 sposob
# print(datetime.date.today() - datetime.date.fromisoformat(input()))