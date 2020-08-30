import os
#import boto3
import sys
import time

bookId="3"
dafId="91"

# bookId=sys.argv[1:][0]
# dafId=sys.argv[1:][1]

with open("c:\\"+bookId+"_"+dafId+".txt", 'w') as f:
    f.write("asdjhasdkhjaskdjhaksdlhj")

print(f"{bookId} - {dafId}")

# if os.path.isfile("c:\\upload.mm"):
#     print("remove upload.mm")
#     os.remove("c:\\upload.mm")

# if os.path.isfile("c:\\upload.html"):
#     print("remove upload.html")
#     os.remove("c:\\upload.html")

# if os.path.isfile("c:\\output.html_files\\image.png"):
#     print("remove image.png")
#     os.remove("c:\\output.html_files\\image.png")    

# with open("c:\\a.txt", 'w') as f:
#     f.write("asdjhasdkhjaskdjhaksdlhj")    

# s3 = boto3.client('s3')
# with open('c:\\upload.mm', 'wb') as f:
#     s3.download_fileobj('daf-yomi', 'assets/upload/'+bookId+"_"+dafId+".mm", f)

# with open("c:\\b.txt", 'w') as f:
#     f.write("asdjhasdkhjaskdjhaksdlhj")       

# os.system('SCHTASKS.EXE /RUN /TN "ouriel"') 

# with open("c:\\"+bookId+"_"+dafId+".txt", 'w') as f:
#     f.write("asdjhasdkhjaskdjhaksdlhj")

# with open("c:\\c.txt", 'w') as f:
#     f.write("asdjhasdkhjaskdjhaksdlhj")       

# time_to_wait = 40
# time_counter = 0
# while not os.path.exists("c:\\output.html") or not os.path.exists("c:\\output.html_files\\image.png"):
#     print(".")
#     time.sleep(1)
#     time_counter += 1
#     if time_counter > time_to_wait:
#         print("timeout")
#         break

# with open("c:\\output.html", "rb") as f:
#     s3.upload_fileobj(f, "daf-yomi", "assets/"+bookId+"/"+dafId+".html")

# with open("c:\\output.html_files\\image.png", "rb") as f:
#     s3.upload_fileobj(f, "daf-yomi", "assets/"+bookId+"/"+dafId+".png")

# print("file uploaded to s3")
