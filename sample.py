import json

ea_f = open('control_pref.json', "r")
js = json.load(ea_f)

chs = []
for el in js:
    ex = js[el]["Example-based"]
    rs = js[el]["Recipe-based"]
    no = js[el]["No preference"]

    ch = {"category": el, "group": "Example-based", "value": ex }
    chs.append(ch)
    ch = {"category": el, "group": "Recipe-based", "value": rs }
    chs.append(ch)
    ch = {"category": el, "group": "No Preference", "value": no }
    chs.append(ch)


au = { "values": chs}

jso_f = open("control-pref-2.json", "w")
json.dump(au, jso_f)
print(chs)
