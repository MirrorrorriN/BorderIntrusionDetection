import collections
def ladder(s1,s2,wordlist):
    wordlist.add(s2)
    queue=collections.deque([[s1,1]])
   
    alphabet="abcdefghijklmnopqrstuvwxyz"
    
    
    while(queue):
        s,length=queue.popleft()
        if s ==s2:
            return length
        for i in range(len(s)):
            for c in alphabet:
                st = s[:i] + c + s[i+1:]
                if st in wordlist:
                    wordlist.remove(st)
                    queue.append([st, length + 1])
    return 0
  
        


if __name__=="__main__":
	s1="hit"
	s2="hog"
	wordlist=set(["hig","dot","dog","log","lot"])
	opt=ladder(s1,s2,wordlist)
	print opt
