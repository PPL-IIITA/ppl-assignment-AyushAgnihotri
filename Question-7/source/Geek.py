from boy import Boy 
class Geek(Boy):
	'Class for geek boy'
	def __init__(self, name, attractiveness, girlfriend_budget, intelligence, minimum_attraction_requirement,type_):
		'Constructor for initialising geek boy'
		Boy.__init__(self, name, attractiveness, girlfriend_budget, intelligence, minimum_attraction_requirement,type_)