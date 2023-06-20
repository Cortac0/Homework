import csv, json

def filter_dict(old:dict, filter_key: str, filter_value):
    new_dict = {}

    for k, v in old.items():
        if filter_key not in v.keys():
            print("Ati indicat o cheie inexistenta")
            return {}

        if type(v[filter_key]) == list and filter_value in v[filter_key]:
            new_dict[k] = v
        elif v[filter_key] == filter_value:
            new_dict[k] = v
    return new_dict
with open("data.tsv", mode="r", encoding='utf-8') as f:
    r = csv.reader(f, delimiter="\t", quotechar='"', quoting=csv.QUOTE_NONE)

# calculam timpul total al filmelor
    total = 0 
    filme = {}
    for i, item in enumerate(r):
        if i == 0:
            continue
        total += int(item[7]) if item[7] != "\\N" else 0

    print("Durata filmelor")
    print("Total minute: ", total )
    print("Total ore: ", total / 60 )
    print("Total zile: ", total / 60 / 24)
    print("Total luni: ", total / 60 / 24 / 30)
    print("Total ani: ", total / 60 / 24 / 365)

# extragem date din json
#     filme = {}
#     for i, item in enumerate(r):
#         if i == 0:
#             continue

#         filme[item[3]] = {
#             "type": item[1],
#             "year": int(item[5]),
#             "duration": int(item[7]) if item[7] != "\\N" else 0,
#             "genres": item[8].split(","),
#         }
#         if i == 10_000:
#             break

# with open("data.json", mode="w") as f:
#     f.write(json.dumps(filme))

# print(filter_dict(filme, "genres", "Comedy"))

