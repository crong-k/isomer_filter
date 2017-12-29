f = open('C6H8O4.sdf')
fw = open('C6H8O4_conv.sdf','w')
for i in f :
	if len(i.strip().split()) ==  6 :
		i = i.strip()
		i = ' '+i+'\n'
	fw.write(i)
fw.close()
print 'END'
