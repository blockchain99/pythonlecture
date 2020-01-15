'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''


print("------------------------------------")
def copy_and_reverse(file_name, new_file_name): 
    with open(file_name, "r") as file: 
        text = file.read()
        print(type(text)) #'str' -> list of char string ex)'hello'

    with open(new_file_name, "w") as file: 
        file.write(text[::-1]) #reverse the text using a slice 

# copy(test305story.txt, test305storynew.txt) #error
copy_and_reverse("test305story.txt", "test305storyreverse.txt")