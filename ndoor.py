#! /usr/bin/env python3
# -*- coding=utf-8 -*-
#================================================================
#
# Project       : n-door problem
# Description   : caculate the probality of n-door problem by simulation
# Usage         : python3 ndoor.py --help
# Author        : chen.minjun
# Time		    : 2023-03-15
#
#================================================================

import re
import sys
import os
import argparse
import random
import time
from tqdm import tqdm,trange
import matplotlib.pyplot as plt
import h5py
import pdb

bindir = os.path.abspath(os.path.dirname(__file__))
__author__='chen.minjun'
__mail__= 'chen.minjun@genecast.com.cn'
__doc__= 'n-door problem'
random.seed(100)


def Expect_ndoor(ndoor:int):
	#第一次选择门后有财富，更改选择为零
	no_change=1/ndoor
	#第一次选择门后无财富，不更改选择为零 
	change=((ndoor-1)/ndoor)*(1/(ndoor-2))
	return [change,no_change]
	
def Simulate_ndoor(ndoor:int,ntrial:int):
	doors=list(range(0,ndoor))
	count_change,count_nochange=0,0
	time_start=time.time()
	for i in trange(ntrial):
		answer=random.choice(doors)
		first=random.choice(doors)
		
		if first == answer: #第一次选择的门后有财富,更改无财富
			count_change+=0
			count_nochange+=1
		else: #第一次选择的门后无财富,不更改无财富，更改需再次判断
			count_nochange+=0 
			host_door=random.choice([i for i in doors if i not in [answer,first]])  #去除财富门和第一次选择门，主持人进行选择
			second=random.choice([i for i in doors if i not in [host_door,first]])     #扣除第一次选择和主持人选择
			if second == answer: #更改后有财富，更改才有效
				count_change+=1
	#pdb.set_trace()
	treasure_change_freq,treasure_nochange_freq='{:.4f}'.format(count_change/ntrial),'{:.4f}'.format(count_nochange/ntrial)
	time_end=time.time()
	time_use = '{:.2f}'.format(time_end-time_start)
	return treasure_change_freq,treasure_nochange_freq,time_use

def database(ndoor:int,ntrial_list):
	dataset=[["Ndoors","Ntrials","probability of change","probability of no-change","runtime"]]
	for num in ntrial_list:
		prob_change,prob_nochange,timeuse=Simulate_ndoor(ndoor,num)
		dataset.append([str(i) for i in [ndoor,num,prob_change,prob_nochange,timeuse]])
		#dataset.append([gate,num,prob_change,prob_nochange,timeuse])
	return dataset
				
def plot(xlabel,ylabel,xdata,ylist,out):
	x=xdata
	for key in ylist:
		y=ylist[key]
		plt.plot(x,y,label=key,marker='.')
		#plt.plot(x,y,marker='.-r')
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.legend(loc='upper right')
	plt.savefig(out)
	plt.close()


def main():
	parser=argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='author:\t{0}\nmail:\t{1}'.format(__author__,__mail__))
	parser.add_argument("-n",dest="ndoor",help="number of doors",required=True,type=int)
	parser.add_argument("-t",dest="ntrial",help="number of trials. ",required=True,type=int)
	parser.add_argument("-fa",dest="figurea",help="Plot:Y=runtime, X=the number of trials",required=False,type=str)
	parser.add_argument("-fb",dest="figureb",help="Plot:the divergence = |模拟答案-理论值| and the number of trials",required=False,type=str)
	parser.add_argument("-o",dest="outfile",help="gates(3,5,10,30) and trials(10^(3,4,5,6,7)), hdf5 files are generated with changing/no-changing probality",required=False)	
	args = parser.parse_args()

	ntrial_list=[1000,10000,100000,1000000]
	#通过实验次数重复来计算ndoor问题的概率
	print("\nNdoor:{} and trials:{}".format(args.ndoor,args.ntrial))
	treasure_change_freq,treasure_nochange_freq,time_use=Simulate_ndoor(args.ndoor,args.ntrial)
	print("The frequency of changing/no-changing the first choice is {}/{} and use time {}s.\n".format(treasure_change_freq,treasure_nochange_freq,time_use))
	
	#作图数据，得到不同实验次数下的概率和时间
	if(args.figurea) or (args.figureb):
		xdata,ylista,ylistb=ntrial_list,{"Time":[]},{"Prob of change":[],"Prob of no-change":[]}
		for trial in tqdm(xdata):
			prob1,prob2,time=Simulate_ndoor(args.ndoor,trial)
			#print(args.ndoor,trial,prob1,prob2,time)
			ylista["Time"].append(float(time))
			ylistb["Prob of change"].append(abs(Expect_ndoor(args.ndoor)[0]-float(prob1)))
			ylistb["Prob of no-change"].append(abs(Expect_ndoor(args.ndoor)[1]-float(prob2)))
	#图1：通过实验次数重复来计算ndoor问题的运行时间
	if(args.figurea):
		plot("the number of trials(ndoor="+str(args.ndoor)+")","runtime(s)",xdata,ylista,args.figurea)
	#图2：通过实验次数重复来计算ndoor问题的与理论值的差别
	if(args.figureb):
		plot("the number of trials(ndoor="+str(args.ndoor)+")","divergence",xdata,ylistb,args.figureb)
	

	#计算不同实验次数的运行时间并存入hdf5文件
	if(args.outfile):
		out = h5py.File(args.outfile,'w')
		for gate in tqdm([3,5,10,30]):
			h5_data=database(gate,ntrial_list)
			out.create_dataset("ndoor:"+str(gate),data=h5_data)
		out.close()


if __name__ == "__main__":
	main()