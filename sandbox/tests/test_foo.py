import pytest

def test_foo():
  assert 1== 1

@pytest.mark.django_db
def test_db():
  from sandbox.apps.corgi.models import Corgi
  assert Corgi.objects.count() == 0
  corgi = Corgi(name='Mollie', weight=25)
  corgi.save()

  assert Corgi.objects.count() == 1
  print Corgi.objects.get(name='Mollie').weight
