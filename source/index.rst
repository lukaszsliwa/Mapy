.. Project documentation master file, created by
   sphinx-quickstart on Tue Jun  1 16:09:00 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Dokumentacja projektu portalu dla ludzi aktywnych
*************************************************

Wstęp
=====

Portal dla ludzi aktywnych umożliwia umieszczenie trasy na mapie. Trasy są umieszczane i tworzone z wykorzystaniem :mod:`Google Maps API`.
Do generowania wykresów wykorzystywane jest :mod:`Google Chart API`. Sam projekt został stworzony w języku :mod:`Python` i :mod:`frameworku Django`. Projekt korzysta z bazy danych :mod:`sqlite3`.

Niniejsza dokumentacja została stworzona przy pomocy narzędzia :mod:`Sphinx`.

Wszelkie zmiany w kodzie były umieszczane w zdalnym repozytorium Git w serwisie `github <http://github.com/>`_.

Wymagania
=========

* Python 2.5.5 / 2.6.5
* Django 1.1.1 / 1.2.1
* SQLite 3.6.20
* przeglądarka z włączoną obsługą javascript oraz ciasteczek (ang. `cookies`)
* dostęp do internetu

Instalacja
==========

Projekt można pobrać bezpośrednio z `repozytorium <http://github.com/mrplum/Mapy/>`_::
  
  $ git clone git@github.com:mrplum/Mapy.git mapy
  $ easy_install django-pagination
  $ cd mapy
  $ python manage.py syncdb
  $ python manage.py runserver

Polecenie :mod:`python manage.py syncdb` tworzy potrzebne tabele.
Polecenie :mod:`python manage.py runserver` uruchamia wbudowany serwer django.

Moduł map -- maps
=================

Moduł :mod:`maps` odpowiada za tworzenie oraz przeglądanie map. Przy tworzeniu map wykorzystywane jest API Google Maps napisane w :mod:`JavaScript`. Na mapach możliwe są następujace operacje:
 * tworzenie ścieżki
 * tworzenie punktów

Każda mapa którą utworzy użytkownik może zostać zapisana w bazie danych.

Model
-----

.. automodule:: maps.models
   :members:

Formularz
---------

.. automodule:: maps.forms
   :members:

Widoki
------

.. automodule:: maps.views
   :members:


Moduł komentarzy do map -- comments
===================================

Komentarze umożliwiają wypowiadanie się użytkownikom pod mapami.

Model
-----

.. automodule:: comments.models
   :members:

Formularze
----------

.. automodule:: comments.forms
   :members:

Widoki
------

.. automodule:: comments.views
   :members:

Moduł profilów użytkownika -- profiles
======================================

Profile użytkownika zawierają podstawowe informacje na temat aktywności danego użytkownika.
Aktywność rozumiemy tutaj jako liczbę przebytych kilometrów, częstość przemierzania ulubionych
tras.

Formularze
----------

.. automodule:: profiles.forms
   :members:

Widoki
------

.. automodule:: profiles.views
   :members:

Moduł punktów na mapie -- points
================================

Moduł implementujący wyświetlanie punktów na mapie.

Model
-----

.. automodule:: points.models
   :members:

Formularz
---------

.. automodule:: points.forms
   :members:

Widoki
------

.. automodule:: points.views
   :members:

Moduł statystyk i wykresów -- stats
===================================

Moduł obsługuje przetwarzanie wyników, pokonanych kilometrów oraz generowanie 
wykresów na podstawie zebranych danych.

Model
-----

.. automodule:: stats.models
   :members:

Formularz
---------

.. automodule:: stats.forms
   :members:

Widoki
------

.. automodule:: stats.views
   :members:

Moduł ulubionych treści -- favorites
====================================

Moduł umożliwia odznaczanie istniejących w bazie danych rekordów jako ulubionych
dla określonych użytkowników. Moduł jest na tyle uniwersalny, że pozwala odznaczyć
dowolny typ obiektu: komentarz, mapę, wypowiedź, zdjęcie etc. Wykorzystywany jest
tutaj mechanizm tabel generycznych.

Zarządcy
--------

.. automodule:: favorites.managers
   :members:

Modele
------

.. automodule:: favorites.models
   :members:


