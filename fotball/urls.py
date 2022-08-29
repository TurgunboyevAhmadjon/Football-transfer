from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', TopFootballView.as_view()),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('latest-transfers/', LatestTransferView.as_view()),
    path('players/', PlayersView.as_view()),
    path('U-players/', U_PlayersView.as_view()),
    path('tryouts/', TryoutsView.as_view()),
    path('stats/', StatsView.as_view()),
    path('about/', AboutView.as_view()),
    path('countries/england/', EnglandView.as_view()),
    path('countries/netherlands/', NetherlandsView.as_view()),
    path('150-accurate-predictions/', PredictionsView.as_view()),
    path('season/', SeasonView.as_view()),
    path('country-clubs/', Country_clubsView.as_view()),
    path('courses/', CoursesView.as_view()),
    path('countries/other/', OtherView.as_view()),
    path('top-50-clubs-by-expenditure-in-2021/', ExpenditureView.as_view()),
    path('top-50-clubs-by-income-in-2021/', IncomeView.as_view()),
    path('transfer-archive/', Transfer_archiveView.as_view()),
    path('transfer-records/', Transfer_recordsView.as_view()),

]
