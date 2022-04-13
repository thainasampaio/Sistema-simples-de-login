import threading 
import socket

clients = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(('localhost', 7777))
        server.listen(10)
    except:
        return print('\n Não foi possível iniciar o servidor\n')

    while True:
        client, addr = server.accept()
        print(addr)
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            send_for_all_clients(msg, client)
        except:
            deleteClient(client)
            break

def send_for_all_clients(msg, c_client):
    for client in clients:
      if client != c_client:
        try:
            client.send(msg)
        except:
            deleteClient(client)

def deleteClient(client):
    client.close()
    clients.remove(client)

main()