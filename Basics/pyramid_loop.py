s=1

while s<5:
    star=""
    starcount=1
    while starcount<=s:
        star = star + " *"
        starcount= starcount+1
    s=s+1
    print(star)

s=3

while s>0:
    star=""
    starcount = s
    while starcount > 0:
        star = star + " *"
        starcount = starcount - 1

    s=s-1
    print(star)


