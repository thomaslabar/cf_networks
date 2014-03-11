alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet=list(alphabet)
task_name_1=-1
task_name_2=0

for start_res_name in ["B","C","D","E","F","G","H","I"]:
    for end_res_name in ["A","B","C","D","E","F","G","H","I"]:
        if start_res_name=="B" and end_res_name=="A":
            continue
        if start_res_name!=end_res_name:
            print_str="REACTION  "+str(start_res_name)+"to"+str(end_res_name)+"  logic_3"
            if task_name_2==0:
                task_name_1+=1
            print_str+=str(alphabet[task_name_1])
            print_str+=str(alphabet[task_name_2])
            task_name_2+=1
            task_name_2%=26
            print_str+="  process:resource=res"+str(start_res_name)+":value=1.0:product=res"+str(end_res_name)+":conversion=0.5:frac=0.0025"
            print(print_str)