from django.shortcuts import render
from django.views import View
from .models import *

class TopFootballView(View):
    def get(self, request):
        return render(request, 'index.html')

class ClubsView(View):
    def get(self, request, pk):
        club = Clubs.objects.filter(id=pk)
        data = {
            'clubs': club,
            'players': Player.objects.all()
        }
        return render(request, 'clubs.html', data)

class LatestTransferView(View):
    def get(self, request):
        data = {
            'transfer': Transfers.objects.all()
        }
        return render(request, 'latest-transfers.html', data)

class PlayersView(View):
    def get(self, request):
        data = {
            'players': Player.objects.all().order_by('-narx')
        }
        return render(request, 'players.html', data)

class U_PlayersView(View):
    def get(self, request):
        data = {
            'U20': Player.objects.filter(yosh__lte=20).order_by('-narx')
        }
        return render(request, 'U-20 players.html', data)

class TryoutsView(View):
    def get(self, request):
        return render(request, 'tryouts.html')

class StatsView(View):
    def get(self, request):
        return render(request, 'stats.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')

class EnglandView(View):
    def get(self, request):
        data = {
            'clubs': Clubs.objects.filter(davlat__startswith='Eng')
        }
        return render(request, 'england.html', data)

class NetherlandsView(View):
    def get(self, request):
        return render(request, 'netherlands.html')

class PredictionsView(View):
    def get(self, request):
        return render(request, '150-accurate-predictions.html')

class SeasonView(View):
    def get(self, request):
        return render(request, '2017-18season.html')

class Country_clubsView(View):
    def get(self, request):
        data = {
            'player': Player.objects.all().order_by('-narx')
        }
        return render(request, 'country-clubs.html', data)

class CoursesView(View):
    def get(self, request):
        return render(request, 'courses.html')

class OtherView(View):
    def get(self, request):
        return render(request, 'other.html')

class ExpenditureView(View):
    def get(self, request):
        return render(request, 'top-50-clubs-by-expenditure-in-2021.html')

class IncomeView(View):
    def get(self, request):
        return render(request, 'top-50-clubs-by-income-in-2021.html')

class Transfer_archiveView(View):
    def get(self, request):
        return render(request, 'transfer-archive.html')

class Transfer_recordsView(View):
    def get(self, request):
        data = {
            'record': Transfers.objects.filter(narx__gte=50).order_by('-narx')
        }
        return render(request, 'transfer-records.html', data)
