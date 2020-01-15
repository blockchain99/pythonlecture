# need to install external module
#  $ python3 -m pip install termcolor
from termcolor import colored
# from termcolor 

text = colored("HI THERE!", color="magenta", on_color="on_cyan", attrs=["blink"])
# text = termcolor.colored("HI THERE!", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)