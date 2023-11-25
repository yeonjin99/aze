from django.shortcuts import render, redirect
from users.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_check = authenticate(username=username, password=password)
        if user_check is not None:
            login(request, user_check)
            user_info = User.objects.get(username=username)
            request.session['user'] = user_info.id
            return redirect('yes')
        else:
            return render(request, '01login.html', {'error': '아이디 혹은 비밀번호가 일치하지 않습니다.'})
    else:
        return render(request, "01login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        nickname = request.POST['nickname']
        email = ''

        if password == password_confirm:
            user = User.objects.create_user(username, email, password)
            user.nickname = nickname
            user.save()

            return redirect("login")

        else:
            return render(request, "01signup.html", {"error": "비밀번호가 일치하지 않습니다."})
    elif request.method == 'GET':
        return render(request, '01signup.html')
