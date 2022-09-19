import random

alt_ma = 0
alt_me = 0
alt = 0
repetidor = 0

while repetidor < 3:
    alt = random.randint(1, 102)
    print(alt)
    if repetidor == 0:
        alt_ma = alt
        alt_me = alt
    elif alt == 1:
        alt_ma = alt
        alt_me = alt
    else:
        if alt > alt_ma:
            alt_ma = alt
        if alt < alt_me:
            alt_me = alt
    repetidor += 1

print(f"A maior altura foi de {alt_ma}m")
print(f"A menor altura foi de {alt_me}m")   
        