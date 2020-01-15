'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

print("------------------------------------")
def copy(file_name, new_file_name): 
    with open(file_name, "r") as file: 
        text = file.read()

    with open(new_file_name, "w") as file: 
        file.write(text)

# copy(test305story.txt, test305storynew.txt) #error
copy("test305story.txt", "test305storynew.txt")