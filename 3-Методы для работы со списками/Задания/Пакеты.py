paks_q = 3
bad_packs = 0
decode_paks = []
one_pack = []

for i_pack in range(paks_q):
    print('Пакет номер:', i_pack+1)
    for i_bit in range(4):
        print(i_bit+1, 'бит:', end=' ')
        one_bit = int(input())
        one_pack.append(one_bit)
    if one_pack.count(-1) <= 1:
        decode_paks.extend(one_pack)
    else:
        bad_packs += 1
        print('Много ошибок в пакете!')
    one_pack.clear()

print("Получено сообщение:", decode_paks)
print("Количество ошибок в сообщении:", decode_paks.count(-1))
print("Количество потеряных пакетов:", bad_packs)