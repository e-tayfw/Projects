#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('input/Names/invited_names.txt') as names:
    name_list = names.readlines()
    new_names = []

    for name in name_list:
        name = name.replace('\n', "").strip()
        new_names.append(name)
    
    with open('input/Letters/starting_letter.txt') as example:
        eg_letter = example.read()

        for name in new_names:
            letter_for_name = eg_letter.replace('[name]', name)

            with open(f"output/ReadyToSend/letter_for_{name}.txt", mode='w') as final:
                final.write(letter_for_name)


        
    