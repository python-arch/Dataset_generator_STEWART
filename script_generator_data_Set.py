import csv
import math
import random

# Define the range of values for x, y, and z
numberofdata_p = 10**5

# Initialize a list to store the dataset
dataset = []

# Define a function to calculate the link lengths based on the given equations
def calculate_link_lengths(x, y, z, a, b, c):
    BR = math.sqrt(((36*math.sqrt(3))+(95*math.cos(math.radians(150-7.5))) + x + (-95*math.cos(math.radians(150-7.5)))*(math.cos(math.radians(c))*math.cos(math.radians(b))) + (-95*math.sin(math.radians(150-7.5)))*(-math.sin(math.radians(c))*math.cos(math.radians(a)) + math.cos(math.radians(c))*math.sin(math.radians(b))*math.sin(math.radians(a))))**2 + 
                    (72 + (95*math.sin(math.radians(150-7.5))) + y + (-95*math.cos(math.radians(150-7.5)))*(math.sin(math.radians(c))*math.cos(math.radians(b))) + (-95*math.sin(math.radians(150-7.5)))*(math.cos(math.radians(c))*math.cos(math.radians(a)) + math.sin(math.radians(c))*math.sin(math.radians(b))*math.sin(math.radians(a))))**2 + 
                    (148 + 0 + z + (-95*math.cos(math.radians(150-7.5)))*(-math.sin(math.radians(b))) + (-95*math.sin(math.radians(150-7.5)))*(math.cos(math.radians(b))*math.sin(math.radians(a))))**2) - math.sqrt(148**2 + (36*math.sqrt(3))**2 + 72**2)

    BL = math.sqrt(((-36*math.sqrt(3)) + (95*math.cos(math.radians(30+7.5))) + x + (-95*math.cos(math.radians(30+7.5)))*(math.cos(math.radians(c))*math.cos(math.radians(b))) + (-95*math.sin(math.radians(30+7.5)))*(-math.sin(math.radians(c))*math.cos(math.radians(a)) + math.cos(math.radians(c))*math.sin(math.radians(b))*math.sin(math.radians(a))))**2 + 
                    (72 + (95*math.sin(math.radians(30+7.5))) + y + (-95*math.cos(math.radians(30+7.5)))*(math.sin(math.radians(c))*math.cos(math.radians(b))) + (-95*math.sin(math.radians(30+7.5)))*(math.cos(math.radians(c))*math.cos(math.radians(a)) + math.sin(math.radians(c))*math.sin(math.radians(b))*math.sin(math.radians(a))))**2 + 
                    (148 + 0 + z + (-95*math.cos(math.radians(30+7.5)))*(-math.sin(math.radians(b))) + (-95*math.sin(math.radians(30+7.5)))*(math.cos(math.radians(b))*math.sin(math.radians(a))))**2) - math.sqrt(148**2 + (36*math.sqrt(3))**2 + 72**2)

    MR = math.sqrt(((-18*math.sqrt(3)) + (95*math.cos(math.radians(150+7.5))) + x + (-95*math.cos(math.radians(150+7.5)))*(math.cos(math.radians(c))*math.cos(math.radians(b))) + (-95*math.sin(math.radians(150+7.5)))*(-math.sin(math.radians(c))*math.cos(math.radians(a)) + math.cos(math.radians(c))*math.sin(math.radians(b))*math.sin(math.radians(a))))**2 + 
                    (-90 + (95*math.sin(math.radians(150+7.5))) + y + (-95*math.cos(math.radians(150+7.5)))*(math.sin(math.radians(c))*math.cos(math.radians(b))) + (-95*math.sin(math.radians(150+7.5)))*(math.cos(math.radians(c))*math.cos(math.radians(a)) + math.sin(math.radians(c))*math.sin(math.radians(b))*math.sin(math.radians(a))))**2 + 
                    (148 + 0 + z + (-95*math.cos(math.radians(150+7.5)))*(-math.sin(math.radians(b))) + (-95*math.sin(math.radians(150+7.5)))*(math.cos(math.radians(b))*math.sin(math.radians(a))))**2) - math.sqrt(148**2 + (36*math.sqrt(3))**2 + 72**2)

    ML = math.sqrt(((18*math.sqrt(3)) + (95*math.cos(math.radians(30-7.5))) + x + (-95*math.cos(math.radians(30-7.5)))*(math.cos(math.radians(c))*math.cos(math.radians(b))) + (-95*math.sin(math.radians(30-7.5)))*(-math.sin(math.radians(c))*math.cos(math.radians(a)) + math.cos(math.radians(c))*math.sin(math.radians(b))*math.sin(math.radians(a))))**2 + 
                    (-90 + (95*math.sin(math.radians(30-7.5))) + y + (-95*math.cos(math.radians(30-7.5)))*(math.sin(math.radians(c))*math.cos(math.radians(b))) + (-95*math.sin(math.radians(30-7.5)))*(math.cos(math.radians(c))*math.cos(math.radians(a)) + math.sin(math.radians(c))*math.sin(math.radians(b))*math.sin(math.radians(a))))**2 + 
                    (148 + 0 + z + (-95*math.cos(math.radians(30-7.5)))*(-math.sin(math.radians(b))) + (-95*math.sin(math.radians(30-7.5)))*(math.cos(math.radians(b))*math.sin(math.radians(a))))**2) - math.sqrt(148**2 + (36*math.sqrt(3))**2 + 72**2)

    FR = math.sqrt(((-54*math.sqrt(3)) + (95*math.cos(math.radians(270-7.5))) + x + (-95*math.cos(math.radians(270-7.5)))*(math.cos(math.radians(c))*math.cos(math.radians(b))) + (-95*math.sin(math.radians(270-7.5)))*(-math.sin(math.radians(c))*math.cos(math.radians(a)) + math.cos(math.radians(c))*math.sin(math.radians(b))*math.sin(math.radians(a))))**2 + 
                    (18 + (95*math.sin(math.radians(270-7.5))) + y + (-95*math.cos(math.radians(270-7.5)))*(math.sin(math.radians(c))*math.cos(math.radians(b))) + (-95*math.sin(math.radians(270-7.5)))*(math.cos(math.radians(c))*math.cos(math.radians(a)) + math.sin(math.radians(c))*math.sin(math.radians(b))*math.sin(math.radians(a))))**2 + 
                    (148 + 0 + z + (-95*math.cos(math.radians(270-7.5)))*(-math.sin(math.radians(b))) + (-95*math.sin(math.radians(270-7.5)))*(math.cos(math.radians(b))*math.sin(math.radians(a))))**2) - math.sqrt(148**2 + (36*math.sqrt(3))**2 + 72**2)

    FL = math.sqrt(((54*math.sqrt(3)) + (95*math.cos(math.radians(7.5-90))) + x + (-95*math.cos(math.radians(7.5-90)))*(math.cos(math.radians(c))*math.cos(math.radians(b))) + (-95*math.sin(math.radians(7.5-90)))*(-math.sin(math.radians(c))*math.cos(math.radians(a)) + math.cos(math.radians(c))*math.sin(math.radians(b))*math.sin(math.radians(a))))**2 + 
                    (18 + (95*math.sin(math.radians(7.5-90))) + y + (-95*math.cos(math.radians(7.5-90)))*(math.sin(math.radians(c))*math.cos(math.radians(b))) + (-95*math.sin(math.radians(7.5-90)))*(math.cos(math.radians(c))*math.cos(math.radians(a)) + math.sin(math.radians(c))*math.sin(math.radians(b))*math.sin(math.radians(a))))**2 + 
                    (148 + 0 + z + (-95*math.cos(math.radians(7.5-90)))*(-math.sin(math.radians(b))) + (-95*math.sin(math.radians(7.5-90)))*(math.cos(math.radians(b))*math.sin(math.radians(a))))**2) - math.sqrt(148**2 + (36*math.sqrt(3))**2 + 72**2)

    return BR, BL, MR, ML, FR, FL

# Iterate over all combinations of x, y, and z values
for d in range(numberofdata_p):
    x = random.uniform(0,300)
    y = random.uniform(0,300)
    z = random.uniform(0,300)
    # Generate random values for a, b, and c within desired ranges
    a = random.uniform(0, 360)
    b = random.uniform(0, 360)
    c = random.uniform(0, 360)

    # Calculate link lengths for the given x, y, z, a, b, and c
    link_lengths = calculate_link_lengths(x, y, z, a, b, c)

    # Append the input values (x, y, z) and link lengths to the dataset
    dataset.append([x, y, z] + [a,b,c] + list(link_lengths))

# Define the CSV file name
csv_file = 'stewart_platform_dataset.csv'

# Write the dataset to a CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['x', 'y', 'z','a','b','c','BR', 'BL', 'MR', 'ML', 'FR', 'FL'])
    # Write data rows
    writer.writerows(dataset)

print(f'Dataset saved to {csv_file}')
