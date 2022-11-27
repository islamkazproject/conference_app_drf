from rest_framework import serializers

from conference_v2.models import Presentation, Room, Schedule, UserScheduleRelation


class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = ("id", "title", "content")


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("id", "room_number")


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


class UserScheduleRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserScheduleRelation
        fields = ("id", "user", "schedule", "registration")
