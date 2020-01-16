=============
Beheerconsole
=============

:Version: 0.1.0
:Source: https://github.com/GemeenteUtrecht/beheerconsole
:Keywords: processen, applicaties, beheer, micro services
:PythonVersion: 3.8

|build-status| |coverage| |black|

Krijg inzicht in applicaties & processen in gebruik bij de gemeente.

Developed by `Maykin Media B.V.`_ for Gemeente Utrecht.

Introduction
============

`Common Ground`_ zet in op een nieuwe, moderne gezamenlijke informatievoorziening. In
het 5-lagen model van Common Ground worden gegevens gescheiden van Interactie en proces,
waarbij gegevens via Services/APIs ontsloten worden.

Dit leidt tot een landschap waarin *processen* en *micro-services* uitgewisseld kunnen
worden. Een setje applicaties kan één of meerdere processen ondersteunen. Echter, het
opbreken van monolitische silo's kan leiden tot verlies van overzicht.

De beheerconsole centraliseert dit overzicht - je kan een inventaris bijhouden van welke
applicaties je gebruikt binnen je organisatie, en welke processen er spelen. Daarnaast
kan je vastleggen welke processen van welke applicaties gebruik maken.

Features
--------

* vastleggen van basisgegevens van processen
* vastleggen basisgegevens applicaties, met classificatie binnen het 5-lagenmodel
* relateren van processen en applicaties
* koppeling van processen met het achterliggende Camunda BPMN-proces

Geplande features
-----------------

* opnemen systematisch overzicht
* introspectie van applicatie-configuratie via een API
* versionering van processen
* ADFS-koppeling voor beheerderslogin

References
==========

* `Issues <https://github.com/GemeenteUtrecht/beheerconsole/issues>`_
* `Code <https://github.com/GemeenteUtrecht/beheerconsole>`_

.. |build-status| image:: https://travis-ci.org/GemeenteUtrecht/beheerconsole.svg?branch=master
    :alt: Build status
    :target: https://travis-ci.org/GemeenteUtrecht/beheerconsole

.. |coverage| image:: https://codecov.io/github/GemeenteUtrecht/beheerconsole/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage
    :target: https://codecov.io/gh/GemeenteUtrecht/beheerconsole

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. _Maykin Media B.V.: https://www.maykinmedia.nl
.. _Common Ground: https://commonground.nl/
