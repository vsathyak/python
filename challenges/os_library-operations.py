import os

#Create a folder named myfolder under /home/ubuntu
if not os.path.exists("/home/ubuntu/"):
        os.makedirs("myfolder")
