#This script is written for work with ubuntu
#Let it take care of all the needs
echo "Installing python3 :"
sudo apt install python3
echo "Installing pip3 :"
sudo apt install pip3

echo "Running python installer"
python3 ./python/install.py

#Kindly replace the following details with what suits your need the best
#Make equivalent changes in nasty.sh as well
echo "Downloading Stanford CoreNLP"
wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip
unzip ./stanford-corenlp-full-2018-10-05.zip -d ../
echo "Moving all classpath code to directory corenlp for standardization"
mkdir ../corenlp
mv ../stanford-corenlp-full-2018-10-05/* ../corenlp/
rm ./stanford-corenlp-full-2018-10-05.zip
rm -rf ../stanford-corenlp-full-2018-10-05

echo "Installing java"
sudo apt install openjdk-11-jdk

echo "Completed."
echo 
echo 
echo "Setting up nasty.sh as executable"
chmod +x ./nasty.sh
echo "Start the program by making use of \n./nasty.sh"
echo "Look up documents online for auto startup"
read -p "Start the program now?(Y/N)  " opt

if [ $opt -eq "y"]; then
	sh nasty.sh
fi
