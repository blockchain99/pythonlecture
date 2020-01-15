
print("How many km did you cycle todoy ?")
kms = input()
miles = float(kms) / 1.60934
roundmiles = round(miles, 1)
#python3.6 above: f"-- {var} --"
print(f"OK, you said {roundmiles} miles") 
#2.7 - 3.5 : "--{}--".fommat(var)
print("OK. you said {} miles".format(roundmiles))