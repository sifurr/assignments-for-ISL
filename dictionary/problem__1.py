login_counts = {"admin": 5, "dev_user": 12, "guest_1": 1}

def record_login(user_dict, username):
    if username in user_dict:
        user_dict[username] = user_dict[username] + 1
    else:
        user_dict[username] = 1

    return user_dict


login_counts.update({"home_user": 3, "sys_admin": 10, "test_user": 33})
report = record_login(login_counts, "admin")
print(f"Records of all logins: {report}")
