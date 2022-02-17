infile = open("WorldSeriesWinners.txt", "r")
infile2 = open("WorldSeriesWinners.txt", "r")

team = {}
year = {}

for t in infile:
    t = t.strip()
    if t in team:
        team[t] = team[t] + 1
    else:
        team[t] = 1

# print(team)

x = 1902

for y in infile2:
    y = y.strip()
    if x == 1903 or x == 1993:
        x += 2
        year[x] = y
    else:
        x += 1
        year[x] = y

# print(year)

specific_year = int(input("Please enter year between 1903 and 2008     "))


if specific_year == 1904 or specific_year == 1994:
    print("There was not a World Series winner that year :(")


else:
    n = specific_year
    x = year[n]
    t = team[t]
    print(
        "The World Series winner in "
        + str(n)
        + ","
        + "was the "
        + x
        + ". They've won the World Series "
        + str(t)
        + " time(s)!",
    )
