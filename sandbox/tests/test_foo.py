import pytest

def test_foo():
  assert 1== 1

from sandbox.apps.corgi.models import Corgi

@pytest.mark.django_db
def test_db():

  assert Corgi.objects.count() == 0
  corgi = Corgi(name='Mollie', weight=25,length=15, description='Best corgi')
  corgi.save()

  assert Corgi.objects.count() == 1
  corgi =  Corgi.objects.get(name='Mollie')
  assert corgi.length == 15
  assert corgi.description == 'Best corgi'

@pytest.mark.django_db
def test_again():

  assert Corgi.objects.count() == 0
  corgi = Corgi(name='Benny')
  corgi.save()
  assert Corgi.objects.count() == 1
