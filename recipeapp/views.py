from django.shortcuts import render
import requests
import json

def home(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        api_url = f'https://api.api-ninjas.com/v1/recipe?query={query}'
        headers = {'X-Api-Key': '63qfH3dheCQoW5q8uMgwJA==QNt5XlbjOyNgzUrn'}
        
        try:
            api_request = requests.get(api_url, headers=headers)
            api = json.loads(api_request.content)
            if api:
                ingredients=api[0]['ingredients'].split('|')
                api[0]['ingredients']=ingredients
        except Exception as e:
            print(e)
        
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
