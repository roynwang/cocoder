def filetodic(filename):
	myfile = open(filename)
	print 'reading file %s' % filename
	filedict = {}
	i = 0
	for line in myfile :
		filedict[i] = line
		print '%d : %s' % (i,line)
		i+=1

	myfile.close()
	return filedict
def hello(msg):
	print '%s' % msg



if __name__ == '__main__':
	import socket
	import json
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('localhost', 8001))
	sock.listen(5)
	hello("ttt")
	#filedict = {}
	while True:
		connection,address = sock.accept()
		try:
			connection.settimeout(5)
			buf = connection.recv(1024)
			print ('got message %s' % buf)
			if buf == '1':
				print 'tring to read file'
				connection.send('please send the filename')
				d = connection.recv(1024)
				#print '%s' % 
				allcontent = filetodic(d)
			else:
				connection.send('please go out!')
		except socket.timeout:
			print 'time out'
			connection.close()






