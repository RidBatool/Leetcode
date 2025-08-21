class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key= lambda x: (-x[0], x[1]))
        queue=[]
        print(people)
        for person in people:
            print(person[1], person)
            queue.insert(person[1], person)
        print(queue)
        return queue
