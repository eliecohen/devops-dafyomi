import os
import boto3
import sys
import time

#bookId="3"
#dafId="91"

bookId=sys.argv[1:][0]
dafId=sys.argv[1:][1]

print(f"{bookId} - {dafId}")

if os.path.isfile("c:\\flowchart.mm"):
    print("remove flowchart.mm")
    os.remove("c:\\flowchart.mm")

if os.path.isfile("c:\\output.html"):
    print("remove output.html")
    os.remove("c:\\output.html")

if os.path.isfile("c:\\output.html_files\\image.png"):
    print("remove image.png")
    os.remove("c:\\output.html_files\\image.png")    

s3 = boto3.client('s3')
with open('c:\\flowchart.mm', 'wb') as f:
    s3.download_fileobj('daf-yomi', 'assets/upload/'+bookId+"_"+dafId+".mm", f)

os.system('SCHTASKS.EXE /RUN /TN "ouriel"') 

time_to_wait = 40
time_counter = 0
while not os.path.exists("c:\\output.html") or not os.path.exists("c:\\output.html_files\\image.png"):
    print(".")
    time.sleep(1)
    time_counter += 1
    if time_counter > time_to_wait:
        print("timeout")
        break

with open("c:\\output.html", "rb") as f:
    s3.upload_fileobj(f, "daf-yomi", "assets/"+bookId+"/"+dafId+".html")

with open("c:\\output.html_files\\image.png", "rb") as f:
    s3.upload_fileobj(f, "daf-yomi", "assets/"+bookId+"/"+dafId+".png")

print("file uploaded to s3")
