import pickle


def save_user(new_user):
    file_name = open('storage/user_list', 'rb')
    loaded_file = pickle.load(file_name)

    loaded_user_list = list(loaded_file)

    print(loaded_user_list)

    loaded_user_list.append(new_user)

    with open('storage/user_list', 'wb') as s:
        pickle.dump(loaded_user_list, s, protocol=pickle.HIGHEST_PROTOCOL)

    print(loaded_user_list)


def load_users():
    file_name = open('storage/user_list', 'rb')
    loaded_file = pickle.load(file_name)

    loaded_user_list = list(loaded_file)

    return loaded_user_list


def delete_users():
    new_user_list = []
    with open('storage/user_list', 'wb') as s:
        pickle.dump(new_user_list, s, protocol=pickle.HIGHEST_PROTOCOL)
