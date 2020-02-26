from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadsSerializer

# LeadViewSet
class LeadsViewSet(viewsets.ModelViewSet):
    # queryset = Lead.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = LeadsSerializer

    def get_query_set(self):
        return self.request.user.leads.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    