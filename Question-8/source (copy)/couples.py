class Couple:
	'Class for couples'
	def __init__(self, boy, girl):
		'Constructor for intialising couple'
		self.happiness = 0
		self.girl = girl
		self.boy = boy
		self.gifts = []
		self.compatibility_status = 0
		
	def set_compatibility(self):
		'Method for setting compatibility'
		a = self.boy.boys_girlfriend_budget - self.girl.maintenance_budget
		b = abs(self.boy.attractiveness - self.girl.attractiveness)
		c = abs(self.boy.intelligence - self.girl.intelligence)
		self.compatility_status = a+b+c	

	def set_happiness(self):
		'Method for setting Happiness'
		self.happiness = self.boy.happiness + self.girl.happiness

	