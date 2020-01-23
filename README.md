# Egunean behin wikidata
Egunean behinerako wikidata iturritik galderak sortzeko kodea.
Galdera hauek sortzeko pythoneko pywikidata liburutegia erabili dugu.

## Wikidata-rako kontsulta prestatu
Aurrena https://query.wikidata.org/ orrialdeko kontsulta baliabidearekin behar ditugun elementuak lortzeaz ziurtatuko gara. Behin emaitzak egokiak direla jakinik, kontsulta.rq fitxategi batean gordeko ditugu.

![Adibide irudia](https://github.com/egunean-behin/egunean_behin_wikidata/blob/master/wikidata.png?raw=true)

## pywikidata baliatuz kontsulta exekutatu eta galderak sortu
https://www.wikidata.org/wiki/Category:Pywikibot_tutorial

Guzak honela, galderakSortu.py fitxategian, kontsulta.rq-tik abiatuta lorturiko item bakoitzarekin galdera bat sortzen dugu. Horretarako, erantzun posible guztiak erauzi ditugu kontsultaren emaitzatik, eta galderak sortzen sartzen gara. Galderentzat beharrezko informazioa erauzi dugu wikidatako arauak jarraituz (ikus getEuskarazkoIzena, getIrudia eta getArtikuluEsteka), eta csv fitxategirako lerroa prestatzeko, erantzun okerrak lortu ditugu getOkerrak funtzioaren bidez. Azkenik, galdera lerroa osatu dugu. Kontsultan lorturiko elementu guztiekin galdera sortuta, 'galderak.csv' fitxategian gordetzen dugu emaitza.
