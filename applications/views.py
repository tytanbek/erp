from django.shortcuts import render, redirect
from .models import Direction, TimeSlot, Application
from django.db.models import Count
from django.utils import timezone
from datetime import date


def statistics(request):
    total_applications = Application.objects.count()

    today = date.today()
    today_applications = Application.objects.filter(
        created_at__date=today
    ).count()

    by_direction = Application.objects.values(
        'direction__name'
    ).annotate(
        total=Count('id')
    )

    by_time = Application.objects.values(
        'time_slot__time'
    ).annotate(
        total=Count('id')
    )

    latest_applications = Application.objects.order_by('-created_at')[:10]

    return render(request, 'statistics.html', {
        'total_applications': total_applications,
        'today_applications': today_applications,
        'by_direction': by_direction,
        'by_time': by_time,
        'latest_applications': latest_applications,
    })

from django.shortcuts import get_object_or_404, redirect

def application_detail(request, pk):
    application = get_object_or_404(Application, pk=pk)

    if request.method == "POST":
        new_status = request.POST.get("status")

        if new_status in ["pending", "approved", "rejected"]:
            application.status = new_status
            application.save()

        return redirect("application_detail", pk=pk)

    return render(request, "application_detail.html", {
        "application": application
    })



def application_form(request):
    directions = Direction.objects.all()
    time_slots = TimeSlot.objects.all()

    if request.method == 'POST':
        Application.objects.create(
            full_name=request.POST['full_name'],
            phone=request.POST['phone'],
            direction_id=request.POST['direction'],
            time_slot_id=request.POST['time_slot']
        )
        return redirect('success')

    return render(request, 'application_form.html', {
        'directions': directions,
        'time_slots': time_slots
    })


def success_page(request):
    return render(request, 'success.html')
