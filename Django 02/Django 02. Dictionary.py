# dct = {}
# dct = dict()
#
# print(type(dct))
tpl = (25, 89)
dct = {
    "key": "value",
    "Vagif": [25, 65],
    23.581001: 25,
    True: True,
    tpl: "sALAM",
}

# for key in dct.keys():
#     print(key, dct[key])
# print()
# for value in dct.values():
#     print(value)

for key, value in dct.items():
    print(key, value)

print(dct.items())