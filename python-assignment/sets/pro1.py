
cc = set(input("Add students to Coding Club: ").split())
rc = set(input("Add students to Robotics Club: ").split())

print("Display Coding Club Students:", cc)
print("Display Robotics Club Students:", rc)
print("Students in Both Clubs:", cc.intersection(rc))
print("Students Only in Coding Club:",cc.difference(rc))
print("Students Only in Robotics Club:",rc.difference(cc))
print("All Unique Club Members:",cc.union(rc))
print(len(cc.union(rc)))