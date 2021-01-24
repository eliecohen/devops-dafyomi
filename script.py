import os
import boto3
import sys
import time
import subprocess
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

  
book_map = {
        "1":"berakhot",
        "2":"shabbat",
        "3":"eruvin",
        "4":"pesachim",
        "5":"shekalim",
        "6":"yoma",
        "7":"sukkah",
        "8":"beitzah",
        "9":"rosh_hashanah",
        "10":"taanit",
        "11":"megillah",
        "12":"moed_katan",
        "13":"chagigah",
        "14":"yevamot",
        "15":"ketubot",
        "16":"nedarim",
        "17":"nazir",
        "18":"sotah",
        "19":"gittin",
        "20":"kiddushin",
        "21":"bava_kamma",
        "22":"bava_metzia",
        "23":"bava_batra",
        "24":"sanhedrin",
        "25":"makkot",
        "26":"shevuot",
        "27":"avodah_zarah",
        "28":"horayot",
        "29":"zevachim",
        "30":"menachot",
        "31":"chullin",
        "32":"bekhorot",
        "33":"arakhin",
        "34":"temurah",
        "35":"keritot",
        "36":"meilah",
        "37":"tamid",
        "38":"niddah"
    }

path = "maps/"+book_map[bookId]+"/"+dafId+".mm"
g = Github(token)
repo = g.get_repo("eliecohen/dafyomi")
try:
    contents = repo.get_contents(path, ref="master")
    a = repo.update_file(contents.path, "update "+path, flowchart_content, contents.sha )
except:
    a = repo.create_file(path, "create "+path, flowchart_content)
print(a)

os.system('SCHTASKS.EXE /RUN /TN "freemind"') 

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


#os.system("aws s3 cp c:\\output.html s3://daf-yomi/assets/"+bookId+"/"+dafId+".html") 
subprocess.run("aws s3 cp c:\\output.html s3://daf-yomi/assets/"+bookId+"/"+dafId+".html", shell=True)
#os.system("aws s3 cp c:\\output.html_files\\image.png s3://daf-yomi/assets/"+bookId+"/"+dafId+".png") 
subprocess.run("aws s3 cp c:\\output.html_files\\image.png s3://daf-yomi/assets/"+bookId+"/"+dafId+".png", shell=True)

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

#time.sleep(20)

print("file uploaded to s3")
