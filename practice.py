import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#data = pd.read_csv("./eva.csv", names=["Number", "Country", "Crew", "Vehicle", "Date", "Duration", "Purpose"])


data = pd.read_csv("./Meteorite_Landings.csv").dropna(axis=0, how='any')

years = {}

for year in data["year"]:
	year = year.split(" ")[0].split("/")[2] # extracts only the years
	if year in years:
		years[year] += 1
	else:
		years[year] = 1

years_list = []
years_totals_list = []

for x in years:
	years_list.append(int(x))
	years_totals_list.append(years[x])


ind = np.arange(len(years_totals_list))

fig, ax = plt.subplots()

rects = ax.bar(ind, years_totals_list, width=0.35)

ax.set_ylabel("No. of Meteorites discovered")
ax.set_xlabel("Year of Observation")
ax.set_xticks(ind)
# ax.set_xticks(years_list)

#plt.show()


# what is the difference between the most recent and first sightings?

min_year = 9999999
max_year = 0
for year in years_list:
	if year > max_year:
		max_year = year
	elif year < min_year:
		min_year = year

# sum fifty data points
years_totals_list_copy = list(years_totals_list)
summed_data = []
summed_fifty = 0
outer_counter = 0
inner_counter = 0

interval = 30

while outer_counter < (len(years_totals_list_copy)/interval):
	summed_fifty = 0
	inner_counter = 0
	while inner_counter < interval:
		try:
			summed_fifty += years_totals_list_copy.pop()
			inner_counter += 1
		except Exception:
			break
		
	summed_data.append(summed_fifty)
	outer_counter += 1

for x in summed_data:
	print(x)
		






# plt.bar()

# for x in data:
# 	print(x)

# for x in data["mass (g)"]:
# 	print(x)

# data = data.dropna(axis=0, how='any')

# for x in data["year"]:
# 	mod = x.split(' ')
# 	mod = mod[0].split('/')
# 	mod = mod[-1]
# 	data["year"][x] = mod

# for x in data["year"]:
# 	print(x)

# plt.scatter(data["year"], data["mass (g)"])
# plt.xlabel('Year')
# plt.ylabel('Mass (g)')
# plt.title("Weight of Meteorite by their Year of Impact")
# plt.yticks(np.arange(min(data["mass (g)"]), max(data["mass (g)"])+1, 500))
# plt.show()
# data["mass (g)"].plot()
# plt.figure()


# countries = data["Country"][1:]

# usa = 0
# russia = 0

# for x in countries:
# 	if x.lower() == "usa":
# 		usa += 1
# 	elif x.lower() == "russia":
# 		russia += 1
# 	else:
# 		raise Exception



# print("USA: %s" % (usa))
# print("Russia: %s" % (russia))


