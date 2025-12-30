from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import MessageSerializer
from nlp_engine.pipeline import EmergencyAIPipeline

# Initialize pipeline once (important)
pipeline = EmergencyAIPipeline("nlp_engine/data/messages.csv")


class AnalyzeMessageView(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        message = serializer.validated_data["message"]
        result = pipeline.analyze_message(message)

        return Response(result, status=status.HTTP_200_OK)
