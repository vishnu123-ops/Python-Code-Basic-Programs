with open('GFG.txt','r') as file:
 
    # reading each line    
    for line in file:
 
        # reading each word        
        for word in line.split():
 
            # displaying the words           
            print(word) 