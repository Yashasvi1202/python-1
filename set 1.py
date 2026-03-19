s1={'maths', 'physics' ,'chemistry'}
s2={'maths', 'physics' ,'biology'}
print("student 1 subject: ", s1)
print("student 2 subject: ", s2)
#find common subjects
common= s1 & s2
print("1. common subjects:-", common)

#subject taken by only first
only1= s1-s2
print("2. subjects taken by only one: ", only1)

#subject taken by only second
only2= s2 - s1
print("2. subjects taken by only second: ", only2)

#unique subjects
unique= s1|s2
print("All unique subjects are: ", unique)
