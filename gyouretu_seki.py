import pandas as pd
import numpy as np
import random as rd
import sys
def main():
	df=[]
	S=1
	k=int(input("k="))
	for i in range(k):
		a=[]
		ix=[]
		cs=[]
		for j in range(3):
			a1=[]
			for l in range(3):
				print("a[%d][%d][%d]=" % (i,j,l),end="")
				a1.append(input())
				if a1[l]=="":
					a1[l]=0
				if a1[l]=="q":
					sys.exit()
				if a1[l]=="r":
					a1[l]=rd.randint(0,10)
				a1[l]=int(a1[l])
			a.append(a1)
			ix.append("row"+str(j+1))
			cs.append("col"+str(j+1))
		#print(a)
		df.append(pd.DataFrame(a,
		index=ix,
		columns=cs
		))
	for i in range(k):
		print(df[i])
		S=np.dot(S,df[i])
		print(S)
if __name__=="__main__":
	main()
