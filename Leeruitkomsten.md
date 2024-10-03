# Leeruitkomsten: Secret Manager Webapplicatie

In deze leeruitkomsten.md toon ik hoe de ontwikkeling van mijn Secret Manager webapplicatie voldoet aan de gestelde leerdoelen. Hieronder wordt elke leeruitkomst besproken en onderbouwd met bewijs uit mijn werkproces en de GitLab-repository.
---

# SIDENOTE: Omdat ik graag zeker ben van mijn zaak, heb ik mijn bewijs op zoveel mogelijk manieren geprobeerd te laten zien. Belangrijkste voorbeelden: PLAN.md, SOURCES.md, progress.md files, Technical Documentation, README.md en uiteraard de 40+ commits en comments bij de commits in GitLab.

---

**Je maakt een (web)applicatie die eenvoudige problemen oplost. Je maakt, volgens geldende standaarden, gebruik van opmaaktalen en programmacode en past daarbij de basisprincipes van programmeren toe. De resultaten worden vastgelegd in een GitLab-repository.**

- Je maakt een (web) applicatie die eenvoudige probleme oplost: De applicatie lost het probleem van veilige opslag van wachtwoorden op en integreert functies zoals gebruikersauthenticatie en tweefactor-authenticatie (2FA). Ik heb de applicatie gemaakt.

- Geldende standaarden: Ik heb mij gehouden aan de HBO-ICT Code Conventies uit de Knowledgebase

- Toepassing van opmaaktalen en programmacode: De webapplicatie is ontwikkeld met HTML, CSS, JavaScript en Python. CSS is gebruikt voor de styling volgens moderne standaarden (gebruik van variabelen voor kleuren, responsive design, en flexbox). Voor de backend zijn server-side technologieën gebruikt.Codefragmenten zoals het gebruik van media queries voor responsiviteit en het toevoegen van interactieve elementen in JavaScript tonen de basisprincipes van programmeren.

- GitLab Repository: De gehele broncode en voortgang zijn gedocumenteerd in mijn GitLab-repository. Elke commit toont de voortgang van de ontwikkeling, inclusief bugfixes, nieuwe features, en code-refactoring.

- Voorbeeld code:

```CSS

/* Responsive design */
@media (max-width: 768px) {
    .nav-links {
        display: none;
    }
}

```

**Je maakt een (web)applicatie met een gebruikersinterface. Deze gebruikersinterface is te gebruiken door de eindgebruiker. Je vraagt feedback aan de gebruiker door het gemaakte product te laten testen.**

- Gebruikersinterface (UI): De UI is ontworpen met de gebruiker in gedachten. Er is een eenvoudig te navigeren dashboard toegevoegd waar gebruikers hun wachtwoorden veilig kunnen beheren. De gebruikersinterface is geoptimaliseerd voor zowel desktop- als mobiele apparaten, zodat de eindgebruiker via verschillende schermformaten toegang heeft tot zijn of haar gegevens.

- Gebruikerstesten: De applicatie is door meerdere eindgebruikers getest. Op basis van hun feedback zijn verschillende verbeteringen doorgevoerd, zoals het toevoegen van een duidelijkere foutmelding bij onjuiste loginpogingen en het verbeteren van de mobiele lay-out.

**Je werkt efficiënt en effectief door principes van Scrum toe te passen. Dit omvat het opstellen van een takenlijst (user en learning stories), de taken te rangschikken volgens prioriteit en het plannen van je doelen en taken.**

- Scrum in de praktijk: Tijdens de ontwikkeling van de webapplicatie heb ik Scrum toegepast door sprints te plannen en user stories te prioriteren in een backlog. Voor elke sprint werd een Sprint Planning Meeting gehouden waarbij de doelen werden bepaald op basis van prioriteit en haalbaarheid. De taken werden op het issue-board bijgehouden en geordend volgens de "to-do", "in progress" en "done"-statussen.

- Scrum-bewijs: Een overzicht van mijn issue-board is beschikbaar in GitLab en toont de voortgang van elke taak per sprint. Daarnaast toont de voortgang van mijn PLAN.md, progress.md files etc. verder mijn progressie.

**Je documenteert je ontwikkeling tijdens de sprints. Na afloop van de sprints evalueer je je eigen voortgang, sta je open voor suggesties en feedback van anderen, en op basis daarvan stel je nieuwe ontwikkeldoelen op.**

- Documentatie en reflectie: Elke sprint werd afgesloten met een retrospective waarin ik mijn eigen voortgang heb geëvalueerd. Suggesties van medestudenten en de projectbegeleider werden besproken en verwerkt in de volgende sprint.

- Voorbeeld: In sprint 1 realiseerde ik me dat mijn website nog geen 2FA systeem had. Op basis van feedback van mijn medestudent en op basis van feedback van een familielid heb ik de versleutelingstechniek toegevoegd voor extra beveiliging van opgeslagen gegevens.

- Nieuw ontwikkeldoel: Na feedback van een docent uit een andere klas heb ik besloten om mijn folders opnieuw in te delen en de app.py op te splitsen in verschillende files.

---

# Overige leerdoelen / bewijzen

- Aan welke Learning Stories heb je gewerkt?: Ik heb aan elke learning story gewerkt, behalve de nog lopende stoeis zoals "Coaching gesprek", "Peer review" etc. Voor Learning stories die ingeleverd konden worden met concreet bewijs, zoals de "UI Wireframe" learning story, heb ik steeds bewijs toegevoegd in de comments van deze issue. Overige Learning Stories, zoals "Scorion", heb ik simpelweg naar verify gesleept omdat ik hier enkel informatie uit kon ophalen. Dat ik deze informatie daadwerkelijk heb geleerd, blijkt uit mijn handelingen in de praktijk.

- Hoe kan je laten zien welk werk je verzet hebt aan de learning stories? En dat je hebt begrepen wat je hebt geleerd? (welke bewijzen zijn er voor?): Zie de Sidenote bovenaan. TL:DR: Door middel van screenshots en meerdere files.

- Welke learning stories ben je nog mee bezig?: De nog lopende learning stories zoals Peer review en Coaching gesprek.

- Welke learning stories zijn al helemaal af: Alle niet lopende learning stories.

- Aan welke User Stories heb je gewerkt?: Allemaal, elke user story is af.

- Welke bewijzen kun je verzamelen die goed illustreren wat je hebt gedaan: Zie de Sidenote bovenaan. TL:DR: Door middel van screenshots en meerdere files.

# Zelf geleerde dingen

---

- Ik heb geleerd om met een plan te werken
- Ik heb geleerd hoe ik een duidelijkere folder structure kan maken
- Ik heb geleerd wat Flask / Jinja is en hoe ik dit gebruik
- Ik heb geleerd hoe routes werken in Flask
- Ik heb geleerd wat templates zijn in Jinja
- Kennis van Python CSV bezit ik al door mijn studie vorig jaar.
- Ik heb geleerd hoe ik mijn progressie bij hou
- Ik heb geleerd hoe ik op meerdere manieren bewijzen kan leveren
- Ik heb geleerd wat de HvA Code Conventies zijn.
- Ik heb geleerd om met Git en GitLab te werken voor versiebeheer.
- Ik heb geleerd hoe ik feedback van gebruikers kan verwerken en mijn code kan verbeteren.
- Ik heb geleerd hoe ik een responsive webdesign kan maken met CSS en media queries.
- Ik heb geleerd om API's te gebruiken en te integreren in een webapplicatie.
- Ik heb geleerd hoe ik mijn applicatie beveilig met tweefactor-authenticatie (2FA).
- Ik heb geleerd om Scrum toe te passen tijdens een project.
- Ik heb geleerd om mijn code te documenteren volgens industriestandaarden.


---

- Paul Stokreef
- Student HBO-ICT aan de Hogeschool van Amsterdam
- https://portfolio-seven-topaz-36.vercel.app/
