from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer

@api_view(['POST'])
def submit_wheel_specification(request):
    serializer = WheelSpecificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {
            "success": True,
            "message": "Wheel specification submitted successfully.",
            "data": {
                "formNumber": serializer.data['formNumber'],
                "submittedBy": serializer.data['submittedBy'],
                "submittedDate": serializer.data['submittedDate'],
                "status": "Saved"
            }
        }
        return Response(response, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_wheel_specifications(request):
    form_number = request.GET.get('formNumber')
    submitted_by = request.GET.get('submittedBy')
    submitted_date = request.GET.get('submittedDate')

    queryset = WheelSpecification.objects.all()

    if form_number:
        queryset = queryset.filter(formNumber=form_number)
    if submitted_by:
        queryset = queryset.filter(submittedBy=submitted_by)
    if submitted_date:
        queryset = queryset.filter(submittedDate=submitted_date)

    serializer = WheelSpecificationSerializer(queryset, many=True)
    response = {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": serializer.data
    }
    return Response(response)
