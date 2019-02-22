from Container import *
from DataParser import *
import socket
import sys

events = ['instructions,bus-cycles,branch-instructions,branch-misses,cache-misses,cache-references,node-loads,node-stores',
		'L1-dcache-load-misses,L1-dcache-loads,L1-dcache-stores,L1-icache-load-misses,LLC-load-misses,LLC-loads,branch-loads,iTLB-load-misses']

troj_dir = "/home/ubuntu/malware_seperated/trojan/"
virus_dir = "/home/ubuntu/malware_seperated/virus/"
backdoor_dir = "/home/ubuntu/malware_seperated/backdoor/"
rootkit_dir = "/home/ubuntu/malware_seperated/rootkit/"
worm_dir = "/home/ubuntu/malware_seperated/worm/"
mibench_dir = "/home/research/work/mibench/scripts/"
spec_dir = "/home/research/work/spec/scripts/"

#########################
file_list = 'worm_list'
file_dir = worm_dir
#########################

def is_net_on():
	try:
		host = socket.gethostbyname('www.google.com')
		s = socket.create_connection((host, 80), 2)
		return True
	except:
		return False


if __name__ == "__main__":

	if is_net_on():
		print "****************************"
		print "Warning : Turn off the Internet!!"
		print "****************************"
		print "exiting..."
		sys.exit()

	# get list of trojans
	fd = open('conf/%s'%(file_list), 'r')
	l_malware = fd.read().split('\n')
	fd.close()
	
	cobj = Container()
	cont = cobj.get()
	
	for num, name in enumerate(l_malware):
		print "%d -> %s" %(num, name)
		clone = cobj.clone(cont)

		cobj.cmd(clone, "chmod 777 %s%s" % (file_dir, name))
		cobj.cmd(clone, "timeout 6s perf stat -I 10 -e %s -x, %s%s" % (events[1], file_dir, name))
		
		# For SPEC benchmarks
		#cobj.cmd(clone, "perf stat -I 10 -e %s -x, runspec --size=test --noreportable --tune=base --iterations=1 %s" % (events[1], name))
		#cobj.cmd(clone, 'runspec')
		clone.destroy()

		p = Parser()
		p.parse(num)
		#p.parse(name.replace(".","_"))
		#break