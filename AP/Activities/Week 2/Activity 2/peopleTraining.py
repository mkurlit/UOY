import json
import pandas as pd
with open('PeopleTrainingDate.csv', 'r') as file:
    people_js, attributes = [], []
    for ix, line in enumerate(file):
        if ix == 0:
            attributes+=[item.replace('\n','') for item in line.split(',')]
        else:
            input_ = line.split(',')
            input_[1:3] = [', '.join(input_[1:3])]
            person = {at : item.replace('\n','').replace('\"','') for at,item in zip(attributes,input_) if item != '' and item != '\n'}
            if person:
                people_js.append(person)
    people_js = json.dumps(people_js)

people_df = pd.read_json(people_js)
people_df = people_df.loc[:,['Updated', 'Title', 'Name', 'ID', 'Email', 'Company']]
people_df['Updated'] = pd.to_datetime(people_df['Updated'], format = '%d/%m/%Y')
people_df = people_df.sort_values(by = 'Updated', axis = 0)

def flatten(object):
    for i in object:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i

with open('PeopleTrainingDateUpdate.csv', 'r') as file_2:
    update_js = []
    attributes = ['Updated', 'Email', 'ID', 'Title', 'Name', 'Company']
    for line in file_2:
        input_ = list(flatten([item if '@' not in item else item.split(' ') for item in line.split(',')]))
        input_[4:6] = [', '.join(input_[4:6])]
        person = {at : item.replace('\n','').replace('\"','') for at,item in zip(attributes,input_) if item != '' and item != '\n'}
        if person:
            update_js.append(person)
    update_df = pd.DataFrame(update_js)
    update_df['Updated'] = pd.to_datetime(update_df['Updated'], format = '%d/%m/%Y')

people_df = pd.concat([people_df, update_df])
