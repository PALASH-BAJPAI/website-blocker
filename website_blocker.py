import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=[]

print("Enter the time in 24 hr format")
a=int(input("starting hour : "))
b=int(input("ending hour : "))
s=input("enter site to block : ")
website_list.append(s)
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,a)< dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,b):
        print("....blocked....")
        with open(hosts_path,"r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        print("Have fun...")
        with open(hosts_temp,"r+") as file:
            content=file.readlines()
            for line in content:
                if not any(website in line for website in website_list ):
                    file.write(line)
            file.truncate()
            file.seek(0)

    time.sleep(5)
