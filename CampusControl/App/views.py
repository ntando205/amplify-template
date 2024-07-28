from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render
import json

@method_decorator(csrf_exempt, name='dispatch')
class HomeView(View):

    def get(self, request):
        # Render the HTML template for the home view
        return render(request, 'index.html')

    def post(self, request):
        # Handle the AJAX request to receive the IP address
        try:
            data = json.loads(request.body)
            ip = data.get('ip')
            # Process the IP address as needed
            print(f"Received IP: {ip}")
            return JsonResponse({'status': 'success', 'ip': ip})
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
            print(f"Request body: {request.body}")
            return JsonResponse({'status': 'fail', 'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'fail', 'error': str(e)}, status=400)
