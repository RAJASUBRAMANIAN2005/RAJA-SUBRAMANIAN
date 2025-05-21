from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>Real-Time Order Status API</h1>
    <p>Welcome to the Order Status API. Available endpoints:</p>
    <ul>
        <li><a href="/admin/">Admin Interface</a></li>
        <li><a href="/api/">API Endpoints</a></li>
    </ul>
    """)