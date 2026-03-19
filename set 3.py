day1={1,2,3,4,5}
day2={4,5,6,7,8}
print("Day 1 visitors are: ", day1)
print("Day 2 visitors are: ", day2)

bothdays=day1 & day2
print("Visitors of both days are: ", bothdays)

onlyoneday=day1 ^day2
print("Visitors of only one day are: ", onlyoneday)

unique=day1 | day2
print("Unique visitors of both days are: ", unique)
