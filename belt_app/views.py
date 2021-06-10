from django.contrib import messages
from login_reg_app.models import *
from django.shortcuts import render, redirect

def friend(request):
    logged_user = User.objects.get(id=request.session["userid"])
    friends = logged_user.friends.all()
    users_friends = logged_user.user_friends.all()
    all_friends = friends | users_friends
    all_friends = all_friends.distinct()
    all_users = User.objects.all()

    context = {
        "user_info": User.objects.get(id=request.session["userid"]),
        "all_friends": all_friends,
        "all_users": all_users
    }
    return render(request, "friend.html", context)

def profile(request, user_id):
    context = {
        "user_info": User.objects.get(id=request.session["userid"]),
        "user":  User.objects.get(id=user_id)
    }
    return render(request, "profile.html", context)

def add_friend(request, user_id):
    # need to make POST
    add_friend = User.objects.get(id=request.session["userid"])
    
    add_friend.friends.add(User.objects.get(id=user_id))
    return redirect('/friend')

def remove_friend(request, user_id):
    remove_friend = User.objects.get(id=request.session["userid"])
    
    remove_friend.friends.remove(User.objects.get(id=user_id))
    return redirect('/friend')