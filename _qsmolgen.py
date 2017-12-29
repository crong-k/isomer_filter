import os
import time
import sys
import shutil
import commands

formula = sys.argv[1]

f = open('%s.log'%(formula))
comend = f.readline().strip()
f.close()
ff = open('%s.log'%(formula),'a')

start_t = time.time()
(exitstatus, outtext) = commands.getstatusoutput(comend)
result =  outtext.split()[-1]
end_t = time.time()
sec = end_t - start_t
line = ""
line = line +'Formula: '+formula +'//Number of isormer:'+result+'//Required time:'+str(sec) 
ff.write(line)
ff.close()
