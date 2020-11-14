import os
import boto3
import sys
import time
import botocore
from github import Github

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

with open ("c:\\github_token", "r") as myfile:
    token=myfile.readlines()[0]

flowchart_content = open("c:\\flowchart.mm", "r").read() 

   
book_map = {"1":"brachot","2":"shabat","3":"eruvin","4":"psachim"}
path = "source/"+book_map[bookId]+"/"+dafId+".mm"
g = Github(token)
repo = g.get_repo("eliecohen/dafyomi")
try:
    contents = repo.get_contents(path, ref="master")
    a = repo.update_file(contents.path, "update "+path, flowchart_content, contents.sha )
except:
    a = repo.create_file(path, "create "+path, flowchart_content)
print(a)

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

#s3_2 = boto3.resource('s3')

os.system("aws s3 cp c:\\output.html s3://daf-yomi/assets/"+bookId+"/"+dafId+".html") 
os.system("aws s3 cp c:\\output.html_files\\image.png s3://daf-yomi/assets/"+bookId+"/"+dafId+".png") 

#try:
#    s3_2.meta.client.upload_file('c:\\output.html', "daf-yomi", "assets/"+bookId+"/"+dafId+".html")
#    s3_2.meta.client.upload_file('c:\\output.html_files\\image.png', "daf-yomi", "assets/"+bookId+"/"+dafId+".png")

# except botocore.exceptions.ClientError as err:
#     f = open("exception.txt", "a")
#     f.write("Bucket {} already exists!".format(err.response['Error']['BucketName']))
#     f.close()
#     raise err


#with open("c:\\output.html", "rb") as f:
#    s3.upload_fileobj(f, "daf-yomi", "assets/"+bookId+"/"+dafId+".html")

#with open("c:\\output.html_files\\image.png", "rb") as f:
#    s3.upload_fileobj(f, "daf-yomi", "assets/"+bookId+"/"+dafId+".png")

time.sleep(10)

print("file uploaded to s3")
