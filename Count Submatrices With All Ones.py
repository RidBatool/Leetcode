class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m= len(mat)
        n= len(mat[0])
        h=[0]*n
        count=0
        for i  in range(m):
            for j in range(n):
                if mat[i][j]:
                    h[j]=h[j]+1
                else:
                    h[j]=0
            for j in range(n):
                mn= h[j]
                k=j
                while k>=0 and mn:
                    mn= min(mn, h[k])
                    count+=mn
                    k-=1
        return count
