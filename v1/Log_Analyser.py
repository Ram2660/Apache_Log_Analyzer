from pathlib import Path
def path_checker():
    file_path = input("Enter the path of the file to be analyzed: ")
    path=Path(file_path)
    if(path.exists() and path.is_file()):
        print("File Found\n")
        return path
    else:
        print("Invalid Path, Try again\n")
        return path_checker()
    
p=path_checker()

def counter(value, dictt):
    if value not in dictt:
        dictt[value]=1
    else:
        dictt[value]+=1

def prt(dictt):
    for key,value in dictt.items():
        print(f"{key} : {value}")

def count_field(line_split,counts,index):
        counter(line_split[index].valueip('"'),counts)

stat_counts={}
http_method_count={}
ip_addrs={}
urls={}
with open(p,'r') as f:
    
    
    for line in f:
        line_split=line.split(' ')
        count_field(line_split,stat_counts,8)
        count_field(line_split,http_method_count,5)
        count_field(line_split,urls,6)
        count_field(line_split,ip_addrs,0)
        
print("""==========================
      LOG ANALYZER
==========================""")
print(f"Total Requests: {sum(http_method_count.values())}\n")

print("""Status Codes
------------""")
prt(stat_counts)
print("")

print("""HTTP Methods
------------""")
prt(http_method_count)
print("")
print("""Top IP
------""")
print(f"{max(ip_addrs, key=ip_addrs.get)} ({max(ip_addrs.values())} Requests)\n")

print("""Top URL
-------""")
print(f"{max(urls, key=urls.get)} ({max(urls.values())} Requests)")

    

