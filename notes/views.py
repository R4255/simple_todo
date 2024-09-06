from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from .models import Note
from .serializers import NoteSerializer
from django.db.models import Q

class NoteCreateView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        if not request.data.get('title') or not request.data.get('body'):
            return Response({'detail': 'Title and body are required fields.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

class NoteDetailView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Note.DoesNotExist:
            raise NotFound({'detail': 'Note not found.'})

class NoteUpdateView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def update(self, request, *args, **kwargs):
        if not request.data.get('title') and not request.data.get('body'):
            return Response({'detail': 'At least one of title or body must be provided.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)

class NoteQueryView(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        title_substring = self.request.query_params.get('title', None)
        if title_substring:
            return Note.objects.filter(Q(title__icontains=title_substring))
        return Note.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({'detail': 'No notes found matching the criteria.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)