#Muhammad Abiya Makruf - 1301213157 - MTA
#TP MODUL 4

#Import library xmlrpc
from xmlrpc.server import SimpleXMLRPCServer    
from xmlrpc.server import SimpleXMLRPCRequestHandler 


#Deklarasi
calonBem = {"nama1":"Muhammad Abiya Makruf","jumlahVoteNama1":0,"nama2":"Muhammad Gading Makruf","jumlahVoteNama2":0}



#Server
class requestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 8008), requestHandler=requestHandler) as server:
    server.register_introspection_functions()

    def voting(inputVoting):
        if inputVoting == 1:
            calonBem["jumlahVoteNama1"] += 1
        elif inputVoting == 2:
            calonBem["jumlahVoteNama2"] += 1
        return("Vote berhasil. Terima kasih atas partisipasinya\n")

    def daftarCalon():
        return f"\n===== Daftar Calon BEM ===== \n1.{calonBem['nama1']} \n2.{calonBem['nama2']}\n"
    
    def hasilVoting():
        return f"\n===== Hasil Voting ===== \n1.{calonBem['nama1']} : {calonBem['jumlahVoteNama1']} \n2.{calonBem['nama2']} : {calonBem['jumlahVoteNama2']}\n"

    server.register_function(voting, 'voting')
    server.register_function(daftarCalon, 'daftarCalon')
    server.register_function(hasilVoting, 'hasilVoting')

    server.serve_forever()


