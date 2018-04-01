import os
import re
rootPath='/Users/xuxiangzhe/Library/Mobile Documents/com~apple~CloudDocs/Learning/Computer Science/CA/lab1/'
def getFiles(filePath):
		files = os.listdir(filePath)
		l1isz=[]
		l1dsz=[]
		l2sz=[]
		clk=[]
		blksz=[]
		with open(os.path.join(rootPath,'write.csv'),'w') as w:
			

			for fi in files:
					fi_d = os.path.join(filePath,fi)
					if os.path.isdir(fi_d):
						if re.search(r'result(.*)',fi_d,re.I):
							print fi
							#every single config
							with open(os.path.join(fi_d,'para.txt'),'r') as f:
								content=f.read()
								pattern=re.compile(r'([^-=]*=[^-\s]*)')
								params=pattern.findall(content)
								#creat dict
								dict1={}
								for para in params:
									tmp=para.split(r'=')
									dict1[tmp[0]]=tmp[1]
							with open(os.path.join(fi_d,'stats.txt'),'r') as f:
								dict2={}
								content=f.read()
								tmp=re.compile(r'sim_insts[\s]*([^\s]*)').search(content)
								if tmp:
									print 'here'
									dict2['sim_insts']=tmp.group(1)
								print dict2

								

						else:
					 	 	getFiles(fi_d)
							
							 
					else:
							with open(os.path.join(filePath,fi),'r') as f:
								content=f.read()
								search=re.finditer( r'--(\w*)=(\D?)(\d\w+)',content,re.I)
								for match in search:
									print "in file ",os.path.join(filePath,fi)," ",match.group(1)," *=* ",match.group(3)


getFiles(os.path.join(rootPath,'ret'))

