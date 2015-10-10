class Solution:
	def __init__(self):
		self.dictions = {0:'Zero', 1: 'One', 2: 'Two', 3: "Three", 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15:'Fifteen', 16: 'Sixteen',17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
	def numberToWordsNoMoreThanThousand(self, num):
		answer = []
		if num >= 100:
			answer.append(self.dictions[num / 100])
			answer.append('Hundred')
			if num % 100:
				num %= 100
			else:
				return answer
		if num <= 20:
			answer.append(self.dictions[num])
		else:
			answer.append(self.dictions[num - num % 10])
			if num % 10 != 0:
				num = num % 10
				answer.append(self.dictions[num])
		return answer
	def numberToWords(self, num):
		answer = []
		if num >= 10 ** 9:
			answer.append(self.dictions[num / (10 ** 9)])
			answer.append('Billion')
			if num > 10 ** 9:
				num = num % (10 ** 9)
			else:
				return ' '.join(answer)
		if num >= 10 ** 6:
			answer.extend(self.numberToWordsNoMoreThanThousand(num / (10 ** 6)))
			answer.append('Million')
			if num % (10 ** 6):
				num = num % (10 ** 6)
			else:
				return ' '.join(answer)
		if num >= 10 ** 3:
			answer.extend(self.numberToWordsNoMoreThanThousand(num / (10 ** 3)))
			answer.append('Thousand')
			if num % (10 ** 3):
				num = num % (10 ** 3)
			else:
				return ' '.join(answer)
		answer.extend(self.numberToWordsNoMoreThanThousand(num))
		return ' '.join(answer)

ins = Solution()

print ins.numberToWords(2147483647)