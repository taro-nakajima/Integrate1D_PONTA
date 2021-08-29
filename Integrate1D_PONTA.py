#Script for 1D integration
#usage:  python Integrate1D_v1_3_2.py [list file name] [output file name]
import math
import sys

version=2.0

args=sys.argv
if (len(args)<3):
	print("1D integration program for PONTA version %f"%(version))
	print("usage:  python Integrate1D_PONTA.py [list file name] [output file name]")
	sys.exit()

FH = open(args[1],"r")

print("Input filename : %s" % args[1])
print("Output filename : %s" % args[2])

temp = FH.readline()
array = temp.split()
skipline = int(array[0])
print("skipline : %d" % skipline)

temp = FH.readline()
array = temp.split()
Index_X = int(array[0])
print("index of x : %d" % Index_X)

temp = FH.readline()
array = temp.split()
Index_Fx = int(array[0])
print("index of F(x) : %d" % Index_Fx)

temp = FH.readline()
array = temp.split()
Index_Fx_er = int(array[0])
print("index of F(x)_err : %d" % Index_Fx_er)

temp = FH.readline()
array = temp.split()
Index_TH = int(array[0])
print("index of T or H : %d" % Index_TH)

temp = FH.readline()
array = temp.split()
RN = int(array[0])
print("Initial run number : %d" % RN)

temp = FH.readline()
array = temp.split()
RN_interval = int(array[0])
print("Run number interval: %d" % RN_interval)

temp = FH.readline()
array = temp.split()
NBK = int(array[0])
print("Num of points for background : %d" % NBK)

temp = FH.readline()
array = temp.split()
Xmin = float(array[0])
Xmax = float(array[1])
print("X range for integration : {0} to {1}".format(Xmin, Xmax))

print("----------------------------------------")

FH3 = open(args[2],"w")
FH3.write("#RN  IntegInt  Error  BG  TorH  THdeviation\n")

FHplt = open("fitcom.txt","w")


for line in FH:
	filename=line.strip()
	FH2 = open(filename,"r")
	print("File open : %s" % filename)

	if skipline > 0:
		for ii in range(skipline):
			dummy = FH2.readline()

	Xall=[]
	Yall=[]
	Yall_err=[]
	THall=[]

	Total_err=0.0
	BG = 0.0

	for line2 in FH2:
		if(line2.find("#")<0):
			array2 = (line2.strip()).split()
			X1=float(array2[Index_X])
			Y1=float(array2[Index_Fx])
			Yerr1=1.0
			TH1=float(array2[Index_TH])
			if(Index_Fx_er>0):
				Yerr1=float(array2[Index_Fx_er])
			else:
				if(Y1==0):
					Yerr1=1.0
				else:
					Yerr1=math.sqrt(Y1)
			if (Yerr1<0):
				Yerr1=0.0

			if (X1 >= Xmin) and (X1 <= Xmax):

				Xall = Xall + [X1]
				Yall = Yall + [Y1]
				Yall_err = Yall_err + [Yerr1]
				THall = THall + [TH1]


	if NBK > 0:
		C1 = 0.0
		C2 = 0.0
		for jj in range(NBK):
			C1 += Yall[jj]/float(NBK)
			C2 += Yall[len(Yall)-1-jj]/float(NBK)

		BG = 0.5*(C1+C2)*abs(float(Xall[len(Xall)-1]-Xall[0]))
	else:
		BG = 0.0

	IntegInt=0.0
	Total_err = 0.0
	for kk in range(len(Xall)-1):
		IntegInt += 0.5*(Yall[kk]+Yall[kk+1])*abs(Xall[kk+1]-Xall[kk])
		Total_err += (0.5*(Xall[kk+1]-Xall[kk]))**2.0*(Yall_err[kk]**2.0+Yall_err[kk+1]**2.0)

	meanTH=0.0
	for kk in range(len(Xall)):
		meanTH += THall[kk]/float(len(Xall))

	deviation=0.0
	for kk in range(len(Xall)):
		deviation += (THall[kk]-meanTH)**2.0/float(len(Xall))
	deviation=math.sqrt(deviation)

	IntegInt -= BG
	Total_err = math.sqrt(Total_err)

	FH3.write("{0}  {1}  {2}  {3}  {4}  {5}\n".format(RN,IntegInt,Total_err,BG,meanTH,deviation))

	print("Run number           : %d" % RN)
	print("Integrated Intensity : {0}" .format(IntegInt))
	print("Error                : {0}" .format(Total_err))
	print("Background           : {0}" .format(BG))
	print("Num of points        : %d" % len(Yall))
	print("Temperature or field        : %f" % meanTH)
	print("----------------------------------------")

	FHplt.write("fit [%f:%f] F(x) '%s' u 1:2:3 yerror via BG1,BG2,A,q,w\n"%(Xmin,Xmax,filename))
	FHplt.write("set out '%s.png'\n"%(filename))
	FHplt.write("plot '%s' u 1:2:3 w yer,F(x)\n\n"%(filename))

	FH2.close()
	RN+=RN_interval

FH.close()
FH3.close()
