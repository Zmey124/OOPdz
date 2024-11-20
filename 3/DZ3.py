import glob

filepaths = glob.glob("*[0-3].txt")


list1 = []
lines_dict = {}
for filepath in filepaths:
    
    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()
        lines_dict[filepath] = [len(lines), lines]
        # lines_dict[len(lines)] = filepath,len(lines), lines 
        # lines_dict = dict(sorted(lines_dict.items()))
sorted_lines_dict = sorted(lines_dict.items(), key=lambda x: x[1][0])

# for x in sorted_lines_dict:
#     res = "".join(x[1][1]).replace("","")
#     itog = f" {x[0]} \n {x[1][0]} \n {res} \n"
#     print(itog)
    


with open('result.txt', 'w',encoding='utf-8') as f:
    for x in sorted_lines_dict:
        res = "".join(x[1][1]).replace("","")
        itog = f" {x[0]} \n {x[1][0]} \n {res} \n"
        f.write(itog)

    

        
           



    
