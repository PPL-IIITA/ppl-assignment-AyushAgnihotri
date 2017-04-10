from gift_item import Gift
class Utility(Gift):
	'Class for utility gift'
	def __init__(self,name,cost,value,type_) :
		'Constructor for initialising Utility gift.'
		Gift.__init__(self,name,cost,value,type_)