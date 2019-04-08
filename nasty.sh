#This is the execution script for the entire project

#First is the sourcing module
#Then comes the the analyzer module, that creates and generates tuples
#The third is the formatter and the JSON upload module

#The first one is threaded, and needs to work alone.
#The third too would need to do the same.
#The analyzer might not need to be threaded.
#But it could be threaded as well
#It is a work in progress

#The individual drivers should be fired seperately

#After first check, only if time difference arises, should the processes be fired again.

while true; do
	clear
	echo "Starting execution"
	python3 ./python/sourcing
	ctr=$?
	sleep 3s
	clear
	if [ $ctr = 0 ]; then
		echo "Sourcing completed"
		echo "Starting anlysis module"
		java -mx8g -cp "./factserver.jar:../corenlp/*" factserver.Driver
		python3 test.py
		ctr=$?
		clear
		if [ $ctr = 0 ]; then
			echo 
	elif [ $ctr = 1 ]; then
		echo "Program error detected. Exiting execution"
		exit
	else
		echo "All satisfied."
		echo "Pausing system for 30 minutes..."
		sleep 30m
	fi

done

