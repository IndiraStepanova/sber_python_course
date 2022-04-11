def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

my_list_of_persons = []
 

with open ('D:\\python\\dataset_pyhon\\task_file.txt', 'r+') as inf:
    for line in inf.readlines():
        list_for_person = line.replace(' ', '').strip().split(',')
        if list_for_person[1] != '' and list_for_person[1] != 'NO_NAME' and list_for_person[2] != '':
            if len(list_for_person[3]) == 7 and list_for_person[3] != '0000000' and list_for_person[3].isdigit and list_for_person[4] != '':
                my_list_of_persons.append(list_for_person[1:3])
                emails = email_gen(my_list_of_persons)
    print(emails)

        
    
            