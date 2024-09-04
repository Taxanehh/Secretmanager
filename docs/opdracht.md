
[[_TOC_]]

## Opdrachtomschrijving

Een nieuwe studie, een nieuwe stad… Als kersverse student komt er veel op je af. Er zijn introductiedagen, je ontmoet nieuwe mensen, kan je voor van alles en nog wat inschrijven, en dan is er nog al die software die je moet installeren voor je nieuwe studie. Omdat alles tegenwoordig digitaal beveiligd wordt, moet je voor al die momenten een eigen account aanmaken. 

Dan begint de pret. Want een account maak je niet zomaar aan. Dat moet je beveiligen met een wachtwoord. De ene organisatie zegt dat een wachtwoord minimaal acht tekens moet bevatten, waaronder minstens een cijfer. De andere wil dat je extra leestekens toevoegt. Een derde vraagt om two-factor authentication. Het is een wonder dat je nog geen hiërogliefen hebt gebruikt!  

Al die verschillende wachtwoorden lijken misschien omslachtig, maar toch zijn ze noodzakelijk. Het gebruik van onveilige wachtwoorden, waaronder ook het hergebruik van wachtwoorden, is één van [de top-10 bedreigingen voor de veiligheid van web-applicaties](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/).\
Toch moet er een gebruiksvriendelijkere manier zijn om al die wachtwoorden te herinneren, én een veiligere manier dan een post-it die je op je monitor plakt. Waar kan je dit soort geheime informatie veilig kwijt?

## Wat je gaat maken

In deze opdracht ga je een Secret Manager bouwen, een applicatie waarin gebruikers hun geheime informatie kunnen opslaan. Wachtwoorden, persoonsgegevens, fantastische bakrecepten - alles wat je geheim wilt houden moet in jouw applicatie veilig zijn. Via een (simpele) PEN-test ga je die veiligheid controleren, want in cybersecurity geldt één motto: "Trust, but verify".

## Ontwikkelomgeving

Je maakt deze opdracht een eigen ontwikkelomgeving op je eigen laptop door eigen tools te installeren.\
De bestandsstructuur en een paar startbestanden die je nodig hebt staan in de GitLab repository. Ook een groot gedeelte van de uitleg die je nodig hebt vind je in de GitLab repository.\
Je bouwt zo op je laptop een omgeving op, zoals een kleine webhoster deze zou inrichten.


## User stories

Om de opdracht te kunnen plannen en uit te voeren zijn in dit eerste blok user stories opgesteld. Die gaan je helpen om de webapplicatie te bouwen.\
Maar wat is een user story eigenlijk? Op [scrumguide.nl](https://scrumguide.nl/user-story/) vind je de volgende definitie:

> “Een User Story is een korte beschrijving (Story) van wat een gebruiker (User) wil. User Stories worden gebruikt bij het ontwikkelen van producten of software binnen Agile raamwerken, waaronder Scrum. Een User Story bestaat uit enkele zinnen waarin staat wat de gebruiker van het product moet / wil doen. Een User Story is eigenlijk weinig gedetailleerd en zou moeten kunnen passen op een post-it. Via de User Story heeft de gebruiker invloed op het ontwikkelen van een systeem of product en uiteindelijk de functionaliteit ervan.”

### User story vorm

Een User story bestaat in het algemeen uit de volgende onderdelen:
- Een Titel
- Een Beschrijving in User Story formaat
- Requirements
- Acceptatie criteria / Definition of Done

Het user story formaat is een afgesproken vorm. Als volgt:\
_Als … (soort gebruiker) wil ik … (feature/actie), zodat … (doel/voordeel)._

Een voorbeeld van een user story is:\
_“Als Cyber Security Specialist wil ik dat de Secret Manager gecontroleerd is met een PEN-test, zodat ik de applicatie niet gemakkelijk gehackt kan worden.”_

### User stories Secret Manager

In de User Stories van de Secret Manager vind je meer informatie, zodat je geholpen wordt om de User Story af te ronden.\
Er zijn verwijzingen naar handleidingen, naar allerhande bronnen, zoals de [Knowledge base](https://knowledgebase.hbo-ict-hva.nl/), een aantal learning stories en diverse internetbronnen, en acceptatiecriteria zodat je weet wanneer de user story af is..

In de GitLab bij `Issues >` staan de User Stories. 
In **Milestone** `Sprint 0` staan alle User Stories van de nodige installaties.
In de eerste 2 weken kan je de eigen omgeving inrichten en je gaan inlezen in de diverse ICT talen en producten.\
Bijvoorbeeld: de basis installatie is issue [85 : “0 Basis Installatie”](#85) met User story: _“Als Software developer wil ik producten installeren op mijn laptop, zodat ik een applicatie kan ontwikkelen”_

In de [getting-started](docs/getting-started) in de GitLab [docs](docs) directory staan bijbehorende installatiehandleidingen.

❗LET OP: De user stories zijn al toegewezen aan sprints. Hou deze volgorde in de gaten tijdens je werk.❗  

### De product backlog van deze opdracht

Omdat we werken volgens Scrum staan de user stories op een zogenaamde Product Backlog. De product backlog vind je in deze Gitlab-repository onder `Issues > Boards >`. Selecteer `<Product Backlog>` in de drop down. 

## Sprints

Je werkt in zogeheten sprints. Tijdens een sprint selecteer je de user stories van de `Product Backlog` die je denkt te kunnen gaan bouwen in 2 of 3 weken (de duur van een sprint in deze opdracht). In totaal zijn er 3 sprints.\
 Om een user story toe te wijzen aan een sprint wijs je deze toe aan een `Milestone`. Dit kun je doen bij de eigenschappen van een user story. Zie hiervoor wederom de pagina `Issues`. Aan het eind van een sprint moet er altijd een bruikbaar product zijn voor de eindgebruiker. User stories die niet af zijn gaan door naar de volgende sprint. Test een user story dus goed voordat je deze op done zet!

## Wanneer is de Secret Manager klaar?

Voor het bouwen van deze opdracht heb je 2 sprints (plus Sprint 0) de tijd. 
Aan het einde van die periode moet je applicatie aan een aantal verwachtingen voldoen. We noemen dit de kwaliteitscriteria. 

## Lesmateriaal

Het lesmateriaal staat op verschillende plekken:
- In de learning stories staat een introductie en verwijzingen naar het lesmateriaal. 
- [De knowledge base](https://knowledgebase.hbo-ict-hva.nl/):\
Hier staan artikelen over de belangrijkste onderwerpen die je gaat tegenkomen in de opdracht.
- [De DLO](https://dlo.mijnhva.nl/):\
Hier worden opdracht-specifieke documenten gezet, zoals oefeningen, templates, of aanvullend materiaal wat gedurende het blok ter beschikking wordt gesteld. Hier vindt je ook eventuele video's van de online lessen.

### Learning stories

Tijdens het project werk je aan zogeheten **learning stories**. Daarin staan de te leren vaardigheden en competenties binnen dit project.\
Deze learning stories vind je in de Gitlab-repository onder `Issues > Boards >`. Selecteer `<Learning stories>` in de dropdown`.

### Knowledge base

Je vindt alle handleidingen en documentatie in het menu van de [knowledge base](https://knowledgebase.hbo-ict-hva.nl/) aan de rechterkant van je scherm.\
Ook kan je zoeken in de knowledgebase.