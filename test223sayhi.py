#__name__ variable :
# if the file is the main file being run, its value is "__main__"
# otherwise, its value is the file name

from test223saysup import say_sup
#Preventing default import excution(
# Ignoring Code on Import), in sub file, 
# if __name__ == "__main__: needed 
def say_hi():
    print(f"Hi! __name__ is is {__name__} ")
say_hi()
say_sup()