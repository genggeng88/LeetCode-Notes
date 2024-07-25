class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        arr1 = []
        arr2 = []
        for log in logs:
            tmp = log.split(" ")
            if tmp[1].isdigit():
                arr2.append(log)
            else:
                arr1.append(log.split(" "))
        arr1.sort(key = lambda x : (x[1:], x[0]))
        
        for i in range(len(arr1)):
            tmp = " ".join(arr1[i])
            arr1[i] = tmp 
        
        return arr1 + arr2