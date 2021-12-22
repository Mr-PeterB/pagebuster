import requests 
import sys 
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Pagebuster")
print(ascii_banner)

sub_list = open(sys.argv[2]).read() 
directories = sub_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}" 
    r = requests.get(dir_enum)
    if r.status_code==404: 
        pass
    else:
        print("Valid directory:" ,dir_enum)

