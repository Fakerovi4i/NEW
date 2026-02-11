file_name = "text.docx"

if file_name.startswith(('@', '№', '$', '%', '^', '&', '*', '()')):
    print("Неверный префикс!")
if not file_name.endswith((".txt", ".docx")):
    print("Неверный окончание")
elif (not file_name.startswith(('@', '№', '$', '%', '^', '&', '*', '()'))
        and
        file_name.endswith((".txt", ".docx"))):
    print("все норм!")