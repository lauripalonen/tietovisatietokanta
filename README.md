# Quiz log

Quiz log on kirjanpitoväline tietovisajoukkueille visailukysymysten tallentamiseksi. Sovelluksessa voi ylläpitää tietovisakysymyksiin liittyvää tietoa (esitetty kysymys, vastaus, kysymyskategoria, esitysajankohta ja onko joukkue vastannut kysymykseen oikein). Tallennetusta tiedosta voi koostaa yhteenvetoja, esimerkiksi joukkueelle haastavimman kategorian.

## Heroku
Heroku-julkaisu:  
https://quizlog.herokuapp.com  
(Huom: Salasanat tallentuvat heroku-julkaisussa selkokielisinä. **ÄLÄ KÄYTÄ ARKALUONTEISIA SALASANOJA!**)  

## Dokumentaatio
[Tietokantakaavio](/documentation/uml-chart.png)  
[User stories](/documentation/userstories.md)

## Testitunnukset
Heroku-sovellukseen pääsee kirjautumaan seuraavilla tunnuksilla:  
käyttäjänimi: test_user  
salasana: test_pw  

## Toiminnot
[User stories](/documentation/userstories.md) -dokumentissa on kuvattu sovelluksen suunnitellut toiminnallisuudet. Jo julkaistuja toimintoja:  
- sisään- ja uloskirjautuminen, sekä rekisteröityminen
- uuden tiimin luominen tai olemassa olevaan liittyminen (rekisteröitymislomakkeella)
- kysymysten luonti, editointi ja poisto
- kysymysten listaaminen (aikajärjestyksessä)
- Tiimin vaikeimman kysymyskategorian näyttö (toiminto ei tällä hetkellä toimi odotesti Herokussa)
- Admin-ominaisuus: kaikkien joukkueiden kysymysten näyttö
- Edustamansa joukkueen näyttö sovelluksen navigointipalkin alla

## Käyttöohje
Heroku-sovelluksessa pääsee kirjautumaan tai rekisteröitymään ylänavigaatiopalkin Login tai Sign up -napeista. Sovelluksessa on jo käytössä seuraavat tunnukset:  

| username | password |
| --- | --- |
| test_user | test_pw |
| another_user | another_pw |
| ADMIN | ADMIN |  

Tunnuksella ADMIN voi tarkastella normaalikäyttäjästä poikkeavia admin-toimintoja.

Uudet käyttäjät lisäävät itselleen joukkueen, tai liittyvät jo olemassa olevaan kirjoittamalla joukkueen nimen rekisteröitymisnäkymän Team-kenttään. Tämän jälkeen kaikki kysymykset jotka käyttäjä lisää, yhdistetään käyttäjän joukkueeseen.

Sisäänkirjautumisen onnistuttua, oman joukkueen kysymyksiä voi selata aikajärjestyksessä List questions -napista. Kysymysten lisäksi sovellus näyttää käyttäjälle joukkueensa vaikeimman kategorian (vähiten oikeita vastauksia prosentuaalisesti). Jos oma joukkue ei ole lisännyt kysymyksiä, List questions ei näytä yhtään kysymystä.  

Uutta kysymystä pääsee luomaan Add a question -napista. Mikäli käyttäjä täyttää kaikki kysymyskentät hyväksyttävästi, kysymys lisätään kaikkine taustatietoineen joukkueen kysymyslistaukseen (johon navigointi List questions -napista).

Kysymyslistauksesta pääsee myös muokkaamaaan jo lisättyä kysymystä painamalla edit-painiketta. Tällöin käyttäjälle avautuu näkymä, jossa voi vapaasti muokata mitä tahansa kysymykseen liittyvää kenttää.

Sovelluksessa on myös nähtävissä Manage teams -toiminto, joka on toistaiseksi vielä kehityksessä. Sivulla voi kuitenkin onnistuneesti lisätä uuden joukkueen käyttäjälle, ja selata käyttäjän kaikkia joukkueita. Edustettavan joukkueen vaihto ei toistaiseksi ole toiminnassa. 

Mikäli käyttäjä on kirjautunut admin-tunnuksilla, on tällöin käytössä normaalitoimintojen lisäksi View all questions, joka näyttää kaikkien joukkueiden kaikki kysymykset yhtenä listana.  

Sovelluksesta pääsee kirjautumaan ulos navigaatiopalkin Logout-napista.

## Asennusohje
Mikäli sovellusta haluaa ajaa paikallisesti omalla koneella, tulee ensin ladata projektin [zip-tiedosto](https://github.com/lauripalonen/tietovisatietokanta/archive/master.zip), ja käydä läpi seuraavat vaiheet:  
1. Pura tiedosto, ja avaa projektikansio terminaalissasi.  
2. Luo kansion sisälle Python-virtuaaliympäristö komennolla ```python3 -m venv venv```.  
3. Aktivoi virtuaaliympäristö komennolla ```source venv/bin/activate```.  
4. Asenna projektin riippuvuudet komennolla ```pip install -r requirements.txt```.  

Nyt sovellus on valmis ajattevaksi paikallisesti komennolla ```python run.py```. Sovellusta voi tarkastella omassa selaimessa, osoitteella http://127.0.0.1:5000/.


