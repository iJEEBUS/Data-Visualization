import numpy as np
import pandas as pd

data = pd.DataFrame (
    {"Major":["CS", "IS", "MBI", "STAT", "OTHER", "CS"],
    "Happiness":[10,10,10,10,2,10]},
    index=["Jon", "Jill", "Javhah", "Jessica", "Joe", "Jack"]
    )

print("\nCounts of each value in the pandas DataFrame: \n %s"
 % (data["Major"].value_counts()))

print("\nNumber of data points in the pandas DataFrame:\n %s" 
	% (len(data)))

print("\nDescription of the pandas DataFrame:\n %s" 
	% (data.describe()))

print("\nPrinting of the pandas DataFrame:\n %s" 
	% (data))

print("\nAccessing the Major for the second record:\n %s" 
	% (data["Major"][1]))