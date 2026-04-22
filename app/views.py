from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client, SignIn, Campaign
from .serializers import ClientSerializer, SignInSerializer, CampaignSerializer


# Home
def home(request):
    return HttpResponse("Hello world!")


# Add client
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


# Client list
@api_view(['GET'])
def client_list(request):

    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)

    return Response(serializer.data)


# Signin
@api_view(['POST'])
def signin(request):
    
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = SignIn.objects.get(email=email, password=password)

        return Response({
            "status": True,
            "message": "Login Success",
            "data": {"email": user.email}
        })

    except SignIn.DoesNotExist:
        return Response({
            "status": False,
            "message": "Invalid Credentials"
        })


# Add Campaign
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


# Campaign List
@api_view(['GET'])
def campaign_list(request):

    campaigns = Campaign.objects.all()
    serializer = CampaignSerializer(campaigns, many=True)

    return Response(serializer.data)


# Update Campaign (Using campaign_id)
@api_view(['PUT'])
def update_campaign(request, campaign_id):

    try:
        campaign = Campaign.objects.get(campaign_id=campaign_id)

    except Campaign.DoesNotExist:
        return Response({
            "status": False,
            "message": "Campaign not found"
        })

    serializer = CampaignSerializer(
        campaign,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()

        return Response({
            "status": True,
            "message": "Campaign Updated Successfully",
            "data": serializer.data
        })

    return Response({
        "status": False,
        "errors": serializer.errors
    })