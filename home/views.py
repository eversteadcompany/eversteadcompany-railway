# from django.shortcuts import render

# def home_view(request):
#     return render(request, 'home/index.html')

# def about_view(request):
#     return render(request, 'home/about.html')


# def contact_view(request):
#     return render(request, 'home/contact.html')

# def investment_view(request):
#     return render(request, 'home/investment.html')



# from utils.email_utils import send_resend_email

# def send_test(request):
#     send_resend_email(
#         to="vanessavaldezwhite@gmail.com",
#         subject="Test Email from Resend API",
#         html="<h2>Hello!</h2><p>Your Resend API is working.</p>"
#     )
#     return HttpResponse("Email sent!")



from django.http import HttpResponse
from django.shortcuts import render

# --- Basic pages ---
def home_view(request):
    return render(request, 'home/index.html')

def about_view(request):
    return render(request, 'home/about.html')

def contact_view(request):
    return render(request, 'home/contact.html')

def investment_view(request):
    return render(request, 'home/investment.html')


# --- Email test view ---
from utils.email_utils import send_resend_email

def send_test(request):
    try:
        send_resend_email(
            to="vanessavaldezwhite@gmail.com",
            subject="Test Email from Resend API",
            html="<h2>Hello!</h2><p>Your Resend API is working.</p>"
        )
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Email failed: {e}", status=500)
