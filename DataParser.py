import pandas as pd
import re
from collections import defaultdict

trojan_dir = "results/malware/trojan/"
worm_dir = "results/malware/worm/"
virus_dir = "results/malware/virus/"
rootkit_dir = "results/malware/rootkit/"
backdoor_dir = "results/malware/backdoor/"
spec_dir = "results/benign/spec/"
mibench_dir = "results/benign/mibench/"

########################
res_dir = worm_dir
##################
""" Parse perf file to create csv """
class Parser(object):

	def __init__(self):
		pass

	def parse(self, num):
		fd_perf = open('perf_out', 'r')
		#fd_perf = open('spec_result/%s'%(num), 'r')
		
		d_data = defaultdict(list)
		
		search = re.findall(r'\s+[\d.].+,(.+),,([^,]+),.+', fd_perf.read())

		for val,event in search:
			if val == '<not counted>':
				pass
			else:
				d_data[event].append(val)

		df = pd.DataFrame(d_data.values(), index=d_data.keys())
		df = df.transpose()
		
		# For malware (stores as numbers)
		df.to_csv('%s%d'%(res_dir,num), index=None)

		# For benign applications (stores as file name)
		#df.to_csv('%s%s'%(res_dir,num), index=None)
		fd_perf.close()
