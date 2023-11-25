from django.shortcuts import render, redirect
from .models import Board
from users.models import User
from django.utils import timezone

# Create your views here.


def index(request):
    return render(request, "borad_index.html", {'list':Board.objects.all()})

def detail(request, id):
    user = request.session.get('user')
    user_id = User.objects.get(pk=user)
    print(user_id.nickname)
    return render(request, "board_detail.html", {'dto': Board.objects.get(id=id), 'user_id' : user_id.nickname})

def insert(request):
    if request.method == 'GET':
        user = request.session.get('user')
        user_id = User.objects.get(pk=user)
        print(user_id.nickname)
        return render(request, 'board_insert.html', {'nickname': user_id.nickname})
    elif request.method == 'POST':
        writer = request.POST['writer']
        title = request.POST['title']
        content = request.POST['content']
        write_date = timezone.now()

        result = Board.objects.create(writer=writer,
                                      title=title,
                                      content=content,
                                      write_date=write_date)
        if result:
            return redirect('index')
        else:
            return redirect('insert')
    else:
        return redirect('index')

def update(request, id):
    if request.method == 'GET':
        user = request.session.get('user')
        user_id = User.objects.get(pk=user)
        return render(request, 'board_update.html', {'dto': Board.objects.get(id=id), 'nickname':user_id.nickname})

    elif request.method == 'POST':
        user = request.session.get('user')
        user_id = User.objects.get(pk=user)

        if request.POST['writer'] == str(user_id.nickname):
            title = request.POST['title']
            content = request.POST['content']

            result = Board.objects.filter(id=id).update(title=title, content=content)

            if result == 1:
                return redirect(f'/board/detail/{id}')
            else:
                return redirect(f'/board/update/{id}')

        else:
            return redirect(f'/board/update/{id}')

    else:
        return redirect('index')

def delete(request, id):
    user = request.session.get('user')
    user_id = User.objects.get(pk=user)

    if Board.objects.get(id=id).writer == str(user_id.nickname):

        result = Board.objects.get(id=id).delete()

        if result[0]:
            return redirect('index')
        else:
            return redirect(f'/board/detail/{id}')

    else:
        return redirect(f'/board/detail/{id}')