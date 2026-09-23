Weight = (float(input("Enter your weight : ")))
print("Weight:", Weight)
kg_or_lb = input("(K)g or (L)b : ")
if kg_or_lb == "K" or kg_or_lb == "k":
    print("Weight in Lbs:", Weight * 2.2)
elif kg_or_lb == "L" or kg_or_lb == "l":
    print("Weight in Kg:", Weight / 2.2)

