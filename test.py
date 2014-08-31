


if __name__ == '__main__':
	from FileTracker import *
	testfile = FileTracker('test.txt')
	testfile.Load()
	appendline = ['234','567']
	testfile.Add(1,appendline)
	testfile.Delete([3,4])
	testfile.Write("test.log",'LOG')
	
