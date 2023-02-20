import json

with open('sample_data.json', 'r') as file:
    data = json.load(file)
    print("""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
    first = data["imdata"]
    for item in first:
        name = item["l1PhysIf"]
        att = name["attributes"]
        dn = att["dn"]
        speed = att["speed"]
        mtu = att["mtu"]
        res = ""
        if len(dn) == 42:
            res += dn + "                              " + speed + "   " + mtu
        else:
            res += dn + "                               " + speed + "   " + mtu
       
        print(res)