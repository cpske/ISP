# Add a user to database.
# To run: python3 manage.py shell < thisscript.py
from django.contrib.auth.models import User

# makeusers.py 
from django.contrib.auth.models import User
# use any username & password that you like 
for (username, pw) in [("harry", "hacker1"),
                       ("sally", "hacker2")]: 
    print(f"add user {username} with {pw}")
    try:
        User.objects.create_user(username, password=pw)
    except Exception as e:
        print(e)
print("All Users:")
for user in User.objects.all():
    print(user.username)
