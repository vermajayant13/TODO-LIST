from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItem

def todoview(request):
    all_todo_items= TodoItem.objects.all()
    return render(request,'todo.html',{'all_items':all_todo_items})

def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')
def deleteTodo(request,todo_id):

    c=TodoItem.objects.get(id=todo_id)
    c.delete()
    return HttpResponseRedirect('/todo/')
