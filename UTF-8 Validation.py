class Solution:
    def getBinary(self, num):
        binary_string = str(bin(num))
        binary_string = binary_string[2:]
        
        pick = 8 - len(binary_string)
        prefix = '0' * pick
        binary_string = prefix + binary_string
        return binary_string

    def validUtf8(self, data):
        binary_strings = []
        for num in data:
            binary_strings.append(self.getBinary(num))
        while binary_strings:
            top = binary_strings.pop(0)
            number = int(top, 2)
            if top.startswith('0'):
                continue
            elif top.startswith('110'):
                if len(binary_strings) >= 1:
                    top += binary_strings.pop(0)
                    if int(top, 2) & 49280 != 49280:
                        return False
                else:
                    return False
            elif top.startswith('1110'):
                if len(binary_strings) >= 2:
                    top += binary_strings.pop(0)
                    top += binary_strings.pop(0)
                    if int(top, 2) & 14712960 != 14712960:
                        return False
                else:
                    return False
            elif top.startswith('11110'):
                if len(binary_strings) >= 3:
                    top += binary_strings.pop(0)
                    top += binary_strings.pop(0)
                    top += binary_strings.pop(0)
                    if int(top, 2) & 4034953344 != 4034953344:
                        return False
                else:
                    return False
            else:
                return False
        return True
