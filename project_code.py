#Name: Jenna Ofiara
#Email: Jofiara@umich.edu
#Student ID: 73223467
#Collaborators: GENAI (chatGPT) and my Tutor helped (worked alone though)

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

def average_body_mass_by_species_sex(data):
    groups = {} #nested dict
    for row in data:
        if row["body_mass_g"] == "NA" or row["sex"] == "": #skip the rows without any data in it
            continue
        species_type = row["species"]
        species_sex = row["sex"]
        mass = float(row["body_mass_g"]) #change to float so it is not a string
        if species_type not in groups:
            groups[species_type] = {} #check is species exist
        if species_sex not in groups[species_type]:
            groups[species_type][species_sex] = []
        groups[species_type][species_sex].append(mass) #check if the sex exists

    results = [] #print results 
    for species_type in groups:
        for species_sex in groups[species_type]:
            values = groups[species_type][species_sex]
            average = round(sum(values)/len(values)) #find average 
            results.append((species_type, species_sex, average))
    return results

#average flipper length
'''this function gives the average flipper length in mm 
    for each species, depending on their island'''

def average_flipper_by_species_island(data):
    groups = {}  # {species: {island: [flippers]}}
    for row in data:
        if row["flipper_length_mm"] == "NA" or row["island"] == "":
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

#Write results (I had generative AI help me with this part because I struggled)
'''write the results of the function'''
def write_results(filename, mass_by_species_sex, flipper_by_species_island):
    with open(filename, "w") as f:
        # Body mass
        f.write("Average Body Mass (g) by Species and Sex\n")
        for species_type, species_sex, average in mass_by_species_sex:
            f.write(f"{species_type} ({species_sex}): {average}\n")

        # Flipper length
        f.write("\nAverage Flipper Length (mm) by Species and Island\n")
        for species_type, island, average in flipper_by_species_island:
            f.write(f"{species_type} on {island}: {average}\n")

    
# --- main program ---
if __name__ == "__main__":
    penguins = load_penguins("penguins.csv")

    #print the output for body mass and flipper length
    body_mass = average_body_mass_by_species_sex(penguins)
    print("Average Body Mass (grams) by Species Sex:")
    print(body_mass)

    flipper_length = average_flipper_by_species_island(penguins)
    print("Average Flipper Length (mm) by Species and Island:")
    print(flipper_length)

    # write results file
    write_results("results.txt", body_mass, flipper_length)
    print("Created results file")
