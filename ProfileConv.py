import pandas as pd                     # Pandas is a very usefull library alowing this script to be super short
df           = pd.read_fwf("input.dat") # Read your inputfile into a dataframe
foilName     = df.columns[0]            # extract the foil Name
openScadStr  = foilName + "Points = ["  # start a string with the OpenScad command
for i, r in df.iterrows():              # loop on all the lines
    openScadStr += ("[%.3f, %.3f], " % (r[0]*1000,r[1]*1000))  # append each line on the string
openScadStr += "];"                     # Finalise the string for the command to be complete
print(openScadStr)                      # Display the string
