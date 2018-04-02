import os
import re
import matplotlib as plt


rootPath='/Users/xuxiangzhe/Library/Mobile Documents/com~apple~CloudDocs/Learning/Computer Science/CA/lab1/'
def getFiles(filePath):
		files = os.listdir(filePath)
		#config
		l1isz=[]
		l1dsz=[]
		l2sz=[]
		clk=[]
		blksz=[]
		#result
		instNum=[]
		tick=[]
		l1iMissRate=[]
		l1dMissRate=[]
		l2MissRate=[]
		time=[]
		with open(os.path.join(rootPath,'write.csv'),'w') as w:
			

			for fi in files:
					fi_d = os.path.join(filePath,fi)
					if os.path.isdir(fi_d):
						if re.search(r'(.*)l1i(.*)',fi_d,re.I):
							print fi
							#every single config
							with open(os.path.join(fi_d,'para.txt'),'r') as f:
								content=f.read()
								pattern=re.compile(r'([^-=]*=[^-\s\D]*)')
								params=pattern.findall(content)
								#creat dict
								dict1={}
								for para in params:
									tmp=para.split(r'=')
									dict1[tmp[0]]=tmp[1]
								print dict1
								#add to list
								l1isz.append(int(dict1.get('l1isz') or '64'))
							print l1isz
							with open(os.path.join(fi_d,'stats.txt'),'r') as f:
								dict2={}
								content=f.read()
								tmp=re.compile(r'sim_insts[\s]*([^\s]*)').search(content)
								if tmp: 
									# dict2['sim_insts']=tmp.group(1)
									instNum.append(int(tmp.group(1)))

								tmp=re.compile(r'final_tick[\s]*([^\s]*)').search(content)
								if tmp: 
									tick.append(int(tmp.group(1)))
								
								tmp=re.compile(r'system.cpu.icache.overall_miss_rate::total[\s]*([^\s]*)').search(content)
								if tmp: 
									l1iMissRate.append(float(tmp.group(1)))
								
								tmp=re.compile(r'system.cpu.dcache.overall_miss_rate::total[\s]*([^\s]*)').search(content)
								if tmp: 
									l1dMissRate.append(float(tmp.group(1)))

								tmp=re.compile(r'system.l2cache.overall_miss_rate::total[\s]*([^\s]*)').search(content)
								if tmp: 
									l2MissRate.append(float(tmp.group(1)))
								
									
								

								

						else:
					 	 	#getFiles(fi_d)
							pass
							
							 
					else:
							# with open(os.path.join(filePath,fi),'r') as f:
							# 	content=f.read()
							# 	search=re.finditer( r'--(\w*)=(\D?)(\d\w+)',content,re.I)
							# 	for match in search:
							# 		print "in file ",os.path.join(filePath,fi)," ",match.group(1)," *=* ",match.group(3)
							pass
		drawDict={}
		for i in range(0,len(l1isz)):
			drawDict[l1isz[i]]=l1iMissRate[i]

		toDraw=[(key,drawDict[key]) for key in sorted(drawDict.keys()) ]
		x=list(map(lambda (x,y):x,toDraw))
		y=list(map(lambda (x,y):y,toDraw))
		print x
		print y

		plt.plot(x,y)
		plt.show()


				


getFiles(os.path.join(rootPath,'ret'))

