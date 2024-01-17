class Solution(object):
    def findRelativeRanks(self, score):
        l = []
        l1 = range(4,len(score)+1)
        clone = sorted(score,reverse=True)
        l2 = []
        for i in range(len(score)):
            if score[i] == clone[0]:
                score[i] = "Gold Medal"
            elif score[i] == clone[1]:
                score[i] = "Silver Medal"
            elif score[i] == clone[2]:
                score[i] = "Bronze Medal"
            else:
                l.append(i)
                l2.append(score[i])
        l2.sort()
        l2.reverse()
        for i in range(len(l2)):
            x = l2.index(score[l[i]])
            score[l[i]] = str(l1[x])
        return score