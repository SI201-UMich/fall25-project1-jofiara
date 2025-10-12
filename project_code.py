import csv

def load_penguins(filename):
    filename = "penguins.csv"
    inFile = open(filename, newline='')
    csv_reader = csv.DictReader(inFile) #genAI recommended Dictreader instead of reader)
    data = list(csv_reader)

    #print contents 
    print("Columns:", csv_reader.fieldnames)
    print("Number of rows:", len(data))
    print("First row sample:", data[0])

    inFile.close() 
    return data


# --- main program ---
if __name__ == "__main__":
    penguins = load_penguins("penguins.csv")