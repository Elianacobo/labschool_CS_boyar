# Step 1: input the mph of the vehicle.
import math
detect = float(input())
workersPresent = bool(input())
    
# Step 2: speed limits (limit 25 MPH)
limit = "25"

speedingA = "limit+12"
speedingB = "limit+16"
speedingC = "limit+20"
speedingD = "limit+30"
speedingE = "limit+40"

fineA = "$60"
fineWorkersA = "$120"
fineB = "$80"
fineWorkersB = "$160"
fineC = "$140"
fineWorkersC = "$280"
fineD = "$270"
fineWorkersD = "$540"
fineE = "$500"
fineWorkersE = "$1,000"

if detect>=40+25:
    if workersPresent==True:
        print(f"You are driving {detect} MPH, so you have to pay {fineWorkersE}. You have 30 days to pay it.")
    else:
        print(f"You are driving {detect} MPH, so you have to pay {fineE}. You have 30 days to pay it.")
    
elif detect>=30+25: 
    if workersPresent==True:
        print(f"You are driving {detect} MPH, so you have to pay {fineWorkersD}. You have 30 days to pay it.")
    else:
        print(f"You are driving {detect} MPH, so you have to pay {fineD}. You have 30 days to pay it.")
elif detect>=20+25:
    if workersPresent==True:
        print(f"You are driving {detect} MPH, so you have to pay {fineWorkersC}. You have 30 days to pay it.")
    else:
        print(f"You are driving {detect} MPH, so you have to pay {fineC}. You have 30 days to pay it.")
elif detect>=16+25:
    if workersPresent==True:
        print(f"You are driving {detect} MPH, so you have to pay {fineWorkersB}. You have 30 days to pay it.")
    else:
        print(f"You are driving {detect} MPH, so you have to pay {fineB}. You have 30 days to pay it.")
elif detect>=12+25:
    if workersPresent==True:
        print(f"You are driving {detect} MPH, so you have to pay {fineWorkersA}. You have 30 days to pay it.")
    else:
        print(f"You are driving {detect} MPH, so you have to pay {fineA}. You have 30 days to pay it.")
else:
    print("You are not speeding and you don't have to pay anything.")
    
    
    
    