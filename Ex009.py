measures = float(input('Write a value for distance in meters: '))
km = measures / 1000
hm = measures / 100
dam = measures /10
dm = measures * 10
cm = measures * 100
mm = measures * 1000
print('The measurement of {}m corresponds to \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(measures, km, hm, dam, dm, cm, mm))