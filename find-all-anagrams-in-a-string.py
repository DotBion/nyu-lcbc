from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #sort the p in ascending
        #take slices of len(p) from s
        #sort the slice
        #check slice equal sorted p
        #store indices
        # result = []
        # sp = "".join(sorted(p))
        
        # for i in range(0,len(s)) :
        #     if i+len(p) > len(s) :
        #         break
        #     s_sliced = "".join(sorted(s[i:i+len(p)]))
        #     if s_sliced == sp :
        #         result.append(i)
        # return result

        #better soln. -sliding window of size len(p)
        from collections import Counter
        pcount = Counter(p)
        scount = Counter()
        plen = len(p)
        slen = len(s)
        if slen < plen :
            return []
        result = []
        for i in range(slen) :
            #update scount
            scount[s[i]] +=1
            
            #if i goes beyond lenp, then left window should slide right or my present scount should remove the element added by the left window or decrease its count
            if i >= plen :
                if scount[s[i-plen]] == 1 :
                    del scount[s[i-plen]]
                else :
                    scount[s[i-plen]] -= 1

            #if the counts on p and s are same, add index to result
            #this section needs to be at the end because  
            if pcount == scount :
                result.append(i-plen+1)

        return result
