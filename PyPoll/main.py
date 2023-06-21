import csv
'Read csv file'
with open ('Resources/election_data.csv') as file:
    data = csv.reader(file,delimiter=',')
    ballot_id=[]
    county=[]
    candidate=[]
    i=0
    'Read text file row by row'
    for row in data:
        if i!=0:
            ballot_id.append(row[0])
            county.append(row[1])
            candidate.append(row[2])
        i=i+1
    
total_votes=str(len(ballot_id))
print(len(ballot_id))

'Ensure that the candidates names are sorted and add a blank cell'
candidate2=sorted(candidate)
candidate2.append('')
'Find different candidates'
persons=[]
votes=[]
vote=0
i=0
u=0
for person in candidate2:
    if i==0:
        persons.append(person)
        i=1
    if persons[u]!=person:
        persons.append(person)
        u=u+1
        votes.insert(u-1,vote)
        vote=0
    else:
        vote=vote+1
persons.pop()
print(persons)
print(votes)
'Write results on text file'
with open ('Analysis/Result.txt','w') as result:
    result.write('Election Results' +'\n'+'\n')
    result.write('-------------------------' +'\n'+'\n')
    result.write('Total Votes: '+ total_votes + '\n'+'\n')
    result.writelines(candidate[1])
