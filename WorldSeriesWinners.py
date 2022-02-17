infile = open("WorldSeriesWinners.txt", "r")


team = {}
year = {}


for t in infile:
    t = t.strip()
    if t in team:
        team[t] = team[t] + 1
    else:
        team[t] = 1


for n in range(1903, 2009):
    if n != 1904 or 1994:
        for line in infile:
            t = line
        year[n] = t
# t + 1


# print(team)
print(year)
