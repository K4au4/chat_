import socket, time

host = ''
port = 8080# Во избежания блокировки подключения(если порт требует рута), или запуске чего-то на порте

clients = []# список клиентов

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))

quit = False #Во избежания бесконечного цикла
print("[ Сервер запущен ]")
print ("[Выполнено студентами группы 1141:\nСухотским Дмитрием и Патерикиной Полиной]")

while not quit:
	try:
		data, addr = s.recvfrom(1024)# 2 переменные (данные и адрес) для серва

		if addr not in clients:# Если у адреса нет клиента, то добавлеим клиента к адресу
			clients.append(addr)

		itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())# Преобразование даты в переменную

		print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/",end="")# Приобразование даты в переменную
		print(data.decode("utf-8"))# Сообщение выводится в utf-8 после декодировки

		for client in clients:# Смотрим клиентов
			if addr != client:# Если адрес не равен клиенту, то сообщение отправляется некст клиенту (Чтобы клиент не получал свои сообщения)
				s.sendto(data,client)
	except:	
		print("\n[ Сервер остановлен ]")
		quit = True
		
s.close()
