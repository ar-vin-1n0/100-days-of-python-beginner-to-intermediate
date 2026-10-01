#TODO: Create a letter using starting_letter.txt
with open("input/letter/starting_letter.txt", "r") as f:
    letter = f.read()


#for each name in invited_names.txt
with open("input/names/invited_names.txt", "r") as n:
    invited_names = n.readlines()

for names in invited_names:
    name = names.strip()

    new_letter = letter.replace("[name]", name)

    with open(f"output/readytosend/{name}.txt", "w") as R:
        R.write(new_letter)



#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp