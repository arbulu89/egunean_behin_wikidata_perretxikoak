# Egunean behin wikidata perretxikoak
Perretxikoei buruzko galderak egin ditugu, Wikipedian oinarrituta. Perretxiko baten argazkia erakusten dugu, eta izenagatik galdetzen dugu. Erantzun zuzenaz gain, bi erantzun oker ere ematen ditugu. Ikus galderak.csv dokumentua

## Wikidatako kontsulta
Wikipediako datuak ateratzeko, Wikidatako Query sisteman kontsulta bat idatzi dugu. (ikus https://w.wiki/G37 edo Kontsulta.rq dokumentua), Honek egiten duena da Wikidatako elementuak arakatu, argazkia dutenak eta euskarazko Wikipedia orria dutenak, eta honako datuak eskuratzen ditugu konsultarekin.
- Izena
- Irudi urla
- Web urla

![Adibide irudia](https://github.com/egunean-behin/egunean_behin_wikidata/blob/master/wikidata.png?raw=true)

## Konsultako datuetatik galderak idaztera
https://www.wikidata.org/wiki/Category:Pywikibot_tutorial

Wikidata Query sisteman datuak ikusi edo jaitsi daitezke modu desberdinetan, adibidez CSV bat eta hortik aurrera, material hori berriro erabili.

Hala ere, guk tarteko urrats hori aurreratu egiten dugu Python lengoaian Pywikibot paketea dagoelako, eta honek Wikidatako kontsulta horiek zuzenean bideratzeko modua ematen dugu.

Guzak honela, galderakSortu.py fitxategian, kontsulta.rq-tik abiatuta lorturiko item bakoitzarekin galdera bat sortzen dugu. Horretarako, erantzun posible guztiak erauzi ditugu kontsultaren emaitzatik, eta galderak sortzen sartzen gara. Galderentzat beharrezko informazioa erauzi dugu wikidatako arauak jarraituz (ikus getEuskarazkoIzena, getIrudia eta getArtikuluEsteka), eta csv fitxategirako lerroa prestatzeko, erantzun okerrak lortu ditugu getOkerrak funtzioaren bidez. Azkenik, galdera lerroa osatu dugu. Kontsultan lorturiko elementu guztiekin galdera sortuta, 'galderak.csv' fitxategian gordetzen dugu emaitza.
