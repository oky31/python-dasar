# mengulangi list
kata = ['kucing','jendela','meja']
# for item in kata:
#     print(item, len(item))

for item in kata[:]:
    if len(item) > 6:
        kata.insert(0,item)

print(kata);

