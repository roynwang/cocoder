


if __name__ == '__main__':
	from FileTracker import *
	from Hub import *
	hub = Hub()

	appendline = ['234','567']
	msg = {'action':'ADD','pre':1, 'lines':appendline}

	hub.LoadFile('test.txt')
	hub.ChangeFile('test.txt', msg);

	hub.ChangeFile('test.txt',{'action':'REMOVE','lines':[3,4]})

	hub.CloseFile('test.txt')

	#testfile = FileTracker('test.txt')
	#testfile.Load()
	#msg = {'action':'ADD','pre':1, 'lines':appendline}
	#testfile.Add(1,appendline)
	#testfile.Execute(msg)
	#testfile.Execute({'action':'REMOVE','lines':[3,4]})
	#testfile.Write("test.log",'LOG')

