#Accept input format such as dd/mm/yyyy, 
# dd.mm.yyyy dd,mm,yyyy  -> order such as month date year 
# rerun dict, { "d": date, "m": month, "y": year}
############### [] set -> represnet just one char(digit)#######
############### [0-20] -> just 0 , 1 represented 
import re
def parse_date(input):
    date_regex = re.compile(r'^(\d\d)[,/.](\d\d)[,/.](\d{4})$') 
    match = date_regex.search(input)
    if match:
        return {"m":match.group(1), "d":match.group(2), "y":match.group(3)}
    return None

def parse_date1(input):
    #mm: one digit(0 - 9) then tow digit(10, 11, 12) -> [0-9]|1[0-2]   
    date_regex = re.compile(r'\b(0[1-9]|1[0-2])[.,/](0[1-9]|1[0-9]|2[0-9]|3[01])[.,/](\d{4})\b')
    match = date_regex.search(input)
    if match:
        return {"m":match.group(1), "d":match.group(2), "y":match.group(3)}
    return None

print("-------- with ^ $ (start end)---------")
print(parse_date("01/22/1999"))
print(parse_date("12,04,2003"))
print(parse_date("12.04.2003"))
print(parse_date("12.04.200312"))
print(parse_date("25.04.2003"))  #not filter month 25!!
print("-------with \b \b (word bounding)------")
print(parse_date1("01/22/1999"))
print(parse_date1("12,04,2003"))
print(parse_date1("12.04.2003"))
print(parse_date1("12.04.200312"))
print(parse_date1("25.04.2003")) #filter month 25