class Solution:
    def reverseWords(self, s: str) -> str:
        #double pass
        # s += " "
        # word = ""
        # wordlist = []
        # lastalpha = 0
        # for i in s :
        #     if i == ' ' and lastalpha == 1 :
        #         wordlist.append(word)
        #         word=""
        #         lastalpha = 0
        #     elif i!=' ' :
        #         word+=i
        #         lastalpha = 1
        # result = ""
        # for i in range(len(wordlist)-1,-1,-1) :
        #     result += wordlist[i] + " "
        # print(result)
        # return result.rstrip()

        #two pointer
        # words = s.split()
        # i,f = 0, len(words) - 1
        # while i<f :
        #     words[i], words[f] = words[f], words[i]
        #     i+=1
        #     f-=1
        # return " ".join(words)   

        #one liner
        return " ".join(reversed((s.split())))  
