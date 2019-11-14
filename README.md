# Quiz log

Quiz log on kirjanpitoväline tietovisajoukkueille visailukysymysten tallentamiseksi. Sovelluksessa voi ylläpitää tietovisakysymyksiin liittyvää tietoa (esitetty kysymys, vastaus, kysymyskategoria, esitys ajankohta ja onko joukkue vastannut kysymykseen oikein). Tallennetusta tiedosta voi koostaa yhteenvetoja, joista joukkue voi reflektoida omaa menestystään esimerkiksi tietyissä kysymyskategoriassa tai eri ajankohtina.

## Heroku
Heroku-julkaisu:  
https://quizlog.herokuapp.com

## Dokumentaatio
[Tietokantakaavio](/documentation/tvtk-uml.png)  
[User stories](/documentation/userstories.md)

## Testitunnukset
Sovellukseen pääsee kirjautumaan seuraavilla tunnuksilla:  
käyttäjänimi: test_user  
salasana: test_pw  

## Huomioita
### salaus
Paikallisesta versiosta poiketen Heroku-versiossa ei tällä hetkellä ole salasanojen kryptausta! Herokussa salasanat siis tallentuvat selkokielisinä tietokantaan, joten **ÄLÄ KÄYTÄ REKISTERÖITYIMSEEN ARKALUONTESIA SALASANOJA!**  

### tiimit
Tiimeihin liittyvät toiminnallisuudet ovat vielä kehityksessä, eivätkä tällä hetkellä toteuta vielä oleellisia toimintoja.

