# Перевірка року на високосність
print("Високосний" if (lambda y: str(y / 4)[len(str(y / 4))-2:] == '.0' and (str(y / 100)[len(str(y/ 100))-2:] != '.0' or str(y / 400)[len(str(y/ 400))-2:] == '.0'))(int(input("Введіть рік: "))) else "Не високосний")


