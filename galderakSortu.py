import random
import pywikibot
from pywikibot import pagegenerators as pg

#Kontsultako emaitzetatik erantzun posible guztiak lortu, ondoren erantzun oker bezala erabili ahal izateko
def getAllLabels(g):
    labels = []
    for p in g:
        try:
            item = p.get()
            label = item['labels']['eu']
            labels.append(label)                
        except:
            pass
    return labels

#Elementuaren euskarazko etiketa edo titulua hartu
def getEuskarazkoIzena(item):
    return item['labels']['eu']

#Elementuaren irudi nabarmendua hartu
def getIrudia(item):
    return item['claims']['P18'][0].getTarget().fileUrl()

#Elementuaren Wikipediako artikulurako esteka hartu
def getArtikuluEsteka(item,zuzena):
    site = pywikibot.Site("eu", "wikipedia")
    return pywikibot.Page(site, zuzena).full_url()

def getOkerrak(zuzena,labels):
    oker1 = random.choice(labels) #Erantzun oker bat hartu posible guztien artetik
    oker2 = random.choice(labels) #Erantzun oker bat hartu posible guztien artetik
    while oker1 == zuzena: oker1 = random.choice(labels) #Ziurtatu zuzena ez dela oker bezala sartzen
    while oker2 == zuzena or oker1 == oker2: oker2 = random.choice(labels) #Ziurtatu zuzena eta lehen okerra ez direla bigarren oker bezala sartzen
    return oker1, oker2

#Elementua eta erantzun posible guztiak pasata, lortu honi buruzko galdera bat
def getGaldera(item,labels):
    try:
        mota='Perretxikoak' #Galdera mota
        iturria='Wikipedia' #Galderaren jatorria edo iturria
        galdera='Nola deitzen da argaziko perretxikoa?' #Testuzko galdera
        irudia = getIrudia(item) 
        zuzena = getEuskarazkoIzena(item) 
        link = getArtikuluEsteka(item,zuzena) 
        oker1, oker2 = getOkerrak(zuzena,labels)
        galdera_osoa = "%s;%s;%s;%s;%s;%s;%s;%s;%s" % (mota,galdera,irudia,zuzena,oker1,oker2,iturria,link,'') #galdera osatu csv formaturako prestatuz
    except:
        galdera_osoa=''

    return galdera_osoa

def generateGalderak(kontsulta,irteera):
    f = open(irteera, 'w')
    with open(kontsulta, 'r') as query_file:
        QUERY = query_file.read()
    wikidata_site = pywikibot.Site("wikidata", "wikidata")
    print("#### hasi da prozesua ####")
    labels = getAllLabels(pg.WikidataSPARQLPageGenerator(QUERY, site=wikidata_site))
    generator = pg.WikidataSPARQLPageGenerator(QUERY, site=wikidata_site)
    f.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % ('Mota','Galdera','Irudia','Zuzena','Oker1','Oker2','Jatorria','Esteka','Egilea','\n')) #csv fitxategian idatzi goiburua
    print("#### galderak sortzen ####")
    for page in generator:
        try:
            item = page.get()
            galdera_osoa = getGaldera(item,labels) #Elementuarekin erlazionatutako galdera lortu 
            if galdera_osoa!='':
                print('.')
                f.write("%s;%s" % (galdera_osoa,'\n')) #csv fitxategian idatzi galdera
        except:
            pass
    print('\nEginda!')
    f.close()

generateGalderak('kontsulta.rq','galderak.csv')
