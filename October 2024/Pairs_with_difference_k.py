#User function Template for python3
class Solution:
	def countPairsWithDiffK(self,arr, k):
    	# code here
    	freq={}
    	for num in arr:
    	    freq[num]=freq.get(num,0)+1
    	
    	count=0
    
    	for num in freq:
    	    if (num+k) in freq:
    	        count+=freq[num]*freq[num+k]
    	    
    	    if k>0 and (num-k) in freq:
    	        count+=freq[num]*freq[num-k]
    	   
    	return count//2
    	    
    	    
