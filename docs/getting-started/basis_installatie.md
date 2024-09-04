# Installatie Package Manager, Python en Visual Studio Code

Dit is de handleiding om de package manager en Visual Studio Code alles klaar te zetten om aan de slag te kunnen gaan. 
Deze gaat uit van een up to date Windows 10, Windows 11 of MacOS systeem.

De Package manager is nodig om alle instalaties eenvoudig en eenduidig te maken.

De volgende onderdelen worden als basis geinstalleerd.


Windows & MacOS:
- package manager (chocolatey of howmbrew)
- python (3.11+) - https://www.python.org/downloads/
- VScode - https://code.visualstudio.com/

Met deze onderdelen kan je de User story's van Sprint 2 uitvoeren. 

## Installatie Windows

### Chocolatey
De package manager voor windows is; Chocolatey (zie https://www.chocolatey.org )
De installatie van Chocolatey staat beschreven op https://www.chocolatey.org/install. 
Gebruik Windows PowerShell of Opdrachtprompt (als administrator uitvoeren) om de Installatie uit te voeren.
Kies de Chocolate "Individual Use" installatie.

Test Chocolatey met het volgende commando in PowerShell of Opdrachtprompt: '''choco'''

### Python

Installeer Python
Start de Terminal applicatie (Powershell) om de Installatie uit te voeren: ```choco install python```

Test Python met het volgende commando in de Terminal: ```python --version```

### Visual Studio Code

Installeer Visual Studio Code vanuit de Terminal applicatie: ```choco install VScode```

Zie onder voor de configuratie van VScode

## Installatie MacOS

### Homebrew
Installeer homebrew (zie https://brew.sh/)
Start de Terminal applicatie en voer het volgende commando uit:
```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```

Je zult je wachtwoord moeten invullen voor sudo access. 
Let op: De cursor zal niet niet verplaatsen waardoor het misschien lijkt alsof het niet werkt. Dit is zodat je je wachtwoord veilig kan intypen zonder dat mensen makkelijk kunnen afkijken.

Druk op Enter als dat gevraagd weordt.
Na de installatie volg de stappen aangegeven bij "Next steps". 
Dit zijn de volgende twee commando's:
 1. ```echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> ~/.zprofile``` Dit zorgt ervoor dat we het brew commando in de Terminal kunnen gebruiken.
 2. ```eval $(/opt/homebrew/bin/brew shellenv)``` Dit commando zorgt dat we de Terminal applicatie niet hoeven herstarten.
 
 Test homebrew met het volgende commando in de Terminal:
```brew help```

### Python

Download python3  - https://www.python.org/downloads/
Installeer python3

Test Python met het volgende commando in PowerShell of Opdrachtprompt: ```..> python3 --version```

### Visual Studio Code

``VScode hoeft niet specifiek geïnstalleerd te worden en wordt automatisch aan de launcher toegevoegd als we deze voor de eerste keer starten met `VScode```

## Configuratie VScode

Start nu de VScode applicatie. Het welkom scherm kan je doorlezen of direct afsluiten.

Als je Windows gebruikt krijg je een pop-up met de suggestie om de wsl extensie te installeren. Deze kan je negeren. 
VSCode zal veelvuldig extensies suggereren. Deze kunnen heel handig zijn, maar het is niet verstandig zomaar lukraak allerlei extensies te installeren.

Voor nu installeren we alleen de Python extensie. Ga naar het extension overzicht doormiddel van de snelkoppeling Ctrl+Shift+X (Cmd+Shift+X voor MacOS). Zoek op "Python" en klik hierop in de gegeven lijst. Je kan zien dat het de juiste extensie is aan het feit dat Microsoft als publisher staat aangegeven met een blauwe checkmark en het gegeven dat deze extensie (op het moment van het schrijven van deze handleiding) ruim 95 miljoen downloads heeft. Klik nu op de install knop. Herstart vscode indien gevraagd.

Je kunt veel functionaliteiten vinden via het command palette. Deze kun je openen door middel van F1 of Ctrl+Shift+P. (Cmd+Shift+P voor MacOS)

Voor nu willen een aantal instellingen veranderen. Type in het command palette (achter de >, verwijder deze niet) "User Settings" en druk op enter zodra de optie "Preferences: Open User Settings" geselecteerd staat.
- Type in de settings zoekbalk "telemetry". Kies vervolgens een telemetry niveau dat jij acceptabel vindt.
- Type vervolgens "Activate Env" in de settings zoekbalk. Je krijgt nu twee opties te zien. "Python › Terminal: Activate Env In Current Terminal" en "Python › Terminal: Activate Environment". Zorg dat bij beide een vinkje staat.
- Sluit nu het settings menu.

Vind meer snelkoppelingen op https://code.visualstudio.com/docs/getstarted/keybindings

Test VScode door een python programmabestand te maken met de naam **helloworld.py** met de volgende inhoud: ```print('Hello', 'World')```

Test het python progran met het volgende commando in de Terminal:
 ```..> python helloworld.py```

