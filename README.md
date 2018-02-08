# Logs Analysis Tool Project:

Logs Analysis Tool is a course related project in Udacity's nanodegree. The Tool performs a number of SQL queries on a database to answer each of the following questions:

**1. What are the most popular three articles of all time? Which articles have been accessed the most?**

**2. Who are the most popular article authors of all time?**

**3. On which days did more than 1% of requests lead to errors?**

The program is structured into 2 main pieces:
- 1.Three functions, each solves one of the 3 questions.
- 2.main function, which interacts with the user and asks for certain input.


# Installation:
--------------

This script will work from any environment with Python and PostgreSQL installed. Setting up a VM will help ensure that all users have the same environment, as long as you have the correct versions of Python, PostgreSQL, and psycopg2 installed, feel free to skip this part.

The VM is a Linux server system that runs on top of your own computer. You can share files easily between your computer and the VM; and you'll be running a Command Line Interface (CLI) tool.

We're using tools called Vagrant and VirtualBox to install and manage the VM. You'll need to install these to do some of the exercises. The instructions on this page will help you do this.


### Install VirtualBox:
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.


### Install Vagrant:
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.


### Download the VM configuration:
Use Github to fork and clone this Vagrantfile [https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile)



### Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!


-----------
# Logged in!

If you are now looking at a shell prompt that starts with the word vagrant (as in the above screenshot), congratulations — you've gotten logged into your Linux VM.

If not, take a look at the Troubleshooting section below.


### The files for this course
Inside the VM, change directory to /vagrant and look around with `ls`

The files you see here are the same as the ones in the vagrant subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to the other. This means that you can edit code in your favorite text editor, and run it inside the VM.

Files in the VM's /vagrant directory are shared with the vagrant folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only inside the VM.


### Running the database
The PostgreSQL database server will automatically be started inside the VM. You can use the psql command-line tool to access it and run SQL statements:


Running psql, the PostgreSQL command interface, inside the VM.


### Logging out and in
If you type exit (or Ctrl-D) at the shell prompt inside the VM, you will be logged out, and put back into your host computer's shell. To log back in, make sure you're in the same directory and type vagrant ssh again.

If you reboot your computer, you will need to run vagrant up to restart the VM.

You can power off the virtual machine by typing `vagrant halt` from the host computer's shell.


### Troubleshooting
I'm not sure if it worked.
If you can type vagrant ssh and log into your VM, then it worked! It's normal for the vagrant up process to display a lot of text in many colors, including sometimes scary-looking messages in red, green, and purple. If you get your shell prompt back at the end, and you can log in, it should be OK.


### vagrant up is taking a long time. Why?
Because it's downloading a whole Linux operating system from the Internet.


### I'm on Windows, and when I run vagrant ssh, I don't get a shell prompt.
Some versions of Windows and Vagrant have a problem communicating the right settings for the terminal. There is a workaround: Instead of vagrant ssh, run the command winpty vagrant ssh instead.


### I'm on Windows and getting an error about virtualization.
Sometimes other virtualization programs such as Docker or Hyper-V can interfere with VirtualBox. Try shutting these other programs down first.

In addition, some Windows PCs have settings in the BIOS or UEFI (firmware) or in the operating system that disable the use of virtualization. To change this, you may need to reboot your computer and access the firmware settings. A web search can help you find the settings for your computer and operating system. Unfortunately there are so many different versions of Windows and PCs that we can't offer a simple guide to doing this.


### Why are we using a VM? It seems complicated.
It is complicated. In this case, the point of it is to be able to offer the same software (Linux and PostgreSQL) regardless of what kind of computer you're running on.


### If all else fails, try an older version.
Udacity mentors have noticed that some newer versions of Vagrant don't work on all operating systems. Version 1.9.2 is reported to be stabler on some systems, and version 1.9.1 is the supported version on Ubuntu 17.04. You can download older versions of Vagrant from the Vagrant releases index.



## Running using the command line
--------------------------------
Windows:
Create a folder on your computer to use for your Python programs, such as C:\pythonpractice, and save your .py files in that folder.
In the Start menu, select "Run...", and type in cmd. This will cause the Windows terminal to open.
Type cd \directory to change directory to your program folder, and hit Enter.
Type loganalysis.py to run your program!

Mac:
Create a folder on your computer to use for your Python programs. A good suggestion would be to name it pythonpractice and place it in your Home folder (the one that contains folders for Documents, Movies, Music, Pictures, etc). Save your .py files into this folder.
Open the Applications folder, go into the Utilities folder, and open the Terminal program.
Type cd your-directory to change directory to your program folder, and hit Enter.
Type python ./loganalysis.py to run your program!
Note:
If you have both Python 2 and Python 3 installed (Your machine comes with a version of Python 2 but you can install Python 3 as well), you should run python3 loganalysis.py

Linux:
Create a folder on your computer to use for your Python programs, such as ~/pythonpractice, and save your .py files in that folder.
Open up the terminal program. In KDE, open the main menu and select "Run Command..." to open Konsole. In GNOME, open the main menu, open the Applications folder, open the Accessories folder, and select Terminal.
Type cd ~/pythonpractice to change directory to your pythonpractice folder, and hit Enter.
Type python ./loganalysis.py to run your program!
Note:
If you have both Python version 2.6.1 and Python 3.0 installed (Very possible if you are using Ubuntu, and ran sudo apt-get install python3 to have python3 installed), you should run python3 loganalysis.py


## Running the file from IDLE
----------------------------
1. Run IDLE. You will be presented with the "Python Shell" window and a >>> prompt.
2. Click File, New Window. You will be presented with an "Untitled" window for editing a script.
3. Enter your script in the "Untitled" window.
4. In the "Untitled" window, select Run, Run Module (or press F5) to run your script.
5. A dialog "Source Must Be Saved. OK to Save?" appears. Click OK.
6. In the Save As dialog:
  A) Browse to a directory to save your script.
  B) Enter a filename.
  C) Click Save.
7. The "Python Shell" window will display the output of your script.
8. Edit script and press F5 as needed to re-run your script.

Please refer to the IDLE documentation if you need further help:
[https://docs.python.org/3.0/library/idle.html](https://docs.python.org/3.0/library/idle.html)
