#host end
import util_functions,socket

print(util_functions.get_ip_adress())
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = util_functions.get_ip_adress()
port = 12345
server_socket.bind((host_ip, port))
server_socket.listen(5)
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")
server_socket.send()
server_socket.recv()
#client end
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = input("What is the ip adress: ")
server_port = 12345
client_socket.connect((server_ip, server_port))
client_socket.send()
client_socket.recv()