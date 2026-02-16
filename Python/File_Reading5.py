import re
import argparse

def isvalid(line) -> bool:

    pattern = (
        r"\d{4}-\d{2}-\d{2} "
        r"\d{2}:\d{2}:\d{2},"
        r"\d{3}"
        r"\s+(INFO|ERROR|WARNING|DEBUG)\:"
        r"\s+\[[a-zA-Z]+\]"
        r".+\.$"
    )
    if(re.match(pattern,line)):
        return True
    else:
        return False


parser = argparse.ArgumentParser(description="Example script")

parser.add_argument("--loglevel", type=str, required=True, help="LOGLEVEL")
parser.add_argument("--module", type=str, required=True, help="MODULE")

args = parser.parse_args()


with open("data_log.txt","r") as file:
    dic = {}
    lines = file.readlines()
    for i,line in enumerate(lines):
        if(isvalid(line)):
            key = "line"+str(i)
            dic[key] = {}
            dic[key]["timestamp"]= line.split(",",1)[0]
            # pattern = r",\d{3}\s+([A-Za-z]+)\s*:"
            pattern = r"\s([A-Z]+)\:"
            dic[key]["loglevel"] = re.search(pattern,line).group(1)
            pattern = r"\[([A-Za-z]+)\]"
            dic[key]["module"] = re.search(pattern,line).group(1)
            pattern = r"-\ ([a-z1-9A-Z\ ]+)"
            dic[key]["message"] =  re.search(pattern,line).group(1)
            
            # if dic[key]["loglevel"] == args.loglevel and dic[key]["module"] == args.module:
            #     print(key," ",dic[key])
        print(i,dic[key])
