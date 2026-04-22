from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client, SignIn, Campaign
from .serializers import ClientSerializer, SignInSerializer, CampaignSerializer

# Create your views here.
def home(request):
    return HttpResponse("Hello world!")



# API function views (submit)

'''
@api_view(['GET','POST'])
def add_client(request):

    # data submit from frontend
    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            print("Client Added Successfully")
            print("Data:", serializer.data)

            return Response(serializer.data, status=200)

        print("Error:", serializer.errors)
        return Response(serializer.errors, status=400)
    return Response(serializer.data)
'''
# Add client API function
@api_view(['POST'])
def add_client(request):

    serializer = ClientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        print("Client Added Successfully")
        print("Data:", serializer.data)

        return Response(serializer.data, status=200)

    print("Error:", serializer.errors)
    return Response(serializer.errors, status=400)


# API views function (Fetch)
@api_view(['GET'])
def client_list(request):

    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)

    return Response(serializer.data)


# Sign in Api view function
@api_view(['POST'])
def signin(request):
    
    email = request.data.get('email')
    password = request.data.get('password')


    try:
        user = SignIn.objects.get(email=email, password=password)

        return Response({
            "status": True,
            "message": "Login Success",
            "data": {"email": user.email}})

    except SignIn.DoesNotExist:
        return Response({
            "status": False,
            "message": "Invalid Credentials"})


# Campaign API view function

@api_view(['POST'])
def add_campaign(request):
    serializer = CampaignSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        print("Campaign Added Successfully")
        print("Data:", serializer.data)

        return Response(serializer.data, status=200)

    print("Error:", serializer.errors)
    return Response(serializer.errors, status=400)

# Get campaign

@api_view(['GET'])
def campaign_list(request):

    campaigns = Campaign.objects.all()
    serializer = CampaignSerializer(campaigns, many=True)

    return Response(serializer.data)
