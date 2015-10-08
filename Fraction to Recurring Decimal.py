class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
	def fractionToDecimal(self, numerator, denominator):
		neg=False
		if numerator<0:
			neg=not neg
			numerator=(~numerator)+1
		if denominator<0:
			neg=not neg
			denominator=(~denominator)+1			
		retstr=str(numerator/denominator)
		numerator=numerator%denominator
		if numerator:
			retstr+='.'
		position={}
		targetPos=-1
		retstrsize=len(retstr)
		while numerator:
			numerator*=10
			if numerator in position:
				targetPos=position[numerator]
				break
			else:
				position[numerator]=retstrsize
			retstr+=str(numerator/denominator)
			numerator%=denominator
			retstrsize+=1
		if targetPos!=-1:
			retstr=retstr[:targetPos]+'('+retstr[targetPos:]+')'
		if neg and str(retstr)!='0':
			retstr='-'+retstr
		return retstr