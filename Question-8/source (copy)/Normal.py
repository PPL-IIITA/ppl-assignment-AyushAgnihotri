from girl import girl
class Normal(girl):
	'Class for normal girl'
	def __init__(self,name,attractiveness,maintenance_budget,intelligence,type_):
		'Constructor for initialising Normal girl.'
		girl.__init__(self,name,attractiveness,maintenance_budget,intelligence,type_)