# TASK:

# Create two lists with at least two/three similar names from both lists.

# Find the common names from both lists and put them in a new list called 'commonNames' list

# Use the input function and then the if statement to search the commonNames list for a specific name

# print out any name(s) found from your search

londonA = ["Mo", "Shayan", "Saeid", "Ely", "Baz","Vita"]
londonB =["Hassan", "Timo", "Hadi", "Androw", "Jes","Saeid", "Ely"]
commonNames = [londonA[i] for i in range(len(londonA)) if londonA[i] in londonB]
searchTheName = (input("who you looking for ?"))

if searchTheName in commonNames:
    print(f"{searchTheName} is a common Name")
else:
    print(f"{searchTheName} is not a common name")
# print(commonNames)
