# Installatie Handleiding Docker

Dit is de handleiding om de Docker teinstalleren op je laptop 
en verbinding te maken met Visual Studio Code.
Deze installatie gaat uit van een up to date Windows 10, Windows 11 of MacOS systeem.
De Package manager moeten geinstalleerd zijn.

## Installatie Windows

Installeer docker:\
Voer het volgende commando uit: ```choco install docker```

Het kan zijn dat je eerst nog virtualization in de bios moet aanzetten.\
Vraag eventueel studentmentor of docent om hulp.
- herstart de computer als dat gevraagd wordt.
- Je krijgt na het herstarten van de computer mogelijk de foutmelding: ```WSL kernel version too low```\
Start in dat geval powershell en voer het commando uit zoals aangegeven in de foutmelding: ```wsl --update```
- In het geval van eventuele andere problemen met wsl, zie: [WSL upgrade: learn.microsoft.../wsl/install-manual](https://learn.microsoft.com/en-us/windows/wsl/install-manual)

## Installatie MacOS

Installeer docker:\
Voer het volgende commando uit: ```brew install docker```

