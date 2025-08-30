from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Activity
from .serializers import ActivitySerializer
from .permissions import IsOwnerOrReadOnly
from django.db.models import Sum

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['activity_type', 'date']
    ordering_fields = ['date', 'duration_minutes', 'calories_burned']
    search_fields = ['activity_type']

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def metrics(self, request):
        qs = self.get_queryset()
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        if date_from:
            qs = qs.filter(date__gte=date_from)
        if date_to:
            qs = qs.filter(date__lte=date_to)
        totals = qs.aggregate(total_duration=Sum('duration_minutes'), total_distance=Sum('distance'), total_calories=Sum('calories_burned'))
        totals = {k: (v or 0) for k,v in totals.items()}
        return Response(totals)
