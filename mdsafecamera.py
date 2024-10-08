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
        print(f"You have to pay {fineWorkersE}.")
    else:
        print(f"You have to pay {fineE}.")
    
elif detect>=30+25: 
    if workersPresent==True:
        print(f"You have to pay {fineWorkersD}.")
    else:
        print(f"You have to pay {fineD}.")
elif detect>=20+25:
    if workersPresent==True:
        print(f"You have to pay {fineWorkersC}.")
    else:
        print(f"You have to pay {fineC}.")
elif detect>=16+25:
    if workersPresent==True:
        print(f"You have to pay {fineWorkersB}.")
    else:
        print(f"You have to pay {fineB}.")
elif detect>=12+25:
    if workersPresent==True:
        print(f"You have to pay {fineWorkersA}.")
    else:
        print(f"You have to pay {fineA}.")
else:
    print("You are not speeding and you don't have to pay anything.")
    
    
    
    