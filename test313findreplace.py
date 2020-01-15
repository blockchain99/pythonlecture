'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

# Python file method seek() sets the file's current position 
# at the offset. The whence argument is optional and defaults to
# 0, which means absolute file positioning, other values are 
# 1  which means seek relative to the current position and 
# 2 means seek relative to the file's end.



def find_and_replace(file_name, origin, replaced):
    with open(file_name, "r+") as file:
        text = file.read() 
        new_text = text.replace(origin, replaced)
        file.seek(0)
        file.write(new_text)
        file.truncate()


find_and_replace('test305haiku.txt', 'test', 'team') 







##############################################################
# def find2(file_name):
#     with open(file_name, "r") as file:
#         # result  = file.readline()  #just get one line
#         result  = file.readlines()  # get all lines
        
# print(find2("test305haiku.txt"))