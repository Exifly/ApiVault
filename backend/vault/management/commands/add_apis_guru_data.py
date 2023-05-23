from django.core.management.base import BaseCommand
from vault.models import API, Category
import requests


class Command(BaseCommand):
   help = 'Populates API data from apis.guru'

   CATEGORY_MAPPING = {
        'financial': 'Finance',
        'entertainment': 'Entertainment',
        'customer_relation': 'Business',
        'cloud': 'Cloud Storage & File Sharing',
        'iot': 'Internet of Things',
        'location': 'Geocoding',
        'ecommerce': 'Shopping',
        'analytics': 'Data Analysis',
        'collaboration': 'Productivity',
        'email': 'Email',
        'forms': 'Data Validation',
        'machine_learning': 'Machine Learning',
        'time_management': 'Calendar',
        'hosting': 'Cloud Storage & File Sharing',
        'enterprise': 'Business',
        'social': 'Social',
        'backend': 'Development',
        'marketing': 'Advertising',
        'developer_tools': 'Development',
        'open_data': 'Open Data',
        'payment': 'Finance',
        'tools': 'Utilities',
        'messaging': 'Chat',
        'support': 'Customer Service',
        'education': 'Education',
        'project_management': 'Project Management',
        'telecom': 'Telephony',
        'search': 'Search',
        'media': 'Media',
        'security': 'Security',
        'text': 'Data Validation',
        'transport': 'Transportation',
        'storage': 'Cloud Storage & File Sharing',
        'monitoring': 'Monitoring',
        's': None
   }

   def handle(self, *args, **options):
      response = requests.get("https://api.apis.guru/v2/list.json")
      data = response.json()

      for api_data in data.values():
         for version_data in api_data['versions'].values():
               self._create_api_from_version_data(version_data)

   def _create_api_from_version_data(self, version_data):
      info = version_data['info']
      response_categories = info.get('x-apisguru-categories', [])
      if not response_categories:
         return

      category_name = self.CATEGORY_MAPPING.get(response_categories[0])
      if not category_name:
         return

      category = Category.objects.filter(name=category_name).first()
      if not category:
         return

      if API.objects.filter(name=info['title']).exists():
         return

      try:
         api = API(
            name=info['title'],
            auth='',
            cors=False,
            description=info.get('description', ''),
            https=True,
            category=category,
            url=version_data['link'],
            source='apis.guru'
         )
         api.save()
         self.stdout.write(self.style.SUCCESS(f'{api} API data populated successfully'))
      except Exception as ex:
         self.stdout.write(self.style.ERROR(f'{ex}'))


