from LineTracker import *

class FileTracker(object):

	def __init__(self,filename):
		self.File = filename
		self.Count = 0
		self.LineDict = []
		self.Head = None
		
	def Load(self):
		#'load to memory'
		fileobj = open(self.File);
		#append the head
		self.Head = LineTracker("HEADER",None,None)
		self.LineDict.append(self.Head)
		#append lines
		head = self.Head
		for line in fileobj:
			head.Next = LineTracker(line.rstrip('\n'), head,None)
			head = head.Next
			self.LineDict.append(head)
		fileobj.close()


	def Write(self, outfile=None, mode='NORMAL'):
		#'write the content to file'
		if outfile == None :
			outfile = self.File
		fw = open(outfile, 'w')
		node = self.Head
		while node.Next != None:
			node = node.Next
			if mode == 'NORMAL' and node.Mode != '-':
				fw.write(node.Content)
				fw.write('\n')
			if mode == 'LOG':
				fw.write(node.ToString())
		fw.close()
			

	def Add(self,pre, lines):
		#'add new line to pre'
		linenum = pre
		pre = self.LineDict[pre]
		for line in lines:
			lineobj = LineTracker(line, pre, pre.Next,'+')
			print '+ %s' % line
			self.LineDict.append(lineobj)
			lineobj.Next = pre.Next
			pre.Next = lineobj
			pre = lineobj
	
	def Delete(self, lines):
		#'delete lines after pre'
		for line in lines:
			cur = self.LineDict[line]
			cur.SetMode('-')
			print '- %s' % cur.Content

	def Modify(self, lineNum, newline):
		'modify the line content'

	def Lock(self, lineNums):
		'Lock the line'

	def Unlock(self, lineNums):
		'unlock the line'

