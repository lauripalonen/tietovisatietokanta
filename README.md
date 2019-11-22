# Quiz log

Quiz log on kirjanpitoväline tietovisajoukkueille visailukysymysten tallentamiseksi. Sovelluksessa voi ylläpitää tietovisakysymyksiin liittyvää tietoa (esitetty kysymys, vastaus, kysymyskategoria, esitys ajankohta ja onko joukkue vastannut kysymykseen oikein). Tallennetusta tiedosta voi koostaa yhteenvetoja, joista joukkue voi reflektoida omaa menestystään esimerkiksi tietyissä kysymyskategoriassa tai eri ajankohtina.

## Heroku
Heroku-julkaisu:  
https://quizlog.herokuapp.com  
(Huom 1: Salasanat tallentuvat heroku-julkaisussa selkokielisinä. **ÄLÄ KÄYTÄ ARKALUONTEISIA SALASANOJA!**)  

## Dokumentaatio
[Tietokantakaavio](/documentation/uml-chart.png)  
[User stories](/documentation/userstories.md)

## Testitunnukset
Sovellukseen pääsee kirjautumaan seuraavilla tunnuksilla:  
käyttäjänimi: test_user  
salasana: test_pw  

## Toiminnot
[User stories](/documentation/userstories.md) -dokumentissa on kuvattu sovelluksen suunnitellut toiminnallisuudet. Jo julkaistuja toimintoja:  
- sisään- ja uloskirjautuminen, sekä rekisteröityminen
- uuden tiimin luominen tai olemassa olevaan liittyminen (rekisteröitymislomakkeella)
- kysymysten luonti, editointi ja poisto
- kysymysten listaaminen
- Tiimin vaikeimman kysymyskategorian näyttö


