# Quiz log

Quiz log on kirjanpitoväline tietovisajoukkueille visailukysymysten tallentamiseksi. Sovelluksessa voi ylläpitää tietovisakysymyksiin liittyvää tietoa (esitetty kysymys, vastaus, kysymyskategoria, esitysajankohta ja onko joukkue vastannut kysymykseen oikein). Tallennettujen tiedostojen perusteella sovelluksesta voi nähdä yhteenvetona joukkueelle henkilökohtaisesti vaikeimman kategorian ja koko tietokannan menestyneimmän joukkueen.  

## Käyttötapaukset
[User stories](/documentation/userstories.md)

## Heroku
Huom: Salasanat tallentuvat heroku-sovelluksessa selkokielisinä. **ÄLÄ KÄYTÄ ARKALUONTEISIA SALASANOJA!**
Heroku-julkaisu:  https://quizlog.herokuapp.com   

## Dokumentaatio
[Tietokantakaavio](/documentation/uml-chart.png)  
[SQL-kyselyt](/documentation/SQL-kyselyt.md)  
[User stories](/documentation/userstories.md)  
[Jatkokehitys](/documentation/jatkokehitys.md)  


## Testitunnukset
Heroku-sovellukseen pääsee kirjautumaan seuraavilla tunnuksilla:    

| username | password |
| --- | --- |
| test_user | test_pw |
| another_user | another_pw |
| ADMIN | ADMIN |  

ADMIN-tunnuksilla voi tarkastella normaalikäyttäjästä poikkeavia admin-toimintoja.

## Toiminnot
[User stories](/documentation/userstories.md) -dokumentissa on kuvattu sovelluksen suunnitellut toiminnallisuudet. [Jatkokehitys](/documentation/jatkokehitys.md) -dokumentissa on avattu tämän hetkisen julkaisun puutteita, ja niille esitettyjä jatkokehitysideoita. Jo julkaistuja toimintoja:  
- sisään- ja uloskirjautuminen, sekä rekisteröityminen
- uuden tiimin luominen, olemassa olevaan liittyminen tai tiimistä poistuminen
- kysymysten luonti, editointi ja poisto
- kysymysten listaaminen (aikajärjestyksessä)
- Tiimin vaikeimman kysymyskategorian näyttö
- Edustamansa joukkueen näyttö sovelluksen navigointipalkin alla  
- Useamman joukkueen lisäys yhdelle käyttäjälle
- Admin-ominaisuus: kaikkien kysymysten näyttö
- Admin-ominaisuus: tietokannan tuhoaminen
- Admin-ominaisuus: menestyneimmän joukkueen näyttö

## Käyttöohje  

### kirjautuminen
Heroku-sovelluksessa pääsee kirjautumaan tai rekisteröitymään ylänavigaatiopalkin Login tai Sign up -napeista.  Sovelluksessa olemassa olevat tunnukset on listattu aiemmin kohdassa **Testitunnukset**.

Uudet käyttäjät lisäävät itselleen joukkueen, tai liittyvät jo olemassa olevaan kirjoittamalla joukkueen nimen rekisteröitymisnäkymän Team-kenttään. Tämän jälkeen kaikki kysymykset jotka käyttäjä lisää, yhdistetään käyttäjän joukkueeseen.  

### kysymysten listaaminen
Oman joukkueen kysymyksiä voi selata aikajärjestyksessä List questions -napista. Kysymysten lisäksi sovellus näyttää käyttäjälle joukkueensa vaikeimman kategorian (vähiten oikeita vastauksia prosentuaalisesti). Jos oma joukkue ei ole lisännyt kysymyksiä, List questions ei näytä yhtään kysymystä.

### kysymyksen lisääminen ja muokkaus
Uutta kysymystä pääsee luomaan Add a question -napista. Mikäli käyttäjä täyttää kaikki kysymyskentät hyväksyttävästi, kysymys lisätään kaikkine taustatietoineen joukkueen kysymyslistaukseen (johon navigointi List questions -napista). Kysymykset lisätään lisäyshetkellä edustavan joukkueen tietoihin.  

Kysymyslistauksesta pääsee myös muokkaamaaan jo lisättyä kysymystä painamalla edit-painiketta. Tällöin käyttäjälle avautuu näkymä, jossa voi vapaasti muokata mitä tahansa kysymykseen liittyvää kenttää.

### tiimien hallinta
Manage teams -sivulla voi hallinnoida omia joukkueitaan. Sivulla voi lisätä uuden joukkueen, tai valita jonkin omista joukkueistaan muokattavaksi. Muokkaussivulla voi vaihtaa joukkueen nimeä, vaihtaa edustettavaa joukkuetta tai poistaa joukkue.

### admin toiminnot
Mikäli käyttäjä on kirjautunut admin-tunnuksilla, on tällöin käytössä normaalitoimintojen lisäksi View all questions. Sivulta näkee parhaiten menestyneen joukkueen (eniten oikeita vastauksia prosentuaalisesti). Lisäksi sivulla on **Destroy**-nappi, jolla voi pyyhkiä tietokannan kaikki tiedot, lukuunottamatta ADMIN tunnuksia.

### uloskirjautuminen
Sovelluksesta pääsee kirjautumaan ulos navigaatiopalkin Logout-napista.

## Asennusohje
Mikäli sovellusta haluaa ajaa paikallisesti omalla koneella, tulee ensin ladata projektin [zip-tiedosto](https://github.com/lauripalonen/tietovisatietokanta/archive/master.zip), ja käydä läpi seuraavat vaiheet:  
1. Pura tiedosto, ja avaa projektikansio terminaalissasi.  
2. Luo kansion sisälle Python-virtuaaliympäristö komennolla ```python3 -m venv venv```.  
3. Aktivoi virtuaaliympäristö komennolla ```source venv/bin/activate```.  
4. Asenna projektin riippuvuudet komennolla ```pip install -r requirements.txt```.  

Nyt sovellus on valmis ajattevaksi paikallisesti komennolla ```python run.py```. Sovellusta voi tarkastella omassa selaimessa, osoitteella http://127.0.0.1:5000/.


