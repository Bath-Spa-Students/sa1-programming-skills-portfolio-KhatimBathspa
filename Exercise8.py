# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask the user for a name to search
search_term = input("Enter the name you want to search for: ").strip()

# Perform the search (case-sensitive)
if search_term in names:
    print(f"{search_term} was found in the list!")
else:
    print(f"{search_term} was NOT found in the list.")
