from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated  
from .serializers import UserSerializer, NoteSerializer          
from .models import Note


#  List and Create notes (only for logged-in users)
class NoteListCreate(generics.ListCreateAPIView):  
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]         

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


#  Delete note (only for logged-in users)
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)  # ✅ This ensures users can only delete their own notes



class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
