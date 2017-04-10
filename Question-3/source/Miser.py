from boy import Boy 
class Miser(Boy):
	'Class for miser boy'
	def __init__(self, name, attractiveness, girlfriend_budget, intelligence, minimum_attraction_requirement,type_):
		'Constructor for initialising Miser boy'
		Boy.__init__(self, name, attractiveness, girlfriend_budget, intelligence, minimum_attraction_requirement,type_)