class Gift :
	name = ''
	cost = 0
	value = 0
	type_ = ''
	'Class for gift'
	def __init__(self,name,cost,value,type_):
		'Constructor for initialising gift'
		self.name = name
		self.cost = cost
		self.value = value
		self.type_ = type_