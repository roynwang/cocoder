from FileTracker import *

class Hub(object):
	def __init__(self):
		self.FileDict = {}

	def LoadFile(filepath, usr=''):
		key = usr + ':' + filepath
		fileobj = FileTracker(filepath)
		fileobj.Load()
		self.FileDict{key} = fileobj;

	

