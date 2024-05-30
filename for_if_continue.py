# for loop using continue statement
Animals = ["Tiger","Lion","Elephant"]           # storage data from Animals variable
for x in Animals:                               # suing for loop executing Animals line by line single data execution
    if x=="Lion":                               # continue the not-execution for Lion
        continue
    print(x)