class LineTracker(object):
	def __init__(self,content, pre, next, mode='='):
		self.Content=content
		self.Mode = mode
		self.Lock = False
		self.Pre = pre
		self.Next = next

	def SetMode(self, mode):
		self.Mode = mode

	def __del__(self):
		self.Content = None
		self.Pre = None
		self.Next = None
	
	def Lock(self):
		self.Lock = True

	def Unlock(self):
		'unlock the line'
		self.Lock = False


	def ToString(self):
		return self.Mode + ':' + self.Content + '\n'
