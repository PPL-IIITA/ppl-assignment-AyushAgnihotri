from gift_item import Gift
class Luxury(Gift):
	'Class for Luxury gift'
	def __init__(self,name,cost,value,type_) :
		'Constructor for initialising the Luxury gift'
		Gift.__init__(self,name,cost,value,type_)