from FileTracker import *
import os

class Hub(object):
	def __init__(self):
		self.FileDict = {}

	def LoadFile(self, filename, usr=''):
		key = usr + ':' + filename
		filepath = usr + '/' + filename
		if usr == '' :
			filepath = filename
		fileobj = FileTracker(filepath)
		fileobj.Load()
		self.FileDict[key] = fileobj;
	
	def CloseFile(self, filename, usr='', giveup=False):
		key = usr + ':' + filename
		if not giveup :
			#TODO need to use NORMAL mode when running
			self.FileDict[key].Write()
			#self.FileDict[key].Write('test.log','LOG')
		self.FileDict[key] = None
	
	def ChangeFile(self, filename, msg, usr=''):
		key = usr + ':' + filename
		self.FileDict[key].Execute(msg)
