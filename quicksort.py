class sort:
    @classmethod
    def qs(cls, l, lo, hi):
        if hi <= lo:
            return
        else:
            # print(l[lo:hi+1])
            p = cls.partition(l, lo, hi)
            cls.qs(l,lo,p-1)
            cls.qs(l,p+1,hi)
            
    @classmethod
    def partition(cls,l, lo, hi):
        pivot = l[lo]
        left = lo+1
        right = hi
        
        while left < right:
            print(l)
            #we will search for value greater than pivot
            while l[left] < pivot and left < hi:
                left += 1
            while l[right] > pivot:
                right -=1
            
            #swap values however we do not want to if right is less than left 
            #because we have found the boundary between values less than and greater
            #than pivot
            if left < right:
                temp = l[left]
                l[left] = l[right]
                l[right] = temp 
                
        l[lo] = l[right]
        l[right] = pivot
        return right
                

    
# alist = [54,26,93,17,77,31,44,55,20]
# # alist=[4,3,2,1]
# sort.qs(alist,0,len(alist)-1)
# # partition(alist,0,len(alist)-1)
# print(alist)


class sortPivot(sort):
    @classmethod
    def partition(cls,l,lo,hi):
        pivot = ((hi-lo) // 2) + lo
        print(l[pivot], l[lo:hi+1])
        left = lo
        right = hi

        while left < right:

            while l[left] <= l[pivot] and left < hi:
                left += 1

            while l[right] >= l[pivot] and right > lo:
                right -= 1

            if left < right:
                temp = l[left]
                l[left] = l[right]
                l[right] = temp

        if right < pivot and left < pivot:
            temp = l[pivot]
            l[pivot] = l[left]
            l[left] = temp
            return left
        elif right > pivot and left > pivot:
            temp = l[pivot]
            l[pivot] = l[right]
            l[right] = temp
            return right
        print(l)
        return pivot
        
alist = [54,26,93,17,77,31,44,55,20]
sortPivot.qs(alist,0,len(alist)-1)
print(alist)
