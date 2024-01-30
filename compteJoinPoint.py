
def compteJoinPoint(s1,s2):

    while s1!=1:
        if s1<s2:
            s1+=sum(map(int,str(s1)))
        
        else:
            s2+=sum(map(int,str(s2)))

        return s1
    

reponse=compteJoinPoint(10,20)
print(reponse)