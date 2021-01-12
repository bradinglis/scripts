import json

uidsearch = "19c00c66-f53a-4abf-af21-65f284a6dbb8"
typ = "sDestIP"

with open('data.json', 'r') as myfile:
        jsondata = myfile.read()
        myfile.close

data = json.loads(jsondata)

i = 0
iplist = []

for keyval in data:
    if keyval['uid'] == uidsearch:
        for member in keyval['members']:
                if 'ipv4-address' in member:
                    iplist.append(member['ipv4-address'])
            
i = 0
with open("output.txt", "w") as f:
    for ip in iplist:
        temp = "Or " + typ + " = \"" + ip + "\""
        f.write("%s " % temp)
        i += 1
        if i == 5:
            f.write("_\n")
            i = 0
    
