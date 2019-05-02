file=open("answer.txt")
lis=[]
for line in file:
	s=""
	for word in line:
		if word==".":
			lis.append((int(s),line))
			break
		else:
			s=s+word	
file.close()

lis.sort(key=lambda x:x[0])


newfile=open("answer2.txt",'w+')

for i in lis:
	newfile.write(str(i[1]))
newfile.close()