def computeMultiplesSum(n):
    if 0<=n<1000:
        somme=0

        for i in range(n):
            if i % 3== 0 or i % 5 == 0  or i % 7 == 0:
                somme=+i
        return somme

    else:
        print("Veuillez respectez la consigne")

        
    

reponse=computeMultiplesSum(11)
print(reponse)
        