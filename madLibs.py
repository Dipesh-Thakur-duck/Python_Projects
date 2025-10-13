import re
with open('./madLib.txt','rt')as file:
    content = re.findall(r'\w+|[^\w\s]',file.read())
final_content = []
for i in content:
    if i in ["ADJECTIVE","ADVERB"]:
        final_content.append(input(f'Enter an {i}: '))
    elif i in ["VERB","NOUN"]:
        final_content.append(input(f'Enter a {i}: '))
    else:
        final_content.append(i)
final_string = ' '.join(final_content)

final_string = re.sub(r'\s+([.,!?])',r'\1',final_string)

with open('./madLib_output.txt','wt') as file:
    file.write(final_string)
print("\nYour final story:\n")
print(final_string)

# re.findall(r'\w+|[^\w\s]',file.read())
# returns a list of strings like a split() function and punctuations are individual strings unlike with split function

# re.sub(r'\s+([.,!?])',r'\1',final_string)
# re.sub(<regex>,<value_sub>,text)
# finds all the strings with whitespaces and punctuators like "   ," and turns them into just punctuators: "   ,"->","
# r'\1' means group 1 which is [.,!?]
        
    
    