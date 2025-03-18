from django.shortcuts import render

def index(request):
    return render(request, 'learning/index.html', {})

def main_page(request):
    return render(request, 'learning/main.html')

def about_page(request):
    return render(request, 'learning/about.html')

def lesson1(request):
    return render(request, 'learning/lesson1.html')

def lesson2(request):
    return render(request, 'learning/lesson2.html')

def practice1(request):
    return render(request, 'learning/practice1.html', {'title': 'Практическое задание 1', 'next_url': 'practice2'})

def practice2(request):
    return render(request, 'learning/practice2.html', {'title': 'Практическое задание 2', 'next_url': 'practice3'})

def practice3(request):
    return render(request, 'learning/practice3.html', {'title': 'Практическое задание 3'})

def get_lesson(request, lesson_id):
    if not lesson_id or lesson_id == "null":
        return render(request, 'learning/practice1.html')
    
    template_path = f'learning/{lesson_id}.html'
    
    try:
        return render(request, template_path)
    except:
        return render(request, 'learning/practice1.html')

def get_practice(request, practice_id):
    return render(request, f'learning/{practice_id}.html')

def custom_404(request, exception):
    return render(request, "learning/404.html", status=404)

def error404(request):
    return render(request, "learning/404.html")