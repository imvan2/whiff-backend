from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .serializers import (
    PerfumeSerializer,
    DesignerSerializer,
    NoteSerializer,
    AccordSerializer,
)
from .models import Perfume, Designer, Note, Accord


# Create your views here.
class PerfumeListApiView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        """List all the perfumes"""
        perfumes = Perfume.objects
        serializer = PerfumeSerializer(perfumes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        """Create the Perfume with given perfume data"""
        data = {
            "name": request.data.get("name"),
            "image": request.data.get("image"),
            "designer": request.data.get("designer"),
            "summary": request.data.get("summary"),
            "tags": request.data.get("tags"),
            "notes": request.data.get("notes"),
            "accords": request.data.get("accords"),
            "likes": request.data.get("likes"),
            "dislikes": request.data.get("dislikes"),
        }

        serializer = PerfumeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DesignerListApiView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        """List all the perfumes"""
        designers = Designer.objects
        serializer = DesignerSerializer(designers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NoteListApiView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        """List all the perfumes"""
        notes = Note.objects
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccordListApiView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        """List all the perfumes"""
        accords = Accord.objects
        serializer = AccordSerializer(accords, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
