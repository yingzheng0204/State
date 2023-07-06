

'''
'''

class State:
	'''
	'''
	def __init__(self, filename):
		with open(filename) as f:
			firstline = f.readline()
			fl = firstline.split()
			if fl[0] != 'System{':
				raise Exception('Not valid State file')
			else:
				self.param = Composite(f, 'System')
				self.thermo = Thermo()
				self.thermo.read(f)

	def writeOut(self, filename):
		with open(filename) as f:
			f.write(self.writeOutString())

	def writeOutString(self):
		out = self.param.writeOutString() + '\n' + self.thermo.writeOutString()
		return out

s = State('data750')
print(s.writeOutString())
