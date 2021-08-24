from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserAccount
import requests
import io
import json
import uuid
import os

@receiver(post_save, sender=UserAccount)
def create_product(sender, instance, created, **kwargs):
    if created:

        CIRCLEAPIKEY = os.getenv('ARTHOLOGY_CIRCLE_SANDBOX')
        UUIDGEN = uuid.uuid4()

        url = 'https://api-sandbox.circle.com/v1/wallets'

        headers = {
            'Accept': 'application/json',
            'Authorization': "Bearer " + CIRCLEAPIKEY,
        }

        data = '{"idempotencyKey": "' + str(UUIDGEN) + '"}'
        try:

            responseCircle = requests.get(url, headers=headers, data=data)
            responseCircleJson = responseCircle.json()


            instance.circle_walletId = responseCircleJson['data'][0]['walletId']
            instance.circle_entityId = responseCircleJson['data'][0]['entityId']
            instance.save()

            print(responseCircleJson)

        except:
            print('erro create circle wallet')