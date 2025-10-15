#Name: Jenna Ofiara
#Email: Jofiara@umich.edu
#Student ID: 73223467
#Collaborators: None, however I meet with my tutor twice a week and he helped a lot with this assignment (helping me figure out how to write the code)
#GENAI: I used Generative AI to help with debugging, to help generate outline for code (for example how to format test cases), and the write results text file because I kept forgetting what to do. 
#Example prompts I used were 
# "What are test cases examples I can do for these calculations, but just give ideas."
# "What is wrong with my code, why is it not running?
# "Can you give me hints on how to start my code" (mainly did this for test cases)
# "Did I meet all the requirements for this assignment?""

import csv

def load_penguins(filename):
    inFile = open(filename, newline='')
    csv_reader = csv.DictReader(inFile)
    data = list(csv_reader)

    print(" - Here are the headers: ", data[0].keys())
    print(" - Here is a sample row: ", data[0])
    print(" - Here are the number of rows:", len(data))
    print("\n")
    
    inFile.close()
    return data

#average body mass
'''this function gives the average body mass in grams
    for each species, depending on their sex'''

def avg_body_mass_by_species_sex(data):
    groups = {} 
    for row in data:
        if row["body_mass_g"] == "NA" or row["sex"] == "NA": #skip the rows without any data in it
            continue
        species_type = row["species"] #extracted
        species_sex = row["sex"]
        mass = float(row["body_mass_g"]) #change to float so it is not a string
        if species_type not in groups: 
            groups[species_type] = {} #create empty dict
        if species_sex not in groups[species_type]: 
            groups[species_type][species_sex] = []
        groups[species_type][species_sex].append(mass) #check if the sex exists
        #print(groups)
        
    results = [] #print averages 
    for species_type in groups:
        for species_sex in groups[species_type]: #loops through every species and sex in groups
            values = groups[species_type][species_sex] #mass value
            average = round(sum(values)/len(values)) #find average 
            results.append((species_type, species_sex, average))
    return results

#average flipper length
'''this function gives the average flipper length in mm 
    for each species, depending on their island'''

def avg_flipper_by_species_island(data):
    groups = {}  # {species: {island: [flippers]}}
    for row in data:
        if row["flipper_length_mm"] == "NA" or row["island"] == "NA":
            continue
        species_type = row["species"]
        island = row["island"]
        fl = float(row["flipper_length_mm"])
        if species_type not in groups:
            groups[species_type] = {}
        if island not in groups[species_type]:
            groups[species_type][island] = []
        groups[species_type][island].append(fl)

    results = []
    for species_type in groups:
        for island in groups[species_type]:
            values = groups[species_type][island]
            average = round(sum(values)/len(values))
            results.append((species_type, island, average))
    return results

#Write results
'''write the results of the function'''
def write_results(filename, avg_body_mass_by_species_sex, avg_flipper_by_species_island):
    with open(filename, "w") as f:
        # Body mass
        f.write("Average Body Mass (g) by Species and Sex: \n")
        for species_type, species_sex, average in avg_body_mass_by_species_sex:
            f.write(f" - {species_type} ({species_sex}): {average}\n")

        # Flipper length
        f.write("\nAverage Flipper Length (mm) by Species and Island: \n")
        for species_type, island, average in avg_flipper_by_species_island:
            f.write(f"- {species_type} on {island}: {average}\n")

    
# --- main program ---
if __name__ == "__main__":
    penguins = load_penguins("penguins.csv")

    #print the output for body mass 
    body_mass = avg_body_mass_by_species_sex(penguins)
    print("Average Body Mass (grams) by Species Sex:")
    print(body_mass)

    #flipper length
    flipper_length = avg_flipper_by_species_island(penguins)
    print("Average Flipper Length (mm) by Species and Island:")
    print(flipper_length)

    # write results file
    write_results("results.txt", body_mass, flipper_length)
    print("Created text results file")
