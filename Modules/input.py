#Put all your needed imports here ('os' is required)
# ⚠️ YOU MUST NOT REMOVE 'OS' ⚠️ 
import os


#Main function, input represents the given line where the function is called
# ⚠️ YOU MUST NOT ALTER THE NAME OR THE ARGUMENTS OF THE FOLLOWING FUNCTION ⚠️ 
def main(input):
    #Put all your code/actions here
    input = input.replace("input","")
    input = input.replace("(","")
    input = input.replace(")","")
    input=input.replace()


#Code used to communicate with the main file
# ⚠️ YOU MUST NOT DELETE THE FOLLOWING CODE ⚠️ 
output = ""
with open(os.getcwd() + '\\Modules\\input.txt', 'r') as f:
    output = f.readlines()[0]
    main(output)