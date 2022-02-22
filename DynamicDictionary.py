'''
A program that will allow the user
1) Add new definitions
2) Look for existing definitions
3) Delete definitions chosen by him
'''

dictionary = {}

end = False


while(end == False):
    print(" What do you want to do?\n1-add new definition\n2-search for definition\n3-delete definition\n4-break")
    choice = int(input())
    print()
    
    if(choice == 1):
        print("Add word and the definition\n")
        dictionary.update({input("Word:"):input('Definition:'),})
  
       
    elif(choice == 2):
        word = input("Insert definition to search: ")
        if(str(word) in dictionary):
            print("Definition:",dictionary[word])
        else:
            print("There is no definition of ",word," in dictionary")
            
    elif(choice == 3):
        word = input("Which definition do you want to delete?: ")
        print("You have just deleted definition of ",word)
        dictionary.pop(word)
        
    elif(choice == 4):
        end = True
    
    else:
        print("Make the right choice !!!")
        
    print()
              
