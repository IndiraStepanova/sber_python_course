my_list_of_persons = []
list_of_persons = []
def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

"""def isvalid_NL(Name_Lastname: list):
    
    return my_list_of_persons"""

"""def isValid_OP(other_parameters: list):
    
        emails = email_gen(my_list_of_persons)"""

cnt = 0 
with open ('D:\\python\\dataset_pyhon\\task_file.txt', 'r') as inf:
    for line in inf.readlines():
        persons = line.replace(' ', '').strip().split(',')
        list_of_persons.append(persons)
        if persons[1] != '' and persons[1] != 'NO_NAME' and persons[2] != '':
            if len(persons[3]) == 7 and persons[3] != '0000000' and persons[3].isdigit and persons[4] != '':
                my_list_of_persons.append(persons[1:3])
                persons.insert(0, email_gen(my_list_of_persons[1:3]))
    print(persons)   

               
    

    
    


        