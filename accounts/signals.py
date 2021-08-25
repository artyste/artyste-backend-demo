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
            'Content-Type': 'application/json',
        }

        data = '{"idempotencyKey": "' + str(UUIDGEN) + '"}'
        try:

            responseCircle = requests.get(url, headers=headers, data=data)
            responseCircleJson = responseCircle.json()
            get_circleWalletID = responseCircleJson['data'][0]['walletId']

            instance.circle_walletId = get_circleWalletID
            instance.circle_entityId = responseCircleJson['data'][0]['entityId']
            instance.save()

            url = 'https://api-sandbox.circle.com/v1/wallets/' + get_circleWalletID + '/addresses'

            try:
                UUIDGEN = uuid.uuid4()

                data = '{"chain": "ETH", "currency": "CUSDC", "idempotencyKey": "' + str(UUIDGEN) + '"}'

                responseCircleChain = requests.post(url, headers=headers, data=data)
                responseCircleChainJson = responseCircleChain.json()
                get_circleChain = responseCircleChainJson['data']['address']

                instance.circle_chainETH = get_circleChain
                instance.save()

            except:
                print('erro create circle chain')

            print(responseCircleJson)

        except:
            print('erro create circle wallet')