class Solution(object):
    def numberOfBoomerangs(self, points):
        counter = 0
        for ipoint in points:
            mapper = {}
            for jpoint in points:
                if ipoint == jpoint:
                    continue
                distance = (ipoint[0] - jpoint[0]) ** 2 + (ipoint[1] - jpoint[1]) ** 2
                if distance not in mapper:
                    mapper[distance] = 0
                mapper[distance] += 1
            for distance in mapper:
                if mapper[distance] > 1:
                    counter += mapper[distance] * (mapper[distance] - 1)
        return counter
