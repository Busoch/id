from django.shortcuts import render, redirect
from .forms import FoundIDForm, LostIDReportForm
from .models import FoundID, LostIDReport
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FoundIDSerializer, LostIDReportSerializer



# Homepage
def home(request):
    return render(request, 'idFinder/home.html')

# Upload Found ID
def upload_found(request):
    if request.method == 'POST':
        form = FoundIDForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoundIDForm()
    return render(request, 'idFinder/upload_found.html', {'form': form})

# Report Lost ID
def report_lost(request):
    if request.method == 'POST':
        form = LostIDReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LostIDReportForm()
    return render(request, 'idFinder/report_lost.html', {'form': form})

# View/Search Found IDs
def found_list(request):
    query = request.GET.get('query', '')
    found_ids = FoundID.objects.filter(approved=True)

    if query:
        found_ids = found_ids.filter(
            Q(name_on_id__icontains=query) |
            Q(location_found__icontains=query)
        )

    return render(request, 'idFinder/found_list.html', {'found_ids': found_ids})

def view_lost_reports(request):
    reports = LostIDReport.objects.all().order_by('-reported_at')
    return render(request, 'idFinder/lost_reports.html', {'reports': reports})

def search_suggestions(request):
    query = request.GET.get('q', '')
    if query:
        results = FoundID.objects.filter(
            Q(name_on_id__icontains=query) | Q(location_found__icontains=query)
        ).values('name_on_id', 'location_found')[:5]
        suggestions = list(results)
    else:
        suggestions = []
    return JsonResponse(suggestions, safe=False)

@api_view(['GET', 'POST'])
def found_id_api(request):
    if request.method == 'GET':
        found = FoundID.objects.filter(approved=True)
        serializer = FoundIDSerializer(found, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FoundIDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def lost_id_api(request):
    if request.method == 'GET':
        lost = LostIDReport.objects.all().order_by('-reported_at')
        serializer = LostIDReportSerializer(lost, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LostIDReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
