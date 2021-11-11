from django.shortcuts import redirect, render

from mytodos.forms import TodoForm
from mytodos.models import Todo

# from allauth.account.forms
# Create your views here.

def HomeView(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TodoForm()
    todo = Todo.objects.all()
    context = {'form': form, 'todo': todo}
    return render(request, 'index.html', context)


def UpdateView(request, id=id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'update.html', context)


def DeleteView(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('home')
