#Muhammad Abiya Makruf - 1301213157 - MTA
#TP MODUL 4

#Import library xmlrpc
from xmlrpc.server import SimpleXMLRPCServer    
from xmlrpc.server import SimpleXMLRPCRequestHandler 


#Deklarasi
class Calon:
    def __init__(self, namaPasangan1, namaPasangan2):
        self.namaPasangan1 = namaPasangan1
        self.namaPasangan2 = namaPasangan2
        self.jumlahVote = 0

    def getNamaPasangan(self):
        return self.namaPasangan1, self.namaPasangan2
    
    def jumlahVote(self):
        return self.jumlahVote
    
    def tambahVote(self):
        self.jumlahVote += 1

Calon1 = Calon("Abiya", "Makruf")
Calon2 = Calon("Gading", "Makruf")

def voting(calon):
    if calon == 1:
        Calon1.tambahVote()
        return "Terima kasih telah memilih"
    elif calon == 2:
        Calon2.tambahVote()
        return "Terima kasih telah memilih"
    else:
        return "Pilihan tidak tersedia"
    
def hasilVoting():
    return "Pasangan 1: " + str(Calon1.jumlahVote) + " suara, Pasangan 2: " + str(Calon2.jumlahVote) + " suara" 

#Server
class requestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 8008), requestHandler=requestHandler) as server:
    server.register_introspection_functions()
    server.register_function(voting, 'voting')
    server.register_function(hasilVoting, 'hasilVoting')
    server.serve_forever()


