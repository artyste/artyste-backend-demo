from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import product
import requests
import io
import json

@receiver(post_save, sender=product)
def create_product(sender, instance, created, **kwargs):
    if created:

        img_get = instance.fileimage.url

        img_url = requests.get(img_get)
        image = io.BytesIO(img_url.content)

        print('Pos - Img Downlaod')

        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweEY0OEI2NjBkMUQ3MEZGNDk1MjYzNjZDMkNDZERFNTExMzZFNWQ1NDEiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTYyODY2NzY0NjE4NywibmFtZSI6IlRlc3QifQ.MVf1uJHqsLPX6HTnZRrSi4VZYfJyS7zS1hNTiqCMUpg',
            'Content-Type': 'image/png',
        }

        try:
            response = requests.post('https://api.nft.storage/upload', headers=headers, data=image)
            response_json = response.json()
            print(response_json['value']['cid'])

            img_cid = response_json['value']['cid']
            instance.filehash = img_cid
            instance.save()

            print('produto criado id:', instance.id)

            # json_metadata = {
            #     "name": instance.title,
            #     "image": "https://" + img_cid + ".ipfs.dweb.link",
            #     "description": instance.description
            # }
            #
            # try:
            #     response_meta = requests.post('https://api.nft.storage/upload', headers=headers, data=json.dumps(json_metadata))
            #     response_meta_json = response_meta.json()
            #     metadata_cid = response_meta_json['value']['cid']
            #     instance.filemeta = metadata_cid
            #     instance.save()
            # except:
            #     print('Algo Ao salvar METADATA para StorageNFT')


        except:
            print('Algo Ao salvar arquivo para StorageNFT')
