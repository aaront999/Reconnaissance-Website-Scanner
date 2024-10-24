## Reconnaissance-Website-Scanner
#### Sometimes, having to manually scan or search a website -or multiple websites- for specific data that you want can be tedious. We can fix that by automating those searches with a Python script that extracts the domain, ip address, nmap scan, and whois from a website url and store that data into txt files for readability.  

### <ins>Disclaimer</ins>: It is illegal to network scan websites without permission. You must use an intentionally vulnerable website to scan. For this project, I used  https://www.hackthissite.org/ to test my scripts.
#
#### Programs we will be using:
- Visual Studio Code: https://code.visualstudio.com/download
- Python: https://www.python.org/downloads/
- Nmap: https://nmap.org/download.html

#### Python Library Documentation:
- import os (operating system): https://docs.python.org/3/library/os.html
- pip install tld (Top Level Domain): https://pypi.org/project/tld/
- import socket: https://pythontic.com/modules/socket/gethostname
- import subprocess: https://docs.python.org/3/library/subprocess.html
- pip install python-whois: https://pypi.org/project/python-whois/
#
1. First we need to import os so that we can interact with the operating system to read and write files. Next we will create 2 core functions that we will be using later which will be create_dir to create a directory and if that directory does not exist, one will be created. Our second function write_file will open the file in write mode and will store our collected data into that file.

![Screenshot 2024-10-23 155157](https://github.com/user-attachments/assets/b45d438b-43c8-4095-80ea-addce9527fac)
#
2. Next we will create a new file named domain_name.py to create a function that will accept a url and extracts its domain name as its output. Pip install the tld package in our terminal and import get_fld. We will also be using urlib.parse to parse the url into sections to check if there was a scheme inputted.

![Screenshot 2024-10-23 160258](https://github.com/user-attachments/assets/6646092a-2d45-4468-8b6c-9e40888020f3)
#
- You can also check if you have properly installed the tld package via the cmd.

![Screenshot 2024-10-23 160849](https://github.com/user-attachments/assets/624444f8-840a-4501-8163-e13d6b79cd50)
#
- If you are having trouble getting the package to work like I did, hit control+shift P and search for 'Python: select interpretor' and make sure you have selected the correct Python environment. I accidentally didn't select the 'add ON PATH' option when I had initially downloaded Python. You can either add it manually by searching "where python" in cmd and copying and pasting the path into your environment variable path or uninstall, re-install, and select the 'add ON PATH' check box.

![Screenshot 2024-10-23 190433](https://github.com/user-attachments/assets/9fd2a963-5170-46f9-a57e-8a3f1e351919)
![Screenshot 2024-10-23 190643](https://github.com/user-attachments/assets/f958b5f7-ca03-4e82-a607-a6ae579b0ad6)

- Let's run our get_domain_name code to see if we get our desired output.
  
![Screenshot 2024-10-23 160914](https://github.com/user-attachments/assets/371b61ac-aa4b-44c7-9b2f-31da78020f25)
#
3. Great, now we can move on to create our ip grabber by importing socket. We could have imported get_tld to get the domain again but I wanted to try something different by using .replace and .split. I used try and except method in the event the code throws an error and ran my code to see if I get the desired output.

![Screenshot 2024-10-23 160958](https://github.com/user-attachments/assets/839644f4-cdd4-41e3-a095-8ed6eeb0a4e6)
#
4. This Nmap section was a little tricky for me and took the most time for me to get the syntax right. After you downloaded Nmap, make sure you have it correctly downloaded via the commandline tool and added in our environment variable path just like our Python program help steps from earlier.
  - Nmap --version (should not throw an error)
  - where Nmap: copy and paste the path and manually add the path onto your environment variables if you need to.
![Screenshot 2024-10-23 161252](https://github.com/user-attachments/assets/53fbea49-ac4b-48b9-8832-cf73a3b18fe9)
#
- Import subprocess and create a function that accepts 2 parameters 'options' which will be 1 or more Nmap commands the user will input, and the ip address. I ran my code to see if my code runs as expected.
![Screenshot 2024-10-23 161150](https://github.com/user-attachments/assets/b495d52f-e332-4c0b-9289-304d94421750)
#
5. 



