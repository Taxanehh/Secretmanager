# Installatie Handleiding Git

Dit is de handleiding om de Git teinstalleren op je laptop 
en verbinding te maken met Visual Studio Code.
Deze installatie gaat uit van een up to date Windows 10, Windows 11 of MacOS systeem.
De Package manager en Visual Studio moeten geinstalleerd zijn.

## Installatie Windows

Installeer git
    - Voer het volgende commando uit:
    ```choco install git```

## Installatie MacOS


Installeer git
    - Voer het volgende commando uit:
    ```brew install git```

## Configuratie git

Voordat we git en onze hva gitlab omgeving kunnen gebruiken moeten we een paar dingen configureren. Dit doen we door commando's uit te voeren in de terminal applicatie.

Ten eerste moet git je naam en email adres weten. Gebruik je volledige naam en je hva email adres. Pas onderstaande commando's aan zodat jouw gegevens worden ingesteld.

```git config --global user.name "Jouw Volledige Naam"```\
```git config --global user.email "jouw.hva.emailadres@hva.nl"```

Voor de communicatie tussen het git programma en de HvA gitlab omgeving is een ssh sleutelpaar nodig. Deze bestaat uit een prive sleutel, die geheim blijft en alleen op jouw computer staat, en een publieke sleutel. De publieke sleutel moet in jouw gitlab account worden toegevoegd.

Om het sleutelpaar aan te maken gebruik je het volgende commando. Er zal enkele malen om input gevraagd worden, onder andere een wachtwoord. Kies bij alle vragen de standaard instelling (dus geen wachtwoord) door op enter te drukken.

```ssh-keygen -t ed25519```

Kopieer de publieke sleutel door middel van het volgende commando naar het clipboard:

Windows: ```cat ~/.ssh/id_ed25519.pub | clip```
MacOS: ```cat ~/.ssh/id_ed25519.pub | pbcopy```

Ga op de gitlab website naar ssh keys pagina te vinden bij preferences: https://gitlab.fdmci.hva.nl/-/profile/keys
En plak de sleutel in het "Key" veld op de website. Die zal er ongeveer zo uit zien:

> ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBoafpFPXETDHWhBbmWyRqQH0jukrWlx9CWPNNmphVzW user@computer

Let op, als je de Expriation date op de standaard waarde laat staan zul je over een jaar een nieuwe sleutel moeten maken en toevoegen.

Test de ssh configuratie met het volgende commando ```ssh -T git@gitlab.fdmci.hva.nl```

Als het goed is krijg je nu een waarschuwing over de authenticity van de host met een fingerprint. Je kunt controleren op https://gitlab.fdmci.hva.nl/help/instance_configuration#ssh-host-keys-fingerprints of deze fingerprint inderdaad overeenkomt. Zo ja type "yes" en enter. Als je bovenstaand commando nogmaals uitvoert krijg je een bericht "Welcome to GitLab @gebruikersnaam".

Zie ook: https://docs.gitlab.com/ee/user/ssh.html

## Importeer project van GitLab

1. Zorg dat je een folder op je computer hebt waar alle (studie)projecten in kunnen. Zorg ervoor dat deze folder (op een plaats staat die) niet met een clouddrive synchroniseert.
2. Klik op de startpagina van dit project op de gitlab website de blauwe "Clone" knop. Kies vervolgens de optie "Visual Studio Code (SSH)" onder "Open in your IDE".
3. Je krijgt nu een popup waarbij je de in stap 1 aangemaakte folder kan kiezen.
4. Je krijgt nu een vraag of je de auteurs (authors) van de repository vertrouwt. Kies ja.

