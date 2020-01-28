import subprocess,time
import os,re
path=str(input("set path for directory: "))
l=path.split()
modified="\\".join(l)
os.chdir(modified)
myset=os.listdir()
key=int(input("choose custom names(1) or default name(2) : "))
if key==2:
    for elements in myset:
        m=re.findall(r"([^\s]+(\.(?i)(exe|gz|zip))$)",elements)
        k=re.findall(r"([^\s]+(\.(?i)(jpg|png|gif|bmp))$)",elements)
        t=re.findall(r"([^\s]+(\.(?i)(json|pdf|ppt|txt))$)",elements)
        if len(k)>0 and ("wallpaper" or "wallpapers") not in myset:
            subprocess.call("mkdir images", shell=True)
        elif len(m)>0 and ("software" or "softwares") not in myset:
            subprocess.call("mkdir softwares", shell=True)
        elif len(t)>0 and ("text" or "texts") not in myset:
            subprocess.call("mkdir texts", shell=True )                           
    subprocess.call("move *.exe "+modified+"\\softwares", shell=True)
    subprocess.call("move *.json "+modified+"\\texts", shell=True)
    subprocess.call("move *.gz "+modified+"\\softwares", shell=True)
    subprocess.call("move *.zip "+modified+"\\softwares", shell=True)
    subprocess.call("move *.jpg "+modified+"\\images", shell=True)
    subprocess.call("move *.png "+modified+"\\images", shell=True)
    subprocess.call("move *.gif "+modified+"\\images", shell=True)
    subprocess.call("move *.bmp "+modified+"\\images", shell=True)
    subprocess.call("move *.pdf "+modified+"\\texts", shell=True)
    subprocess.call("move *.txt "+modified+"\\texts", shell=True)
    subprocess.call("move *.ppt "+modified+"\\texts", shell=True)
elif key==1:
    j,a,b=[],[],[]
    
    for elements in myset:
        m=re.findall(r"([^\s]+(\.(?i)(exe|gz|zip))$)",elements)
        k=re.findall(r"([^\s]+(\.(?i)(jpg|png|gif|bmp))$)",elements)
        t=re.findall(r"([^\s]+(\.(?i)(json|pdf|ppt|txt))$)",elements)
        j.append(m)
        a.append(k)
        b.append(t)
    if len(a)>0:
        images=str(input("Enter name for image folder: "))
        subprocess.call("mkdir "+images, shell=True)
        subprocess.call("move *.jpg "+modified+"\\"+images, shell=True)
        subprocess.call("move *.png "+modified+"\\"+images, shell=True)
        subprocess.call("move *.gif "+modified+"\\"+images, shell=True)
        subprocess.call("move *.bmp "+modified+"\\"+images, shell=True)
        time.sleep(1)
    if len(j)>0:
        softwares=str(input("Enter name for software folder: "))
        subprocess.call("mkdir "+softwares, shell=True)
        subprocess.call("move *.exe "+modified+"\\"+softwares, shell=True)
        subprocess.call("move *.gz "+modified+"\\"+softwares, shell=True)
        subprocess.call("move *.zip "+modified+"\\"+softwares, shell=True)
        time.sleep(1)
    if len(b)>0:
        texts=str(input("Enter name for texts folder: "))
        subprocess.call("mkdir "+texts, shell=True)
        subprocess.call("move *.pdf "+modified+"\\"+texts, shell=True)
        subprocess.call("move *.txt "+modified+"\\"+texts, shell=True)
        subprocess.call("move *.ppt "+modified+"\\"+texts, shell=True)
        subprocess.call("move *.json "+modified+"\\"+texts, shell=True)
        time.sleep(1)
else:
    print("Try agin Enter valid input")
            


    


