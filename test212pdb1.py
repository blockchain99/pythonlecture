def add_numbers(a,b,c,d):  #terrible var name!! conflict with pdb command name
    import pdb; pdb.set_trace()

    return a + b + c + d
# l(list)
# n(next line)
# p(print)
# c(continue - finishes debugging)

add_numbers(1,2,3,4)

# (Pdb) d -> ** Newest frame
# (Pdb) a -> All(command) values such as a=1 b=2 c =3 d =4
# (Pdb) c -> Continue to quit(command) instead of var c
# If I need print var c -> (Pdb) p c -> print var c