# print("Hello World!")
# counties = ["Arapahoe","Denver","Jefferson"]
# if "Arapahoe" in counties and "El Paso" not in counties:
#    print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# for county in counties:
#     print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    # prints the value of the county index/key
    # print(counties_dict[county])

    #prints the key
    print(county)
# for voters in counties_dict.values():
#     print(voters)

#Get key value pairs
for key,value in counties_dict.items():
    print(f"{key} county has {value:,} registred voters")


# List of Dictionaries


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print("LIST OF DICTIONARIES")
    print(county_dict)
    # GET THE VALUE OF DICT
    print()
    print("VALUES")
    for value in county_dict.values():
        print(value)


# PRINT THE COUNTY
# print("JUST THE COUNTY USING RANGE FUNC")
# for i in range(len(voting_data)):
#     print(voting_data[i]['county'])

