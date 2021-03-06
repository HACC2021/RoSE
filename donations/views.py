from django.shortcuts import render
from .forms import DonationForm
from .models import Donation
import stripe
from roseHACC.settings import STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY
from django.contrib.auth.decorators import login_required

stripe.api_key = STRIPE_SECRET_KEY

@login_required
def donationsPage(request):
    # save donation to db
    form = DonationForm()
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            donation = Donation(
                user=request.user,
                amount=data['amount'],
            )
            donation.save()

            # charge the card
            charge = stripe.Charge.create(
                amount=donation.amount * 100,
                currency='usd',
                description='Donation',
                source=request.POST.get('stripeToken')
            )
        

    return render(request, 'donationsPage.html', {'form': form, "public_key":STRIPE_PUBLIC_KEY})



