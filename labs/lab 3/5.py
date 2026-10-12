identifier=input()
print("Длина:", len(identifier))
if identifier=="":
    only_letters=False
    only_digits=False
    alphanumeric=False
else:
    only_letters=identifier.isalpha()
    only_digits=identifier.isdigit()
    alphanumeric=identifier.isalnum()
contains_huphen="-" in identifier
print("Только буквы:", only_letters)
print("Только цифры:", only_digits)
print("Буквенно-цифровая:", alphanumeric)
print("Содержит дефис:", contains_huphen)