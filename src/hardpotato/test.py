import potentiostat

model = 'chi920d'
path = r"C:\Users\parasita\Downloads\chi920d\chi920d.exe"
folder = 'data'

#print(potentiostat.models_available)
info = potentiostat.Info(model)
info.specifications()


potentiostat.Setup(model, path, folder)
secm = potentiostat.SECM()
secm.MOVE('step', z=-150)
secm.PAC(E1=0.4, qt = 30, sens=1e-9)
secm.RUN()
# stepx = 1
# stepy = 5
# sizex= 3
# sizey= 15
# currentx = 0
# currenty = 0
# for x in range (0,sizex,stepx):
#     for y in range (0, sizey, stepy):
#         dx = x - currentx
#         currentx = x
#         dy = y - currenty
#         currenty = y
#         pacFileName = f'PAC_x{x}_y{y}'
#         secm.MOVE('step', x=dx, y=dy, z=-150)
#         # secm.CV(sr=0.5)
#         secm.PAC(E2=-0.4, sens2=0.3, resistance=100, fileName=pacFileName)
#         secm.RUN()
#         cvFileName = f'CV_x{x}_y{y}'
#         secm.CV(fileName=cvFileName)
#         secm.RUN()
#cv.bipot()


# lsv = potentiostat.LSV(sr=0.5)
# lsv.bipot()
# lsv.run()

# ca = potentiostat.CA()
# ca.bipot()
# ca.run()

#ocp = potentiostat.OCP()
#ocp.run()
