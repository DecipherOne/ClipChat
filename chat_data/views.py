
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import PostMessage
from django.utils import timezone

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('messages/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
	
def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect('/account/login')
	else:
		return redirect('messages/')
		
	return render(request, 'index.html')
	
	
def post_message(request):
	if request.method == "POST":
		form = PostMessage(request.POST)
		if form.is_valid():
			message = form.save(commit=False)
			message.author_id = request.user.id
			message.date_time_created = timezone.now()
			message.save()
			#return redirect('post_detail', pk=post.pk)
	else:
		form = PostMessage()
		
	return render(request,'post_message.html', {'form':form})