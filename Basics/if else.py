marklist = int(input('enter the student marks'))
if marklist <=34:
    print('FAILED')
elif marklist >=35 and marklist <=45:
    print('Grade E')
elif marklist >=46 and marklist <=55:
    print('Grade D')
elif marklist >=56 and marklist <=65:
    print('Grade C')
elif marklist >=66 and marklist <=75:
    print('Grade B')
elif marklist >=76 and marklist <=85:
    print('Grade A')
elif marklist >=86 and marklist <=100:
    print('Grade A+')
else:
    print('INVALID NUMBER')