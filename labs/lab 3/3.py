phone=input()
cleaned_phone=(
    phone.replace("+","")
    .replace(" ","")
    .replace("(","")
    .replace(")","")
    .replace("-","")
)
print(cleaned_phone)