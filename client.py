#Muhammad Abiya Makruf - 1301213157 - MTA
#TP MODUL 4

import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://localhost:8008')

print(s.voting(1))
print(s.hasilVoting())
print(s.system.listMethods())

