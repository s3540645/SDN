
import socket

TCP_IP = '192.168.1.164'
TCP_PORT = 62
BUFFER_SIZE = 20 # Normally 1024, but we want fast response
if __name__ == '__main__':
	print("start 1")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("start 2")
	s.bind((TCP_IP, TCP_PORT))
	print("start 3")
	s.listen(10)

	print("start 4")
	conn, address = s.accept()
	print("start 5")
	print ('Connection address:', address)
	while 1:
		data = conn.recv(BUFFER_SIZE)
		if not data: break
		print ("received data:", data)
		conn.send(data) # echo
	conn.close()
