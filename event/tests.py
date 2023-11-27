from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.utils import timezone
from register.models import CustomUser
from .models import Events, EventCategory, Ticket


class EventViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create_user(
           username='testuser',
           password='testpassword',
           email='test@example.com',
           isPromoter=True
           )
        self.category = EventCategory.objects.create(name='Test Category')
        self.event_start_date = timezone.make_aware(timezone.datetime.strptime('2023-01-01T12:00', "%Y-%m-%dT%H:%M"))
        self.event_end_date = timezone.make_aware(timezone.datetime.strptime('2023-01-02T12:00', "%Y-%m-%dT%H:%M"))

        self.event = Events.objects.create(
            name='Test Event',
            address='123 Test St',
            start_date=self.event_start_date,
            end_date=self.event_end_date,
            description='Description of the event',
            capacity=100,
            image='eventos/test_event.jpg',
            category=self.category,
            promoter=self.user
        )
        self.ticket = Ticket.objects.create(event=self.event, ticket_price=50.0, qtd_ticket=100)

    def test_view_event(self):
        response = self.client.get(reverse('viewEvent', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pagina_evento.html')

    def test_list_event_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('listEvent'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meuseventos.html')

 

    def test_edit_event(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'nameEvent': 'Updated Event Name',
            'address': '456 Updated St',
            'start_date': '2023-02-01T12:00',
            'end_date': '2023-02-02T12:00',
            'description': 'Updated Description',
            'capacity': 150,
            'ticketPrice': 60.0,
        }
        response = self.client.post(reverse('editEvent', args=[self.event.id]), data)
        self.assertEqual(response.status_code, 302)
        updated_event = Events.objects.get(id=self.event.id)
        self.assertEqual(updated_event.name, 'Updated Event Name')
        self.assertEqual(updated_event.address, '456 Updated St')
        self.assertEqual(updated_event.capacity, 150)
        updated_ticket = Ticket.objects.get(event=self.event)
        self.assertEqual(updated_ticket.ticket_price, 60.0)

    def test_delete_event(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delEvent', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Events.objects.filter(id=self.event.id).exists())
        self.assertFalse(Ticket.objects.filter(event=self.event).exists())