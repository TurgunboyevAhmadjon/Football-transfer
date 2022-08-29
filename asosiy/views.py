from django.shortcuts import render
from django.views import View
from .models import *

class TopFootballView(View):
    def get(self, request):
        return render(request, 'index.html')

class ClubsView(View):
    def get(self, request):
        data = {
            'clubs': Clubs.objects.all(),
            'players': Player.objects.all()
        }
        return render(request, 'clubs.html', data)

class LatestTransferView(View):
    def get(self, request):
        return render(request, 'latest-transfers.html')

class PlayersView(View):
    def get(self, request):
        return render(request, 'players.html')

class U_PlayersView(View):
    def get(self, request):
        return render(request, 'U-20 players.html')

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
        return render(request, 'england.html')

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
            'clubs': Clubs.objects.all(),
            'clublar': Player.objects.all()
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
        return render(request, 'transfer-records.html')
