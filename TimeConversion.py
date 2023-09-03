######################      12th May 2022   ######################

# Convert the time from 12 Hr format to 24 Hr format.

timev = "02:04:45 PM"
if timev[-2:]=="AM" and timev[:2]=="12":
    print(timev[2:-2])
elif timev[-2:]=="AM":
    print(timev[:-2])
elif timev[-2:]=="PM" and timev[:2] == "12":
    print(timev[:-2])
else:
    print(str(int(timev[:2])+12)+timev[2:8])