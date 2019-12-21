
import os
#from banner import xe_header
import sys, traceback
print ('--------------                              ----------------')
print ('------------------Kama Kepar Script for mysql --------------')
print ('Hello it is the program to install all needed apps and libs ')
print ('0.Exit Script')
print ('1.Start installing in Kali, Mint, Fedora, Arch, Parrot')
print ('2.Start installing in Termux')
print ('3.Start installing gnome in Debian')
a = int(input('punkt> '))
if a == 0:
   sys.exit("Kamakepar Exit...")
if a == 1:
   os.system('sudo apt-get install nano && sudo apt-get install gdebi && sudo apt-get install git && sudo apt-get install libvirt-manager')
   print('Setting MySql...')
   os.system('sudo apt-get install mysql-server && sudo apt-get install mysql-client && sudo apt-get install mysql-workbench')
   print('Starting workbench')
   os.system('sudo mysql-workbench')
if (a == 2):
   os.system('apt-get install proot && apt-get install wget -y && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh')
   os.system('apt-get update && apt-get install wget -y && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh')
   os.system('bash debian.sh')
   os.system('./start-debian.sh')
   os.system('sudo apt-get install nano && sudo apt-get install gdebi && sudo apt-get install git && sudo apt-get install libvirt-manager')
   print('Setting MySql...')
   os.system('sudo apt-get install mysql-server && sudo apt-get install mysql-client && sudo apt-get install mysql-workbench')
   print('Starting workbench')
   os.system('sudo mysql-workbench')
if (a == 3):
   os.system('sudo apt-get install gnome')

