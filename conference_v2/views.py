
from rest_framework import viewsets, generics
from conference_v2.models import Presentation, Room, Schedule
from conference_v2.serializers import PresentationSerializer, RoomSerializer, ScheduleSerializer


class PresentationViewSet(viewsets.ModelViewSet):
    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer



