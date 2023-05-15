from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .models import Subscription
import stripe
import json
from django.conf import settings
from django.views import View
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.


def home(request):
	return render(request,'accounts/main.html')




def success(request,):
	
	return render(request,'accounts/success.html')


def checkout(request):


	return render(request,'accounts/checkout.html')		



class StripeIntentView(View):
	def post (serlf,request, *args, **kwargs):
		try:
			
			# Create a PaymentIntent with the order amount and currency
			intent = stripe.PaymentIntent.create(
            amount='1000',
            currency='eur',
            automatic_payment_methods={
                'enabled': True,
            },
        )
			
			return JsonResponse({'clientSecret': intent['client_secret']})
		except Exception as e:
			return JsonResponse({ 'error': str(e) })
	


@csrf_exempt
def webhook():
    event = None
    payload = request.data

    try:
        event = json.loads(payload)
    except:
        print('⚠️  Webhook error while parsing basic request.' + str(e))
        return jsonify(success=False)
    #if endpoint_secret:
    #    # Only verify the event if there is an endpoint secret defined
    #    # Otherwise use the basic event deserialized with json
    #    sig_header = request.headers.get('stripe-signature')
    #    try:
    #        event = stripe.Webhook.construct_event(
    #            payload, sig_header, endpoint_secret
    #        )
    #    except stripe.error.SignatureVerificationError as e:
    #        print('⚠️  Webhook signature verification failed.' + str(e))
    #        return jsonify(success=False)

    # Handle the event
    if event and event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']  # contains a stripe.PaymentIntent
        print('Payment for {} succeeded'.format(payment_intent['amount']))
        # Then define and call a method to handle the successful payment intent.
        # handle_payment_intent_succeeded(payment_intent)
    elif event['type'] == 'payment_method.attached':
        payment_method = event['data']['object']  # contains a stripe.PaymentMethod
        # Then define and call a method to handle the successful attachment of a PaymentMethod.
        # handle_payment_method_attached(payment_method)
    else:
        # Unexpected event type
        print('Unhandled event type {}'.format(event['type']))

    return HttpResponse(status=200)
