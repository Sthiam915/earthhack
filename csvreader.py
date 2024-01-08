import csv
def add_data_to_model():
    # Open the CSV file with 'latin-1' encoding
    solutions = []
    with open("AI EarthHack Dataset.csv", 'r', encoding='latin-1') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)

        # Iterate over rows in the CSV file
        for row in csv_reader:
            # Unpack values into variables
            id, problem, solution = row 

            # Now you can use id, problem, solution as separate variables
            #print("ID:", id)
            #print("Problem:", problem)
            #print("Solution:", solution)
            solutions.append(solution)
    return solutions

