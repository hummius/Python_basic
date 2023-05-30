def job_maker(dict):
    pairs_list = list()
    interests_list = list()
    amount = 0
    for key, value in dict.items():
        pairs_list.append((key, value['age']))
        interests_list += [interest for interest in value['interests']]
        amount += len(list(value['surname']))
    return pairs_list, interests_list, amount

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

pairs_list, interests_list, surnames_amount = job_maker(students)

print(f'Список пар "ID студента - возраст": {pairs_list}')
print(f'Полный список интересов всех студентов: {interests_list}')
print(f'Общая длина всех фамилий: {surnames_amount}')