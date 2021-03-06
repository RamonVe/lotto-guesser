from tkinter import messagebox as m
import json
import os


# This function saves a new user to a user list file via the pickle package.
def save_user(new_user):
    with open('storage/user_list.txt', 'a+') as file:
        json_user = json.dumps(new_user.__dict__)
        file.write(str(json_user) + '\n')

    with open('storage/practice_tests/' + new_user.username + '_practice_test_storage.txt', 'a+') as f:
        f.close()

    with open('storage/future_tests/' + new_user.username + '_future_test_storage.txt', 'a+') as f:
        f.close()

    with open('storage/future_tests/' + new_user.username + '_future_test_results_storage.txt', 'a+') as f:
        f.close()

    m.showinfo('Success!', new_user.username + ' has been successfully registered!')


# This function loads the user list.
def load_users():
    f = open('storage/user_list.txt', "r")
    users = f.readlines()

    return users


# This function deletes all saved users and creates a new user list file.
# Currently, this function is not implemented.
def delete_users():
    os.remove('storage/user_list.txt')


def save_practice_test(user, practice_test):
    with open('storage/practice_tests/' + user.username + '_practice_test_storage.txt', 'a') as f:
        json_practice_test = json.dumps(practice_test.__dict__)
        f.write(str(json_practice_test) + '\n')


# This function saves a future test for the logged-in user.
# Each user will have their own file.
def save_future_test(user, future_test):
    with open('storage/future_tests/' + user.username + '_future_test_storage.txt', 'a') as f:
        json_future_test = json.dumps(future_test.__dict__)
        f.write(str(json_future_test) + '\n')


def save_future_test_results(user, future_test):
    with open('storage/future_tests/' + user.username + '_future_test_results_storage.txt', 'a') as f:
        json_future_test = json.dumps(future_test.__dict__)
        f.write(str(json_future_test) + '\n')
