from django.core.management.base import BaseCommand
from vault.models import API, Category
import requests

class Command(BaseCommand):
    help = 'Populates API data from an endpoint'

    def handle(self, *args, **options):
        # Make a GET request to the endpoint
        response = requests.get('https://api.apivault.dev//api/all')

        # Check if the request was successful
        if response.status_code == 200:
            api_data = response.json()
            self.populate_models(api_data)
            self.stdout.write(self.style.SUCCESS(f'DONE'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch API data'))

    def populate_models(self, api_data):
        # Iterate over the received API data
        for api_info in api_data:
            # Extract the information from the API object
            name = api_info['API']
            auth = api_info['Auth']
            category_name = api_info['Category']
            cors = api_info['Cors'].lower() == 'yes'
            description = api_info['Description']
            https = api_info['HTTPS']
            url = api_info['Link']

            # Find or create the corresponding category
            category, _ = Category.objects.get_or_create(name=category_name)

            # Create a new API object
            api = API(
                name=name,
                auth=auth,
                category=category,
                cors= True if cors == 'yes' else False,
                description=description,
                https=https,
                url=url,
                source = "public-apis"
            )
            api.save()
            self.stdout.write(self.style.SUCCESS(f'{api}API data populated successfully'))

