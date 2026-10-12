doc_code=input()
category=doc_code[0:3]
year=doc_code[4:8]
number=doc_code[9:13]
reversed_number=number[::-1]
print(f"Категория: {category}")
print(F"Год: {year}")
print(f"Номер: {number}")
print(f"Обратный номер: {reversed_number}")

