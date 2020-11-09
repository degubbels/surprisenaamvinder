from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from naamvinder.serializers import NaamSerializer
from naamvinder.models import Naam, Config

from django.core.mail import send_mail
import copy

def sendResultEmail(naam):
    
    send_mail(
        "Surprise naam bekend",
        "Hey pap,\n\n" \
            "Iedereen heeft een naam ingevuld en er is er een over gebleven, jij hebt " + str(naam) + ".\n\n" \
            "Succes!",
        'surprisenaamvinder@gmail.com',
        [Config.get_solo().destinationEmail],
        fail_silently=False
    )

class NaamAPI(APIView):
    """
    Naam van een van de surprisedeelnemers
    """

    def post(self, request):

        if Config.get_solo().selfDestroyed:
            return

        serializer = NaamSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            # Send the last name to hans
            if Naam.objects.all().count() >= 6:

                names = copy.deepcopy(Config.get_solo().deelnemers)
                
                # Figure out the missing name
                for naam in [n.naam for n in Naam.objects.all()]:
                    names.remove(naam)
                
                if len(names) > 1:
                    return Response("Ongeldig aantal deelnemers over na eliminatie", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    sendResultEmail(names[0])
                    Naam.objects.all().delete()
                    Config.get_solo().destroy()
                    return Response("Email naar Hans verstuurd, zelfvernietiging in 5 seconden.", status=status.HTTP_202_ACCEPTED)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class EnteredCountAPI(APIView):
    """
    Retrieve the amount of names entered so far
    """

    def get(self, request):

        if Config.get_solo().selfDestroyed:
            return

        return Response(Naam.objects.all().count())

def frontend(request):
    return render(request, 'index.html')