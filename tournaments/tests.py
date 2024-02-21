from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Certificate, CertificateUser, TournamentUser, Tournament
from datetime import date


# Create your tests here.
class TestCertificate(TestCase):
    def setUp(self):
        self.test_certificate = Certificate.objects.create(Title="Completion of course", topic="python")

    def test_certificate_creation(self):
        self.assertEqual(self.test_certificate.Title, "Completion of course")
        self.assertEqual(self.test_certificate.topic, "python")


class CertificateUserTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username="jashan", password="xyz")
        self.certificate = Certificate.objects.create(Title="Completion of course", topic="python")

        self.certificate_data = CertificateUser.objects.create(
            user=self.user,
            certificate=self.certificate,
            Attained=False,
        )

    def test_creation_certificate_user(self):
        self.assertEqual(self.certificate_data.user, self.user)
        self.assertEqual(self.certificate_data.certificate, self.certificate)
        self.assertFalse(self.certificate_data.Attained)

    def test_status_change(self):
        self.certificate_data.Attained = True
        self.certificate_data.save()
        updated_status = CertificateUser.objects.get(id=self.certificate_data.id)
        self.assertTrue(updated_status.Attained)


class TournamentTest(TestCase):
    def setUp(self):
        self.tournament_data = Tournament.objects.create(
            Title="Tournament",
            Photo="image",
            StartDate=date(2024, 1, 9),
            EndDate=date(2024, 1, 19),
            Description="Jashnapreet owned this",
            MinLevel=20,
            MaxLevel=40,
            Reward1="$ 1000",
            Reward2="$ 1000",
            Reward3="$ 1000"
        )

    def test_creation(self):
        self.assertEqual(self.tournament_data.Title, "Tournament")
        self.assertEqual(self.tournament_data.Photo, "image")
        self.assertEqual(self.tournament_data.StartDate, date(2024, 1, 9))
        self.assertEqual(self.tournament_data.EndDate, date(2024, 1, 19))
        self.assertEqual(self.tournament_data.Description, "Jashnapreet owned this")
        self.assertEqual(self.tournament_data.MinLevel, 20)
        self.assertEqual(self.tournament_data.MaxLevel, 40)
        self.assertEqual(self.tournament_data.Reward1, "$ 1000")
        self.assertEqual(self.tournament_data.Reward2, "$ 1000")
        self.assertEqual(self.tournament_data.Reward3, "$ 1000")


class TournamentUserTest(TestCase):
    def setUp(self):
        self.tournament_data = Tournament.objects.create(
            Title="Tournament",
            Photo="image",
            StartDate=date(2024, 1, 9),
            EndDate=date(2024, 1, 19),
            Description="Jashnapreet owned this",
            MinLevel=20,
            Reward1="$ 1000",
            Reward2="$ 1000",
            Reward3="$ 1000"
        )
        self.user = get_user_model().objects.create_user(username="jashan", password="xyz")

        self.data = TournamentUser.objects.create(
            Tournament=self.tournament_data,
            user=self.user,
            participated=False
        )

    def test_creation(self):
        self.assertEqual(self.data.Tournament, self.tournament_data)
        self.assertEqual(self.data.user, self.user)
        self.assertFalse(self.data.participated)

    def test_status_change(self):
        self.data.participated = True
        self.data.save()
        updated_data = TournamentUser.objects.get(id=self.data.id)
        self.assertTrue(updated_data.participated)
