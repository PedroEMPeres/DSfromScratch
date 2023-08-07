users = [{'id':0, 'name':'Hero'},
         {'id':1, 'name':'Dunn'},
         {'id':2, 'name':'Sue'},
         {'id':3, 'name':'Chi'},
         {'id':4, 'name':'Thor'},
         {'id':5, 'name':'Clive'},
         {'id':6, 'name':'Hicks'},
         {'id':7, 'name':'Devin'},
         {'id':8, 'name':'Kate'},
         {'id':9, 'name':'Klein'}]

friendship_pais = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
                   (4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

#checking pairs to create a dict that will give us the pairs
#initializing empty list
friendship = {user['id']:[] for user in users}


for i in friendship_pais:
    friendship[i[0]].append(i[1])
    friendship[i[1]].append(i[0])

#QUESTIONS:
#1 - Average number of conections:

#This function will return the amount of friends the user passed as an argument has
def number_of_friends(user):
    user_id = user['id']
    friend_ids = friendship[user_id]
    return len(friend_ids)

#using the above function we can determine the total connection:
total_connection = sum(number_of_friends(user) for user in users)
#Than we can calculate the mean
num_users = len(users)
avg_connection = total_connection / num_users

print(f' the Average connection is: {avg_connection}')
    
#2 - Sorting by number of connections:
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]
num_friends_by_id.sort(key = lambda id_and_friends: id_and_friends[1],reverse = True)

#here we have a lambda function, that will take the second value from the tuple with id and num of friends and sort it in descending order
#hence the reverse= True

print(num_friends_by_id) #this is a list of tuples, with the first value being the id and the second the num of connections.


##FRIEND OF A FRIEND
from collections import Counter

def frinds_of_friends(user):
    user_id = user['id']
    return Counter(foaf_id for friend_id in friendship[user_id]
                   for foaf_id in friendship[friend_id]
                   if foaf_id != user_id
                   and foaf_id not in friendship[user_id])


print(frinds_of_friends(users[3])) #te key of the dictionary is the friend from users[3] and the value is the number of distinct friends in common

##INTERESTS

interests = [(0,'Hadoop'),(0,'Big Data'),(0,'Hbase'),(0,'Java'),
             (0,'Spark'),(0,'Storm'),(0,'Cassandra'),
             (1,'NoSQL'),(1,'MongoDB'),(1,'Cassandra'),(1,'Hbase'),
             (1,'Postgres'),(2,'Python'),(2,'scikit-learn'),(2,'scipy'),
             (2,'numpy'),(2,'statsmodels'),(2,'pandas'),(3,'R'),(3,'Python'),
             (3,'statistics'),(3,'regression'),(3,'probability'),
             (4,'machine learning'),(4,'regression'),(4,'probability'),
             (4,'libsvm'),(5,'Python'),(5,'R'),(5,'Java'),(5,'C++'),
             (5,'haskell'),(5,'programming languages'),(6,'statistics'),
             (6,'probability'),(6,'mathematics'),(6,'theory'),
             (7,'machine learning'),(7,'scikit-learn'),(7,'Mahout'),
             (7,'neural networks'),(8,'neural networks'),(8,'deep learning'),
             (8,'Big Data'),(8,'artificial intelligence'),(9,'Hadoop'),
             (9,'Java'),(9,'MapReduce'),(9,'Big Data')]

from collections import defaultdict

user_id_by_interests = defaultdict(list)
for user_id, interest in interests:
    user_id_by_interests[interest].append(user_id)

user_interests_by_id= defaultdict(list)
for user_id, interest in interests:
    user_interests_by_id[user_id].append(interest)

print(user_id_by_interests)
print(user_interests_by_id)

def most_common_interest(user):
    return Counter( interested_user_id
                   for interest in user_interests_by_id[user['id']]
                   for interested_user_id in user_id_by_interests[interest]
                   if interested_user_id != user['id'])

print(most_common_interest(users[3])) 
# this returns a dict, with the key being another user id, with similar interests as the user passed
#as an argument. And the value means the number of common interests

# SALARIES AND TENURES
#

salaries_and_tenures = [(83000,8.7),(88000,8.1),
                       (48000,0.7),(76000,6),
                       (69000,6.5),(76000,7.5),
                       (60000,2.5),(83000,10),
                       (48000,1.9),(63000,4.2)]

    #yearly salarie avg

def tenure_bucket(tenute):
    if tenure <2:
        return 'Less than two'
    elif tenure <5:
        return 'Less than five'
    else:
        return 'More than five'

salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure_bucket(tenure)].append(salary)

avg_salary_by_tenure = {tenure: sum(salaries)/len(salaries) for tenure, salaries in salary_by_tenure.items()}

print(avg_salary_by_tenure)
