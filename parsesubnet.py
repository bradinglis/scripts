import json

uidsearch = "19c00c66-f53a-4abf-af21-65f284a6dbb8"
typ = "sDestIP"

with open('data.json', 'r') as myfile:
        jsondata = myfile.read()
        myfile.close

data = json.loads(jsondata)

i = 0
iplist = []
subnetlist = []
masklengthlist = []

for keyval in data:
    if keyval['uid'] == uidsearch:
        for member in keyval['members']:
                if 'ipv4-address' in member:
                    iplist.append(member['ipv4-address'])
                if 'subnet4' in member:
                    subnetlist.append(member['subnet4'])
                    masklengthlist.append(member['mask-length4'])

            
with open("output.txt", "w") as f:
    i = 0

    for ip in iplist:
        if i == 5:
            f.write("_\n")
            i = 0
        temp = "Or " + typ + " = \"" + ip + "\""
        f.write("%s " % temp)
        i += 1

    f.write("_\n")
    
    i = 0

    for j in range(len(subnetlist)):
        if i == 5:
            f.write("_\n")
            i = 0
        temp = "Or IpIsInSubnet(" + typ + ", \"" + str(subnetlist[j]) + "/" + str(masklengthlist[j]) + "\")"
        f.write("%s " % temp)
        i += 1

    f.write("_\n")
 


