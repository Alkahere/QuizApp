from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz  ,  UserProfile
from django.contrib.auth import logout
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Create UserProfile for the newly registered user
            UserProfile.objects.create(user=user)
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    
    return render(request, 'quiz/register.html', {'form': form})

def index(request):
    return render(request, 'quiz/index.html')






from django.shortcuts import render, get_object_or_404
from .models import Quiz

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_choice_id = request.POST.get(f"question_{question.id}")
            if selected_choice_id:
                selected_choice = question.choices.get(pk=selected_choice_id)
                if selected_choice.is_correct:
                    score += 1

        
        try:
            user_profile = request.user.userprofile
            user_profile.total_points += score
            user_profile.save()
        except UserProfile.DoesNotExist:
           
            pass

        return render(request, 'quiz/profile.html', {'quiz': quiz, 'score': score, 'total': questions.count()})
    
    username = request.user.username if request.user.is_authenticated else 'Guest'
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz, 'questions': questions, 'username': username})




def logout_view(request):
    logout(request)
    return redirect('index') 