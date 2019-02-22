import lxc

# generic container class
class Container(object):

	def __init__(self):
		pass

	# get available container
	def get(self):
		cont = None
		for cont_obj in lxc.list_containers(as_object=True):
			if cont_obj.name == 'new-cont':
				cont = cont_obj

		assert cont.name == 'new-cont'

		return cont

	# clone container
	def clone(self, cont):
		print "cloning container for test..."

		clone = cont.clone('tmp-cont', flags=lxc.LXC_CLONE_SNAPSHOT)

		assert clone.name == 'tmp-cont'

		return clone

	# run command
	def cmd(self, cont, command):
		
		fd = open('output', 'w')
		fd_perf = open('perf_out', 'w')

		print "starting container.."
		cont.start()

		cont.attach_wait(lxc.attach_run_command, command.split(' '),
			stdout=fd, stderr=fd_perf)

		fd.close()
		fd_perf.close()
		
		print "stopping container.."
		cont.stop()
