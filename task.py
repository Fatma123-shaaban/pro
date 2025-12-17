def createFile():
    with open("data.txt",'w',encoding='utf-8') as file:
        file.write('id,name,phone,age,from\n')
        file.write('1,fatma,010068060301,20,egypt\n')
        file.write('2,Sara,010068060301,21,Amirica\n')
        file.write('3,Mona,010768060301,22,Aman\n')
        file.write('4,Heba,010568060301,23,Corea\n')
        file.write('5,Ola,010668060301,24,UK\n')
        file.write('6,Rahma,010068068301,25,Soudia\n')

def reading():
    with open("data.txt",'r',encoding='utf-8') as file:
        lines=file.readlines()
        for line in lines:
            print(line)

def insert():
    with open("data.txt",'r',encoding='utf-8') as file:
        lines=file.readlines()
        numberOfLines=int(lines[-1].split(',')[0]) if len(lines)>1 else 0
        name=input("enter the name: ")
        phone=input("enter the phone number: ")
        age=input("enter the age: ")
        country=input("enter where come from: ")
        with open("data.txt",'a',encoding='utf-8') as file:
            file.write(f'{numberOfLines+1},{name},{phone},{age},{country}\n')


def searching(value):
    value=str(value).lower()
    ids=[]
    with open("data.txt","r",encoding="utf-8") as file:
        for line in file.readlines()[1:]:  
            parts=line.strip().split(',')
            for part in parts[1:]:  
                if value in part.lower():
                    ids.append(parts[0])
                    break  
    return ids


def update(old,new):
    found=searching(old)
    if found:
        with open("data.txt",'r',encoding='utf-8') as file:
            lines=file.readlines()
            update_rec=[]
            for line in lines:
                if old.lower() in line.lower():
                    new_value=line.replace(old,new)
                    update_rec.append(new_value)
                else:
                    update_rec.append(line)
        with open("data.txt",'w',encoding='utf-8') as file:
            for line in update_rec:
                file.write(line)


def delete_rec(record_id):
    record_id=str(record_id)  
    with open("data.txt","r",encoding="utf-8") as file:
        lines=file.readlines()
    header=lines[0].strip() 
    new_data=[]
    for line in lines[1:]:
        parts=line.strip().split(',')
        if parts[0]!=record_id:  
            new_data.append(line.strip())
    updated_list=[header]
    for index,line in enumerate(new_data,start=1):
        parts=line.split(',')
        parts[0]=str(index)
        updated_list.append(','.join(parts))
    with open("data.txt","w",encoding="utf-8") as file:
        for line in updated_list:
            file.write(line + "\n")

    print(f"record that id -> {record_id} deleted successfully")




createFile()
reading()
# insert()
# print("\n\t\t\tafter inserting")
# reading()
print('\n\n\nfound' if searching("egypt") else"\n\n\nnot found")
update("010068060301","123654")
print('\n\t\t\tafter updateing')
reading()
delete_rec(2)
print('\n\t\t\tafter deleting')
reading() 