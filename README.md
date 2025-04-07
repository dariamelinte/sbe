# 🛰️ Sistem Publicatii - Subscriptii

Scrieti un program care sa genereze aleator seturi echilibrate de subscriptii si publicatii cu posibilitatea de fixare a: numarului total de mesaje (publicatii, respectiv subscriptii), ponderii pe frecventa campurilor din subscriptii si ponderii operatorilor de egalitate din subscriptii pentru cel putin un camp. Publicatiile vor avea o structura fixa de campuri. Implementarea temei va include o posibilitate de paralelizare pentru eficientizarea generarii subscriptiilor si publicatiilor, si o evaluare a timpilor obtinuti.

Exemplu:
Publicatie: {(stationid,1);(city,"Bucharest");(temp,15);(rain,0.5);(wind,12);(direction,"NE");(date,2.02.2023)} - Structura fixa a campurilor publicatiei e: stationid-integer, city-string, temp-integer, rain-double, wind-integer, direction-string, date-data; pentru anumite campuri (stationid, city, direction, date), se pot folosi seturi de valori prestabilite de unde se va alege una la intamplare; pentru celelalte campuri se pot stabili limite inferioare si superioare intre care se va alege una la intamplare.

Subscriptie:{(city,=,"Bucharest");(temp,>=,10);(wind,<,11)} - Unele campuri pot lipsi; frecventa campurilor prezente trebuie sa fie configurabila (ex. 90% city - exact 90% din subscriptiile generate, cu eventuala rotunjire la valoarea cea mai apropiata de procentul respectiv, trebuie sa includa campul "city"); pentru cel putin un camp (exemplu - city) trebui sa se poate configura un minim de frecventa pentru operatorul "=" (ex. macar 70% din subscriptiile generate sa aiba ca operator pe acest camp egalitatea).


Note:
- cazul in care suma procentelor configurate pentru campuri e mai mica decat 100 reprezinta o situatie de exceptie care nu e necesar sa fie tratata (pentru testare se vor folosi intotdeauna valori de procentaj ce sunt egale sau depasesc 100 ca suma)
- tema cere doar generarea de date, nu implementarea unei topologii Storm care sa includa functionalitatea de matching intre subscriptii si publicatii; nu exista restrictii de limbaj sau platforma pentru implementare
- pentru optimizarea de performanta prin paralelizare pot fi considerate fie threaduri (preferabil) sau o rulare multiproces pentru generarea subscriptiilor si publicatiilor; se va lua in calcul posibila necesitate de sincronizare a implementarii paralelizate ce poate sa apara in functie de algoritmul ales pentru generarea subscriptiilor
- evaluarea implementarii va preciza in fisierul "readme" asociat temei urmatoarele informatii: tipul de paralelizare (threads/procese), factorul de paralelism (nr. de threads/procese) - se cere executia pentru macar doua valori de test comparativ, ex. 1 (fara paralelizare) si 4 (threads/procese), numarul de mesaje generat, timpii obtinuti si specificatiile procesorului pe care s-a rulat testul.

Hint: NU se recomanda utilizarea distributiei random in obtinerea procentelor cerute pentru campurile subscriptiilor (nu garanteaza o distributie precisa).

## 📦 Structura Proiectului

```
sbe/
├── data                        # Folder cu datele obtinute in urma rularilor
├── docs                        # Folder cu pagina html catre statistici
├── .gitignore                  # Fișier pentru ignorarea inserarii rezultatelor pe git
├── __init__.py                 # Fisier generat 
├── config.json                 # Fisier de configuratie pentru generarea publicatiilor si subscriptiilor
├── configs.py                  # Fisier pentru incarcarea configuratiei (config.json)
├── generator_pub_sub.py        # Utilitare: class GeneratorPubSub: generare subscriptii, filtrare
├── main.py                     # Main file
├── utils.py                    # Functii pentru validarea schemei si generarea frecventelor pentru operator si campuri
```

---

## Parametri de test
- Număr minim publicații: 1000
- Număr minim subscriptii: 1000

Generatiile de la 1-676:
- Threaduri: 1, 2, 3, 5, 8
  
Generatiile de la 677-10065:
- Threaduri: 1, 2, 3, 4, 5, 6

---

## Rezultate testare (timp execuție) - generarea 678:

- Număr publicații: 1313
- Număr subscriptii: 1477

- city_config_percentage: 0,81
- city_actual_percentage	0,811

| Threads | Timp generare (sec) |
|---------|---------------------|
| 1       | 0,175 sec           |
| 2       | 0,1151 sec          |
| 3       | 0,0949 sec          |
| 4       | 0,0944 sec          |
| 5       | 0,083 sec           |
| 6       | 0,0963 sec          |

---

## Rezultate testare (timp execuție) - generarea 2358:

- Număr publicații: 1245
- Număr subscriptii: 1202

- wind_config_percentage: 0
- wind_actual_percentage	0,1852

| Threads | Timp generare (sec) |
|---------|---------------------|
| 1       | 0,1881 sec          |
| 2       | 0,1538 sec          |
| 3       | 0,0941 sec          |
| 4       | 0,0983 sec          |
| 5       | 0,1021 sec          |
| 6       | 0,07 sec            |

---

## Specificații sistem

- Procesor: Intel i7-11850H 11th Gen, 16CPUs, 2.5Ghz
- Memorie: 16 GB RAM

---

## 📊 Evaluare Automată

Statisticile sunt salvate în folderul `data`:
- Generatiile de la 677-10065;
- Număr de publicații si subscripti dupa configuratie;
- Durata totală
- Durata per fiecare thread
- Ponderile asteptate si calculate

---

## Observații

- Structura publicației este fixă
- Subscriptiile includ doar câmpurile conform procentajelor configurate
- Operatorul "=" este forțat pe anumite câmpuri după pondere

---
