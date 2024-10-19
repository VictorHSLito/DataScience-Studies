"""Um exemplo de algumas análises de dados em uma rede de amigos"""

from collections import Counter

users = [{"id": 0, "name": "Hero"},
         {"id": 1, "name": "Dunn"},
         {"id": 2, "name": "Sue"},
         {"id": 3, "name": "Chi"},
         {"id": 4, "name": "Thor"},
         {"id": 5, "name": "Clive"},
         {"id": 6, "name": "Hicks"},
         {"id": 7, "name": "Devin"},
         {"id": 8, "name": "Kate"},
         {"id": 9, "name": "Klein"}, ]

friendship_pair = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                   (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

"""Reagrupa a lista de amigos com base no id de cada um"""
friendships = {user["id"]: [] for user in users}

for i, j in friendship_pair:
    friendships[i].append(j)
    friendships[j].append(i)

#Descobrindo o número médio de conexões entre os usuários

def number_of_friend(user):
        """Função que descobrirá a quantidade de amigos
        por usuário"""
        user_id = user["id"]
        friend_ids = friendships[user_id]
        return len(friend_ids)

total_conections = sum(number_of_friend(user) for user in users)
print(total_conections)

num_user = len(users)
avg_connections = total_conections/num_user
print(f"Conexões médias entre usuários: {avg_connections}")


#Descobrindo a quantidade de pessoas que mais tem amigos do maior para o menor

num_friends_by_id = [(user["id"], number_of_friend(user)) for user in users]

num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)
print(num_friends_by_id)  # Primeiro o Id da pessoa e depois a quantidade de amigos

def foaf_ids(user):
    """Essa função retorna os amigos dos amigos
    de um usuário"""
    return [foaf_id for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(foaf_id for friend_id in friendships[user_id]
            for foaf_id in friendships[friend_id]
            if foaf_id != user_id and
            foaf_id not in friendships[user_id])

for user in users:  #Informa a quantidade de amigos em comum por usuário
    print(friends_of_friends(user))