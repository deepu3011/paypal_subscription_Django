from django.shortcuts import render
from django.http import JsonResponse
from .models import Subscription
import uuid

def subscribe(request):
    return render(request, "subscribe.html")

def subscription_success(request):

    # Generate PayPal Request ID
    request_id = str(uuid.uuid4())

    subscription_id = request.GET.get("subscriptionID")

    if not subscription_id:
        return JsonResponse({"error": "Subscription ID missing"})

    Subscription.objects.create(
        email="testuser@gmail.com",
        subscription_id=subscription_id,
        plan="Premium"
    )

    return JsonResponse({
        "status": "Subscription stored successfully",
        "paypal_request_id": request_id
    })