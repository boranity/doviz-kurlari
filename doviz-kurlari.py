import requests, socket
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook



# Doviz Kurları
rD = requests.get("https://kur.doviz.com/")
soupD = BeautifulSoup(rD.content, "html.parser")

amerikan_dolari = soupD.find("td", {"data-socket-key":"USD"}, {"data-socket-attr":"b"}).text
euro = soupD.find("td", {"data-socket-key":"EUR"}, {"data-socket-attr":"b"}).text
ingiliz_sterlini = soupD.find("td", {"data-socket-key":"GBP"}, {"data-socket-attr":"b"}).text
isvicre_frangi = soupD.find("td", {"data-socket-key":"CHF"}, {"data-socket-attr":"b"}).text
kanada_dolari = soupD.find("td", {"data-socket-key":"CAD"}, {"data-socket-attr":"b"}).text
rus_rublesi = soupD.find("td", {"data-socket-key":"RUB"}, {"data-socket-attr":"b"}).text
avustralya_dolari = soupD.find("td", {"data-socket-key":"AUD"}, {"data-socket-attr":"b"}).text
danimarka_kronu = soupD.find("td", {"data-socket-key":"DKK"}, {"data-socket-attr":"b"}).text
isvec_kronu = soupD.find("td", {"data-socket-key":"SEK"}, {"data-socket-attr":"b"}).text
norvec_kronu = soupD.find("td", {"data-socket-key":"NOK"}, {"data-socket-attr":"b"}).text
yuz_japon_yeni = soupD.find("td", {"data-socket-key":"JPY"}, {"data-socket-attr":"b"}).text



# Altın Fiyatları
rA = requests.get("https://altin.doviz.com/")
soupA = BeautifulSoup(rA.content, "html.parser")

gram_altin = soupA.find("td", {"data-socket-key":"gram-altin"}, {"data-socket-attr":"b"}).text
ceyrek_altin = soupA.find("td", {"data-socket-key":"ceyrek-altin"}, {"data-socket-attr":"b"}).text
tam_altin = soupA.find("td", {"data-socket-key":"tam-altin"}, {"data-socket-attr":"b"}).text
cumhuriyet_altini = soupA.find("td", {"data-socket-key":"cumhuriyet-altini"}, {"data-socket-attr":"b"}).text
ata_altin = soupA.find("td", {"data-socket-key":"ata-altin"}, {"data-socket-attr":"b"}).text
resat_altin = soupA.find("td", {"data-socket-key":"resat-altin"}, {"data-socket-attr":"b"}).text
hamit_altin = soupA.find("td", {"data-socket-key":"hamit-altin"}, {"data-socket-attr":"b"}).text
ikibucuk_altin = soupA.find("td", {"data-socket-key":"ikibucuk-altin"}, {"data-socket-attr":"b"}).text
gremse_altin = soupA.find("td", {"data-socket-key":"gremse-altin"}, {"data-socket-attr":"b"}).text
besli_altin = soupA.find("td", {"data-socket-key":"besli-altin"}, {"data-socket-attr":"b"}).text
ondortayar_altin = soupA.find("td", {"data-socket-key":"14-ayar-altin"}, {"data-socket-attr":"b"}).text
onsekizayar_altin = soupA.find("td", {"data-socket-key":"18-ayar-altin"}, {"data-socket-attr":"b"}).text
yirmiikiayar_bilezik = soupA.find("td", {"data-socket-key":"22-ayar-bilezik"}, {"data-socket-attr":"b"}).text
gumus = soupA.find("td", {"data-socket-key":"gumus"}, {"data-socket-attr":"b"}).text



# Kripto Paralar 

rK = requests.get("https://piyasa.paratic.com/kripto-coin/")
soupK = BeautifulSoup(rK.content, "html.parser")

bitcointry = soupK.find("td", {"data-code":"BTCTRY"}).text # türk lirası
bitcoinusd = soupK.find("td", {"data-code":"BTCUSDT"}).text # dolar

ethereumtry = soupK.find("td", {"data-code":"ETHTRY"}).text # türk lirası
ethereumusd = soupK.find("td", {"data-code":"ETHUSDT"}).text # dolar

binancetry = soupK.find("td", {"data-code":"BNBTRY"}).text # türk lirası
binanceusd = soupK.find("td", {"data-code":"BNBUSDT"}).text # dolar

monerotry = soupK.find("td", {"data-code":"XMRTRY"}).text # türk lirası
monerousd = soupK.find("td", {"data-code":"XMRUSDT"}).text # dolar


print("""
1-) Döviz Kurları       4-) Döviz Kuru Hesaplayıcı
2-) Altın Fiyatları     5-) Discord Webhook'a Bastır
3-) Kripto Paralar     
""")

secim = input("Seçiniz: ")

if secim == "1":
    print("")
    print("\033[36mAmerikan Doları:\033[35m", amerikan_dolari)
    print("\033[36mEuro:\033[35m", euro)
    print("\033[36mİngiliz Sterlini:\033[35m", ingiliz_sterlini)
    print("\033[36mİsviçre Frangı:\033[35m", isvicre_frangi)
    print("\033[36mKanada Doları:\033[35m", kanada_dolari)
    print("\033[36mRus Rublesi:\033[35m", rus_rublesi)
    print("\033[36mAvustralya Doları:\033[35m", avustralya_dolari)
    print("\033[36mDanimarka Kronu:\033[35m", danimarka_kronu)
    print("\033[36mİsveç Kronu:\033[35m", isvec_kronu)
    print("\033[36mNorveç Kronu:\033[35m", norvec_kronu)
    print("\033[36m100 Japon Yeni:\033[35m", yuz_japon_yeni, "\033[0m")

if secim == "2":
    print("")
    print("\033[33mGram Altın:\033[31m", gram_altin)
    print("\033[33mÇeyrek Altın:\033[31m", ceyrek_altin)
    print("\033[33mTam Altın:\033[31m", tam_altin)
    print("\033[33mCumhuriyet Altını:\033[31m", cumhuriyet_altini)
    print("\033[33mAta Altın:\033[31m", ata_altin)
    print("\033[33mReşat Altın:\033[31m", resat_altin)
    print("\033[33mHamit Altın:\033[31m", hamit_altin)
    print("\033[33m2 Buçuk Altın:\033[31m", ikibucuk_altin)
    print("\033[33mGremse Altın:\033[31m", gremse_altin)
    print("\033[33mBeşli Altın:\033[31m", besli_altin)
    print("\033[33m14 Ayar Altın:\033[31m", ondortayar_altin)
    print("\033[33m18 Ayar Altın:\033[31m", onsekizayar_altin)
    print("\033[33m22 Ayar Bilezik:\033[31m", yirmiikiayar_bilezik)
    print("\033[33mGümüş:\033[31m", gumus, "\033[0m")


if secim == "3":
    print("")
    print("\033[31mBitcoin TRY:\033[33m", bitcointry)
    print("\033[31mBitcoin USD:\033[33m", bitcoinusd)
    print("")
    print("\033[31mEthereum TRY:\033[33m", ethereumtry)
    print("\033[31mEthereum USD:\033[33m", ethereumusd)
    print("")
    print("\033[31mBinance TRY:\033[33m", binancetry)
    print("\033[31mBinance USD:\033[33m", binanceusd)
    print("")
    print("\033[31mMonero TRY:\033[33m", monerotry)
    print("\033[31mMonero USD:\033[33m", monerousd, "\033[0m")



if secim == "4":
    print("""
    1-) Amerikan Doları     6-) Rus Rublesi
    2-) Euro                7-) Avustralya Doları
    3-) İngiliz Sterlini    8-) Danimarka Kronu
    4-) İsviçre Frangı      9-) İsveç Kronu
    5-) Kanada Doları       10-) Norveç Kronu
                            11-) Japon Yeni \n""")
    
    kur = input("Hesaplamak istediğiniz kuru seçiniz: ")
    
    if kur == "1":
        miktar1 = float(input("Kaç Amerikan Dolar'ını Türk Lirasına Hesaplayalım: "))
        print("\033[36m Amerikan Dolar'ının güncel fiyatı:\033[35m", amerikan_dolari, "\033[0m")
        print(miktar1,"ile çarpılınca çıkan sonuc:", float(miktar1) * float(amerikan_dolari.replace(",",".")))

    if kur == "2":
        miktar1 = float(input("Kaç Euro'yu Türk Lirasına Hesaplayalım: "))
        print("\033[36m Euro'nun güncel fiyatı:\033[35m", euro, "\033[0m")
        print(miktar1,"ile çarpılınca çıkan sonuc:", float(miktar1) * float(euro.replace(",",".")))

    if kur == "3":
        miktar1 = float(input("Kaç İngiliz Sterlin'inin Türk Lirasına Hesaplayalım: "))
        print("\033[36m İngiliz Sterlin'inin güncel fiyatı:\033[35m", ingiliz_sterlini, "\033[0m")
        print(miktar1,"ile çarpılınca çıkan sonuc:", float(miktar1) * float(ingiliz_sterlini.replace(",",".")))
        
    if kur == "4":
        miktar1 = float(input("Kaç İsviçre Frangı'nı Türk Lirasına Hesaplayalım: "))
        print("\033[36m İsviçre Frangı'nın güncel fiyatı:\033[35m", isvicre_frangi, "\033[0m")
        print(miktar1,"ile çarpılınca çıkan sonuc:", float(miktar1) * float(isvicre_frangi.replace(",",".")))

    if kur == "5":
        miktar1 = float(input("Kaç Kanada Dolar'ını Türk Lirasına Hesaplayalım: "))
        print("\033[36m Kanada Dolar'ının güncel fiyatı:\033[35m", kanada_dolari, "\033[0m")
        print(miktar1,"ile çarpılınca çıkan sonuc:", float(miktar1) * float(kanada_dolari.replace(",",".")))

    if kur == "6":
        miktar1 = float(input("Kaç Rus Ruble'sini Türk Lirasına Hesaplayalım: "))
        print("\033[36m Rus Ruble'sinin güncel fiyatı:\033[35m", rus_rublesi, "\033[0m")
        print(miktar1,"ile çarpılınca çıkan sonuc:", float(miktar1) * float(rus_rublesi.replace(",",".")))

    if kur == "7":
        miktar1 = float(input("Kaç Avustralya Dolar'ını Türk Lirasına Hesaplayalım: "))
        print("\033[36m Avustralya Doları'nın güncel fiyatı:\033[35m", avustralya_dolari, "\033[0m")
        print(miktar1,"ile çarpılınca çıkan sonuc:", float(miktar1) * float(avustralya_dolari.replace(",",".")))

    if kur == "8":
        miktar1 = float(input("Kaç Danimarka Kronu'nu Türk Lirasına Hesaplayalım: "))
        print("\033[36m Danimarka Kronu'nun güncel fiyatı:\033[35m", danimarka_kronu, "\033[0m")
        print(miktar1,"ile çarpılınca çıkan sonuc:", float(miktar1) * float(danimarka_kronu.replace(",",".")))

    if kur == "9":
        miktar1 = float(input("Kaç İsveç Kronu'nu Türk Lirasına Hesaplayalım: "))
        print("\033[36m İsveç Kronu'nun güncel fiyatı:\033[35m", isvec_kronu, "\033[0m")
        print(miktar1,"ile çarpılınca çıkan sonuc:", float(miktar1) * float(isvec_kronu.replace(",",".")))

    if kur == "10":
        miktar1 = float(input("Kaç Norveç Kronu'nu Türk Lirasına Hesaplayalım: "))
        print("\033[36m Norveç Kronu'nun güncel fiyatı:\033[35m", norvec_kronu, "\033[0m")
        print(miktar1,"ile çarpılınca çıkan sonuc:", float(miktar1) * float(norvec_kronu.replace(",",".")))

    if kur == "11":
        japon_yeni = float(yuz_japon_yeni.replace(",",".")) / 100 
        miktar1 = float(input("Kaç Japon  Yeni'ni Türk Lirasına Hesaplayalım: "))
        print("\033[36m 1 Japon Yeni'nin güncel fiyatı:\033[35m", japon_yeni, "\033[0m")
        print(miktar1,"ile çarpılınca çıkan sonuc:", float(miktar1) * float(japon_yeni))

# Webhook

#webhook_url kısmınıza Webhook URL'nizi giriniz yoksa hata verir.
webhook_url = "https://discordapp.com/api/webhooks/"

if secim == "5":
    print("Tüm Kurları Webhook'a bastırıyorum... ")
    webhook = DiscordWebhook(url=webhook_url, content=
    "Amerikan Doları: " + amerikan_dolari + 
    "\nEuro: " + euro + 
    "\nİngiliz Sterlini: " + ingiliz_sterlini + 
    "\nİsviçre Frangı: " + isvicre_frangi + 
    "\nKanada Doları: " + kanada_dolari + 
    "\nRus Rublesi: " + rus_rublesi +
    "\nAvustralya Doları: " + avustralya_dolari + 
    "\nDanimarka Kronu: " + danimarka_kronu + 
    "\nİsveç Kronu: " + isvec_kronu + 
    "\nNorveç Kronu: " + norvec_kronu + 
    "\n100 Japon Yeni: " + yuz_japon_yeni +
    "\n--------------------------------------"
    "\nGram Altın: " + gram_altin + 
    "\nÇeyrek Altın : " + ceyrek_altin + 
    "\nTam Altın: " + tam_altin + 
    "\nCumhuriyet Altını: " + cumhuriyet_altini + 
    "\nAta Altın: " + ata_altin +
    "\nReşat Altın: " + resat_altin + 
    "\nHamit Altın: " + hamit_altin + 
    "\n2 Buçuk Altın Altın: " + ikibucuk_altin + 
    "\nGremse Altın: " + gremse_altin + 
    "\nBeşli Altın: " + besli_altin +
    "\n14 Ayar Altın: " + ondortayar_altin +
    "\n18 Ayar Altın: " + onsekizayar_altin +
    "\n22 Ayar Bilezik: " + yirmiikiayar_bilezik +
    "\nGümüş: " + gumus +
    "\n--------------------------------------"
    "\nBitcoin TRY: " + bitcointry + 
    "\nBitcoin USD : " + bitcoinusd + 
    "\n" +
    "\nEthereum TRY: " + ethereumtry + 
    "\nEthereum USD: " + cumhuriyet_altini + 
    "\n" +
    "\nBinance TRY: " + binancetry +
    "\nBinance USD: " + binanceusd + 
    "\n" +
    "\nMonero TRY: " + monerotry + 
    "\nMonero USD: " + monerousd).execute()
    
