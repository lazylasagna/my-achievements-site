from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from .forms import AchievementForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Achievement, Review
from .forms import ReviewForm


def achievements_list(request):
    advantages = Achievement.objects.all().order_by('-created_at')
    return render(request, 'achievements/achievements_list.html', {'advantages': advantages})


def achievement_detail(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    likes = achievement.likes.all()
    return render(request, 'achievements/achievement_detail.html', {'achievement': achievement, 'likes': likes})


def achievement_detail(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    reviews = achievement.reviews.all().order_by('-created_at')  # Отзывы в обратном порядке

    form = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.achievement = achievement
                review.user = request.user
                review.save()
                return redirect('achievements:achievement_detail', pk=pk)
        else:
            form = ReviewForm()

    return render(request, 'achievements/achievement_detail.html', {
        'achievement': achievement,
        'reviews': reviews,
        'form': form,
    })


@staff_member_required
def add_achievement(request):
    if request.method == 'POST':
        form = AchievementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('achievements:achievements_list')
    else:
        form = AchievementForm()
    return render(request, 'achievements/achievement_form.html', {'form': form})


@staff_member_required
def edit_achievement(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
        form = AchievementForm(request.POST, instance=achievement)
        if form.is_valid():
            form.save()
            return redirect('achievements:achievements_list')
    else:
        form = AchievementForm(instance=achievement)
    return render(request, 'achievements/achievement_form.html', {'form': form})


@staff_member_required
def delete_achievement(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
        achievement.delete()
        return redirect('achievements:achievements_list')
    return render(request, 'achievements/achievement_confirm_delete.html', {'achievement': achievement})


@login_required
def like_achievement(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)

    already_liked = achievement.likes.filter(user=request.user).exists()

    if already_liked:
        achievement.likes.filter(user=request.user).delete()
        liked = False
    else:
        achievement.likes.create(user=request.user)
        liked = True

    return JsonResponse({
        'likes': achievement.likes.count(),
        'liked': liked
    })
