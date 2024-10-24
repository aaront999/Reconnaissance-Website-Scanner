## Reconnaissance-Website-Scanner
#### Sometimes manually scanning or searching multiple websites for specific data can be tedious and time-consuming. We can fix that by automating these tasks with a Python script that extracts the domain name, IP address, performs an Nmap scan, and retrieves WHOIS information from a given website URL. The script also stores the results in text files for easy readability.

### <ins>Disclaimer</ins>: Scanning websites without explicit permission is illegal. For this project, I used the intentionally vulnerable website https://www.hackthissite.org to test my script.
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
5. Finally our WHOIS function. Luckily this script is the easiest to code. Pip install python-whois in our terminal, Import os and whois. Create a function that will accept a url and use whois.whois on the input url to get the website's whois information. I was getting an error in the terminal that the output couldn't be read because it wasn't a string. So I just converted the output into a str and I got the desired output.

![Screenshot 2024-10-23 161327](https://github.com/user-attachments/assets/e3eb05db-d8f1-46d3-8170-c30be0c44bbe)
![Screenshot 2024-10-23 161441](https://github.com/user-attachments/assets/3b878a2f-1ab7-40e6-8646-32237ab755cd)
#
6. Now that we have all of our scripts ready, let's create a new file titled main.py to tie everything together. Start by importing all of our scripts and creating a root directory named to whatever you would like.

![Screenshot 2024-10-23 161918](https://github.com/user-attachments/assets/7332ac19-9dbb-4455-81c6-358b63cf7e4e)
#
7. This scan_data function will take 2 parameters: the name of our website, and the full url. when it is called, it will call all of our scripts and store the results into their respective variables and at the end will call the scan_results function that takes in all of those results as arguments to store in a txt file; which we will create next.

![Screenshot 2024-10-23 162400](https://github.com/user-attachments/assets/7a88c7eb-2506-4b1c-9fe6-00d5d1ffdf94)
#
8. This scan_results function will be called in our scan_data function. It will add the name of the website we want to scan to our root directory and create a new directory, then it will write the scanned data/results into txt files and add it to that new directory.

![Screenshot 2024-10-23 162513](https://github.com/user-attachments/assets/7b22d02f-0363-474b-a08a-7beb430e0355)
#
9. Now, we can finally hit run on our code and the scripts should save everything!

![Screenshot 2024-10-23 162541](https://github.com/user-attachments/assets/4e01ca8e-44bd-467b-9304-f4d2e15c3f7e)
![Screenshot 2024-10-23 162643](https://github.com/user-attachments/assets/1ac5a2d8-5d91-41b9-934c-e4421b76796e)
![Screenshot 2024-10-23 162659](https://github.com/user-attachments/assets/dd979755-98e4-4c8c-abeb-d1cf057a7be2)
![Screenshot 2024-10-23 162740](https://github.com/user-attachments/assets/70443d37-0890-427b-a6d8-0f66131ca2e9)
![Screenshot 2024-10-23 162755](https://github.com/user-attachments/assets/f9055827-9fa2-4ad1-b9a1-5e4b5cbf65d1)
![Screenshot 2024-10-23 162809](https://github.com/user-attachments/assets/e1c06444-6aa4-4802-9216-4321352f60a9)
