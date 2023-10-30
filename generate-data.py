from faker import Faker
import json
import random


# Inputs
n_people = 10
n_couple = 5


# Generate names
m = n_people
m_max = 600  # more than 600 may raise faker.exceptions.UniquenessException
if n_people > m_max:
    m = m_max

faker = Faker()
unique_names = [faker.unique.first_name() for _ in range(m)]

people = []
for i in range(n_people):
    j = i % m_max
    k = i // m_max
    name = unique_names[j]
    if n_people > m_max:
        name += '_' + str(k)
    people.append(name)

# Generate couples
couples = []
_people = people.copy()
for i in range(n_couple):
    couple = random.sample(_people, 2)
    couples.append(couple)
    for member in couple:
        _people.remove(member)

data = {
    "people": people,
    "couples": couples, 
}

# Create data file
with open(f'data-people{n_people}-couples{n_couple}.json', 'w') as f:
    json.dump(data, f)