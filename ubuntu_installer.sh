#This script is written for work with ubuntu
#Let it take care of all the needs
echo "Installing python3 :"
sudo apt install python3
echo "Installing pip3 :"
sudo apt install pip3

echo "Running python installer"
python3 ./python/install.py
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
