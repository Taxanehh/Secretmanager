# Installatie Handleiding Flask

Dit is de handleiding om Flask teinstalleren op je laptop.
Deze installatie gaat uit van een up to date Windows 10, Windows 11 of MacOS systeem.
De Python moeten geinstalleerd zijn.
`
## Flask

Een essentieel onderdeel van de captive portal die jullie ntwikkelen is de website waar gebruikers kunnen inloggen
om toegang te krijgen tot hun eieg secrets. Eerder in het project hebben jullie al een (simpele) website gebouwd met HTML en CSS. 
Echter, deze website miste een aantal essentiële onderdelen: zo was het niet vereist dat de website automatisch toegang gaf succesvol inloggen, 
en hoefde inlog-gegevens niet gecontroleerd te worden in een database.
 
Met het implementeren van Flask op je access point zet je de volgende stap naar het eindproduct, waarin deze functionaliteiten wél werken. Maar… Wat is Flask eigenlijk?
Simpel gezegd is Flask een basis waarop je een website kan bouwen, op dezelfde manier dat je een website kan bouwen met WordPress of Django. 
Die basis bevat veel van de standaard functionaliteiten van een website waarvan het niet nodig is dat developers die voor elke website opnieuw ontwikkelen. 
Zo'n basis wordt ook wel een framework genoemd: een softwareoplossing die je een structuur biedt waarop je een programma of applicatie kan bouwen. 
In dit geval bestaat die structuur uit de onderdelen die je nodig hebt om een website te draaien, zoals een onderdeel wat HTTP(S) requests afhandelt (Werkzeug), 
een onderdeel wat op basis van templates een dynamische front-end genereert (Jinja2), en een manier om cookies op te slaan en te beveiligen (ItsDangerous). 
Al deze onderdelen worden met elkaar verbonden via Python-code, die je zelf gaat schrijven voor dit project. 
Deze code regelt dat de juiste pagina wordt geladen als een gebruiker een URL opvraagt, verifieert inloggegevens, 
en kan zelfs communiceren met het operating system indien nodig. 

Dit hoeft geen complexe code te zijn – bij voorkeur niet zelfs – en je kan de meeste basis-functionaliteiten schrijven met de Python-kennis die je hebt opgedaan met de Learning Story Python. 
De rest van de kennis om de website volledig werkend te krijgen doe je op tijdens deze handleiding, en door zelf op onderzoek uit te gaan op het internet.
De website die je gaat bouwen is officieel een web application. Web applications hebben een web server nodig om op te draaien. 
Flask heeft de mogelijkheid om een eigen server op te zetten, dit is een development server. 

## Installatie Windows/MacOS

### Installateer Flask ###

Installeer de python flask module met pip:

``` bash
pip install flask
```


### Maak een Flask Hello World applicatie ###

Kies de volgende structuur voor de Flask secrets applicatie:

```
└───webapp
    └───secretsapp
        ├───static
        │   └───css
        └───templates
```

``maak in de secretsapp directory eem file met de naam `__init__.py` met de volgende inhoud:``

``` python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

```

### Test de Flask Hello World applicatie ###

Nu heb je een Flask applicatie gemaakt. Deze applicatie draai je met het volgende commando 

``` bash
python -m flask run --app secretsapp --debug
```
of

``` bash
python3 -m flask run --app secretsapp --debug
```
of
``` bash
flask run --app secretsapp --debug
```

Kies welke commando het beste voor jou werkt.

Flask toont dan ongeveer de volgende informatie:

``` bash
 * Serving Flask app 'webapp'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 ```
 
 Ga met je webbrowser maar  http://127.0.0.1:5000 en controleer of de Hello World Webapplicatie werkt.
 
 Sluit de Flask applicatie met Crtl-C (of Cmd-C). 

**In het geval je een herinstallatie doet controleer dat "show only new options" uitstaat.**


## Installatie MacOS

Installeer docker
    - Voer het volgende commando uit:
    ```brew install docker``