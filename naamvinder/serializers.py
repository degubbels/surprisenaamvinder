from rest_framework import serializers
from naamvinder.models import Naam, Config


# Serializer for Naam
class NaamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Naam
        fields = ("naam", )

    def validate(self, data):
        """
        Surprise rules validation
        """

        # Ensure the name is known
        if not(data['naam'] in Config.get_solo().deelnemers):
            msg = "<naam_onbekend> hmm, " + data['naam'] + " staat niet in het lijstje. " \
                "De volgend namen zijn bekend: " + str(Config.get_solo().deelnemers)
            raise serializers.ValidationError(msg)

        # Ensure the name has not been entered before
        if data['naam'] in [n.naam for n in Naam.objects.all()]:
            raise serializers.ValidationError("<naam_al_geweest> Oh nee! Die naam is al door iemand anders ingevuld...")
        
        return data