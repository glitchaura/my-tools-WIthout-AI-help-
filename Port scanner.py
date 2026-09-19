import socket

target_ip=input("enter target ip:\n")
user_ports=input("enter ports range seperated by ,")

try:
    ports_to_scan = [int(p.strip()) for p in user_ports.split(",")]
except ValueError:
 print("Error: Make sure you only enter numbers separated by commas!")
 ports_to_scan = []
 
for port in ports_to_scan:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(0.5)
  
  try:
     result = s.connect_ex((target_ip, port))
     if result == 0:
                    print(f" Port {port} OPEN")
     else:
          print(f" Port {port} CLOSE")

  except socket.error:
    print("socket error,don't panic")
  finally:
      s.close()
