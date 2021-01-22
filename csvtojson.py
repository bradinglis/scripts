import csv

with open('./file.csv', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    data = list(reader)

f = open('./toimport.json', 'w')

f.write('{ "zabbix_export": { "version": "5.2", "date": "2021-01-21T23:15:21Z", "groups": [ { "name": "Slab Caster" }, { "name": "Slabmaking" } ], "hosts": [');

for i in range(len(data)):
    f.write('{ "host": "%(hostname)s", "name": "%(hostname)s - %(description)s", "proxy": { "name": "SMKVZAB01" }, "templates": [ { "name": "Template ICMP Ping" } ], "groups": [ { "name": "BOS" }, { "name": "Clients" } ], "interfaces": [ { "ip": "%(ip)s", "interface_ref": "if1" } ], "inventory_mode": "DISABLED" } ' %{'hostname': data[i][3].strip(), 'description': data[i][4], 'ip': data[i][0]});
    if i != (len(data) - 1):
        f.write(',');

f.write(' ] } }');

f.close()
