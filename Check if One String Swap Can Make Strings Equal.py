class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count_=0
        list1=[]
        list2=[]
        for i in range(len(s2)):
            if s2[i]!= s1[i] :
                count_+=1
                list1.append(s1[i])
                list2.append(s2[i])
        list1=list(set(list1))
        list2=list(set(list2))
        if (count_==2 or count_==0) and(sorted(list1)==sorted(list2)):
            return True
        return False
