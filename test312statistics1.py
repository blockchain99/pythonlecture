'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

# def statistics(file_name):
#     # with open(file_name, "r") as file:
#     #     readfile = file.read()
#     #     chars = len(readfile)
#     # with open(file_name, "r") as file:
#     #     readlinefile = file.readline()
        
#     with open(file_name, "r") as file:
#         readlinesfile = file.readlines()
#         # num_line = (sum[1 for i in range(0, len(num_line)])
#         # line = (sum[1 for i in range(0, len(num_line)])
#         num_line = 0
#         num_word = 0
#         num_char = 0
#         split_list = []
#         word_list = []
#         for line in readlinesfile:
#             num_line +=1
#             split = line.split(" ") #word list
#             for word in split: #each word, count & sum
#                 word_list.append(word)
#                 num_char += len(''.join(word.split())) 
#                 num_word += 1

#         return {"lines":num_line, "words":num_word, "chars": num_char}


def statistics(file_name):  #lec ver
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
            #  "characters": sum(len(line) for line in lines) } # incl blank
             "characters": sum(len(''.join(line.split())) for line in lines) }


print(statistics("test305.txt"))
#ouput char: 34, actual 32 -> may be carrage return included 
# --> OK regard this out to be correct
print(statistics("test305haiku.txt")) #char number is less one by line than correct

## lec ver: chars are 40, which reflect blank chars. -> may be wrong!

#remove leading and ending spaces, use str.strip()
#remove all space sentence.replace(" ", "")

# #######################################################
# To remove only spaces use str.replace:

# sentence = sentence.replace(' ', '')
# To remove all whitespace characters (space, tab, newline, and so on) you can use split then join:

# sentence = ''.join(sentence.split())