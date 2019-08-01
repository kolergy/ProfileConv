# ProfileConv
## ProfileConv is a Super simple Python script to convert wing profile from .dat file to a series of points useable in OpenScad

If you are using OpenScad: https://www.openscad.org/ & want to design a wing you can use http://chaaawa.com/airfoils/  which has a little generator for the wing profile for OpenScad, but this is limited to the available profiles in the site.

Here is a little Python script to convert any profile you can find in the .dat format like that you can get from http://airfoiltools.com/ from a source dat file or soon a Selig dat file.

This is even more usefull if you need to modify the profile with the famous xFoil from Marc Drela: https://web.mit.edu/drela/Public/web/xfoil/, or if you use the more modern aircraft design tool xFlr5 http://www.xflr5.tech/xflr5.htm (which is still based on xFoil)

Here is the code:
```python
import pandas as pd                     # Pandas is a very usefull library alowing this script to be super short
df           = pd.read_fwf("input.dat") # Read your inputfile into a dataframe
foilName     = df.columns[0]            # extract the foil Name
openScadStr  = foilName + "Points = ["  # start a string with the OpenScad command
for i, r in df.iterrows():              # loop on all the lines
    openScadStr += ("[%.3f, %.3f], " % (r[0]*1000,r[1]*1000))  # append each line on the string
openScadStr += "];"                     # Finalise the string for the command to be complete
print(openScadStr)                      # Display the string
```
