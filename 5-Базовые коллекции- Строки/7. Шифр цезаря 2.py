def cezar_pass(text, move):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    str_pass = [
        alphabet[(alphabet.index(i)+move)%33] if i in alphabet
        else i
        for i in text]
    str_pass = "".join(str_pass)
    return str_pass

text = 'это питон'.lower()
K = 3

pass_text = cezar_pass(text, K)
print(pass_text)