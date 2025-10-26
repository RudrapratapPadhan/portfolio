from django.shortcuts import render, get_object_or_404
from .models import Project, Education
from django.core.mail import send_mail


def home(request):
    return render(request, "portfolio/home.html")


def project(request):
    projects = Project.objects.all()
    education = Education.objects.all()
    context = {
        "projects": projects,
        "education": education,
    }

    return render(request, "portfolio/project.html", context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    # Get related projects (excluding current one)
    related_projects = Project.objects.exclude(pk=pk)[:3]
    context = {
        "project": project,
        "related_projects": related_projects,
    }
    return render(request, "portfolio/project_detail.html", context)


from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    context = {}
    
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if not all([name, email, message]):
            context["error"] = "Please fill out all fields."
        else:
            subject = f"📩 New Contact Message from {name}"
            body = (
                f"Hi Rudra,\n\n"
                f"You have received a new message from your portfolio contact form.\n\n"
                f"🧑 Name: {name}\n"
                f"📧 Email: {email}\n\n"
                f"💬 Message:\n{message}\n\n"
                f"— Portfolio Contact Form"
            )

            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    ["rudrapratappadhan2211@gmail.com"],
                    fail_silently=False,
                )
                context["success"] = "Your message has been sent successfully!"
            except Exception as e:
                print(e)
                context["error"] = "Sorry, something went wrong. Please try again later."

    return render(request, "portfolio/contact.html", context)

