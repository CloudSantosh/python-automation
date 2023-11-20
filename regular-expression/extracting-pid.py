import re
log="The process ID is [12345]. Another process has ID [6789]."
regex=r"\[(\d+)\]"
#result=re.search(regex,log)
result=re.findall(regex,log)
for each_item in result:
    print(each_item)