
import json

with open('stations1.json', 'r') as file:
    content = file.read()

y = json.loads(content)
def remove_comma (x) :
    changer = x.split(',')
    changing = ''
    for i in changer:
        changing = changing + i + ' ' 
    print(changing)
    return changing
with open('newtest.csv', 'w+') as file1:
    file1.writelines('name, url_resolved, country, tags \n')
with open('newtest.csv', 'a') as filess:
    for i, j in enumerate(y):
        #print(j['name'],end=',')
        #print(j['url_resolved'],end= ',')
        #print(j['tags'])
        #remove_comma(j['tags'])


        name_convention =  j['name']
        if '\t' in name_convention:
            name_convention = name_convention.replace('\t', ' ')
        if '\n' in name_convention:
            name_convention = name_convention.replace('\n', ' ')

        if name_convention.startswith(' '):
            name_convention = name_convention.split(' ' , 1)[1]
        filess.writelines(name_convention+', '+j['url_resolved']+', '+j['country']+', ' +'['+ remove_comma(j['tags'])+']'+'\n')
