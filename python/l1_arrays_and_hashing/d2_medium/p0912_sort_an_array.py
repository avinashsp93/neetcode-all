class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arry, L, M, R):
            left, right = arry[L:M+1], arry[M+1:R+1]
            i,j,k = L,0,0
            while(j < len(left) and k < len(right)):
                if left[j] <= right[k]:
                    arry[i] = left[j]
                else:
                    arry[i] = right[k]

            while(j < len(left)):
                arry[i] = left[j]
                i+=1
                j+=1


            while(k < len(right)):
                arry[i] = right[k]
                i+=1
                k+=1

        def mergeSort(arr, l, r):
            if l == r:
                return arr

            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)