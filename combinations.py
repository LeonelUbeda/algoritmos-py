
Dictionary = ['A','B','C','D'] #Letters to combine

CombinationResult = [Dictionary[0]]

maxCombinations  =  500


print(''.join(CombinationResult))

for increase in range(maxCombinations):
    carriage = False
    for position in range(0,len(CombinationResult)):
        
        for unit in range(0,len(Dictionary)): 

            if CombinationResult[-position-1] == Dictionary[unit]:
                if CombinationResult[-position-1] == Dictionary[-1]:

                    CombinationResult[-position-1] = Dictionary[0] #Reset
                    carriage = True 

                else:

                    carriage = False
                    CombinationResult[-position-1] = Dictionary[unit+1]

                break
            
        if carriage == False:
            break

    if carriage == True:
        CombinationResult.append(Dictionary[0]) #Adds a digit
    print(''.join(CombinationResult))
print('Finish!')