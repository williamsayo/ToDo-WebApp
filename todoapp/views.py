from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator 
from .models import Todo

def home(request):
    return render(request,'todoapp/home.html')

def todolist(request):
    if request.method == 'POST':
        activity1 = request.POST['activity']
        todo = Todo()
        todo.activity = activity1
        todo.date = request.POST['date']
        todo.save()
        
        messages.success(request,'Task Added successfully')
        return redirect('todolist')

    else:
        todo_list = Todo.objects.all().order_by('-date')

        paginate = Paginator(todo_list, 5)
        page = request.GET.get('page')
        todo_list  = paginate.get_page(page)


    context = {'todolists':todo_list,'date':timezone.now()}
    return render(request,'todoapp/todolist.html',context)

def mark(request,activity_id):
    activity = Todo.objects.get(pk=activity_id)

    if activity.completed == False:
        activity.completed = True
    else:
        activity.completed = False

    activity.save()
    return redirect('todolist')

def edit(request,activity_id):
    if request.method == 'POST':
        todo = Todo.objects.get(pk=activity_id)
        todo.activity = request.POST['activity']
        todo.date = request.POST['date']
        todo.completed = False

        todo.save()
        messages.success(request,'Task updated successfully')
        return redirect('todolist')

    else:
        todo = Todo.objects.get(pk=activity_id)
    
    context = {'todolist':todo}

    return render(request,'todoapp/edit.html',context)
    
def delete(request,activity_id):
    activity = Todo.objects.get(pk=activity_id)
    activity.delete()

    messages.success(request,'Task deleted successfully')
    return redirect('todolist')

# def filter(request):    
#     if request.method == 'POST':
#         val= request.POST['filter']
#         if val == 'all':
#             return redirect('todolist')

#         todolist = Todo.objects.filter(completed=val).order_by('-date')
#         if len(list(todolist)) > 5:
#             paginate = Paginator(todolist, 5)
#             page = request.GET.get('page')
#             todolist  = paginate.get_page(page)

#     else:
#         todolist = Todo.objects.filter(completed=val).order_by('-date')

#         paginate = Paginator(todolist, 5)
#         page = request.GET.get('page')
#         todolist  = paginate.get_page(page)

#     context = {'todolists':todolist,'date':timezone.now(),'val':val}
#     return render(request,'todoapp/todolist.html',context)


