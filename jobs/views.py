from rest_framework import generics
from .serializers import JobSerializer
from .models import Job
from .permissions import IsOwnerOrReadOnly


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)  # new
    queryset = Job.objects.all()
    serializer_class = JobSerializer
