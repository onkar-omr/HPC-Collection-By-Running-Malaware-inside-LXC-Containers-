# Hardware-Based-Malware-Detection
Python script which collects Hardware Performance Counters in a text file by executing malware inside LXC containers.

############
This work is part of my MS Thesis for Analyzing Hardware Based Malware Detectors using Machine Learning Techniques 

############
The Repo contains 3 python scripts named: 
1. Container
2. DataParser
3. HPC_data_collector

Important note: Please make sure your internet is disconnected before running any malware on your system

1. Container
The Container script is used to create a container, clone it and run the command inside the container. The main objective is to provide an isolated environment to run the malwares so that they do not infect the system.

2. DataParser
It parses the perf file to create csv. Please make sure you change the path of the directories to the path where you want the output files to be on your computer. These paths are mentioned at the start of the code. Please change the res_dir as per your malware type. res_dir is the path where the output is going to be saved.

3. HPC_data_collector
This is the file that you actually have to run to collect HPC's. It imports the Container and DataParser files mentioned above. This file will automatically invoke the two files. Please make sure you change the path of the directories to the path where the application/malware to be run are present on your computer. You change the file_list to the file containing the list of applications/malware to be run. This file to create a container (imported from Containers.py) clone it, and run the application inside the container and will use the DataParser to parse the perf data in to csv.
