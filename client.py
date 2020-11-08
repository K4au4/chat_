import socket, threading, time

key = 8194

shutdown = False
join = False

def receving (name, sock):#Принимает данные от пользователей
	while not shutdown:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				

				
				decrypt = ""; k = False
				for i in data.decode("utf-8"):
					if i == ":":
						k = True
						decrypt += i
					elif k == False or i == " ":
						decrypt += i
					else:
						decrypt += chr(ord(i)^key)
				print(decrypt)
				

				time.sleep(0.2)
		except:
			pass
host = ''
port = 0#Для подключчения клиента

server = ("192.168.1.6",8080)# указываем переменный сервер

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))# для присвоения Имени клиенту
s.setblocking(0)#чтоб не вылазила ошибка

alias = input("Name: ")# ПРисвоение имени

rT = threading.Thread(target = receving, args = ("RecvThread",s))#Работа с многопоточностью (Функция (RecvThread", s) всегда обрабатывается с UPD)
rT.start()

while shutdown == False:# Пока клиент не вышел
	if join == False:# ПОка нет пользователя
		s.sendto(("["+alias + "] => join chat ").encode("utf-8"),server)#отправление сообщения от пользователя
		join = True
	else:
		try:
			message = input()#Ввод сообщения и его обработка на сервере

			
			crypt = ""
			for i in message:
				crypt += chr(ord(i)^key)
			message = crypt
			

			if message != "":
				s.sendto(("["+alias + "] :: "+message).encode("utf-8"),server)# Если сообщение пустое, то его не защитывается со стороны сервера

			
			time.sleep(0.2)#Диапозон между отправкой или получением сообщений
		except:
			s.sendto(("["+alias + "] <= left chat ").encode("utf-8"),server)
			shutdown = True

rT.join()#функция может просматривать всю программу. Благодаря ей пользователи контактируют без разрывов во времени
s.close()#Закрываем соединени
