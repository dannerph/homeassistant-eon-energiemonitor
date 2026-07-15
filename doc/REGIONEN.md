# EON Energiemonitor — Regionen (Gemeinden)

Abzug aller Regionen, die die öffentliche EON-API pro Netzbetreiber (Tenant) ausliefert.

| | |
|---|---|
| **Stand** | 2026-05-31 |
| **Quelle** | `https://api-energiemonitor.eon.com` |
| **Regionen gesamt** | 1551 (eindeutige `regionCode`) |
| **Aktualisieren** | `python3 scripts/generate-regions-doc.py` |

> Der Energiemonitor deckt **nicht ganz Deutschland** ab, sondern nur Gemeinden/Regionen in den Netzgebieten der jeweiligen E.ON-Netzbetreiber. Ob eure Gemeinde dabei ist, sieht ihr in der Liste oder über die Suche unten.

## Eigene Gemeinde finden

### 1. Regionsübersicht im Browser

Auf der Seite des zuständigen Netzbetreibers (z. B. [Bayernwerk Regionsübersicht](https://energiemonitor.bayernwerk.de/regions-dashboard)) nach dem Ortsnamen suchen. Die URL der Gemeinde lautet `https://<netzbetreiber-host>/<regionUrlKey>` — der letzte Pfadteil ist der **URL-Slug**.

### 2. `region_code` aus dem URL-Slug (für Home Assistant)

Slug aus der Dashboard-URL nehmen und die API abfragen:

```bash
curl -s "https://api-energiemonitor.eon.com/region-data?regionUrlKey=<slug>" | python3 -m json.tool
```

Relevantes Feld: **`regionCode`** → Wert für `region_code` in `configuration.yaml`.  
Beispiel Bayernwerk: `curl -s "https://api-energiemonitor.eon.com/region-data?regionUrlKey=aichach"`

### 3. In dieser Datei suchen

Editor-Suche (`Cmd+F` / `Strg+F`) nach dem Gemeindenamen, oder im Terminal:

```bash
rg -i "Poing" doc/REGIONEN.md
# oder
grep -i "Poing" doc/REGIONEN.md
```

Die Spalte **`region_code`** ist der Wert für die Integration.

### 4. Live in der API (ohne diese Datei)

Alle Netzbetreiber:

```bash
curl -s "https://api-energiemonitor.eon.com/tenants" | python3 -m json.tool
```

Alle Regionen eines Netzbetreibers (z. B. Bayernwerk `tenantId=3190`):

```bash
curl -s "https://api-energiemonitor.eon.com/region-data?tenantId=3190" | python3 -m json.tool
```

Einzelne Gemeinde per Slug — siehe Abschnitt 2.

**Hinweis:** `GET /regions` antwortet mit HTTP 403. Die vollständige Liste kommt über **`region-data?tenantId=…`** ohne `regionCode`/`regionUrlKey`.

## Liste neu erzeugen

Diese Markdown-Datei wird nicht von Hand gepflegt:

```bash
cd /path/to/eon-energiemonitor
python3 scripts/generate-regions-doc.py
```

Das Skript liest `tenants` und pro Tenant `region-data?tenantId=…` und überschreibt `doc/REGIONEN.md`.

## Übersicht Netzbetreiber

| Kürzel | Netzbetreiber | `tenantId` | Regionen |
|---|---|---|---|
| AVACON | Avacon Netz GmbH | `0901` | 312 |
| BAGR | Bayernwerk Netz GmbH | `3190` | 138 |
| EDIS | E.DIS Netz GmbH | `1101` | 2 |
| LEW | Lechwerke AG | `LEW` | 8 |
| SHNETZ | Schleswig-Holstein Netz GmbH | `1556` | 1004 |
| VSE | VSE AG | `5030` | 1 |
| WHITELABEL | E.ON Grid Solutions GmbH | `4711` | 36 |
| WN | Westenergie AG | `2200` | 50 |
| enviaM | envia Mitteldeutsche Energie AG | `2700` | 0 |

## Regionen nach Netzbetreiber

### AVACON — Avacon Netz GmbH (`tenantId=0901`)

Dashboard-Basis: `https://energiemonitor.avacon.de/<regionUrlKey>` — **312** Regionen.

| Gemeinde / Region | `region_code` | URL-Slug | Dashboard |
|---|---|---|---|
| Adendorf | `03355001` | `adendorf` | [adendorf](https://energiemonitor.avacon.de/adendorf) |
| Algermissen | `03254003` | `algermissen` | [algermissen](https://energiemonitor.avacon.de/algermissen) |
| Amelinghausen | `03355002` | `amelinghausen` | [amelinghausen](https://energiemonitor.avacon.de/amelinghausen) |
| Bad Salzdetfurth | `03254005` | `bad-salzdetfurth` | [bad-salzdetfurth](https://energiemonitor.avacon.de/bad-salzdetfurth) |
| Barnstorf | `03251005` | `barnstorf` | [barnstorf](https://energiemonitor.avacon.de/barnstorf) |
| Barsinghausen | `03241002` | `barsinghausen` | [barsinghausen](https://energiemonitor.avacon.de/barsinghausen) |
| Bergen an der Dumme | `03354001` | `bergen-an-der-dumme` | [bergen-an-der-dumme](https://energiemonitor.avacon.de/bergen-an-der-dumme) |
| Betzendorf | `03355008` | `betzendorf` | [betzendorf](https://energiemonitor.avacon.de/betzendorf) |
| Bockenem | `03254008` | `bockenem` | [bockenem](https://energiemonitor.avacon.de/bockenem) |
| Burgwedel | `03241004` | `burgwedel` | [burgwedel](https://energiemonitor.avacon.de/burgwedel) |
| Calbe (Saale) | `15089055` | `calbe` | [calbe](https://energiemonitor.avacon.de/calbe) |
| Celle-Uelzen Netz | `03351006` | `celle-uelzen-netz` | [celle-uelzen-netz](https://energiemonitor.avacon.de/celle-uelzen-netz) |
| Clenze | `03354002` | `clenze` | [clenze](https://energiemonitor.avacon.de/clenze) |
| Cremlingen | `03158006` | `cremlingen` | [cremlingen](https://energiemonitor.avacon.de/cremlingen) |
| Diekholzen | `03254011` | `diekholzen` | [diekholzen](https://energiemonitor.avacon.de/diekholzen) |
| Dörverden | `03361003` | `doerverden` | [doerverden](https://energiemonitor.avacon.de/doerverden) |
| Elze | `03254014` | `elze` | [elze](https://energiemonitor.avacon.de/elze) |
| Flecken Ahlden (Aller) | `03358001` | `ahlden` | [ahlden](https://energiemonitor.avacon.de/ahlden) |
| Flecken Artlenburg | `03355003` | `artlenburg` | [artlenburg](https://energiemonitor.avacon.de/artlenburg) |
| Flecken Bardowick | `03355004` | `flecken-bardowick` | [flecken-bardowick](https://energiemonitor.avacon.de/flecken-bardowick) |
| Flecken Delligsen | `03255008` | `delligsen` | [delligsen](https://energiemonitor.avacon.de/delligsen) |
| Flecken Diepenau | `03256004` | `diepenau` | [diepenau](https://energiemonitor.avacon.de/diepenau) |
| Flecken Duingen | `03254041` | `duingen` | [duingen](https://energiemonitor.avacon.de/duingen) |
| Flecken Gartow | `03354005` | `flecken-gartow` | [flecken-gartow](https://energiemonitor.avacon.de/flecken-gartow) |
| Flecken Harpstedt | `03458008` | `harpstedt` | [harpstedt](https://energiemonitor.avacon.de/harpstedt) |
| Flecken Steyerberg | `03256030` | `flecken-steyerberg` | [flecken-steyerberg](https://energiemonitor.avacon.de/flecken-steyerberg) |
| Flecken Uchte | `03256033` | `flecken-uchte` | [flecken-uchte](https://energiemonitor.avacon.de/flecken-uchte) |
| Freden (Leine) | `03254042` | `freden` | [freden](https://energiemonitor.avacon.de/freden) |
| Gardelegen | `15081135` | `gardelegen` | [gardelegen](https://energiemonitor.avacon.de/gardelegen) |
| Gehrden | `03241006` | `gehrden` | [gehrden](https://energiemonitor.avacon.de/gehrden) |
| Gemeinde Aland | `15090003` | `aland` | [aland](https://energiemonitor.avacon.de/aland) |
| Gemeinde Altenhausen | `15083020` | `gemeinde-altenhausen` | [gemeinde-altenhausen](https://energiemonitor.avacon.de/gemeinde-altenhausen) |
| Gemeinde Altmärkische Höhe | `15090007` | `altmaerkische-hoehe` | [altmaerkische-hoehe](https://energiemonitor.avacon.de/altmaerkische-hoehe) |
| Gemeinde Altmärkische Wische | `15090008` | `altmaerkische-wische` | [altmaerkische-wische](https://energiemonitor.avacon.de/altmaerkische-wische) |
| Gemeinde Am Großen Bruch | `15083025` | `am-grossen-bruch` | [am-grossen-bruch](https://energiemonitor.avacon.de/am-grossen-bruch) |
| Gemeinde Angern | `15083030` | `angern` | [angern](https://energiemonitor.avacon.de/angern) |
| Gemeinde Arneburg | `15090010` | `arneburg` | [arneburg](https://energiemonitor.avacon.de/arneburg) |
| Gemeinde Asendorf | `03251002` | `asendorf` | [asendorf](https://energiemonitor.avacon.de/asendorf) |
| Gemeinde Ausleben | `15083035` | `ausleben` | [ausleben](https://energiemonitor.avacon.de/ausleben) |
| Gemeinde Baddeckenstedt | `03158002` | `baddeckenstedt` | [baddeckenstedt](https://energiemonitor.avacon.de/baddeckenstedt) |
| Gemeinde Balge | `03256001` | `balge` | [balge](https://energiemonitor.avacon.de/balge) |
| Gemeinde Barendorf | `03355005` | `gemeinde-barendorf` | [gemeinde-barendorf](https://energiemonitor.avacon.de/gemeinde-barendorf) |
| Gemeinde Barleben | `15083040` | `gemeinde-barleben` | [gemeinde-barleben](https://energiemonitor.avacon.de/gemeinde-barleben) |
| Gemeinde Barnstedt | `03355006` | `barnstedt` | [barnstedt](https://energiemonitor.avacon.de/barnstedt) |
| Gemeinde Barum | `03355007` | `gemeinde-barum` | [gemeinde-barum](https://energiemonitor.avacon.de/gemeinde-barum) |
| Gemeinde Beendorf | `15083060` | `gemeinde-beendorf` | [gemeinde-beendorf](https://energiemonitor.avacon.de/gemeinde-beendorf) |
| Gemeinde Biederitz | `15086005` | `biederitz` | [biederitz](https://energiemonitor.avacon.de/biederitz) |
| Gemeinde Binnen | `03256002` | `binnen` | [binnen](https://energiemonitor.avacon.de/binnen) |
| Gemeinde Borne | `15089045` | `borne` | [borne](https://energiemonitor.avacon.de/borne) |
| Gemeinde Brietlingen | `03355011` | `brietlingen` | [brietlingen](https://energiemonitor.avacon.de/brietlingen) |
| Gemeinde Bruchhausen-Vilsen | `03251049` | `gemeinde-bruchhausen-vilsen` | [gemeinde-bruchhausen-vilsen](https://energiemonitor.avacon.de/gemeinde-bruchhausen-vilsen) |
| Gemeinde Buchholz (Aller) | `03358005` | `buchholz` | [buchholz](https://energiemonitor.avacon.de/buchholz) |
| Gemeinde Burgdorf | `03158004` | `gemeinde-burgdorf` | [gemeinde-burgdorf](https://energiemonitor.avacon.de/gemeinde-burgdorf) |
| Gemeinde Burgstall | `15083120` | `burgstall` | [burgstall](https://energiemonitor.avacon.de/burgstall) |
| Gemeinde Börde-Hakel | `15089043` | `boerde-hakel` | [boerde-hakel](https://energiemonitor.avacon.de/boerde-hakel) |
| Gemeinde Bördeaue | `15089041` | `boerdeaue` | [boerdeaue](https://energiemonitor.avacon.de/boerdeaue) |
| Gemeinde Bücken | `03256003` | `buecken` | [buecken](https://energiemonitor.avacon.de/buecken) |
| Gemeinde Bülstringen | `15083115` | `gemeinde-buelstringen` | [gemeinde-buelstringen](https://energiemonitor.avacon.de/gemeinde-buelstringen) |
| Gemeinde Calvörde | `15083125` | `gemeinde-calvoerde` | [gemeinde-calvoerde](https://energiemonitor.avacon.de/gemeinde-calvoerde) |
| Gemeinde Colbitz | `15083130` | `colbitz` | [colbitz](https://energiemonitor.avacon.de/colbitz) |
| Gemeinde Cramme | `03158005` | `cramme` | [cramme](https://energiemonitor.avacon.de/cramme) |
| Gemeinde Dahlum | `03158007` | `dahlum` | [dahlum](https://energiemonitor.avacon.de/dahlum) |
| Gemeinde Denkte | `03158008` | `denkte` | [denkte](https://energiemonitor.avacon.de/denkte) |
| Gemeinde Dettum | `03158009` | `dettum` | [dettum](https://energiemonitor.avacon.de/dettum) |
| Gemeinde Deutsch Evern | `03355014` | `deutsch-evern` | [deutsch-evern](https://energiemonitor.avacon.de/deutsch-evern) |
| Gemeinde Diesdorf | `15081105` | `diesdorf` | [diesdorf](https://energiemonitor.avacon.de/diesdorf) |
| Gemeinde Drakenburg | `03256005` | `drakenburg` | [drakenburg](https://energiemonitor.avacon.de/drakenburg) |
| Gemeinde Dähre | `15081095` | `daehre` | [daehre](https://energiemonitor.avacon.de/daehre) |
| Gemeinde Echem | `03355015` | `echem` | [echem](https://energiemonitor.avacon.de/echem) |
| Gemeinde Edemissen | `03157001` | `gemeinde-edemissen` | [gemeinde-edemissen](https://energiemonitor.avacon.de/gemeinde-edemissen) |
| Gemeinde Eichstedt | `15090135` | `eichstedt` | [eichstedt](https://energiemonitor.avacon.de/eichstedt) |
| Gemeinde Eickeloh | `03358006` | `eickeloh` | [eickeloh](https://energiemonitor.avacon.de/eickeloh) |
| Gemeinde Eilsleben | `15083190` | `gemeinde-eilsleben` | [gemeinde-eilsleben](https://energiemonitor.avacon.de/gemeinde-eilsleben) |
| Gemeinde Elbe | `03158011` | `elbe` | [elbe](https://energiemonitor.avacon.de/elbe) |
| Gemeinde Elbe-Parey | `15086035` | `elbe-parey` | [elbe-parey](https://energiemonitor.avacon.de/elbe-parey) |
| Gemeinde Embsen | `03355016` | `embsen` | [embsen](https://energiemonitor.avacon.de/embsen) |
| Gemeinde Erkerode | `03158012` | `erkerode` | [erkerode](https://energiemonitor.avacon.de/erkerode) |
| Gemeinde Erxleben | `15083205` | `gemeinde-erxleben` | [gemeinde-erxleben](https://energiemonitor.avacon.de/gemeinde-erxleben) |
| Gemeinde Essel | `03358007` | `essel` | [essel](https://energiemonitor.avacon.de/essel) |
| Gemeinde Estorf | `03256006` | `gemeinde-estorf` | [gemeinde-estorf](https://energiemonitor.avacon.de/gemeinde-estorf) |
| Gemeinde Evessen | `03158013` | `evessen` | [evessen](https://energiemonitor.avacon.de/evessen) |
| Gemeinde Eystrup | `03256007` | `eystrup` | [eystrup](https://energiemonitor.avacon.de/eystrup) |
| Gemeinde Flechtingen | `15083230` | `flechtingen` | [flechtingen](https://energiemonitor.avacon.de/flechtingen) |
| Gemeinde Flöthe | `03158014` | `floethe` | [floethe](https://energiemonitor.avacon.de/floethe) |
| Gemeinde Gandesbergen | `03256008` | `gandesbergen` | [gandesbergen](https://energiemonitor.avacon.de/gandesbergen) |
| Gemeinde Gilten | `03358010` | `gilten` | [gilten](https://energiemonitor.avacon.de/gilten) |
| Gemeinde Goldbeck | `15090180` | `goldbeck` | [goldbeck](https://energiemonitor.avacon.de/goldbeck) |
| Gemeinde Gorleben | `03354007` | `gorleben` | [gorleben](https://energiemonitor.avacon.de/gorleben) |
| Gemeinde Groß Quenstedt | `15085125` | `gross-quenstedt` | [gross-quenstedt](https://energiemonitor.avacon.de/gross-quenstedt) |
| Gemeinde Handorf | `03355017` | `gemeinde-handorf` | [gemeinde-handorf](https://energiemonitor.avacon.de/gemeinde-handorf) |
| Gemeinde Harbke | `15083275` | `gemeinde-harbke` | [gemeinde-harbke](https://energiemonitor.avacon.de/gemeinde-harbke) |
| Gemeinde Harsleben | `15085140` | `harsleben` | [harsleben](https://energiemonitor.avacon.de/harsleben) |
| Gemeinde Hassel | `15090220` | `hassel` | [hassel](https://energiemonitor.avacon.de/hassel) |
| Gemeinde Hassel (Weser) | `03256010` | `hassel-weser` | [hassel-weser](https://energiemonitor.avacon.de/hassel-weser) |
| Gemeinde Haverlah | `03158016` | `haverlah` | [haverlah](https://energiemonitor.avacon.de/haverlah) |
| Gemeinde Haßbergen | `03256011` | `hassbergen` | [hassbergen](https://energiemonitor.avacon.de/hassbergen) |
| Gemeinde Heemsen | `03256012` | `gemeinde-heemsen` | [gemeinde-heemsen](https://energiemonitor.avacon.de/gemeinde-heemsen) |
| Gemeinde Heere | `03158018` | `heere` | [heere](https://energiemonitor.avacon.de/heere) |
| Gemeinde Hilgermissen | `03256013` | `hilgermissen` | [hilgermissen](https://energiemonitor.avacon.de/hilgermissen) |
| Gemeinde Hillerse | `03151012` | `hillerse` | [hillerse](https://energiemonitor.avacon.de/hillerse) |
| Gemeinde Hittbergen | `03355018` | `hittbergen` | [hittbergen](https://energiemonitor.avacon.de/hittbergen) |
| Gemeinde Hohe Börde | `15083298` | `hohe-boerde` | [hohe-boerde](https://energiemonitor.avacon.de/hohe-boerde) |
| Gemeinde Hohenberg-Krusemark | `15090245` | `hohenberg-krusemark` | [hohenberg-krusemark](https://energiemonitor.avacon.de/hohenberg-krusemark) |
| Gemeinde Hohnstorf (Elbe) | `03355019` | `hohnstorf` | [hohnstorf](https://energiemonitor.avacon.de/hohnstorf) |
| Gemeinde Hoya | `03256014` | `gemeinde-hoya` | [gemeinde-hoya](https://energiemonitor.avacon.de/gemeinde-hoya) |
| Gemeinde Hoyerhagen | `03256015` | `hoyerhagen` | [hoyerhagen](https://energiemonitor.avacon.de/hoyerhagen) |
| Gemeinde Husum | `03256016` | `gemeinde-husum` | [gemeinde-husum](https://energiemonitor.avacon.de/gemeinde-husum) |
| Gemeinde Hämelhausen | `03256009` | `haemelhausen` | [haemelhausen](https://energiemonitor.avacon.de/haemelhausen) |
| Gemeinde Hötensleben | `15083320` | `gemeinde-hoetensleben` | [gemeinde-hoetensleben](https://energiemonitor.avacon.de/gemeinde-hoetensleben) |
| Gemeinde Iden | `15090270` | `iden` | [iden](https://energiemonitor.avacon.de/iden) |
| Gemeinde Ingersleben | `15083323` | `gemeinde-ingersleben` | [gemeinde-ingersleben](https://energiemonitor.avacon.de/gemeinde-ingersleben) |
| Gemeinde Kamern | `15090285` | `kamern` | [kamern](https://energiemonitor.avacon.de/kamern) |
| Gemeinde Klietz | `15090310` | `klietz` | [klietz](https://energiemonitor.avacon.de/klietz) |
| Gemeinde Kneitlingen | `03158022` | `kneitlingen` | [kneitlingen](https://energiemonitor.avacon.de/kneitlingen) |
| Gemeinde Landesbergen | `03256017` | `gemeinde-landesbergen` | [gemeinde-landesbergen](https://energiemonitor.avacon.de/gemeinde-landesbergen) |
| Gemeinde Leese | `03256018` | `gemeinde-leese` | [gemeinde-leese](https://energiemonitor.avacon.de/gemeinde-leese) |
| Gemeinde Leiferde | `03151015` | `leiferde` | [leiferde](https://energiemonitor.avacon.de/leiferde) |
| Gemeinde Liebenau | `03256019` | `liebenau` | [liebenau](https://energiemonitor.avacon.de/liebenau) |
| Gemeinde Lindwedel | `03358015` | `lindwedel` | [lindwedel](https://energiemonitor.avacon.de/lindwedel) |
| Gemeinde Loitsche-Heinrichsberg | `15083361` | `loitsche-heinrichsberg` | [loitsche-heinrichsberg](https://energiemonitor.avacon.de/loitsche-heinrichsberg) |
| Gemeinde Marklohe | `03256021` | `marklohe` | [marklohe](https://energiemonitor.avacon.de/marklohe) |
| Gemeinde Martfeld | `03251026` | `martfeld` | [martfeld](https://energiemonitor.avacon.de/martfeld) |
| Gemeinde Mechtersen | `03355023` | `gemeinde-mechtersen` | [gemeinde-mechtersen](https://energiemonitor.avacon.de/gemeinde-mechtersen) |
| Gemeinde Meinersen | `03151017` | `gemeinde-meinersen` | [gemeinde-meinersen](https://energiemonitor.avacon.de/gemeinde-meinersen) |
| Gemeinde Melbeck | `03355024` | `melbeck` | [melbeck](https://energiemonitor.avacon.de/melbeck) |
| Gemeinde Müden (Aller) | `03151018` | `mueden-aller` | [mueden-aller](https://energiemonitor.avacon.de/mueden-aller) |
| Gemeinde Niedere Börde | `15083390` | `niedere-boerde` | [niedere-boerde](https://energiemonitor.avacon.de/niedere-boerde) |
| Gemeinde Nordharz | `15085227` | `gemeinde-nordharz` | [gemeinde-nordharz](https://energiemonitor.avacon.de/gemeinde-nordharz) |
| Gemeinde Pennigsehl | `03256023` | `pennigsehl` | [pennigsehl](https://energiemonitor.avacon.de/pennigsehl) |
| Gemeinde Radbruch | `03355028` | `radbruch` | [radbruch](https://energiemonitor.avacon.de/radbruch) |
| Gemeinde Remlingen-Semmenstedt | `03158040` | `remlingen-semmenstedt` | [remlingen-semmenstedt](https://energiemonitor.avacon.de/remlingen-semmenstedt) |
| Gemeinde Rochau | `15090435` | `rochau` | [rochau](https://energiemonitor.avacon.de/rochau) |
| Gemeinde Rogätz | `15083440` | `rogaetz` | [rogaetz](https://energiemonitor.avacon.de/rogaetz) |
| Gemeinde Rohrsen | `03256027` | `rohrsen` | [rohrsen](https://energiemonitor.avacon.de/rohrsen) |
| Gemeinde Roklum | `03158025` | `roklum` | [roklum](https://energiemonitor.avacon.de/roklum) |
| Gemeinde Rullstorf | `03355032` | `rullstorf` | [rullstorf](https://energiemonitor.avacon.de/rullstorf) |
| Gemeinde Sandau (Elbe) | `15090445` | `sandau` | [sandau](https://energiemonitor.avacon.de/sandau) |
| Gemeinde Scharnebeck | `03355033` | `scharnebeck` | [scharnebeck](https://energiemonitor.avacon.de/scharnebeck) |
| Gemeinde Schollene | `15090485` | `schollene` | [schollene](https://energiemonitor.avacon.de/schollene) |
| Gemeinde Schwarme | `03251033` | `schwarme` | [schwarme](https://energiemonitor.avacon.de/schwarme) |
| Gemeinde Schwarmstedt | `03358020` | `schwarmstedt` | [schwarmstedt](https://energiemonitor.avacon.de/schwarmstedt) |
| Gemeinde Schweringen | `03256028` | `schweringen` | [schweringen](https://energiemonitor.avacon.de/schweringen) |
| Gemeinde Schönhausen (Elbe) | `15090500` | `schoenhausen` | [schoenhausen](https://energiemonitor.avacon.de/schoenhausen) |
| Gemeinde Seehausen (Altmark) | `15090520` | `gemeinde-seehausen` | [gemeinde-seehausen](https://energiemonitor.avacon.de/gemeinde-seehausen) |
| Gemeinde Sehlde | `03158028` | `sehlde` | [sehlde](https://energiemonitor.avacon.de/sehlde) |
| Gemeinde Sickte | `03158030` | `gemeinde-sickte` | [gemeinde-sickte](https://energiemonitor.avacon.de/gemeinde-sickte) |
| Gemeinde Sommersdorf | `15083485` | `gemeinde-sommersdorf` | [gemeinde-sommersdorf](https://energiemonitor.avacon.de/gemeinde-sommersdorf) |
| Gemeinde Stuhr | `03251037` | `stuhr` | [stuhr](https://energiemonitor.avacon.de/stuhr) |
| Gemeinde Südergellersen | `03355035` | `suedergellersen` | [suedergellersen](https://energiemonitor.avacon.de/suedergellersen) |
| Gemeinde Sülzetal | `15083490` | `suelzetal` | [suelzetal](https://energiemonitor.avacon.de/suelzetal) |
| Gemeinde Thomasburg | `03355036` | `gemeinde-thomasburg` | [gemeinde-thomasburg](https://energiemonitor.avacon.de/gemeinde-thomasburg) |
| Gemeinde Uehrde | `03158031` | `uehrde` | [uehrde](https://energiemonitor.avacon.de/uehrde) |
| Gemeinde Ummendorf | `15083505` | `gemeinde-ummendorf` | [gemeinde-ummendorf](https://energiemonitor.avacon.de/gemeinde-ummendorf) |
| Gemeinde Vahlberg | `03158032` | `vahlberg` | [vahlberg](https://energiemonitor.avacon.de/vahlberg) |
| Gemeinde Veltheim (Ohe) | `03158033` | `veltheim` | [veltheim](https://energiemonitor.avacon.de/veltheim) |
| Gemeinde Vögelsen | `03355039` | `voegelsen` | [voegelsen](https://energiemonitor.avacon.de/voegelsen) |
| Gemeinde Völpke | `15083515` | `gemeinde-voelpke` | [gemeinde-voelpke](https://energiemonitor.avacon.de/gemeinde-voelpke) |
| Gemeinde Wagenfeld | `03251044` | `wagenfeld` | [wagenfeld](https://energiemonitor.avacon.de/wagenfeld) |
| Gemeinde Wallstawe | `15081545` | `wallstawe` | [wallstawe](https://energiemonitor.avacon.de/wallstawe) |
| Gemeinde Warpe | `03256035` | `warpe` | [warpe](https://energiemonitor.avacon.de/warpe) |
| Gemeinde Wefensleben | `15083535` | `gemeinde-wefensleben` | [gemeinde-wefensleben](https://energiemonitor.avacon.de/gemeinde-wefensleben) |
| Gemeinde Werben | `15090610` | `werben` | [werben](https://energiemonitor.avacon.de/werben) |
| Gemeinde Westheide | `15083557` | `westheide` | [westheide](https://energiemonitor.avacon.de/westheide) |
| Gemeinde Wietzen | `03256036` | `wietzen` | [wietzen](https://energiemonitor.avacon.de/wietzen) |
| Gemeinde Winnigstedt | `03158035` | `winnigstedt` | [winnigstedt](https://energiemonitor.avacon.de/winnigstedt) |
| Gemeinde Wittmar | `03158036` | `wittmar` | [wittmar](https://energiemonitor.avacon.de/wittmar) |
| Gemeinde Wittorf | `03355042` | `wittorf` | [wittorf](https://energiemonitor.avacon.de/wittorf) |
| Gemeinde Wolmirsleben | `15089365` | `wolmirsleben` | [wolmirsleben](https://energiemonitor.avacon.de/wolmirsleben) |
| Gemeinde Wust-Fischbeck | `15090631` | `wust-fischbeck` | [wust-fischbeck](https://energiemonitor.avacon.de/wust-fischbeck) |
| Gemeinde Zehrental | `15090635` | `zehrental` | [zehrental](https://energiemonitor.avacon.de/zehrental) |
| Gemeinde Zielitz | `15083580` | `zielitz` | [zielitz](https://energiemonitor.avacon.de/zielitz) |
| Giesen | `03254017` | `giesen` | [giesen](https://energiemonitor.avacon.de/giesen) |
| Gommern | `15086055` | `gommern` | [gommern](https://energiemonitor.avacon.de/gommern) |
| Grethem | `03358011` | `grethem` | [grethem](https://energiemonitor.avacon.de/grethem) |
| Gröningen | `15083245` | `groeningen` | [groeningen](https://energiemonitor.avacon.de/groeningen) |
| Gödenstorf | `03353013` | `goedenstorf` | [goedenstorf](https://energiemonitor.avacon.de/goedenstorf) |
| Hademstorf | `03358012` | `hademstorf` | [hademstorf](https://energiemonitor.avacon.de/hademstorf) |
| Hansestadt Lüneburg | `03355022` | `lueneburg` | [lueneburg](https://energiemonitor.avacon.de/lueneburg) |
| Hansestadt Osterburg (Altmark) | `15090415` | `osterburg` | [osterburg](https://energiemonitor.avacon.de/osterburg) |
| Hansestadt Salzwedel | `15081455` | `salzwedel` | [salzwedel](https://energiemonitor.avacon.de/salzwedel) |
| Harsum | `03254020` | `harsum` | [harsum](https://energiemonitor.avacon.de/harsum) |
| Hemmingen | `03241007` | `hemmingen` | [hemmingen](https://energiemonitor.avacon.de/hemmingen) |
| Hodenhagen | `03358014` | `hodenhagen` | [hodenhagen](https://energiemonitor.avacon.de/hodenhagen) |
| Hohenhameln | `03157002` | `hohenhameln` | [hohenhameln](https://energiemonitor.avacon.de/hohenhameln) |
| Holle | `03254022` | `holle` | [holle](https://energiemonitor.avacon.de/holle) |
| Höhbeck | `03354010` | `hoehbeck` | [hoehbeck](https://energiemonitor.avacon.de/hoehbeck) |
| Ilsede | `03157009` | `ilsede` | [ilsede](https://energiemonitor.avacon.de/ilsede) |
| Isernhagen | `03241008` | `isernhagen` | [isernhagen](https://energiemonitor.avacon.de/isernhagen) |
| Kirchgellersen | `03355020` | `kirchgellersen` | [kirchgellersen](https://energiemonitor.avacon.de/kirchgellersen) |
| Königslutter am Elm | `03154013` | `koenigslutter-am-elm` | [koenigslutter-am-elm](https://energiemonitor.avacon.de/koenigslutter-am-elm) |
| Küsten | `03354013` | `kuesten` | [kuesten](https://energiemonitor.avacon.de/kuesten) |
| Lamspringe | `03254044` | `lamspringe` | [lamspringe](https://energiemonitor.avacon.de/lamspringe) |
| Landkreis Gifhorn | `03151` | `landkreis-gifhorn` | [landkreis-gifhorn](https://energiemonitor.avacon.de/landkreis-gifhorn) |
| Landkreis Goslar | `03153` | `landkreis-goslar` | [landkreis-goslar](https://energiemonitor.avacon.de/landkreis-goslar) |
| Landkreis Helmstedt | `03154` | `landkreis-helmstedt` | [landkreis-helmstedt](https://energiemonitor.avacon.de/landkreis-helmstedt) |
| Landkreis Hildesheim | `03254` | `landkreis-hildesheim` | [landkreis-hildesheim](https://energiemonitor.avacon.de/landkreis-hildesheim) |
| Landkreis Lüneburg | `03355` | `landkreis-lueneburg` | [landkreis-lueneburg](https://energiemonitor.avacon.de/landkreis-lueneburg) |
| Landkreis Nienburg | `03256` | `landkreis-nienburg` | [landkreis-nienburg](https://energiemonitor.avacon.de/landkreis-nienburg) |
| Landkreis Peine | `03157` | `landkreis-peine` | [landkreis-peine](https://energiemonitor.avacon.de/landkreis-peine) |
| Landkreis Uelzen | `03360` | `landkreis-uelzen` | [landkreis-uelzen](https://energiemonitor.avacon.de/landkreis-uelzen) |
| Landkreis Wolfenbüttel | `03158` | `landkreis-wolfenbuettel` | [landkreis-wolfenbuettel](https://energiemonitor.avacon.de/landkreis-wolfenbuettel) |
| Lehre | `03154014` | `lehre` | [lehre](https://energiemonitor.avacon.de/lehre) |
| Lehrte | `03241011` | `lehrte` | [lehrte](https://energiemonitor.avacon.de/lehrte) |
| Lemgow | `03354015` | `lemgow` | [lemgow](https://energiemonitor.avacon.de/lemgow) |
| Lengede | `03157005` | `lengede` | [lengede](https://energiemonitor.avacon.de/lengede) |
| Liebenburg | `03153008` | `liebenburg` | [liebenburg](https://energiemonitor.avacon.de/liebenburg) |
| Linsburg | `03256020` | `linsburg` | [linsburg](https://energiemonitor.avacon.de/linsburg) |
| Luckau (Wendland) | `03354016` | `luckau-wendland` | [luckau-wendland](https://energiemonitor.avacon.de/luckau-wendland) |
| Lübbow | `03354017` | `luebbow` | [luebbow](https://energiemonitor.avacon.de/luebbow) |
| Lüchow (Wendland) | `03354018` | `luechow-wendland` | [luechow-wendland](https://energiemonitor.avacon.de/luechow-wendland) |
| Möser | `15086145` | `moeser` | [moeser](https://energiemonitor.avacon.de/moeser) |
| Neetze | `03355026` | `neetze` | [neetze](https://energiemonitor.avacon.de/neetze) |
| Nordstemmen | `03254026` | `nordstemmen` | [nordstemmen](https://energiemonitor.avacon.de/nordstemmen) |
| Oldendorf (Luhe) | `03355027` | `oldendorf-luhe` | [oldendorf-luhe](https://energiemonitor.avacon.de/oldendorf-luhe) |
| Oschersleben (Bode) | `15083415` | `oschersleben` | [oschersleben](https://energiemonitor.avacon.de/oschersleben) |
| Pattensen | `03241013` | `pattensen` | [pattensen](https://energiemonitor.avacon.de/pattensen) |
| Prezelle | `03354020` | `prezelle` | [prezelle](https://energiemonitor.avacon.de/prezelle) |
| Raddestorf | `03256024` | `raddestorf` | [raddestorf](https://energiemonitor.avacon.de/raddestorf) |
| Region Hannover | `03241` | `region-hannover` | [region-hannover](https://energiemonitor.avacon.de/region-hannover) |
| Regionalverband Großraum Braunschweig | `03777` | `rgb` | [rgb](https://energiemonitor.avacon.de/rgb) |
| Rehlingen | `03355029` | `rehlingen` | [rehlingen](https://energiemonitor.avacon.de/rehlingen) |
| Reppenstedt | `03355031` | `reppenstedt` | [reppenstedt](https://energiemonitor.avacon.de/reppenstedt) |
| Rodewald | `03256026` | `rodewald` | [rodewald](https://energiemonitor.avacon.de/rodewald) |
| Ronnenberg | `03241014` | `ronnenberg` | [ronnenberg](https://energiemonitor.avacon.de/ronnenberg) |
| Samtgemeinde Ahlden | `033585401` | `samtgemeinde-ahlden` | [samtgemeinde-ahlden](https://energiemonitor.avacon.de/samtgemeinde-ahlden) |
| Samtgemeinde Amelinghausen | `033555401` | `samtgemeinde-amelinghausen` | [samtgemeinde-amelinghausen](https://energiemonitor.avacon.de/samtgemeinde-amelinghausen) |
| Samtgemeinde Baddeckenstedt | `031585402` | `samtgemeinde-baddeckenstedt` | [samtgemeinde-baddeckenstedt](https://energiemonitor.avacon.de/samtgemeinde-baddeckenstedt) |
| Samtgemeinde Bardowick | `033555402` | `bardowick` | [bardowick](https://energiemonitor.avacon.de/bardowick) |
| Samtgemeinde Bruchhausen-Vilsen | `032515403` | `bruchhausen-vilsen` | [bruchhausen-vilsen](https://energiemonitor.avacon.de/bruchhausen-vilsen) |
| Samtgemeinde Elbmarsch | `033535401` | `samtgemeinde-elbmarsch` | [samtgemeinde-elbmarsch](https://energiemonitor.avacon.de/samtgemeinde-elbmarsch) |
| Samtgemeinde Elm-Asse | `031585407` | `elm-asse` | [elm-asse](https://energiemonitor.avacon.de/elm-asse) |
| Samtgemeinde Gartow | `033545403` | `samtgemeinde-gartow` | [samtgemeinde-gartow](https://energiemonitor.avacon.de/samtgemeinde-gartow) |
| Samtgemeinde Gellersen | `033555404` | `samtgemeinde-gellersen` | [samtgemeinde-gellersen](https://energiemonitor.avacon.de/samtgemeinde-gellersen) |
| Samtgemeinde Grafschaft Hoya | `032565409` | `sg-grafschaft-hoya` | [sg-grafschaft-hoya](https://energiemonitor.avacon.de/sg-grafschaft-hoya) |
| Samtgemeinde Heemsen | `032565402` | `heemsen` | [heemsen](https://energiemonitor.avacon.de/heemsen) |
| Samtgemeinde Ilmenau | `033555405` | `ilmenau` | [ilmenau](https://energiemonitor.avacon.de/ilmenau) |
| Samtgemeinde Leinebergland | `032545406` | `leinebergland` | [leinebergland](https://energiemonitor.avacon.de/leinebergland) |
| Samtgemeinde Lüchow | `033545407` | `samtgemeinde-luechow` | [samtgemeinde-luechow](https://energiemonitor.avacon.de/samtgemeinde-luechow) |
| Samtgemeinde Meinersen | `031515405` | `samtgemeinde-meinersen` | [samtgemeinde-meinersen](https://energiemonitor.avacon.de/samtgemeinde-meinersen) |
| Samtgemeinde Mittelweser | `032565410` | `mittelweser` | [mittelweser](https://energiemonitor.avacon.de/mittelweser) |
| Samtgemeinde Oderwald | `031585403` | `oderwald` | [oderwald](https://energiemonitor.avacon.de/oderwald) |
| Samtgemeinde Rehden | `032515405` | `rehden` | [rehden](https://energiemonitor.avacon.de/rehden) |
| Samtgemeinde Scharnebeck | `033555407` | `samtgemeinde-scharnebeck` | [samtgemeinde-scharnebeck](https://energiemonitor.avacon.de/samtgemeinde-scharnebeck) |
| Samtgemeinde Schwarmstedt | `033585403` | `samtgemeinde-schwarmstedt` | [samtgemeinde-schwarmstedt](https://energiemonitor.avacon.de/samtgemeinde-schwarmstedt) |
| Samtgemeinde Sickte | `031585406` | `sickte` | [sickte](https://energiemonitor.avacon.de/sickte) |
| Samtgemeinde Steimbke | `032565407` | `samtgemeinde-steimbke` | [samtgemeinde-steimbke](https://energiemonitor.avacon.de/samtgemeinde-steimbke) |
| Samtgemeinde Uchte | `032565408` | `samtgemeinde-uchte` | [samtgemeinde-uchte](https://energiemonitor.avacon.de/samtgemeinde-uchte) |
| Samtgemeinde Weser-Aue | `032565411` | `weser-aue` | [weser-aue](https://energiemonitor.avacon.de/weser-aue) |
| Sarstedt | `03254028` | `sarstedt` | [sarstedt](https://energiemonitor.avacon.de/sarstedt) |
| Schellerten | `03254029` | `schellerten` | [schellerten](https://energiemonitor.avacon.de/schellerten) |
| Schladen-Werla | `03158039` | `schladen-werla` | [schladen-werla](https://energiemonitor.avacon.de/schladen-werla) |
| Schnega | `03354022` | `schnega` | [schnega](https://energiemonitor.avacon.de/schnega) |
| Schöningen | `03154019` | `schoeningen` | [schoeningen](https://energiemonitor.avacon.de/schoeningen) |
| Seelze | `03241015` | `seelze` | [seelze](https://energiemonitor.avacon.de/seelze) |
| Sehnde | `03241016` | `sehnde` | [sehnde](https://energiemonitor.avacon.de/sehnde) |
| Sibbesse | `03254045` | `sibbesse` | [sibbesse](https://energiemonitor.avacon.de/sibbesse) |
| Soderstorf | `03355034` | `soderstorf` | [soderstorf](https://energiemonitor.avacon.de/soderstorf) |
| Springe | `03241017` | `springe` | [springe](https://energiemonitor.avacon.de/springe) |
| Stadt Alfeld | `03254002` | `alfeld` | [alfeld](https://energiemonitor.avacon.de/alfeld) |
| Stadt Arendsee (Altmark) | `15081030` | `arendsee` | [arendsee](https://energiemonitor.avacon.de/arendsee) |
| Stadt Barby | `15089026` | `stadt-barby` | [stadt-barby](https://energiemonitor.avacon.de/stadt-barby) |
| Stadt Bassum | `03251007` | `bassum` | [bassum](https://energiemonitor.avacon.de/bassum) |
| Stadt Bismark (Altmark) | `15090070` | `bismark` | [bismark](https://energiemonitor.avacon.de/bismark) |
| Stadt Braunschweig | `03101000` | `braunschweig` | [braunschweig](https://energiemonitor.avacon.de/braunschweig) |
| Stadt Diepholz | `03251012` | `diepholz` | [diepholz](https://energiemonitor.avacon.de/diepholz) |
| Stadt Egeln | `15089075` | `egeln` | [egeln](https://energiemonitor.avacon.de/egeln) |
| Stadt Genthin | `15086040` | `genthin` | [genthin](https://energiemonitor.avacon.de/genthin) |
| Stadt Helmstedt | `03154028` | `stadt-helmstedt` | [stadt-helmstedt](https://energiemonitor.avacon.de/stadt-helmstedt) |
| Stadt Jerichow | `15086080` | `jerichow` | [jerichow](https://energiemonitor.avacon.de/jerichow) |
| Stadt Kalbe (Milde) | `15081240` | `kalbe` | [kalbe](https://energiemonitor.avacon.de/kalbe) |
| Stadt Klötze | `15081280` | `kloetze` | [kloetze](https://energiemonitor.avacon.de/kloetze) |
| Stadt Kroppenstedt | `15083355` | `kroppenstedt` | [kroppenstedt](https://energiemonitor.avacon.de/kroppenstedt) |
| Stadt Möckern | `15086140` | `moeckern` | [moeckern](https://energiemonitor.avacon.de/moeckern) |
| Stadt Nienburg/Weser | `03256022` | `nienburg` | [nienburg](https://energiemonitor.avacon.de/nienburg) |
| Stadt Oebisfelde-Weferlingen | `15083411` | `oebisfelde-weferlingen` | [oebisfelde-weferlingen](https://energiemonitor.avacon.de/oebisfelde-weferlingen) |
| Stadt Salzgitter | `03102000` | `salzgitter` | [salzgitter](https://energiemonitor.avacon.de/salzgitter) |
| Stadt Schnackenburg | `03354021` | `schnackenburg` | [schnackenburg](https://energiemonitor.avacon.de/schnackenburg) |
| Stadt Schwanebeck | `15085285` | `schwanebeck` | [schwanebeck](https://energiemonitor.avacon.de/schwanebeck) |
| Stadt Schöppenstedt | `03158027` | `schoeppenstedt` | [schoeppenstedt](https://energiemonitor.avacon.de/schoeppenstedt) |
| Stadt Tangerhütte | `15090546` | `tangerhuette` | [tangerhuette](https://energiemonitor.avacon.de/tangerhuette) |
| Stadt Tangermünde | `15090550` | `tangermuende` | [tangermuende](https://energiemonitor.avacon.de/tangermuende) |
| Stadt Visselhövede | `03357051` | `visselhoevede` | [visselhoevede](https://energiemonitor.avacon.de/visselhoevede) |
| Stadt Wegeleben | `15085365` | `wegeleben` | [wegeleben](https://energiemonitor.avacon.de/wegeleben) |
| Stadt Wolfsburg | `03103000` | `wolfsburg` | [wolfsburg](https://energiemonitor.avacon.de/wolfsburg) |
| Steimbke | `03256029` | `steimbke` | [steimbke](https://energiemonitor.avacon.de/steimbke) |
| Stöckse | `03256031` | `stoeckse` | [stoeckse](https://energiemonitor.avacon.de/stoeckse) |
| Syke | `03251041` | `syke` | [syke](https://energiemonitor.avacon.de/syke) |
| Söhlde | `03254032` | `soehlde` | [soehlde](https://energiemonitor.avacon.de/soehlde) |
| Trebel | `03354023` | `trebel` | [trebel](https://energiemonitor.avacon.de/trebel) |
| Twistringen | `03251042` | `twistringen` | [twistringen](https://energiemonitor.avacon.de/twistringen) |
| Uetze | `03241018` | `uetze` | [uetze](https://energiemonitor.avacon.de/uetze) |
| Vechelde | `03157007` | `vechelde` | [vechelde](https://energiemonitor.avacon.de/vechelde) |
| Verbandsgemeinde Arneburg-Goldbeck | `150905051` | `arneburg-goldbeck` | [arneburg-goldbeck](https://energiemonitor.avacon.de/arneburg-goldbeck) |
| Verbandsgemeinde Egelner Mulde | `150895051` | `egelner-mulde` | [egelner-mulde](https://energiemonitor.avacon.de/egelner-mulde) |
| Verbandsgemeinde Elbe-Havel-Land | `150905052` | `elbe-havel-land` | [elbe-havel-land](https://energiemonitor.avacon.de/elbe-havel-land) |
| Verbandsgemeinde Elbe-Heide | `150835051` | `elbe-heide` | [elbe-heide](https://energiemonitor.avacon.de/elbe-heide) |
| Verbandsgemeinde Flechtingen | `150835052` | `verbandsgemeinde-flechtingen` | [verbandsgemeinde-flechtingen](https://energiemonitor.avacon.de/verbandsgemeinde-flechtingen) |
| Verbandsgemeinde Obere Aller | `150835053` | `verbandsgemeinde-obere-aller` | [verbandsgemeinde-obere-aller](https://energiemonitor.avacon.de/verbandsgemeinde-obere-aller) |
| Verbandsgemeinde Seehausen (Altmark) | `150905053` | `seehausen` | [seehausen](https://energiemonitor.avacon.de/seehausen) |
| Verbandsgemeinde Westliche Börde | `150835054` | `westlicheboerde` | [westlicheboerde](https://energiemonitor.avacon.de/westlicheboerde) |
| Waddeweitz | `03354024` | `waddeweitz` | [waddeweitz](https://energiemonitor.avacon.de/waddeweitz) |
| Wanzleben-Börde | `15083531` | `wanzleben-boerde` | [wanzleben-boerde](https://energiemonitor.avacon.de/wanzleben-boerde) |
| Warmsen | `03256034` | `warmsen` | [warmsen](https://energiemonitor.avacon.de/warmsen) |
| Wedemark | `03241019` | `wedemark` | [wedemark](https://energiemonitor.avacon.de/wedemark) |
| Wendeburg | `03157008` | `wendeburg` | [wendeburg](https://energiemonitor.avacon.de/wendeburg) |
| Wendisch Evern | `03355040` | `wendisch-evern` | [wendisch-evern](https://energiemonitor.avacon.de/wendisch-evern) |
| Wennigsen | `03241020` | `wennigsen` | [wennigsen](https://energiemonitor.avacon.de/wennigsen) |
| Westergellersen | `03355041` | `westergellersen` | [westergellersen](https://energiemonitor.avacon.de/westergellersen) |
| Weyhe | `03251047` | `weyhe` | [weyhe](https://energiemonitor.avacon.de/weyhe) |
| Wolfenbüttel | `03158037` | `stadt-wolfenbuettel` | [stadt-wolfenbuettel](https://energiemonitor.avacon.de/stadt-wolfenbuettel) |
| Woltersdorf (Wendland) | `03354025` | `woltersdorf-wendland` | [woltersdorf-wendland](https://energiemonitor.avacon.de/woltersdorf-wendland) |
| Wustrow (Wendland) | `03354026` | `wustrow-wendland` | [wustrow-wendland](https://energiemonitor.avacon.de/wustrow-wendland) |
### BAGR — Bayernwerk Netz GmbH (`tenantId=3190`)

Dashboard-Basis: `https://energiemonitor.bayernwerk.de/<regionUrlKey>` — **138** Regionen.

| Gemeinde / Region | `region_code` | URL-Slug | Dashboard |
|---|---|---|---|
| Aichach | `09771113` | `aichach` | [aichach](https://energiemonitor.bayernwerk.de/aichach) |
| Altomünster | `09174111` | `altomuenster` | [altomuenster](https://energiemonitor.bayernwerk.de/altomuenster) |
| Anzing | `09175111` | `anzing` | [anzing](https://energiemonitor.bayernwerk.de/anzing) |
| Arzberg | `09479112` | `arzberg` | [arzberg](https://energiemonitor.bayernwerk.de/arzberg) |
| Ascha | `09278116` | `ascha` | [ascha](https://energiemonitor.bayernwerk.de/ascha) |
| Auerbach | `09371113` | `auerbach` | [auerbach](https://energiemonitor.bayernwerk.de/auerbach) |
| Aying | `09184137` | `aying` | [aying](https://energiemonitor.bayernwerk.de/aying) |
| Bad Feilnbach | `09187129` | `bad-feilnbach` | [bad-feilnbach](https://energiemonitor.bayernwerk.de/bad-feilnbach) |
| Bad Heilbrunn | `09173111` | `bad-heilbrunn` | [bad-heilbrunn](https://energiemonitor.bayernwerk.de/bad-heilbrunn) |
| Berching | `09373112` | `berching` | [berching](https://energiemonitor.bayernwerk.de/berching) |
| Berchtesgaden | `09172116` | `berchtesgaden` | [berchtesgaden](https://energiemonitor.bayernwerk.de/berchtesgaden) |
| Berchtesgadener Land | `09172` | `berchtesgadener-land` | [berchtesgadener-land](https://energiemonitor.bayernwerk.de/berchtesgadener-land) |
| Bergkirchen | `09174113` | `bergkirchen` | [bergkirchen](https://energiemonitor.bayernwerk.de/bergkirchen) |
| Bernau am Chiemsee | `09187118` | `bernau-am-chiemsee` | [bernau-am-chiemsee](https://energiemonitor.bayernwerk.de/bernau-am-chiemsee) |
| Bischofswiesen | `09172117` | `bischofswiesen` | [bischofswiesen](https://energiemonitor.bayernwerk.de/bischofswiesen) |
| Bodenwöhr | `09376116` | `bodenwoehr` | [bodenwoehr](https://energiemonitor.bayernwerk.de/bodenwoehr) |
| Bogen | `09278118` | `bogen` | [bogen](https://energiemonitor.bayernwerk.de/bogen) |
| Bruckberg | `09274194` | `bruckberg` | [bruckberg](https://energiemonitor.bayernwerk.de/bruckberg) |
| Bruckmühl | `09187122` | `bruckmuehl` | [bruckmuehl](https://energiemonitor.bayernwerk.de/bruckmuehl) |
| Brunnthal | `09184114` | `brunnthal` | [brunnthal](https://energiemonitor.bayernwerk.de/brunnthal) |
| Burghausen | `09171112` | `burghausen` | [burghausen](https://energiemonitor.bayernwerk.de/burghausen) |
| Burglengenfeld | `09376119` | `burglengenfeld` | [burglengenfeld](https://energiemonitor.bayernwerk.de/burglengenfeld) |
| Bärnau | `09377112` | `baernau` | [baernau](https://energiemonitor.bayernwerk.de/baernau) |
| Creußen | `09472127` | `creussen` | [creussen](https://energiemonitor.bayernwerk.de/creussen) |
| Dietfurt a. d. Altmühl | `09373121` | `dietfurt` | [dietfurt](https://energiemonitor.bayernwerk.de/dietfurt) |
| Dittelbrunn | `09678123` | `dittelbrunn` | [dittelbrunn](https://energiemonitor.bayernwerk.de/dittelbrunn) |
| Ebersberg | `09175115` | `ebersberg` | [ebersberg](https://energiemonitor.bayernwerk.de/ebersberg) |
| Erbendorf | `09377116` | `erbendorf` | [erbendorf](https://energiemonitor.bayernwerk.de/erbendorf) |
| Feldkirchen-Westerham | `09187130` | `feldkirchen-westerham` | [feldkirchen-westerham](https://energiemonitor.bayernwerk.de/feldkirchen-westerham) |
| Forstinning | `09175118` | `forstinning` | [forstinning](https://energiemonitor.bayernwerk.de/forstinning) |
| Fraunberg | `09177120` | `fraunberg` | [fraunberg](https://energiemonitor.bayernwerk.de/fraunberg) |
| Freilassing | `09172118` | `freilassing` | [freilassing](https://energiemonitor.bayernwerk.de/freilassing) |
| Freystadt | `09373126` | `freystadt` | [freystadt](https://energiemonitor.bayernwerk.de/freystadt) |
| Freyung | `09272118` | `freyung` | [freyung](https://energiemonitor.bayernwerk.de/freyung) |
| Furth | `09274132` | `furth` | [furth](https://energiemonitor.bayernwerk.de/furth) |
| Fürstenzell | `09275122` | `fuerstenzell` | [fuerstenzell](https://energiemonitor.bayernwerk.de/fuerstenzell) |
| Gauting | `09188120` | `gauting` | [gauting](https://energiemonitor.bayernwerk.de/gauting) |
| Gemeinde Chieming | `09189114` | `gemeinde-chieming` | [gemeinde-chieming](https://energiemonitor.bayernwerk.de/gemeinde-chieming) |
| Gemeinde Guteneck | `09376133` | `gemeinde-guteneck` | [gemeinde-guteneck](https://energiemonitor.bayernwerk.de/gemeinde-guteneck) |
| Gemeinde Kalchreuth | `09572137` | `kalchreuth` | [kalchreuth](https://energiemonitor.bayernwerk.de/kalchreuth) |
| Gemeinde Poing | `09175135` | `poing` | [poing](https://energiemonitor.bayernwerk.de/poing) |
| Gemeinde Ruderting | `09275144` | `gemeinde-ruderting` | [gemeinde-ruderting](https://energiemonitor.bayernwerk.de/gemeinde-ruderting) |
| Grafenau | `09272120` | `grafenau` | [grafenau](https://energiemonitor.bayernwerk.de/grafenau) |
| Grafenwöhr | `09374124` | `grafenwoehr` | [grafenwoehr](https://energiemonitor.bayernwerk.de/grafenwoehr) |
| Hallbergmoos | `09178130` | `hallbergmoos` | [hallbergmoos](https://energiemonitor.bayernwerk.de/hallbergmoos) |
| Hammelburg | `09672127` | `hammelburg` | [hammelburg](https://energiemonitor.bayernwerk.de/hammelburg) |
| Hebertshausen | `09174122` | `hebertshausen` | [hebertshausen](https://energiemonitor.bayernwerk.de/hebertshausen) |
| Hirschau | `09371127` | `hirschau` | [hirschau](https://energiemonitor.bayernwerk.de/hirschau) |
| Höchstadt an der Aisch | `09572135` | `hoechstadt` | [hoechstadt](https://energiemonitor.bayernwerk.de/hoechstadt) |
| Höhenkirchen-Siegertsbrunn | `09184127` | `hoehenkirchen-siegertsbrunn` | [hoehenkirchen-siegertsbrunn](https://energiemonitor.bayernwerk.de/hoehenkirchen-siegertsbrunn) |
| Iffeldorf | `09190132` | `iffeldorf` | [iffeldorf](https://energiemonitor.bayernwerk.de/iffeldorf) |
| ILE an Rott und Inn | `092751` | `ile-rott-inn` | [ile-rott-inn](https://energiemonitor.bayernwerk.de/ile-rott-inn) |
| Irschenberg | `09182123` | `irschenberg` | [irschenberg](https://energiemonitor.bayernwerk.de/irschenberg) |
| Kastl | `09377128` | `kastl` | [kastl](https://energiemonitor.bayernwerk.de/kastl) |
| Kemnath | `09377129` | `kemnath` | [kemnath](https://energiemonitor.bayernwerk.de/kemnath) |
| Kleinheubach | `09676132` | `kleinheubach` | [kleinheubach](https://energiemonitor.bayernwerk.de/kleinheubach) |
| Landkreis Amberg-Sulzbach | `09371` | `lk-amberg-sulzbach` | [lk-amberg-sulzbach](https://energiemonitor.bayernwerk.de/lk-amberg-sulzbach) |
| Landkreis Bamberg | `09471` | `bamberg-landkreis` | [bamberg-landkreis](https://energiemonitor.bayernwerk.de/bamberg-landkreis) |
| Landkreis Cham | `09372` | `cham-landkreis` | [cham-landkreis](https://energiemonitor.bayernwerk.de/cham-landkreis) |
| Landkreis Ebersberg | `09175` | `ebersberg-landkreis` | [ebersberg-landkreis](https://energiemonitor.bayernwerk.de/ebersberg-landkreis) |
| Landkreis Freyung-Grafenau | `09272` | `freyung-grafenau-landkreis` | [freyung-grafenau-landkreis](https://energiemonitor.bayernwerk.de/freyung-grafenau-landkreis) |
| Landkreis Miltenberg | `09676` | `miltenberg-landkreis` | [miltenberg-landkreis](https://energiemonitor.bayernwerk.de/miltenberg-landkreis) |
| Landkreis Mühldorf a. Inn | `09183` | `muehldorf-am-inn-landkreis` | [muehldorf-am-inn-landkreis](https://energiemonitor.bayernwerk.de/muehldorf-am-inn-landkreis) |
| Landkreis Passau | `09275` | `passau-landkreis` | [passau-landkreis](https://energiemonitor.bayernwerk.de/passau-landkreis) |
| Landkreis Pfaffenhofen | `09186` | `pfaffenhofen-landkreis` | [pfaffenhofen-landkreis](https://energiemonitor.bayernwerk.de/pfaffenhofen-landkreis) |
| Landkreis Regen | `09276` | `regen-landkreis` | [regen-landkreis](https://energiemonitor.bayernwerk.de/regen-landkreis) |
| Landkreis Regensburg | `09375` | `regensburg-landkreis` | [regensburg-landkreis](https://energiemonitor.bayernwerk.de/regensburg-landkreis) |
| Landkreis Rottal-Inn | `09277` | `landkreis-rottal-inn` | [landkreis-rottal-inn](https://energiemonitor.bayernwerk.de/landkreis-rottal-inn) |
| Landkreis Schwandorf | `09376` | `schwandorf-landkreis` | [schwandorf-landkreis](https://energiemonitor.bayernwerk.de/schwandorf-landkreis) |
| Landkreis Straubing-Bogen | `09278` | `straubing-bogen-landkreis` | [straubing-bogen-landkreis](https://energiemonitor.bayernwerk.de/straubing-bogen-landkreis) |
| Landkreis Tirschenreuth | `09377` | `tirschenreuth-landkreis` | [tirschenreuth-landkreis](https://energiemonitor.bayernwerk.de/tirschenreuth-landkreis) |
| Landkreis Traunstein | `09189` | `traunstein-landkreis` | [traunstein-landkreis](https://energiemonitor.bayernwerk.de/traunstein-landkreis) |
| Landkreis Würzburg | `09679` | `wuerzburg-landkreis` | [wuerzburg-landkreis](https://energiemonitor.bayernwerk.de/wuerzburg-landkreis) |
| Langquaid | `09273141` | `langquaid` | [langquaid](https://energiemonitor.bayernwerk.de/langquaid) |
| Laufen | `09172122` | `laufen` | [laufen](https://energiemonitor.bayernwerk.de/laufen) |
| Lichtenfels | `09478139` | `lichtenfels` | [lichtenfels](https://energiemonitor.bayernwerk.de/lichtenfels) |
| Loiching | `09279124` | `loiching` | [loiching](https://energiemonitor.bayernwerk.de/loiching) |
| Maisach | `09179134` | `maisach` | [maisach](https://energiemonitor.bayernwerk.de/maisach) |
| Mallersdorf-Pfaffenberg | `09278148` | `mallersdorf-pfaffenberg` | [mallersdorf-pfaffenberg](https://energiemonitor.bayernwerk.de/mallersdorf-pfaffenberg) |
| Markt Altdorf | `09274113` | `altdorf` | [altdorf](https://energiemonitor.bayernwerk.de/altdorf) |
| Markt Beratzhausen | `09375118` | `beratzhausen` | [beratzhausen](https://energiemonitor.bayernwerk.de/beratzhausen) |
| Markt Burgebrach | `09471120` | `markt-burgebrach` | [markt-burgebrach](https://energiemonitor.bayernwerk.de/markt-burgebrach) |
| Markt Eggolsheim | `09474123` | `markt-eggolsheim` | [markt-eggolsheim](https://energiemonitor.bayernwerk.de/markt-eggolsheim) |
| Markt Gars am Inn | `09183118` | `gars-am-inn` | [gars-am-inn](https://energiemonitor.bayernwerk.de/gars-am-inn) |
| Markt Großostheim | `09671122` | `grossostheim` | [grossostheim](https://energiemonitor.bayernwerk.de/grossostheim) |
| Markt Kleinwallstadt | `09676133` | `kleinwallstadt` | [kleinwallstadt](https://energiemonitor.bayernwerk.de/kleinwallstadt) |
| Markt Moosbach | `09374137` | `markt-moosbach` | [markt-moosbach](https://energiemonitor.bayernwerk.de/markt-moosbach) |
| Markt Parkstein | `09374144` | `parkstein` | [parkstein](https://energiemonitor.bayernwerk.de/parkstein) |
| Markt Schierling | `09375196` | `schierling` | [schierling](https://energiemonitor.bayernwerk.de/schierling) |
| Markt Triefenstein | `09677154` | `triefenstein` | [triefenstein](https://energiemonitor.bayernwerk.de/triefenstein) |
| Marktschellenberg | `09172124` | `marktschellenberg` | [marktschellenberg](https://energiemonitor.bayernwerk.de/marktschellenberg) |
| Maxhütte-Haidhof | `09376141` | `maxhuette-haidhof` | [maxhuette-haidhof](https://energiemonitor.bayernwerk.de/maxhuette-haidhof) |
| Musterstadt | `DEMO` | `demo` | [demo](https://energiemonitor.bayernwerk.de/demo) |
| Münnerstadt | `09672135` | `muennerstadt` | [muennerstadt](https://energiemonitor.bayernwerk.de/muennerstadt) |
| Nabburg | `09376144` | `nabburg` | [nabburg](https://energiemonitor.bayernwerk.de/nabburg) |
| Neuburg am Inn | `09275133` | `neuburg-am-inn` | [neuburg-am-inn](https://energiemonitor.bayernwerk.de/neuburg-am-inn) |
| Neufahrn/Eching | `09178100` | `neufahrn-eching` | [neufahrn-eching](https://energiemonitor.bayernwerk.de/neufahrn-eching) |
| Neuötting | `09171125` | `neuoetting` | [neuoetting](https://energiemonitor.bayernwerk.de/neuoetting) |
| Niederwinkling | `09278159` | `niederwinkling` | [niederwinkling](https://energiemonitor.bayernwerk.de/niederwinkling) |
| Oberhaching | `09184134` | `oberhaching` | [oberhaching](https://energiemonitor.bayernwerk.de/oberhaching) |
| Oberschleißheim | `09184135` | `oberschleissheim` | [oberschleissheim](https://energiemonitor.bayernwerk.de/oberschleissheim) |
| Oberviechtach | `09376151` | `oberviechtach` | [oberviechtach](https://energiemonitor.bayernwerk.de/oberviechtach) |
| Odelzhausen | `09174135` | `odelzhausen` | [odelzhausen](https://energiemonitor.bayernwerk.de/odelzhausen) |
| Otterfing | `09182127` | `otterfing` | [otterfing](https://energiemonitor.bayernwerk.de/otterfing) |
| Piding | `09172128` | `piding` | [piding](https://energiemonitor.bayernwerk.de/piding) |
| Pressath | `09374149` | `pressath` | [pressath](https://energiemonitor.bayernwerk.de/pressath) |
| Prien am Chiemsee | `09187162` | `prien` | [prien](https://energiemonitor.bayernwerk.de/prien) |
| Prutting | `09187163` | `prutting` | [prutting](https://energiemonitor.bayernwerk.de/prutting) |
| Putzbrunn | `09184140` | `putzbrunn` | [putzbrunn](https://energiemonitor.bayernwerk.de/putzbrunn) |
| Regenstauf | `09375190` | `regenstauf` | [regenstauf](https://energiemonitor.bayernwerk.de/regenstauf) |
| Riedenburg | `09273164` | `riedenburg` | [riedenburg](https://energiemonitor.bayernwerk.de/riedenburg) |
| Roding | `09372153` | `roding` | [roding](https://energiemonitor.bayernwerk.de/roding) |
| Ruhstorf an der Rott | `09275145` | `ruhstorf` | [ruhstorf](https://energiemonitor.bayernwerk.de/ruhstorf) |
| Salzweg | `09275146` | `salzweg` | [salzweg](https://energiemonitor.bayernwerk.de/salzweg) |
| Samerberg | `09187172` | `samerberg` | [samerberg](https://energiemonitor.bayernwerk.de/samerberg) |
| Sauerlach | `09184141` | `sauerlach` | [sauerlach](https://energiemonitor.bayernwerk.de/sauerlach) |
| Schrobenhausen | `09185158` | `schrobenhausen` | [schrobenhausen](https://energiemonitor.bayernwerk.de/schrobenhausen) |
| Schwandorf | `09376161` | `schwandorf` | [schwandorf](https://energiemonitor.bayernwerk.de/schwandorf) |
| Schwarzenfeld | `09376163` | `schwarzenfeld` | [schwarzenfeld](https://energiemonitor.bayernwerk.de/schwarzenfeld) |
| Schönau a. Königssee | `09172132` | `schoenau-koenigssee` | [schoenau-koenigssee](https://energiemonitor.bayernwerk.de/schoenau-koenigssee) |
| Sinzing | `09375199` | `sinzing` | [sinzing](https://energiemonitor.bayernwerk.de/sinzing) |
| Stadt Altötting | `09171111` | `altoetting` | [altoetting](https://energiemonitor.bayernwerk.de/altoetting) |
| Stadt Baunach | `09471115` | `baunach` | [baunach](https://energiemonitor.bayernwerk.de/baunach) |
| Stadt Haar | `09184123` | `haar` | [haar](https://energiemonitor.bayernwerk.de/haar) |
| Stadt Pegnitz | `09472175` | `pegnitz` | [pegnitz](https://energiemonitor.bayernwerk.de/pegnitz) |
| Stadt Traunreut | `09189154` | `traunreut` | [traunreut](https://energiemonitor.bayernwerk.de/traunreut) |
| Steinhöring | `09175137` | `steinhoering` | [steinhoering](https://energiemonitor.bayernwerk.de/steinhoering) |
| Teublitz | `09376170` | `teublitz` | [teublitz](https://energiemonitor.bayernwerk.de/teublitz) |
| Tiefenbach | `09274182` | `tiefenbach` | [tiefenbach](https://energiemonitor.bayernwerk.de/tiefenbach) |
| Tiefenbach (bei Passau) | `09275151` | `tiefenbach-passau` | [tiefenbach-passau](https://energiemonitor.bayernwerk.de/tiefenbach-passau) |
| Unterschleißheim | `09184149` | `unterschleissheim` | [unterschleissheim](https://energiemonitor.bayernwerk.de/unterschleissheim) |
| Valley | `09182133` | `valley` | [valley](https://energiemonitor.bayernwerk.de/valley) |
| Viechtach | `09276144` | `viechtach` | [viechtach](https://energiemonitor.bayernwerk.de/viechtach) |
| Vilseck | `09371156` | `vilseck` | [vilseck](https://energiemonitor.bayernwerk.de/vilseck) |
| Wackersdorf | `09376175` | `wackersdorf` | [wackersdorf](https://energiemonitor.bayernwerk.de/wackersdorf) |
| Wenzenbach | `09375208` | `wenzenbach` | [wenzenbach](https://energiemonitor.bayernwerk.de/wenzenbach) |
| Weyarn | `09182137` | `weyarn` | [weyarn](https://energiemonitor.bayernwerk.de/weyarn) |
| Ökomodell Achental | `09189999` | `oekomodell-achental` | [oekomodell-achental](https://energiemonitor.bayernwerk.de/oekomodell-achental) |
### EDIS — E.DIS Netz GmbH (`tenantId=1101`)

Dashboard-Basis: `https://energiemonitor.e-dis.de/<regionUrlKey>` — **2** Regionen.

| Gemeinde / Region | `region_code` | URL-Slug | Dashboard |
|---|---|---|---|
| Königs Wusterhausen | `12061260` | `koenigs-wusterhausen` | [koenigs-wusterhausen](https://energiemonitor.e-dis.de/koenigs-wusterhausen) |
| Nauen | `12063208` | `nauen` | [nauen](https://energiemonitor.e-dis.de/nauen) |
### LEW — Lechwerke AG (`tenantId=LEW`)

Dashboard-Basis: `https://energiemonitor.lew.de/<regionUrlKey>` — **8** Regionen.

| Gemeinde / Region | `region_code` | URL-Slug | Dashboard |
|---|---|---|---|
| Breitenbrunn | `09778121` | `breitenbrunn` | [breitenbrunn](https://energiemonitor.lew.de/breitenbrunn) |
| Gersthofen | `09772147` | `gersthofen` | [gersthofen](https://energiemonitor.lew.de/gersthofen) |
| Gundremmingen | `09774136` | `gundremmingen` | [gundremmingen](https://energiemonitor.lew.de/gundremmingen) |
| Landkreis Augsburg | `09772000` | `landkreis-augsburg` | [landkreis-augsburg](https://energiemonitor.lew.de/landkreis-augsburg) |
| LEW Energiemonitor Bayerisch-Schwaben | `LEWSCHWABEN` | `lew-schwaben` | [lew-schwaben](https://energiemonitor.lew.de/lew-schwaben) |
| Memmingen | `09764000` | `memmingen` | [memmingen](https://energiemonitor.lew.de/memmingen) |
| Scherstetten | `09772197` | `scherstetten` | [scherstetten](https://energiemonitor.lew.de/scherstetten) |
| Vöhringen | `09775162` | `voehringen` | [voehringen](https://energiemonitor.lew.de/voehringen) |
### SHNETZ — Schleswig-Holstein Netz GmbH (`tenantId=1556`)

Dashboard-Basis: `https://dev.sh-netz.energiemonitor.de/<regionUrlKey>` — **1004** Regionen.

| Gemeinde / Region | `region_code` | URL-Slug | Dashboard |
|---|---|---|---|
| Aasbüttel | `01061001` | `aasbuettel` | [aasbuettel](https://dev.sh-netz.energiemonitor.de/aasbuettel) |
| Achterwehr | `01058001` | `achterwehr` | [achterwehr](https://dev.sh-netz.energiemonitor.de/achterwehr) |
| Achtrup | `01054001` | `achtrup` | [achtrup](https://dev.sh-netz.energiemonitor.de/achtrup) |
| Aebtissinwisch | `01061002` | `aebtissinwisch` | [aebtissinwisch](https://dev.sh-netz.energiemonitor.de/aebtissinwisch) |
| Agethorst | `01061003` | `agethorst` | [agethorst](https://dev.sh-netz.energiemonitor.de/agethorst) |
| Ahlefeld-Bistensee | `01058175` | `ahlefeld-bistensee` | [ahlefeld-bistensee](https://dev.sh-netz.energiemonitor.de/ahlefeld-bistensee) |
| Ahneby | `01059102` | `ahneby` | [ahneby](https://dev.sh-netz.energiemonitor.de/ahneby) |
| Ahrensburg | `01062001` | `ahrensburg` | [ahrensburg](https://dev.sh-netz.energiemonitor.de/ahrensburg) |
| Ahrensbök | `01055001` | `ahrensboek` | [ahrensboek](https://dev.sh-netz.energiemonitor.de/ahrensboek) |
| Ahrenshöft | `01054002` | `ahrenshoeft` | [ahrenshoeft](https://dev.sh-netz.energiemonitor.de/ahrenshoeft) |
| Ahrenviöl | `01054003` | `ahrenvioel` | [ahrenvioel](https://dev.sh-netz.energiemonitor.de/ahrenvioel) |
| Ahrenviölfeld | `01054004` | `ahrenvioelfeld` | [ahrenvioelfeld](https://dev.sh-netz.energiemonitor.de/ahrenvioelfeld) |
| Albersdorf | `01051001` | `albersdorf` | [albersdorf](https://dev.sh-netz.energiemonitor.de/albersdorf) |
| Alkersum | `01054005` | `alkersum` | [alkersum](https://dev.sh-netz.energiemonitor.de/alkersum) |
| Almdorf | `01054006` | `almdorf` | [almdorf](https://dev.sh-netz.energiemonitor.de/almdorf) |
| Alt Bennebek | `01059001` | `alt-bennebek` | [alt-bennebek](https://dev.sh-netz.energiemonitor.de/alt-bennebek) |
| Alt Duvenstedt | `01058003` | `alt-duvenstedt` | [alt-duvenstedt](https://dev.sh-netz.energiemonitor.de/alt-duvenstedt) |
| Alt-Mölln | `01053002` | `alt-moelln` | [alt-moelln](https://dev.sh-netz.energiemonitor.de/alt-moelln) |
| Altenhof | `01058004` | `altenhof` | [altenhof](https://dev.sh-netz.energiemonitor.de/altenhof) |
| Altenholz | `01058005` | `altenholz` | [altenholz](https://dev.sh-netz.energiemonitor.de/altenholz) |
| Altenkrempe | `01055002` | `altenkrempe` | [altenkrempe](https://dev.sh-netz.energiemonitor.de/altenkrempe) |
| Altenmoor | `01061004` | `altenmoor` | [altenmoor](https://dev.sh-netz.energiemonitor.de/altenmoor) |
| Alveslohe | `01060002` | `alveslohe` | [alveslohe](https://dev.sh-netz.energiemonitor.de/alveslohe) |
| Ammersbek | `01062090` | `ammersbek` | [ammersbek](https://dev.sh-netz.energiemonitor.de/ammersbek) |
| Amt Achterwehr | `010585803` | `amt-achterwehr` | [amt-achterwehr](https://dev.sh-netz.energiemonitor.de/amt-achterwehr) |
| Amt Arensharde | `010595993` | `amt-arensharde` | [amt-arensharde](https://dev.sh-netz.energiemonitor.de/amt-arensharde) |
| Amt Auenland Südholstein | `010605043` | `amt-auenland-suedholstein` | [amt-auenland-suedholstein](https://dev.sh-netz.energiemonitor.de/amt-auenland-suedholstein) |
| Amt Bad Bramstedt-Land | `010605005` | `amt-bad-bramstedt-land` | [amt-bad-bramstedt-land](https://dev.sh-netz.energiemonitor.de/amt-bad-bramstedt-land) |
| Amt Bad Oldesloe-Land | `010625207` | `amt-bad-oldesloe-land` | [amt-bad-oldesloe-land](https://dev.sh-netz.energiemonitor.de/amt-bad-oldesloe-land) |
| Amt Bargteheide-Land | `010625218` | `amt-bargteheide-land` | [amt-bargteheide-land](https://dev.sh-netz.energiemonitor.de/amt-bargteheide-land) |
| Amt Bokhorst-Wankendorf | `010575785` | `amt-bokhorst-wankendorf` | [amt-bokhorst-wankendorf](https://dev.sh-netz.energiemonitor.de/amt-bokhorst-wankendorf) |
| Amt Boostedt-Rickling | `010605063` | `amt-boostedt-rickling` | [amt-boostedt-rickling](https://dev.sh-netz.energiemonitor.de/amt-boostedt-rickling) |
| Amt Bordesholm | `010585889` | `amt-bordesholm` | [amt-bordesholm](https://dev.sh-netz.energiemonitor.de/amt-bordesholm) |
| Amt Bornhöved | `010605024` | `amt-bornhoeved` | [amt-bornhoeved](https://dev.sh-netz.energiemonitor.de/amt-bornhoeved) |
| Amt Breitenburg | `010615104` | `amt-breitenburg` | [amt-breitenburg](https://dev.sh-netz.energiemonitor.de/amt-breitenburg) |
| Amt Breitenfelde | `010535313` | `amt-breitenfelde` | [amt-breitenfelde](https://dev.sh-netz.energiemonitor.de/amt-breitenfelde) |
| Amt Burg-St. Michaelisdonn | `010515163` | `amt-burg-st-michaelisdonn` | [amt-burg-st-michaelisdonn](https://dev.sh-netz.energiemonitor.de/amt-burg-st-michaelisdonn) |
| Amt Büchen | `010535318` | `amt-buechen` | [amt-buechen](https://dev.sh-netz.energiemonitor.de/amt-buechen) |
| Amt Büsum-Wesselburen | `010515178` | `amt-buesum-wesselburen` | [amt-buesum-wesselburen](https://dev.sh-netz.energiemonitor.de/amt-buesum-wesselburen) |
| Amt Dänischenhagen | `010585822` | `amt-daenischenhagen` | [amt-daenischenhagen](https://dev.sh-netz.energiemonitor.de/amt-daenischenhagen) |
| Amt Dänischer Wohld | `010585824` | `amt-daenischer-wohld` | [amt-daenischer-wohld](https://dev.sh-netz.energiemonitor.de/amt-daenischer-wohld) |
| Amt Eggebek | `010595912` | `amt-eggebek` | [amt-eggebek](https://dev.sh-netz.energiemonitor.de/amt-eggebek) |
| Amt Eider | `010515169` | `amt-eider` | [amt-eider](https://dev.sh-netz.energiemonitor.de/amt-eider) |
| Amt Eiderkanal | `010585888` | `amt-eiderkanal` | [amt-eiderkanal](https://dev.sh-netz.energiemonitor.de/amt-eiderkanal) |
| Amt Eiderstedt | `010545417` | `amt-eiderstedt` | [amt-eiderstedt](https://dev.sh-netz.energiemonitor.de/amt-eiderstedt) |
| Amt Eidertal | `010585896` | `amt-eidertal` | [amt-eidertal](https://dev.sh-netz.energiemonitor.de/amt-eidertal) |
| Amt Fockbek | `010585833` | `amt-fockbek` | [amt-fockbek](https://dev.sh-netz.energiemonitor.de/amt-fockbek) |
| Amt Föhr-Amrum | `010545488` | `amt-foehr-amrum` | [amt-foehr-amrum](https://dev.sh-netz.energiemonitor.de/amt-foehr-amrum) |
| Amt Geest und Marsch Südholstein | `010565690` | `amt-geest-und-marsch-suedholst` | [amt-geest-und-marsch-suedholst](https://dev.sh-netz.energiemonitor.de/amt-geest-und-marsch-suedholst) |
| Amt Geltinger Bucht | `010595990` | `amt-geltinger-bucht` | [amt-geltinger-bucht](https://dev.sh-netz.energiemonitor.de/amt-geltinger-bucht) |
| Amt Großer Plöner See | `010575739` | `amt-grosser-ploener-see` | [amt-grosser-ploener-see](https://dev.sh-netz.energiemonitor.de/amt-grosser-ploener-see) |
| Amt Haddeby | `010595915` | `amt-haddeby` | [amt-haddeby](https://dev.sh-netz.energiemonitor.de/amt-haddeby) |
| Amt Heider Umland | `010515172` | `amt-heider-umland` | [amt-heider-umland](https://dev.sh-netz.energiemonitor.de/amt-heider-umland) |
| Amt Hohe Elbgeest | `010535323` | `amt-hohe-elbgeest` | [amt-hohe-elbgeest](https://dev.sh-netz.energiemonitor.de/amt-hohe-elbgeest) |
| Amt Hohner Harde | `010585847` | `amt-hohner-harde` | [amt-hohner-harde](https://dev.sh-netz.energiemonitor.de/amt-hohner-harde) |
| Amt Horst-Herzhorn | `010615134` | `amt-horst-herzhorn` | [amt-horst-herzhorn](https://dev.sh-netz.energiemonitor.de/amt-horst-herzhorn) |
| Amt Hörnerkirchen | `010565636` | `amt-hoernerkirchen` | [amt-hoernerkirchen](https://dev.sh-netz.energiemonitor.de/amt-hoernerkirchen) |
| Amt Hürup | `010595919` | `amt-huerup` | [amt-huerup](https://dev.sh-netz.energiemonitor.de/amt-huerup) |
| Amt Hüttener Berge | `010585890` | `amt-huettener-berge` | [amt-huettener-berge](https://dev.sh-netz.energiemonitor.de/amt-huettener-berge) |
| Amt Itzehoe-Land | `010615138` | `amt-itzehoe-land` | [amt-itzehoe-land](https://dev.sh-netz.energiemonitor.de/amt-itzehoe-land) |
| Amt Itzstedt | `010605034` | `amt-itzstedt` | [amt-itzstedt](https://dev.sh-netz.energiemonitor.de/amt-itzstedt) |
| Amt Jevenstedt | `010585853` | `amt-jevenstedt` | [amt-jevenstedt](https://dev.sh-netz.energiemonitor.de/amt-jevenstedt) |
| Amt Kappeln-Land | `010595920` | `amt-kappeln-land` | [amt-kappeln-land](https://dev.sh-netz.energiemonitor.de/amt-kappeln-land) |
| Amt Kellinghusen | `010615189` | `amt-kellinghusen` | [amt-kellinghusen](https://dev.sh-netz.energiemonitor.de/amt-kellinghusen) |
| Amt Kisdorf | `010605048` | `amt-kisdorf` | [amt-kisdorf](https://dev.sh-netz.energiemonitor.de/amt-kisdorf) |
| Amt Krempermarsch | `010615153` | `amt-krempermarsch` | [amt-krempermarsch](https://dev.sh-netz.energiemonitor.de/amt-krempermarsch) |
| Amt Kropp-Stapelholm | `010595996` | `amt-kropp-stapelholm` | [amt-kropp-stapelholm](https://dev.sh-netz.energiemonitor.de/amt-kropp-stapelholm) |
| Amt Langballig | `010595937` | `amt-langballig` | [amt-langballig](https://dev.sh-netz.energiemonitor.de/amt-langballig) |
| Amt Leezen | `010605053` | `amt-leezen` | [amt-leezen](https://dev.sh-netz.energiemonitor.de/amt-leezen) |
| Amt Lensahn | `010555546` | `amt-lensahn` | [amt-lensahn](https://dev.sh-netz.energiemonitor.de/amt-lensahn) |
| Amt Lütjenburg | `010575727` | `amt-luetjenburg` | [amt-luetjenburg](https://dev.sh-netz.energiemonitor.de/amt-luetjenburg) |
| Amt Marne-Nordsee | `010515166` | `amt-marne-nordsee` | [amt-marne-nordsee](https://dev.sh-netz.energiemonitor.de/amt-marne-nordsee) |
| Amt Mittelangeln | `010595949` | `amt-mittelangeln` | [amt-mittelangeln](https://dev.sh-netz.energiemonitor.de/amt-mittelangeln) |
| Amt Mitteldithmarschen | `010515175` | `amt-mitteldithmarschen` | [amt-mitteldithmarschen](https://dev.sh-netz.energiemonitor.de/amt-mitteldithmarschen) |
| Amt Mittelholstein | `010585895` | `amt-mittelholstein` | [amt-mittelholstein](https://dev.sh-netz.energiemonitor.de/amt-mittelholstein) |
| Amt Mittleres Nordfriesland | `010545494` | `amt-mittleres-nordfriesland` | [amt-mittleres-nordfriesland](https://dev.sh-netz.energiemonitor.de/amt-mittleres-nordfriesland) |
| Amt Nordsee-Treene | `010545492` | `amt-nordsee-treene` | [amt-nordsee-treene](https://dev.sh-netz.energiemonitor.de/amt-nordsee-treene) |
| Amt Nortorfer Land | `010585864` | `amt-nortorfer-land` | [amt-nortorfer-land](https://dev.sh-netz.energiemonitor.de/amt-nortorfer-land) |
| Amt Oeversee | `010595940` | `amt-oeversee` | [amt-oeversee](https://dev.sh-netz.energiemonitor.de/amt-oeversee) |
| Amt Oldenburg-Land | `010555543` | `amt-oldenburg-land` | [amt-oldenburg-land](https://dev.sh-netz.energiemonitor.de/amt-oldenburg-land) |
| Amt Ostholstein-Mitte | `010555591` | `amt-ostholstein-mitte` | [amt-ostholstein-mitte](https://dev.sh-netz.energiemonitor.de/amt-ostholstein-mitte) |
| Amt Pellworm | `010545459` | `amt-pellworm` | [amt-pellworm](https://dev.sh-netz.energiemonitor.de/amt-pellworm) |
| Amt Pinnau | `010565687` | `amt-pinnau` | [amt-pinnau](https://dev.sh-netz.energiemonitor.de/amt-pinnau) |
| Amt Preetz-Land | `010575747` | `amt-preetz-land` | [amt-preetz-land](https://dev.sh-netz.energiemonitor.de/amt-preetz-land) |
| Amt Probstei | `010575755` | `amt-probstei` | [amt-probstei](https://dev.sh-netz.energiemonitor.de/amt-probstei) |
| Amt Rantzau | `010565660` | `amt-rantzau` | [amt-rantzau](https://dev.sh-netz.energiemonitor.de/amt-rantzau) |
| Amt Schafflund | `010595952` | `amt-schafflund` | [amt-schafflund](https://dev.sh-netz.energiemonitor.de/amt-schafflund) |
| Amt Schenefeld | `010615168` | `amt-schenefeld` | [amt-schenefeld](https://dev.sh-netz.energiemonitor.de/amt-schenefeld) |
| Amt Schlei-Ostsee | `010585893` | `amt-schlei-ostsee` | [amt-schlei-ostsee](https://dev.sh-netz.energiemonitor.de/amt-schlei-ostsee) |
| Amt Schrevenborn | `010575782` | `amt-schrevenborn` | [amt-schrevenborn](https://dev.sh-netz.energiemonitor.de/amt-schrevenborn) |
| Amt Schwarzenbek-Land | `010535373` | `amt-schwarzenbek-land` | [amt-schwarzenbek-land](https://dev.sh-netz.energiemonitor.de/amt-schwarzenbek-land) |
| Amt Selent/ Schlesen | `010575775` | `amt-selent/-schlesen` | [amt-selent/-schlesen](https://dev.sh-netz.energiemonitor.de/amt-selent/-schlesen) |
| Amt Siek | `010625262` | `amt-siek` | [amt-siek](https://dev.sh-netz.energiemonitor.de/amt-siek) |
| Amt Südangeln | `010595987` | `amt-suedangeln` | [amt-suedangeln](https://dev.sh-netz.energiemonitor.de/amt-suedangeln) |
| Amt Süderbrarup | `010595974` | `amt-suederbrarup` | [amt-suederbrarup](https://dev.sh-netz.energiemonitor.de/amt-suederbrarup) |
| Amt Südtondern | `010545489` | `amt-suedtondern` | [amt-suedtondern](https://dev.sh-netz.energiemonitor.de/amt-suedtondern) |
| Amt Trave-Land | `010605086` | `amt-trave-land` | [amt-trave-land](https://dev.sh-netz.energiemonitor.de/amt-trave-land) |
| Amt Trittau | `010625270` | `amt-trittau` | [amt-trittau](https://dev.sh-netz.energiemonitor.de/amt-trittau) |
| Amt Viöl | `010545453` | `amt-vioel` | [amt-vioel](https://dev.sh-netz.energiemonitor.de/amt-vioel) |
| Amt Wilstermarsch | `010615179` | `amt-wilstermarsch` | [amt-wilstermarsch](https://dev.sh-netz.energiemonitor.de/amt-wilstermarsch) |
| Appen | `01056001` | `appen` | [appen](https://dev.sh-netz.energiemonitor.de/appen) |
| Arkebek | `01051002` | `arkebek` | [arkebek](https://dev.sh-netz.energiemonitor.de/arkebek) |
| Arlewatt | `01054007` | `arlewatt` | [arlewatt](https://dev.sh-netz.energiemonitor.de/arlewatt) |
| Armstedt | `01060003` | `armstedt` | [armstedt](https://dev.sh-netz.energiemonitor.de/armstedt) |
| Arnis | `01059002` | `arnis` | [arnis](https://dev.sh-netz.energiemonitor.de/arnis) |
| Arpsdorf | `01058007` | `arpsdorf` | [arpsdorf](https://dev.sh-netz.energiemonitor.de/arpsdorf) |
| Ascheberg | `01057001` | `ascheberg` | [ascheberg](https://dev.sh-netz.energiemonitor.de/ascheberg) |
| Ascheffel | `01058008` | `ascheffel` | [ascheffel](https://dev.sh-netz.energiemonitor.de/ascheffel) |
| Aukrug | `01058009` | `aukrug` | [aukrug](https://dev.sh-netz.energiemonitor.de/aukrug) |
| Aumühle | `01053003` | `aumuehle` | [aumuehle](https://dev.sh-netz.energiemonitor.de/aumuehle) |
| Ausacker | `01059103` | `ausacker` | [ausacker](https://dev.sh-netz.energiemonitor.de/ausacker) |
| Auufer | `01061005` | `auufer` | [auufer](https://dev.sh-netz.energiemonitor.de/auufer) |
| Aventoft | `01054009` | `aventoft` | [aventoft](https://dev.sh-netz.energiemonitor.de/aventoft) |
| Averlak | `01051003` | `averlak` | [averlak](https://dev.sh-netz.energiemonitor.de/averlak) |
| Bad Bramstedt | `01060004` | `bad-bramstedt` | [bad-bramstedt](https://dev.sh-netz.energiemonitor.de/bad-bramstedt) |
| Bad Segeberg | `01060005` | `bad-segeberg` | [bad-segeberg](https://dev.sh-netz.energiemonitor.de/bad-segeberg) |
| Bahrenfleth | `01061006` | `bahrenfleth` | [bahrenfleth](https://dev.sh-netz.energiemonitor.de/bahrenfleth) |
| Bahrenhof | `01060006` | `bahrenhof` | [bahrenhof](https://dev.sh-netz.energiemonitor.de/bahrenhof) |
| Bargenstedt | `01051004` | `bargenstedt` | [bargenstedt](https://dev.sh-netz.energiemonitor.de/bargenstedt) |
| Bargfeld-Stegen | `01062005` | `bargfeld-stegen` | [bargfeld-stegen](https://dev.sh-netz.energiemonitor.de/bargfeld-stegen) |
| Bargstall | `01058010` | `bargstall` | [bargstall](https://dev.sh-netz.energiemonitor.de/bargstall) |
| Bargstedt | `01058011` | `bargstedt` | [bargstedt](https://dev.sh-netz.energiemonitor.de/bargstedt) |
| Bargteheide | `01062006` | `bargteheide` | [bargteheide](https://dev.sh-netz.energiemonitor.de/bargteheide) |
| Bargum | `01054010` | `bargum` | [bargum](https://dev.sh-netz.energiemonitor.de/bargum) |
| Bark | `01060007` | `bark` | [bark](https://dev.sh-netz.energiemonitor.de/bark) |
| Barkelsby | `01058012` | `barkelsby` | [barkelsby](https://dev.sh-netz.energiemonitor.de/barkelsby) |
| Barkenholm | `01051005` | `barkenholm` | [barkenholm](https://dev.sh-netz.energiemonitor.de/barkenholm) |
| Barlt | `01051006` | `barlt` | [barlt](https://dev.sh-netz.energiemonitor.de/barlt) |
| Barmissen | `01057002` | `barmissen` | [barmissen](https://dev.sh-netz.energiemonitor.de/barmissen) |
| Barsbek | `01057003` | `barsbek` | [barsbek](https://dev.sh-netz.energiemonitor.de/barsbek) |
| Basthorst | `01053007` | `basthorst` | [basthorst](https://dev.sh-netz.energiemonitor.de/basthorst) |
| Bebensee | `01060008` | `bebensee` | [bebensee](https://dev.sh-netz.energiemonitor.de/bebensee) |
| Behrendorf | `01054011` | `behrendorf` | [behrendorf](https://dev.sh-netz.energiemonitor.de/behrendorf) |
| Behrensdorf | `01057004` | `behrensdorf` | [behrensdorf](https://dev.sh-netz.energiemonitor.de/behrensdorf) |
| Beidenfleth | `01061007` | `beidenfleth` | [beidenfleth](https://dev.sh-netz.energiemonitor.de/beidenfleth) |
| Bekdorf | `01061008` | `bekdorf` | [bekdorf](https://dev.sh-netz.energiemonitor.de/bekdorf) |
| Belau | `01057005` | `belau` | [belau](https://dev.sh-netz.energiemonitor.de/belau) |
| Beldorf | `01058013` | `beldorf` | [beldorf](https://dev.sh-netz.energiemonitor.de/beldorf) |
| Bendfeld | `01057006` | `bendfeld` | [bendfeld](https://dev.sh-netz.energiemonitor.de/bendfeld) |
| Bendorf | `01058014` | `bendorf` | [bendorf](https://dev.sh-netz.energiemonitor.de/bendorf) |
| Bergenhusen | `01059005` | `bergenhusen` | [bergenhusen](https://dev.sh-netz.energiemonitor.de/bergenhusen) |
| Bergewöhrden | `01051008` | `bergewoehrden` | [bergewoehrden](https://dev.sh-netz.energiemonitor.de/bergewoehrden) |
| Beringstedt | `01058015` | `beringstedt` | [beringstedt](https://dev.sh-netz.energiemonitor.de/beringstedt) |
| Beschendorf | `01055006` | `beschendorf` | [beschendorf](https://dev.sh-netz.energiemonitor.de/beschendorf) |
| Besdorf | `01061011` | `besdorf` | [besdorf](https://dev.sh-netz.energiemonitor.de/besdorf) |
| Besenthal | `01053010` | `besenthal` | [besenthal](https://dev.sh-netz.energiemonitor.de/besenthal) |
| Bevern | `01056003` | `bevern` | [bevern](https://dev.sh-netz.energiemonitor.de/bevern) |
| Bilsen | `01056004` | `bilsen` | [bilsen](https://dev.sh-netz.energiemonitor.de/bilsen) |
| Bimöhlen | `01060009` | `bimoehlen` | [bimoehlen](https://dev.sh-netz.energiemonitor.de/bimoehlen) |
| Bissee | `01058016` | `bissee` | [bissee](https://dev.sh-netz.energiemonitor.de/bissee) |
| Blekendorf | `01057007` | `blekendorf` | [blekendorf](https://dev.sh-netz.energiemonitor.de/blekendorf) |
| Blomesche Wildnis | `01061012` | `blomesche-wildnis` | [blomesche-wildnis](https://dev.sh-netz.energiemonitor.de/blomesche-wildnis) |
| Blunk | `01060010` | `blunk` | [blunk](https://dev.sh-netz.energiemonitor.de/blunk) |
| Bohmstedt | `01054012` | `bohmstedt` | [bohmstedt](https://dev.sh-netz.energiemonitor.de/bohmstedt) |
| Bokel (Kreis Pinneberg) | `01056006` | `bokel-pinneberg` | [bokel-pinneberg](https://dev.sh-netz.energiemonitor.de/bokel-pinneberg) |
| Bokel (Kreis Rendsburg-Eckernförde) | `01058021` | `bokel-rendsburg` | [bokel-rendsburg](https://dev.sh-netz.energiemonitor.de/bokel-rendsburg) |
| Bokelrehm | `01061013` | `bokelrehm` | [bokelrehm](https://dev.sh-netz.energiemonitor.de/bokelrehm) |
| Bokholt-Hanredder | `01056008` | `bokholt-hanredder` | [bokholt-hanredder](https://dev.sh-netz.energiemonitor.de/bokholt-hanredder) |
| Bokhorst | `01061014` | `bokhorst` | [bokhorst](https://dev.sh-netz.energiemonitor.de/bokhorst) |
| Bollingstedt | `01059010` | `bollingstedt` | [bollingstedt](https://dev.sh-netz.energiemonitor.de/bollingstedt) |
| Bondelum | `01054013` | `bondelum` | [bondelum](https://dev.sh-netz.energiemonitor.de/bondelum) |
| Boostedt | `01060011` | `boostedt` | [boostedt](https://dev.sh-netz.energiemonitor.de/boostedt) |
| Bordelum | `01054014` | `bordelum` | [bordelum](https://dev.sh-netz.energiemonitor.de/bordelum) |
| Bordesholm | `01058022` | `bordesholm` | [bordesholm](https://dev.sh-netz.energiemonitor.de/bordesholm) |
| Boren | `01059187` | `boren` | [boren](https://dev.sh-netz.energiemonitor.de/boren) |
| Borgdorf-Seedorf | `01058023` | `borgdorf-seedorf` | [borgdorf-seedorf](https://dev.sh-netz.energiemonitor.de/borgdorf-seedorf) |
| Borgstedt | `01058024` | `borgstedt` | [borgstedt](https://dev.sh-netz.energiemonitor.de/borgstedt) |
| Borgsum | `01054015` | `borgsum` | [borgsum](https://dev.sh-netz.energiemonitor.de/borgsum) |
| Borgwedel | `01059012` | `borgwedel` | [borgwedel](https://dev.sh-netz.energiemonitor.de/borgwedel) |
| Bornholt | `01058025` | `bornholt` | [bornholt](https://dev.sh-netz.energiemonitor.de/bornholt) |
| Bornhöved | `01060012` | `bornhoeved` | [bornhoeved](https://dev.sh-netz.energiemonitor.de/bornhoeved) |
| Borsfleth | `01061015` | `borsfleth` | [borsfleth](https://dev.sh-netz.energiemonitor.de/borsfleth) |
| Borstel | `01060013` | `borstel` | [borstel](https://dev.sh-netz.energiemonitor.de/borstel) |
| Borstorf | `01053013` | `borstorf` | [borstorf](https://dev.sh-netz.energiemonitor.de/borstorf) |
| Bosau | `01055007` | `bosau` | [bosau](https://dev.sh-netz.energiemonitor.de/bosau) |
| Bosbüll | `01054016` | `bosbuell` | [bosbuell](https://dev.sh-netz.energiemonitor.de/bosbuell) |
| Bothkamp | `01057011` | `bothkamp` | [bothkamp](https://dev.sh-netz.energiemonitor.de/bothkamp) |
| Bovenau | `01058026` | `bovenau` | [bovenau](https://dev.sh-netz.energiemonitor.de/bovenau) |
| Braak | `01062011` | `braak` | [braak](https://dev.sh-netz.energiemonitor.de/braak) |
| Braderup | `01054017` | `braderup` | [braderup](https://dev.sh-netz.energiemonitor.de/braderup) |
| Brammer | `01058027` | `brammer` | [brammer](https://dev.sh-netz.energiemonitor.de/brammer) |
| Bramstedtlund | `01054018` | `bramstedtlund` | [bramstedtlund](https://dev.sh-netz.energiemonitor.de/bramstedtlund) |
| Brande-Hörnerkirchen | `01056010` | `brande-hoernerkirchen` | [brande-hoernerkirchen](https://dev.sh-netz.energiemonitor.de/brande-hoernerkirchen) |
| Bredenbek | `01058028` | `bredenbek` | [bredenbek](https://dev.sh-netz.energiemonitor.de/bredenbek) |
| Bredstedt | `01054019` | `bredstedt` | [bredstedt](https://dev.sh-netz.energiemonitor.de/bredstedt) |
| Breiholz | `01058029` | `breiholz` | [breiholz](https://dev.sh-netz.energiemonitor.de/breiholz) |
| Breitenberg | `01061016` | `breitenberg` | [breitenberg](https://dev.sh-netz.energiemonitor.de/breitenberg) |
| Breitenfelde | `01053014` | `breitenfelde` | [breitenfelde](https://dev.sh-netz.energiemonitor.de/breitenfelde) |
| Brekendorf | `01058030` | `brekendorf` | [brekendorf](https://dev.sh-netz.energiemonitor.de/brekendorf) |
| Breklum | `01054020` | `breklum` | [breklum](https://dev.sh-netz.energiemonitor.de/breklum) |
| Brickeln | `01051010` | `brickeln` | [brickeln](https://dev.sh-netz.energiemonitor.de/brickeln) |
| Brinjahe | `01058031` | `brinjahe` | [brinjahe](https://dev.sh-netz.energiemonitor.de/brinjahe) |
| Brodersby | `01058032` | `brodersby` | [brodersby](https://dev.sh-netz.energiemonitor.de/brodersby) |
| Brodersby-Goltoft | `01059189` | `brodersby-goltoft` | [brodersby-goltoft](https://dev.sh-netz.energiemonitor.de/brodersby-goltoft) |
| Brodersdorf | `01057012` | `brodersdorf` | [brodersdorf](https://dev.sh-netz.energiemonitor.de/brodersdorf) |
| Brokdorf | `01061018` | `brokdorf` | [brokdorf](https://dev.sh-netz.energiemonitor.de/brokdorf) |
| Brokstedt | `01061019` | `brokstedt` | [brokstedt](https://dev.sh-netz.energiemonitor.de/brokstedt) |
| Brunsbek | `01062088` | `brunsbek` | [brunsbek](https://dev.sh-netz.energiemonitor.de/brunsbek) |
| Brunstorf | `01053017` | `brunstorf` | [brunstorf](https://dev.sh-netz.energiemonitor.de/brunstorf) |
| Bröthen | `01053015` | `broethen` | [broethen](https://dev.sh-netz.energiemonitor.de/broethen) |
| Brügge | `01058033` | `bruegge` | [bruegge](https://dev.sh-netz.energiemonitor.de/bruegge) |
| Buchholz Burg-St. Michaelidonn | `01051012` | `buchholz-burg-st-michaelidonn` | [buchholz-burg-st-michaelidonn](https://dev.sh-netz.energiemonitor.de/buchholz-burg-st-michaelidonn) |
| Bullenkuhlen | `01056011` | `bullenkuhlen` | [bullenkuhlen](https://dev.sh-netz.energiemonitor.de/bullenkuhlen) |
| Bunsoh | `01051015` | `bunsoh` | [bunsoh](https://dev.sh-netz.energiemonitor.de/bunsoh) |
| Burg | `01051016` | `burg` | [burg](https://dev.sh-netz.energiemonitor.de/burg) |
| Busdorf | `01059018` | `busdorf` | [busdorf](https://dev.sh-netz.energiemonitor.de/busdorf) |
| Busenwurth | `01051017` | `busenwurth` | [busenwurth](https://dev.sh-netz.energiemonitor.de/busenwurth) |
| Bälau | `01053005` | `baelau` | [baelau](https://dev.sh-netz.energiemonitor.de/baelau) |
| Böel | `01059006` | `boeel` | [boeel](https://dev.sh-netz.energiemonitor.de/boeel) |
| Böhnhusen | `01058019` | `boehnhusen` | [boehnhusen](https://dev.sh-netz.energiemonitor.de/boehnhusen) |
| Böklund | `01059008` | `boeklund` | [boeklund](https://dev.sh-netz.energiemonitor.de/boeklund) |
| Bönebüttel | `01057008` | `boenebuettel` | [boenebuettel](https://dev.sh-netz.energiemonitor.de/boenebuettel) |
| Börm | `01059009` | `boerm` | [boerm](https://dev.sh-netz.energiemonitor.de/boerm) |
| Börnsen | `01053012` | `boernsen` | [boernsen](https://dev.sh-netz.energiemonitor.de/boernsen) |
| Bösdorf | `01057009` | `boesdorf` | [boesdorf](https://dev.sh-netz.energiemonitor.de/boesdorf) |
| Böxlund | `01059105` | `boexlund` | [boexlund](https://dev.sh-netz.energiemonitor.de/boexlund) |
| Büchen | `01053020` | `buechen` | [buechen](https://dev.sh-netz.energiemonitor.de/buechen) |
| Bühnsdorf | `01060015` | `buehnsdorf` | [buehnsdorf](https://dev.sh-netz.energiemonitor.de/buehnsdorf) |
| Bünsdorf | `01058035` | `buensdorf` | [buensdorf](https://dev.sh-netz.energiemonitor.de/buensdorf) |
| Büsum | `01051013` | `buesum` | [buesum](https://dev.sh-netz.energiemonitor.de/buesum) |
| Büsumer Deichhausen | `01051014` | `buesumer-deichhausen` | [buesumer-deichhausen](https://dev.sh-netz.energiemonitor.de/buesumer-deichhausen) |
| Büttel | `01061020` | `buettel` | [buettel](https://dev.sh-netz.energiemonitor.de/buettel) |
| Christiansholm | `01058036` | `christiansholm` | [christiansholm](https://dev.sh-netz.energiemonitor.de/christiansholm) |
| Christinenthal | `01061021` | `christinenthal` | [christinenthal](https://dev.sh-netz.energiemonitor.de/christinenthal) |
| Dagebüll | `01054022` | `dagebuell` | [dagebuell](https://dev.sh-netz.energiemonitor.de/dagebuell) |
| Dahme | `01055010` | `dahme` | [dahme](https://dev.sh-netz.energiemonitor.de/dahme) |
| Dahmker | `01053021` | `dahmker` | [dahmker](https://dev.sh-netz.energiemonitor.de/dahmker) |
| Daldorf | `01060016` | `daldorf` | [daldorf](https://dev.sh-netz.energiemonitor.de/daldorf) |
| Damendorf | `01058039` | `damendorf` | [damendorf](https://dev.sh-netz.energiemonitor.de/damendorf) |
| Damlos | `01055011` | `damlos` | [damlos](https://dev.sh-netz.energiemonitor.de/damlos) |
| Dammfleth | `01061023` | `dammfleth` | [dammfleth](https://dev.sh-netz.energiemonitor.de/dammfleth) |
| Damp | `01058040` | `damp` | [damp](https://dev.sh-netz.energiemonitor.de/damp) |
| Damsdorf | `01060017` | `damsdorf` | [damsdorf](https://dev.sh-netz.energiemonitor.de/damsdorf) |
| Dannau | `01057013` | `dannau` | [dannau](https://dev.sh-netz.energiemonitor.de/dannau) |
| Dannewerk | `01059019` | `dannewerk` | [dannewerk](https://dev.sh-netz.energiemonitor.de/dannewerk) |
| Dassendorf | `01053023` | `dassendorf` | [dassendorf](https://dev.sh-netz.energiemonitor.de/dassendorf) |
| Delingsdorf | `01062014` | `delingsdorf` | [delingsdorf](https://dev.sh-netz.energiemonitor.de/delingsdorf) |
| Dellstedt | `01051019` | `dellstedt` | [dellstedt](https://dev.sh-netz.energiemonitor.de/dellstedt) |
| Delve | `01051020` | `delve` | [delve](https://dev.sh-netz.energiemonitor.de/delve) |
| Dersau | `01057015` | `dersau` | [dersau](https://dev.sh-netz.energiemonitor.de/dersau) |
| Diekhusen-Fahrstedt | `01051021` | `diekhusen-fahrstedt` | [diekhusen-fahrstedt](https://dev.sh-netz.energiemonitor.de/diekhusen-fahrstedt) |
| Dingen | `01051022` | `dingen` | [dingen](https://dev.sh-netz.energiemonitor.de/dingen) |
| Dobersdorf | `01057016` | `dobersdorf` | [dobersdorf](https://dev.sh-netz.energiemonitor.de/dobersdorf) |
| Dollerup | `01059106` | `dollerup` | [dollerup](https://dev.sh-netz.energiemonitor.de/dollerup) |
| Drage (Nordfriesland) | `01054023` | `drage-nordfriesland` | [drage-nordfriesland](https://dev.sh-netz.energiemonitor.de/drage-nordfriesland) |
| Drage (Steinburg) | `01061024` | `drage-steinburg` | [drage-steinburg](https://dev.sh-netz.energiemonitor.de/drage-steinburg) |
| Dreggers | `01060018` | `dreggers` | [dreggers](https://dev.sh-netz.energiemonitor.de/dreggers) |
| Drelsdorf | `01054024` | `drelsdorf` | [drelsdorf](https://dev.sh-netz.energiemonitor.de/drelsdorf) |
| Dunsum | `01054025` | `dunsum` | [dunsum](https://dev.sh-netz.energiemonitor.de/dunsum) |
| Dägeling | `01061022` | `daegeling` | [daegeling](https://dev.sh-netz.energiemonitor.de/daegeling) |
| Dänischenhagen | `01058037` | `daenischenhagen` | [daenischenhagen](https://dev.sh-netz.energiemonitor.de/daenischenhagen) |
| Dätgen | `01058038` | `daetgen` | [daetgen](https://dev.sh-netz.energiemonitor.de/daetgen) |
| Dörnick | `01057017` | `doernick` | [doernick](https://dev.sh-netz.energiemonitor.de/doernick) |
| Dörphof | `01058042` | `doerphof` | [doerphof](https://dev.sh-netz.energiemonitor.de/doerphof) |
| Dörpling | `01051023` | `doerpling` | [doerpling](https://dev.sh-netz.energiemonitor.de/doerpling) |
| Dörpstedt | `01059020` | `doerpstedt` | [doerpstedt](https://dev.sh-netz.energiemonitor.de/doerpstedt) |
| Eckernförde | `01058043` | `eckernfoerde` | [eckernfoerde](https://dev.sh-netz.energiemonitor.de/eckernfoerde) |
| Ecklak | `01061025` | `ecklak` | [ecklak](https://dev.sh-netz.energiemonitor.de/ecklak) |
| Eddelak | `01051024` | `eddelak` | [eddelak](https://dev.sh-netz.energiemonitor.de/eddelak) |
| Eggebek | `01059107` | `eggebek` | [eggebek](https://dev.sh-netz.energiemonitor.de/eggebek) |
| Eggstedt | `01051026` | `eggstedt` | [eggstedt](https://dev.sh-netz.energiemonitor.de/eggstedt) |
| Ehndorf | `01058044` | `ehndorf` | [ehndorf](https://dev.sh-netz.energiemonitor.de/ehndorf) |
| Eisendorf | `01058045` | `eisendorf` | [eisendorf](https://dev.sh-netz.energiemonitor.de/eisendorf) |
| Elisabeth-Sophien-Koog | `01054026` | `elisabeth-sophien-koog` | [elisabeth-sophien-koog](https://dev.sh-netz.energiemonitor.de/elisabeth-sophien-koog) |
| Ellerbek | `01056013` | `ellerbek` | [ellerbek](https://dev.sh-netz.energiemonitor.de/ellerbek) |
| Ellerdorf | `01058046` | `ellerdorf` | [ellerdorf](https://dev.sh-netz.energiemonitor.de/ellerdorf) |
| Ellerhoop | `01056014` | `ellerhoop` | [ellerhoop](https://dev.sh-netz.energiemonitor.de/ellerhoop) |
| Ellhöft | `01054027` | `ellhoeft` | [ellhoeft](https://dev.sh-netz.energiemonitor.de/ellhoeft) |
| Ellingstedt | `01059023` | `ellingstedt` | [ellingstedt](https://dev.sh-netz.energiemonitor.de/ellingstedt) |
| Elmenhorst | `01053027` | `elmenhorst` | [elmenhorst](https://dev.sh-netz.energiemonitor.de/elmenhorst) |
| Elmenhorst | `01062016` | `elmenhorst` | [elmenhorst](https://dev.sh-netz.energiemonitor.de/elmenhorst) |
| Elpersbüttel | `01051027` | `elpersbuettel` | [elpersbuettel](https://dev.sh-netz.energiemonitor.de/elpersbuettel) |
| Elsdorf-Westermühlen | `01058047` | `elsdorf-westermuehlen` | [elsdorf-westermuehlen](https://dev.sh-netz.energiemonitor.de/elsdorf-westermuehlen) |
| Elskop | `01061026` | `elskop` | [elskop](https://dev.sh-netz.energiemonitor.de/elskop) |
| Embühren | `01058048` | `embuehren` | [embuehren](https://dev.sh-netz.energiemonitor.de/embuehren) |
| Emkendorf | `01058049` | `emkendorf` | [emkendorf](https://dev.sh-netz.energiemonitor.de/emkendorf) |
| Emmelsbüll-Horsbüll | `01054166` | `emmelsbuell-horsbuell` | [emmelsbuell-horsbuell](https://dev.sh-netz.energiemonitor.de/emmelsbuell-horsbuell) |
| Enge-Sande | `01054167` | `enge-sande` | [enge-sande](https://dev.sh-netz.energiemonitor.de/enge-sande) |
| Engelbrechtsche Wildnis | `01061027` | `engelbrechtsche-wildnis` | [engelbrechtsche-wildnis](https://dev.sh-netz.energiemonitor.de/engelbrechtsche-wildnis) |
| Epenwöhrden | `01051028` | `epenwoehrden` | [epenwoehrden](https://dev.sh-netz.energiemonitor.de/epenwoehrden) |
| Erfde | `01059024` | `erfde` | [erfde](https://dev.sh-netz.energiemonitor.de/erfde) |
| Escheburg | `01053028` | `escheburg` | [escheburg](https://dev.sh-netz.energiemonitor.de/escheburg) |
| Esgrus | `01059109` | `esgrus` | [esgrus](https://dev.sh-netz.energiemonitor.de/esgrus) |
| Fahrdorf | `01059026` | `fahrdorf` | [fahrdorf](https://dev.sh-netz.energiemonitor.de/fahrdorf) |
| Fahren | `01057018` | `fahren` | [fahren](https://dev.sh-netz.energiemonitor.de/fahren) |
| Fahrenkrug | `01060020` | `fahrenkrug` | [fahrenkrug](https://dev.sh-netz.energiemonitor.de/fahrenkrug) |
| Fargau-Pratjau | `01057090` | `fargau-pratjau` | [fargau-pratjau](https://dev.sh-netz.energiemonitor.de/fargau-pratjau) |
| Fedderingen | `01051030` | `fedderingen` | [fedderingen](https://dev.sh-netz.energiemonitor.de/fedderingen) |
| Fehmarn | `01055046` | `fehmarn` | [fehmarn](https://dev.sh-netz.energiemonitor.de/fehmarn) |
| Felde | `01058050` | `felde` | [felde](https://dev.sh-netz.energiemonitor.de/felde) |
| Felm | `01058051` | `felm` | [felm](https://dev.sh-netz.energiemonitor.de/felm) |
| Fiefbergen | `01057020` | `fiefbergen` | [fiefbergen](https://dev.sh-netz.energiemonitor.de/fiefbergen) |
| Fitzbek | `01061028` | `fitzbek` | [fitzbek](https://dev.sh-netz.energiemonitor.de/fitzbek) |
| Fitzen | `01053029` | `fitzen` | [fitzen](https://dev.sh-netz.energiemonitor.de/fitzen) |
| Fleckeby | `01058052` | `fleckeby` | [fleckeby](https://dev.sh-netz.energiemonitor.de/fleckeby) |
| Fockbek | `01058054` | `fockbek` | [fockbek](https://dev.sh-netz.energiemonitor.de/fockbek) |
| Fredesdorf | `01060022` | `fredesdorf` | [fredesdorf](https://dev.sh-netz.energiemonitor.de/fredesdorf) |
| Freienwill | `01059182` | `freienwill` | [freienwill](https://dev.sh-netz.energiemonitor.de/freienwill) |
| Fresendelf | `01054032` | `fresendelf` | [fresendelf](https://dev.sh-netz.energiemonitor.de/fresendelf) |
| Frestedt | `01051032` | `frestedt` | [frestedt](https://dev.sh-netz.energiemonitor.de/frestedt) |
| Friedrich-Wilhelm-Lübke-Koog | `01054034` | `friedrich-wilhelm-luebke-koog` | [friedrich-wilhelm-luebke-koog](https://dev.sh-netz.energiemonitor.de/friedrich-wilhelm-luebke-koog) |
| Friedrichsgabekoog | `01051033` | `friedrichsgabekoog` | [friedrichsgabekoog](https://dev.sh-netz.energiemonitor.de/friedrichsgabekoog) |
| Friedrichsgraben | `01058055` | `friedrichsgraben` | [friedrichsgraben](https://dev.sh-netz.energiemonitor.de/friedrichsgraben) |
| Friedrichsholm | `01058056` | `friedrichsholm` | [friedrichsholm](https://dev.sh-netz.energiemonitor.de/friedrichsholm) |
| Friedrichskoog | `01051034` | `friedrichskoog` | [friedrichskoog](https://dev.sh-netz.energiemonitor.de/friedrichskoog) |
| Friedrichstadt | `01054033` | `friedrichstadt` | [friedrichstadt](https://dev.sh-netz.energiemonitor.de/friedrichstadt) |
| Fuhlendorf | `01060023` | `fuhlendorf` | [fuhlendorf](https://dev.sh-netz.energiemonitor.de/fuhlendorf) |
| Fuhlenhagen | `01053031` | `fuhlenhagen` | [fuhlenhagen](https://dev.sh-netz.energiemonitor.de/fuhlenhagen) |
| Föhrden-Barl | `01060021` | `foehrden-barl` | [foehrden-barl](https://dev.sh-netz.energiemonitor.de/foehrden-barl) |
| Galmsbüll | `01054165` | `galmsbuell` | [galmsbuell](https://dev.sh-netz.energiemonitor.de/galmsbuell) |
| Gammelby | `01058057` | `gammelby` | [gammelby](https://dev.sh-netz.energiemonitor.de/gammelby) |
| Gaushorn | `01051035` | `gaushorn` | [gaushorn](https://dev.sh-netz.energiemonitor.de/gaushorn) |
| Gelting | `01059112` | `gelting` | [gelting](https://dev.sh-netz.energiemonitor.de/gelting) |
| Geltorf | `01059032` | `geltorf` | [geltorf](https://dev.sh-netz.energiemonitor.de/geltorf) |
| Geschendorf | `01060024` | `geschendorf` | [geschendorf](https://dev.sh-netz.energiemonitor.de/geschendorf) |
| Gettorf | `01058058` | `gettorf` | [gettorf](https://dev.sh-netz.energiemonitor.de/gettorf) |
| Giekau | `01057021` | `giekau` | [giekau](https://dev.sh-netz.energiemonitor.de/giekau) |
| Glasau | `01060025` | `glasau` | [glasau](https://dev.sh-netz.energiemonitor.de/glasau) |
| Glüsing | `01051036` | `gluesing` | [gluesing](https://dev.sh-netz.energiemonitor.de/gluesing) |
| Gnutz | `01058059` | `gnutz` | [gnutz](https://dev.sh-netz.energiemonitor.de/gnutz) |
| Gokels | `01058061` | `gokels` | [gokels](https://dev.sh-netz.energiemonitor.de/gokels) |
| Goldebek | `01054037` | `goldebek` | [goldebek](https://dev.sh-netz.energiemonitor.de/goldebek) |
| Goldelund | `01054038` | `goldelund` | [goldelund](https://dev.sh-netz.energiemonitor.de/goldelund) |
| Goosefeld | `01058102` | `goosefeld` | [goosefeld](https://dev.sh-netz.energiemonitor.de/goosefeld) |
| Grabau | `01053036` | `grabau` | [grabau](https://dev.sh-netz.energiemonitor.de/grabau) |
| Grabau | `01062019` | `grabau` | [grabau](https://dev.sh-netz.energiemonitor.de/grabau) |
| Grambek | `01053037` | `grambek` | [grambek](https://dev.sh-netz.energiemonitor.de/grambek) |
| Grande | `01062020` | `grande` | [grande](https://dev.sh-netz.energiemonitor.de/grande) |
| Grauel | `01058062` | `grauel` | [grauel](https://dev.sh-netz.energiemonitor.de/grauel) |
| Grebin | `01057022` | `grebin` | [grebin](https://dev.sh-netz.energiemonitor.de/grebin) |
| Gremersdorf | `01055015` | `gremersdorf` | [gremersdorf](https://dev.sh-netz.energiemonitor.de/gremersdorf) |
| Grevenkop | `01061030` | `grevenkop` | [grevenkop](https://dev.sh-netz.energiemonitor.de/grevenkop) |
| Gribbohm | `01061031` | `gribbohm` | [gribbohm](https://dev.sh-netz.energiemonitor.de/gribbohm) |
| Grothusenkoog | `01054040` | `grothusenkoog` | [grothusenkoog](https://dev.sh-netz.energiemonitor.de/grothusenkoog) |
| Grove | `01053045` | `grove` | [grove](https://dev.sh-netz.energiemonitor.de/grove) |
| Groven | `01051038` | `groven` | [groven](https://dev.sh-netz.energiemonitor.de/groven) |
| Groß Kummerfeld | `01060028` | `gross-kummerfeld` | [gross-kummerfeld](https://dev.sh-netz.energiemonitor.de/gross-kummerfeld) |
| Groß Niendorf | `01060029` | `gross-niendorf` | [gross-niendorf](https://dev.sh-netz.energiemonitor.de/gross-niendorf) |
| Groß Nordende | `01056016` | `gross-nordende` | [gross-nordende](https://dev.sh-netz.energiemonitor.de/gross-nordende) |
| Groß Offenseth-Aspern | `01056017` | `gross-offenseth-aspern` | [gross-offenseth-aspern](https://dev.sh-netz.energiemonitor.de/gross-offenseth-aspern) |
| Groß Pampau | `01053042` | `gross-pampau` | [gross-pampau](https://dev.sh-netz.energiemonitor.de/gross-pampau) |
| Groß Rheide | `01059035` | `gross-rheide` | [gross-rheide](https://dev.sh-netz.energiemonitor.de/gross-rheide) |
| Groß Rönnau | `01060030` | `gross-roennau` | [gross-roennau](https://dev.sh-netz.energiemonitor.de/gross-roennau) |
| Groß Vollstedt | `01058065` | `gross-vollstedt` | [gross-vollstedt](https://dev.sh-netz.energiemonitor.de/gross-vollstedt) |
| Groß Wittensee | `01058066` | `gross-wittensee` | [gross-wittensee](https://dev.sh-netz.energiemonitor.de/gross-wittensee) |
| Großbarkau | `01057023` | `grossbarkau` | [grossbarkau](https://dev.sh-netz.energiemonitor.de/grossbarkau) |
| Großenaspe | `01060027` | `grossenaspe` | [grossenaspe](https://dev.sh-netz.energiemonitor.de/grossenaspe) |
| Großenbrode | `01055017` | `grossenbrode` | [grossenbrode](https://dev.sh-netz.energiemonitor.de/grossenbrode) |
| Großenrade | `01051037` | `grossenrade` | [grossenrade](https://dev.sh-netz.energiemonitor.de/grossenrade) |
| Großensee | `01062022` | `grossensee` | [grossensee](https://dev.sh-netz.energiemonitor.de/grossensee) |
| Großenwiehe | `01059115` | `grossenwiehe` | [grossenwiehe](https://dev.sh-netz.energiemonitor.de/grossenwiehe) |
| Großhansdorf | `01062023` | `grosshansdorf` | [grosshansdorf](https://dev.sh-netz.energiemonitor.de/grosshansdorf) |
| Großharrie | `01057024` | `grossharrie` | [grossharrie](https://dev.sh-netz.energiemonitor.de/grossharrie) |
| Großsolt | `01059116` | `grosssolt` | [grosssolt](https://dev.sh-netz.energiemonitor.de/grosssolt) |
| Grube | `01055018` | `grube` | [grube](https://dev.sh-netz.energiemonitor.de/grube) |
| Grundhof | `01059118` | `grundhof` | [grundhof](https://dev.sh-netz.energiemonitor.de/grundhof) |
| Gröde | `01054039` | `groede` | [groede](https://dev.sh-netz.energiemonitor.de/groede) |
| Grödersby | `01059034` | `groedersby` | [groedersby](https://dev.sh-netz.energiemonitor.de/groedersby) |
| Grömitz | `01055016` | `groemitz` | [groemitz](https://dev.sh-netz.energiemonitor.de/groemitz) |
| Grönwohld | `01062021` | `groenwohld` | [groenwohld](https://dev.sh-netz.energiemonitor.de/groenwohld) |
| Gudendorf | `01051039` | `gudendorf` | [gudendorf](https://dev.sh-netz.energiemonitor.de/gudendorf) |
| Gudow | `01053046` | `gudow` | [gudow](https://dev.sh-netz.energiemonitor.de/gudow) |
| Göhl | `01055014` | `goehl` | [goehl](https://dev.sh-netz.energiemonitor.de/goehl) |
| Gönnebek | `01060026` | `goennebek` | [goennebek](https://dev.sh-netz.energiemonitor.de/goennebek) |
| Göttin | `01053035` | `goettin` | [goettin](https://dev.sh-netz.energiemonitor.de/goettin) |
| Güby | `01058067` | `gueby` | [gueby](https://dev.sh-netz.energiemonitor.de/gueby) |
| Gülzow | `01053047` | `guelzow` | [guelzow](https://dev.sh-netz.energiemonitor.de/guelzow) |
| Güster | `01053048` | `guester` | [guester](https://dev.sh-netz.energiemonitor.de/guester) |
| Haale | `01058068` | `haale` | [haale](https://dev.sh-netz.energiemonitor.de/haale) |
| Haby | `01058069` | `haby` | [haby](https://dev.sh-netz.energiemonitor.de/haby) |
| Hadenfeld | `01061033` | `hadenfeld` | [hadenfeld](https://dev.sh-netz.energiemonitor.de/hadenfeld) |
| Hagen | `01060031` | `hagen` | [hagen](https://dev.sh-netz.energiemonitor.de/hagen) |
| Hallig Hooge | `01054050` | `hallig-hooge` | [hallig-hooge](https://dev.sh-netz.energiemonitor.de/hallig-hooge) |
| Hamdorf | `01058070` | `hamdorf` | [hamdorf](https://dev.sh-netz.energiemonitor.de/hamdorf) |
| Hamfelde | `01062026` | `hamfelde` | [hamfelde](https://dev.sh-netz.energiemonitor.de/hamfelde) |
| Hamfelde | `01053049` | `hamfelde` | [hamfelde](https://dev.sh-netz.energiemonitor.de/hamfelde) |
| Hamwarde | `01053050` | `hamwarde` | [hamwarde](https://dev.sh-netz.energiemonitor.de/hamwarde) |
| Hamweddel | `01058071` | `hamweddel` | [hamweddel](https://dev.sh-netz.energiemonitor.de/hamweddel) |
| Handewitt | `01059183` | `handewitt` | [handewitt](https://dev.sh-netz.energiemonitor.de/handewitt) |
| Hanerau-Hademarschen | `01058072` | `hanerau-hademarschen` | [hanerau-hademarschen](https://dev.sh-netz.energiemonitor.de/hanerau-hademarschen) |
| Hardebek | `01060033` | `hardebek` | [hardebek](https://dev.sh-netz.energiemonitor.de/hardebek) |
| Harmsdorf | `01055020` | `harmsdorf` | [harmsdorf](https://dev.sh-netz.energiemonitor.de/harmsdorf) |
| Hartenholm | `01060034` | `hartenholm` | [hartenholm](https://dev.sh-netz.energiemonitor.de/hartenholm) |
| Haselund | `01054041` | `haselund` | [haselund](https://dev.sh-netz.energiemonitor.de/haselund) |
| Hasenkrug | `01060035` | `hasenkrug` | [hasenkrug](https://dev.sh-netz.energiemonitor.de/hasenkrug) |
| Hasenmoor | `01060036` | `hasenmoor` | [hasenmoor](https://dev.sh-netz.energiemonitor.de/hasenmoor) |
| Hasloh | `01056021` | `hasloh` | [hasloh](https://dev.sh-netz.energiemonitor.de/hasloh) |
| Hasselberg | `01059121` | `hasselberg` | [hasselberg](https://dev.sh-netz.energiemonitor.de/hasselberg) |
| Hattstedtermarsch | `01054043` | `hattstedtermarsch` | [hattstedtermarsch](https://dev.sh-netz.energiemonitor.de/hattstedtermarsch) |
| Havekost | `01053052` | `havekost` | [havekost](https://dev.sh-netz.energiemonitor.de/havekost) |
| Havetoft | `01059037` | `havetoft` | [havetoft](https://dev.sh-netz.energiemonitor.de/havetoft) |
| Haßmoor | `01058073` | `hassmoor` | [hassmoor](https://dev.sh-netz.energiemonitor.de/hassmoor) |
| Hedwigenkoog | `01051043` | `hedwigenkoog` | [hedwigenkoog](https://dev.sh-netz.energiemonitor.de/hedwigenkoog) |
| Heede | `01056022` | `heede` | [heede](https://dev.sh-netz.energiemonitor.de/heede) |
| Heidgraben | `01056023` | `heidgraben` | [heidgraben](https://dev.sh-netz.energiemonitor.de/heidgraben) |
| Heidmoor | `01060037` | `heidmoor` | [heidmoor](https://dev.sh-netz.energiemonitor.de/heidmoor) |
| Heidmühlen | `01060038` | `heidmuehlen` | [heidmuehlen](https://dev.sh-netz.energiemonitor.de/heidmuehlen) |
| Heiligenhafen | `01055021` | `heiligenhafen` | [heiligenhafen](https://dev.sh-netz.energiemonitor.de/heiligenhafen) |
| Heinkenborstel | `01058074` | `heinkenborstel` | [heinkenborstel](https://dev.sh-netz.energiemonitor.de/heinkenborstel) |
| Heist | `01056024` | `heist` | [heist](https://dev.sh-netz.energiemonitor.de/heist) |
| Helgoland | `01056025` | `helgoland` | [helgoland](https://dev.sh-netz.energiemonitor.de/helgoland) |
| Hellschen-Heringsand-Unterschaar | `01051045` | `hellschen-heringsand-unterscha` | [hellschen-heringsand-unterscha](https://dev.sh-netz.energiemonitor.de/hellschen-heringsand-unterscha) |
| Helmstorf | `01057026` | `helmstorf` | [helmstorf](https://dev.sh-netz.energiemonitor.de/helmstorf) |
| Helse | `01051046` | `helse` | [helse](https://dev.sh-netz.energiemonitor.de/helse) |
| Hemdingen | `01056026` | `hemdingen` | [hemdingen](https://dev.sh-netz.energiemonitor.de/hemdingen) |
| Hemme | `01051047` | `hemme` | [hemme](https://dev.sh-netz.energiemonitor.de/hemme) |
| Hemmingstedt | `01051048` | `hemmingstedt` | [hemmingstedt](https://dev.sh-netz.energiemonitor.de/hemmingstedt) |
| Hennstedt | `01051049` | `hennstedt` | [hennstedt](https://dev.sh-netz.energiemonitor.de/hennstedt) |
| Hennstedt | `01061036` | `hennstedt` | [hennstedt](https://dev.sh-netz.energiemonitor.de/hennstedt) |
| Henstedt-Ulzburg | `01060039` | `henstedt-ulzburg` | [henstedt-ulzburg](https://dev.sh-netz.energiemonitor.de/henstedt-ulzburg) |
| Heringsdorf | `01055022` | `heringsdorf` | [heringsdorf](https://dev.sh-netz.energiemonitor.de/heringsdorf) |
| Herzhorn | `01061037` | `herzhorn` | [herzhorn](https://dev.sh-netz.energiemonitor.de/herzhorn) |
| Hillgroven | `01051050` | `hillgroven` | [hillgroven](https://dev.sh-netz.energiemonitor.de/hillgroven) |
| Hingstheide | `01061038` | `hingstheide` | [hingstheide](https://dev.sh-netz.energiemonitor.de/hingstheide) |
| Hitzhusen | `01060040` | `hitzhusen` | [hitzhusen](https://dev.sh-netz.energiemonitor.de/hitzhusen) |
| Hochdonn | `01051051` | `hochdonn` | [hochdonn](https://dev.sh-netz.energiemonitor.de/hochdonn) |
| Hohenaspe | `01061040` | `hohenaspe` | [hohenaspe](https://dev.sh-netz.energiemonitor.de/hohenaspe) |
| Hohenfelde (Kreis Plön) | `01057029` | `hohenfelde-kreis-ploen` | [hohenfelde-kreis-ploen](https://dev.sh-netz.energiemonitor.de/hohenfelde-kreis-ploen) |
| Hohenfelde (Steinburg) | `01061041` | `hohenfelde-steinburg` | [hohenfelde-steinburg](https://dev.sh-netz.energiemonitor.de/hohenfelde-steinburg) |
| Hohenfelde (Stormarn) | `01062033` | `hohenfelde-stormarn` | [hohenfelde-stormarn](https://dev.sh-netz.energiemonitor.de/hohenfelde-stormarn) |
| Hohenhorn | `01053053` | `hohenhorn` | [hohenhorn](https://dev.sh-netz.energiemonitor.de/hohenhorn) |
| Hohenlockstedt | `01061042` | `hohenlockstedt` | [hohenlockstedt](https://dev.sh-netz.energiemonitor.de/hohenlockstedt) |
| Hohenwestedt | `01058077` | `hohenwestedt` | [hohenwestedt](https://dev.sh-netz.energiemonitor.de/hohenwestedt) |
| Hohn | `01058078` | `hohn` | [hohn](https://dev.sh-netz.energiemonitor.de/hohn) |
| Hohwacht | `01057030` | `hohwacht` | [hohwacht](https://dev.sh-netz.energiemonitor.de/hohwacht) |
| Hoisdorf | `01062035` | `hoisdorf` | [hoisdorf](https://dev.sh-netz.energiemonitor.de/hoisdorf) |
| Hollingstedt (Dithmarschen) | `01051053` | `hollingstedt-dithmarschen` | [hollingstedt-dithmarschen](https://dev.sh-netz.energiemonitor.de/hollingstedt-dithmarschen) |
| Hollingstedt (Treene) | `01059039` | `hollingstedt-treene` | [hollingstedt-treene](https://dev.sh-netz.energiemonitor.de/hollingstedt-treene) |
| Holm (Kreis Pinneberg) | `01056028` | `holm-kreis-pinneberg` | [holm-kreis-pinneberg](https://dev.sh-netz.energiemonitor.de/holm-kreis-pinneberg) |
| Holm (Nordfriesland) | `01054048` | `holm-nordfriesland` | [holm-nordfriesland](https://dev.sh-netz.energiemonitor.de/holm-nordfriesland) |
| Holstenniendorf | `01061043` | `holstenniendorf` | [holstenniendorf](https://dev.sh-netz.energiemonitor.de/holstenniendorf) |
| Holt | `01059124` | `holt` | [holt](https://dev.sh-netz.energiemonitor.de/holt) |
| Holtsee | `01058080` | `holtsee` | [holtsee](https://dev.sh-netz.energiemonitor.de/holtsee) |
| Holzbunge | `01058081` | `holzbunge` | [holzbunge](https://dev.sh-netz.energiemonitor.de/holzbunge) |
| Holzdorf | `01058082` | `holzdorf` | [holzdorf](https://dev.sh-netz.energiemonitor.de/holzdorf) |
| Honigsee | `01057031` | `honigsee` | [honigsee](https://dev.sh-netz.energiemonitor.de/honigsee) |
| Hornbek | `01053056` | `hornbek` | [hornbek](https://dev.sh-netz.energiemonitor.de/hornbek) |
| Horst | `01061044` | `horst` | [horst](https://dev.sh-netz.energiemonitor.de/horst) |
| Horstedt | `01054052` | `horstedt` | [horstedt](https://dev.sh-netz.energiemonitor.de/horstedt) |
| Hude | `01054054` | `hude` | [hude](https://dev.sh-netz.energiemonitor.de/hude) |
| Huje | `01061045` | `huje` | [huje](https://dev.sh-netz.energiemonitor.de/huje) |
| Hummelfeld | `01058084` | `hummelfeld` | [hummelfeld](https://dev.sh-netz.energiemonitor.de/hummelfeld) |
| Humptrup | `01054055` | `humptrup` | [humptrup](https://dev.sh-netz.energiemonitor.de/humptrup) |
| Husby | `01059127` | `husby` | [husby](https://dev.sh-netz.energiemonitor.de/husby) |
| Högel | `01054045` | `hoegel` | [hoegel](https://dev.sh-netz.energiemonitor.de/hoegel) |
| Högersdorf | `01060041` | `hoegersdorf` | [hoegersdorf](https://dev.sh-netz.energiemonitor.de/hoegersdorf) |
| Högsdorf | `01057027` | `hoegsdorf` | [hoegsdorf](https://dev.sh-netz.energiemonitor.de/hoegsdorf) |
| Höhndorf | `01057028` | `hoehndorf` | [hoehndorf](https://dev.sh-netz.energiemonitor.de/hoehndorf) |
| Hörsten | `01058075` | `hoersten` | [hoersten](https://dev.sh-netz.energiemonitor.de/hoersten) |
| Hörup | `01059123` | `hoerup` | [hoerup](https://dev.sh-netz.energiemonitor.de/hoerup) |
| Hövede | `01051052` | `hoevede` | [hoevede](https://dev.sh-netz.energiemonitor.de/hoevede) |
| Hürup | `01059126` | `huerup` | [huerup](https://dev.sh-netz.energiemonitor.de/huerup) |
| Hüsby | `01059041` | `huesby` | [huesby](https://dev.sh-netz.energiemonitor.de/huesby) |
| Hüttblek | `01060042` | `huettblek` | [huettblek](https://dev.sh-netz.energiemonitor.de/huettblek) |
| Hütten | `01058083` | `huetten` | [huetten](https://dev.sh-netz.energiemonitor.de/huetten) |
| Idstedt | `01059042` | `idstedt` | [idstedt](https://dev.sh-netz.energiemonitor.de/idstedt) |
| Immenstedt | `01054057` | `immenstedt` | [immenstedt](https://dev.sh-netz.energiemonitor.de/immenstedt) |
| Itzstedt | `01060043` | `itzstedt` | [itzstedt](https://dev.sh-netz.energiemonitor.de/itzstedt) |
| Jagel | `01059043` | `jagel` | [jagel](https://dev.sh-netz.energiemonitor.de/jagel) |
| Jahrsdorf | `01058085` | `jahrsdorf` | [jahrsdorf](https://dev.sh-netz.energiemonitor.de/jahrsdorf) |
| Janneby | `01059128` | `janneby` | [janneby](https://dev.sh-netz.energiemonitor.de/janneby) |
| Jardelund | `01059129` | `jardelund` | [jardelund](https://dev.sh-netz.energiemonitor.de/jardelund) |
| Jerrishoe | `01059131` | `jerrishoe` | [jerrishoe](https://dev.sh-netz.energiemonitor.de/jerrishoe) |
| Jersbek | `01062036` | `jersbek` | [jersbek](https://dev.sh-netz.energiemonitor.de/jersbek) |
| Jevenstedt | `01058086` | `jevenstedt` | [jevenstedt](https://dev.sh-netz.energiemonitor.de/jevenstedt) |
| Joldelund | `01054059` | `joldelund` | [joldelund](https://dev.sh-netz.energiemonitor.de/joldelund) |
| Jörl | `01059132` | `joerl` | [joerl](https://dev.sh-netz.energiemonitor.de/joerl) |
| Jübek | `01059044` | `juebek` | [juebek](https://dev.sh-netz.energiemonitor.de/juebek) |
| Kaaks | `01061047` | `kaaks` | [kaaks](https://dev.sh-netz.energiemonitor.de/kaaks) |
| Kabelhorst | `01055023` | `kabelhorst` | [kabelhorst](https://dev.sh-netz.energiemonitor.de/kabelhorst) |
| Kaisborstel | `01061048` | `kaisborstel` | [kaisborstel](https://dev.sh-netz.energiemonitor.de/kaisborstel) |
| Kaiser-Wilhelm-Koog | `01051057` | `kaiser-wilhelm-koog` | [kaiser-wilhelm-koog](https://dev.sh-netz.energiemonitor.de/kaiser-wilhelm-koog) |
| Kalübbe | `01057032` | `kaluebbe` | [kaluebbe](https://dev.sh-netz.energiemonitor.de/kaluebbe) |
| Kankelau | `01053059` | `kankelau` | [kankelau](https://dev.sh-netz.energiemonitor.de/kankelau) |
| Kappeln | `01059045` | `kappeln` | [kappeln](https://dev.sh-netz.energiemonitor.de/kappeln) |
| Karby | `01058087` | `karby` | [karby](https://dev.sh-netz.energiemonitor.de/karby) |
| Karlum | `01054062` | `karlum` | [karlum](https://dev.sh-netz.energiemonitor.de/karlum) |
| Karolinenkoog | `01051058` | `karolinenkoog` | [karolinenkoog](https://dev.sh-netz.energiemonitor.de/karolinenkoog) |
| Kasseburg | `01053060` | `kasseburg` | [kasseburg](https://dev.sh-netz.energiemonitor.de/kasseburg) |
| Kasseedorf | `01055024` | `kasseedorf` | [kasseedorf](https://dev.sh-netz.energiemonitor.de/kasseedorf) |
| Katharinenheerd | `01054063` | `katharinenheerd` | [katharinenheerd](https://dev.sh-netz.energiemonitor.de/katharinenheerd) |
| Kattendorf | `01060045` | `kattendorf` | [kattendorf](https://dev.sh-netz.energiemonitor.de/kattendorf) |
| Kayhude | `01060046` | `kayhude` | [kayhude](https://dev.sh-netz.energiemonitor.de/kayhude) |
| Kellenhusen | `01055025` | `kellenhusen` | [kellenhusen](https://dev.sh-netz.energiemonitor.de/kellenhusen) |
| Kellinghusen | `01061049` | `kellinghusen` | [kellinghusen](https://dev.sh-netz.energiemonitor.de/kellinghusen) |
| Kiebitzreihe | `01061050` | `kiebitzreihe` | [kiebitzreihe](https://dev.sh-netz.energiemonitor.de/kiebitzreihe) |
| Kirchbarkau | `01057033` | `kirchbarkau` | [kirchbarkau](https://dev.sh-netz.energiemonitor.de/kirchbarkau) |
| Kirchnüchel | `01057034` | `kirchnuechel` | [kirchnuechel](https://dev.sh-netz.energiemonitor.de/kirchnuechel) |
| Kirchspiel Garding | `01054035` | `kirchspiel-garding` | [kirchspiel-garding](https://dev.sh-netz.energiemonitor.de/kirchspiel-garding) |
| Kisdorf | `01060047` | `kisdorf` | [kisdorf](https://dev.sh-netz.energiemonitor.de/kisdorf) |
| Klamp | `01057035` | `klamp` | [klamp](https://dev.sh-netz.energiemonitor.de/klamp) |
| Klanxbüll | `01054065` | `klanxbuell` | [klanxbuell](https://dev.sh-netz.energiemonitor.de/klanxbuell) |
| Klappholz | `01059049` | `klappholz` | [klappholz](https://dev.sh-netz.energiemonitor.de/klappholz) |
| Klein Barkau | `01057037` | `klein-barkau` | [klein-barkau](https://dev.sh-netz.energiemonitor.de/klein-barkau) |
| Klein Bennebek | `01059050` | `klein-bennebek` | [klein-bennebek](https://dev.sh-netz.energiemonitor.de/klein-bennebek) |
| Klein Gladebrügge | `01060048` | `klein-gladebruegge` | [klein-gladebruegge](https://dev.sh-netz.energiemonitor.de/klein-gladebruegge) |
| Klein Pampau | `01053064` | `klein-pampau` | [klein-pampau](https://dev.sh-netz.energiemonitor.de/klein-pampau) |
| Klein Rheide | `01059051` | `klein-rheide` | [klein-rheide](https://dev.sh-netz.energiemonitor.de/klein-rheide) |
| Klein Rönnau | `01060049` | `klein-roennau` | [klein-roennau](https://dev.sh-netz.energiemonitor.de/klein-roennau) |
| Klein Wittensee | `01058088` | `klein-wittensee` | [klein-wittensee](https://dev.sh-netz.energiemonitor.de/klein-wittensee) |
| Kletkamp | `01057038` | `kletkamp` | [kletkamp](https://dev.sh-netz.energiemonitor.de/kletkamp) |
| Kleve | `01061052` | `kleve` | [kleve](https://dev.sh-netz.energiemonitor.de/kleve) |
| Kleve | `01051060` | `kleve-hennstedt` | [kleve-hennstedt](https://dev.sh-netz.energiemonitor.de/kleve-hennstedt) |
| Klixbüll | `01054068` | `klixbuell` | [klixbuell](https://dev.sh-netz.energiemonitor.de/klixbuell) |
| Koldenbüttel | `01054070` | `koldenbuettel` | [koldenbuettel](https://dev.sh-netz.energiemonitor.de/koldenbuettel) |
| Kolkerheide | `01054071` | `kolkerheide` | [kolkerheide](https://dev.sh-netz.energiemonitor.de/kolkerheide) |
| Kollmar | `01061118` | `kollmar` | [kollmar](https://dev.sh-netz.energiemonitor.de/kollmar) |
| Kollmoor | `01061053` | `kollmoor` | [kollmoor](https://dev.sh-netz.energiemonitor.de/kollmoor) |
| Kollow | `01053071` | `kollow` | [kollow](https://dev.sh-netz.energiemonitor.de/kollow) |
| Kosel | `01058090` | `kosel` | [kosel](https://dev.sh-netz.energiemonitor.de/kosel) |
| Kotzenbüll | `01054072` | `kotzenbuell` | [kotzenbuell](https://dev.sh-netz.energiemonitor.de/kotzenbuell) |
| Kreis Dithmarschen | `01051` | `kreis-dithmarschen` | [kreis-dithmarschen](https://dev.sh-netz.energiemonitor.de/kreis-dithmarschen) |
| Kreis Herzogtum-Lauenburg | `01053` | `kreis-herzogtum-lauenburg` | [kreis-herzogtum-lauenburg](https://dev.sh-netz.energiemonitor.de/kreis-herzogtum-lauenburg) |
| Kreis Nordfriesland | `01054` | `kreis-nordfriesland` | [kreis-nordfriesland](https://dev.sh-netz.energiemonitor.de/kreis-nordfriesland) |
| Kreis Ostholstein | `01055` | `kreis-ostholstein` | [kreis-ostholstein](https://dev.sh-netz.energiemonitor.de/kreis-ostholstein) |
| Kreis Pinneberg | `01056` | `kreis-pinneberg` | [kreis-pinneberg](https://dev.sh-netz.energiemonitor.de/kreis-pinneberg) |
| Kreis Plön | `01057` | `kreis-ploen` | [kreis-ploen](https://dev.sh-netz.energiemonitor.de/kreis-ploen) |
| Kreis Rendsburg-Eckernförde | `01058` | `kreis-rendsburg-eckernfoerde` | [kreis-rendsburg-eckernfoerde](https://dev.sh-netz.energiemonitor.de/kreis-rendsburg-eckernfoerde) |
| Kreis Schleswig-Flensburg | `01059` | `kreis-schleswig-flensburg` | [kreis-schleswig-flensburg](https://dev.sh-netz.energiemonitor.de/kreis-schleswig-flensburg) |
| Kreis Segeberg | `01060` | `kreis-segeberg` | [kreis-segeberg](https://dev.sh-netz.energiemonitor.de/kreis-segeberg) |
| Kreis Steinburg | `01061` | `kreis-steinburg` | [kreis-steinburg](https://dev.sh-netz.energiemonitor.de/kreis-steinburg) |
| Kreis Stormarn | `01062` | `kreis-stormarn` | [kreis-stormarn](https://dev.sh-netz.energiemonitor.de/kreis-stormarn) |
| Krempel | `01051061` | `krempel` | [krempel](https://dev.sh-netz.energiemonitor.de/krempel) |
| Krempermoor | `01061057` | `krempermoor` | [krempermoor](https://dev.sh-netz.energiemonitor.de/krempermoor) |
| Krems II | `01060050` | `krems-ii` | [krems-ii](https://dev.sh-netz.energiemonitor.de/krems-ii) |
| Krogaspe | `01058091` | `krogaspe` | [krogaspe](https://dev.sh-netz.energiemonitor.de/krogaspe) |
| Krokau | `01057040` | `krokau` | [krokau](https://dev.sh-netz.energiemonitor.de/krokau) |
| Kronprinzenkoog | `01051062` | `kronprinzenkoog` | [kronprinzenkoog](https://dev.sh-netz.energiemonitor.de/kronprinzenkoog) |
| Kronsgaard | `01059136` | `kronsgaard` | [kronsgaard](https://dev.sh-netz.energiemonitor.de/kronsgaard) |
| Kronsmoor | `01061058` | `kronsmoor` | [kronsmoor](https://dev.sh-netz.energiemonitor.de/kronsmoor) |
| Kropp | `01059053` | `kropp` | [kropp](https://dev.sh-netz.energiemonitor.de/kropp) |
| Krummbek | `01057041` | `krummbek` | [krummbek](https://dev.sh-netz.energiemonitor.de/krummbek) |
| Krummendiek | `01061059` | `krummendiek` | [krummendiek](https://dev.sh-netz.energiemonitor.de/krummendiek) |
| Krummwisch | `01058093` | `krummwisch` | [krummwisch](https://dev.sh-netz.energiemonitor.de/krummwisch) |
| Krumstedt | `01051063` | `krumstedt` | [krumstedt](https://dev.sh-netz.energiemonitor.de/krumstedt) |
| Kröppelshagen-Fahrendorf | `01053072` | `kroeppelshagen-fahrendorf` | [kroeppelshagen-fahrendorf](https://dev.sh-netz.energiemonitor.de/kroeppelshagen-fahrendorf) |
| Kuddewörde | `01053076` | `kuddewoerde` | [kuddewoerde](https://dev.sh-netz.energiemonitor.de/kuddewoerde) |
| Kuden | `01051064` | `kuden` | [kuden](https://dev.sh-netz.energiemonitor.de/kuden) |
| Kudensee | `01061060` | `kudensee` | [kudensee](https://dev.sh-netz.energiemonitor.de/kudensee) |
| Kummerfeld | `01056032` | `kummerfeld` | [kummerfeld](https://dev.sh-netz.energiemonitor.de/kummerfeld) |
| Köhn | `01057039` | `koehn` | [koehn](https://dev.sh-netz.energiemonitor.de/koehn) |
| Königshügel | `01058089` | `koenigshuegel` | [koenigshuegel](https://dev.sh-netz.energiemonitor.de/koenigshuegel) |
| Köthel | `01053070` | `koethel` | [koethel](https://dev.sh-netz.energiemonitor.de/koethel) |
| Köthel | `01062040` | `koethel` | [koethel](https://dev.sh-netz.energiemonitor.de/koethel) |
| Kühren | `01057042` | `kuehren` | [kuehren](https://dev.sh-netz.energiemonitor.de/kuehren) |
| Kükels | `01060051` | `kuekels` | [kuekels](https://dev.sh-netz.energiemonitor.de/kuekels) |
| Laboe | `01057043` | `laboe` | [laboe](https://dev.sh-netz.energiemonitor.de/laboe) |
| Ladelund | `01054073` | `ladelund` | [ladelund](https://dev.sh-netz.energiemonitor.de/ladelund) |
| Lammershagen | `01057044` | `lammershagen` | [lammershagen](https://dev.sh-netz.energiemonitor.de/lammershagen) |
| Landrecht | `01061062` | `landrecht` | [landrecht](https://dev.sh-netz.energiemonitor.de/landrecht) |
| Landscheide | `01061063` | `landscheide` | [landscheide](https://dev.sh-netz.energiemonitor.de/landscheide) |
| Langballig | `01059137` | `langballig` | [langballig](https://dev.sh-netz.energiemonitor.de/langballig) |
| Langeln | `01056034` | `langeln` | [langeln](https://dev.sh-netz.energiemonitor.de/langeln) |
| Langeneß | `01054074` | `langeness` | [langeness](https://dev.sh-netz.energiemonitor.de/langeness) |
| Langenhorn | `01054075` | `langenhorn` | [langenhorn](https://dev.sh-netz.energiemonitor.de/langenhorn) |
| Langenlehsten | `01053080` | `langenlehsten` | [langenlehsten](https://dev.sh-netz.energiemonitor.de/langenlehsten) |
| Langstedt | `01059138` | `langstedt` | [langstedt](https://dev.sh-netz.energiemonitor.de/langstedt) |
| Langwedel | `01058094` | `langwedel` | [langwedel](https://dev.sh-netz.energiemonitor.de/langwedel) |
| Latendorf | `01060052` | `latendorf` | [latendorf](https://dev.sh-netz.energiemonitor.de/latendorf) |
| Lebrade | `01057045` | `lebrade` | [lebrade](https://dev.sh-netz.energiemonitor.de/lebrade) |
| Leck | `01054076` | `leck` | [leck](https://dev.sh-netz.energiemonitor.de/leck) |
| Leezen | `01060053` | `leezen` | [leezen](https://dev.sh-netz.energiemonitor.de/leezen) |
| Lehe | `01051065` | `lehe` | [lehe](https://dev.sh-netz.energiemonitor.de/lehe) |
| Lehmkuhlen | `01057046` | `lehmkuhlen` | [lehmkuhlen](https://dev.sh-netz.energiemonitor.de/lehmkuhlen) |
| Lehmrade | `01053084` | `lehmrade` | [lehmrade](https://dev.sh-netz.energiemonitor.de/lehmrade) |
| Lensahn | `01055027` | `lensahn` | [lensahn](https://dev.sh-netz.energiemonitor.de/lensahn) |
| Lentföhrden | `01060054` | `lentfoehrden` | [lentfoehrden](https://dev.sh-netz.energiemonitor.de/lentfoehrden) |
| Lexgaard | `01054077` | `lexgaard` | [lexgaard](https://dev.sh-netz.energiemonitor.de/lexgaard) |
| Lieth | `01051067` | `lieth` | [lieth](https://dev.sh-netz.energiemonitor.de/lieth) |
| Lindau | `01058096` | `lindau` | [lindau](https://dev.sh-netz.energiemonitor.de/lindau) |
| Linden | `01051068` | `linden` | [linden](https://dev.sh-netz.energiemonitor.de/linden) |
| Lindewitt | `01059179` | `lindewitt` | [lindewitt](https://dev.sh-netz.energiemonitor.de/lindewitt) |
| Lockstedt | `01061064` | `lockstedt` | [lockstedt](https://dev.sh-netz.energiemonitor.de/lockstedt) |
| Lohbarbek | `01061065` | `lohbarbek` | [lohbarbek](https://dev.sh-netz.energiemonitor.de/lohbarbek) |
| Lohe-Föhrden | `01058097` | `lohe-foehrden` | [lohe-foehrden](https://dev.sh-netz.energiemonitor.de/lohe-foehrden) |
| Lohe-Rickelshof | `01051069` | `lohe-rickelshof` | [lohe-rickelshof](https://dev.sh-netz.energiemonitor.de/lohe-rickelshof) |
| Loit | `01059055` | `loit` | [loit](https://dev.sh-netz.energiemonitor.de/loit) |
| Looft | `01061066` | `looft` | [looft](https://dev.sh-netz.energiemonitor.de/looft) |
| Loop | `01058098` | `loop` | [loop](https://dev.sh-netz.energiemonitor.de/loop) |
| Loose | `01058099` | `loose` | [loose](https://dev.sh-netz.energiemonitor.de/loose) |
| Lottorf | `01059056` | `lottorf` | [lottorf](https://dev.sh-netz.energiemonitor.de/lottorf) |
| Luhnstedt | `01058101` | `luhnstedt` | [luhnstedt](https://dev.sh-netz.energiemonitor.de/luhnstedt) |
| Lunden | `01051071` | `lunden` | [lunden](https://dev.sh-netz.energiemonitor.de/lunden) |
| Lutterbek | `01057049` | `lutterbek` | [lutterbek](https://dev.sh-netz.energiemonitor.de/lutterbek) |
| Lutzhorn | `01056035` | `lutzhorn` | [lutzhorn](https://dev.sh-netz.energiemonitor.de/lutzhorn) |
| Lägerdorf | `01061061` | `laegerdorf` | [laegerdorf](https://dev.sh-netz.energiemonitor.de/laegerdorf) |
| Löptin | `01057047` | `loeptin` | [loeptin](https://dev.sh-netz.energiemonitor.de/loeptin) |
| Löwenstedt | `01054079` | `loewenstedt` | [loewenstedt](https://dev.sh-netz.energiemonitor.de/loewenstedt) |
| Lürschau | `01059057` | `luerschau` | [luerschau](https://dev.sh-netz.energiemonitor.de/luerschau) |
| Lütjenburg | `01057048` | `luetjenburg` | [luetjenburg](https://dev.sh-netz.energiemonitor.de/luetjenburg) |
| Lütjenholm | `01054080` | `luetjenholm` | [luetjenholm](https://dev.sh-netz.energiemonitor.de/luetjenholm) |
| Lütjensee | `01062045` | `luetjensee` | [luetjensee](https://dev.sh-netz.energiemonitor.de/luetjensee) |
| Lütjenwestedt | `01058100` | `luetjenwestedt` | [luetjenwestedt](https://dev.sh-netz.energiemonitor.de/luetjenwestedt) |
| Maasholm | `01059142` | `maasholm` | [maasholm](https://dev.sh-netz.energiemonitor.de/maasholm) |
| Malente | `01055028` | `malente` | [malente](https://dev.sh-netz.energiemonitor.de/malente) |
| Manhagen | `01055029` | `manhagen` | [manhagen](https://dev.sh-netz.energiemonitor.de/manhagen) |
| Marne | `01051072` | `marne` | [marne](https://dev.sh-netz.energiemonitor.de/marne) |
| Marnerdeich | `01051073` | `marnerdeich` | [marnerdeich](https://dev.sh-netz.energiemonitor.de/marnerdeich) |
| Martensrade | `01057050` | `martensrade` | [martensrade](https://dev.sh-netz.energiemonitor.de/martensrade) |
| Medelby | `01059143` | `medelby` | [medelby](https://dev.sh-netz.energiemonitor.de/medelby) |
| Meezen | `01058103` | `meezen` | [meezen](https://dev.sh-netz.energiemonitor.de/meezen) |
| Meggerdorf | `01059058` | `meggerdorf` | [meggerdorf](https://dev.sh-netz.energiemonitor.de/meggerdorf) |
| Mehlbek | `01061067` | `mehlbek` | [mehlbek](https://dev.sh-netz.energiemonitor.de/mehlbek) |
| Meldorf | `01051074` | `meldorf` | [meldorf](https://dev.sh-netz.energiemonitor.de/meldorf) |
| Meyn | `01059144` | `meyn` | [meyn](https://dev.sh-netz.energiemonitor.de/meyn) |
| Midlum | `01054083` | `midlum` | [midlum](https://dev.sh-netz.energiemonitor.de/midlum) |
| Mittelangeln | `01059185` | `mittelangeln` | [mittelangeln](https://dev.sh-netz.energiemonitor.de/mittelangeln) |
| Mohrkirch | `01059060` | `mohrkirch` | [mohrkirch](https://dev.sh-netz.energiemonitor.de/mohrkirch) |
| Moordiek | `01061068` | `moordiek` | [moordiek](https://dev.sh-netz.energiemonitor.de/moordiek) |
| Moorhusen | `01061070` | `moorhusen` | [moorhusen](https://dev.sh-netz.energiemonitor.de/moorhusen) |
| Moorrege | `01056036` | `moorrege` | [moorrege](https://dev.sh-netz.energiemonitor.de/moorrege) |
| Mucheln | `01057052` | `mucheln` | [mucheln](https://dev.sh-netz.energiemonitor.de/mucheln) |
| Munkbrarup | `01059145` | `munkbrarup` | [munkbrarup](https://dev.sh-netz.energiemonitor.de/munkbrarup) |
| Möhnsen | `01053089` | `moehnsen` | [moehnsen](https://dev.sh-netz.energiemonitor.de/moehnsen) |
| Mönkloh | `01060056` | `moenkloh` | [moenkloh](https://dev.sh-netz.energiemonitor.de/moenkloh) |
| Mörel | `01058106` | `moerel` | [moerel](https://dev.sh-netz.energiemonitor.de/moerel) |
| Mözen | `01060057` | `moezen` | [moezen](https://dev.sh-netz.energiemonitor.de/moezen) |
| Mühbrook | `01058108` | `muehbrook` | [muehbrook](https://dev.sh-netz.energiemonitor.de/muehbrook) |
| Mühlenbarbek | `01061071` | `muehlenbarbek` | [muehlenbarbek](https://dev.sh-netz.energiemonitor.de/muehlenbarbek) |
| Mühlenrade | `01053091` | `muehlenrade` | [muehlenrade](https://dev.sh-netz.energiemonitor.de/muehlenrade) |
| Münsterdorf | `01061072` | `muensterdorf` | [muensterdorf](https://dev.sh-netz.energiemonitor.de/muensterdorf) |
| Müssen | `01053092` | `muessen` | [muessen](https://dev.sh-netz.energiemonitor.de/muessen) |
| Nahe | `01060058` | `nahe` | [nahe](https://dev.sh-netz.energiemonitor.de/nahe) |
| Nebel | `01054085` | `nebel` | [nebel](https://dev.sh-netz.energiemonitor.de/nebel) |
| Negenharrie | `01058109` | `negenharrie` | [negenharrie](https://dev.sh-netz.energiemonitor.de/negenharrie) |
| Negernbötel | `01060059` | `negernboetel` | [negernboetel](https://dev.sh-netz.energiemonitor.de/negernboetel) |
| Nehms | `01060060` | `nehms` | [nehms](https://dev.sh-netz.energiemonitor.de/nehms) |
| Nehmten | `01057053` | `nehmten` | [nehmten](https://dev.sh-netz.energiemonitor.de/nehmten) |
| Neritz | `01062050` | `neritz` | [neritz](https://dev.sh-netz.energiemonitor.de/neritz) |
| Nettelsee | `01057054` | `nettelsee` | [nettelsee](https://dev.sh-netz.energiemonitor.de/nettelsee) |
| Neu Duvenstedt | `01058111` | `neu-duvenstedt` | [neu-duvenstedt](https://dev.sh-netz.energiemonitor.de/neu-duvenstedt) |
| Neuberend | `01059062` | `neuberend` | [neuberend](https://dev.sh-netz.energiemonitor.de/neuberend) |
| Neudorf-Bornstein | `01058110` | `neudorf-bornstein` | [neudorf-bornstein](https://dev.sh-netz.energiemonitor.de/neudorf-bornstein) |
| Neuenbrook | `01061073` | `neuenbrook` | [neuenbrook](https://dev.sh-netz.energiemonitor.de/neuenbrook) |
| Neuendeich | `01056037` | `neuendeich` | [neuendeich](https://dev.sh-netz.energiemonitor.de/neuendeich) |
| Neuendorf b. Elmshorn | `01061074` | `neuendorf-b-elmshorn` | [neuendorf-b-elmshorn](https://dev.sh-netz.energiemonitor.de/neuendorf-b-elmshorn) |
| Neuendorf-Sachsenbande | `01061119` | `neuendorf-sachsenbande` | [neuendorf-sachsenbande](https://dev.sh-netz.energiemonitor.de/neuendorf-sachsenbande) |
| Neuengörs | `01060061` | `neuengoers` | [neuengoers](https://dev.sh-netz.energiemonitor.de/neuengoers) |
| Neuenkirchen | `01051075` | `neuenkirchen` | [neuenkirchen](https://dev.sh-netz.energiemonitor.de/neuenkirchen) |
| Neufeld | `01051076` | `neufeld` | [neufeld](https://dev.sh-netz.energiemonitor.de/neufeld) |
| Neufelderkoog | `01051077` | `neufelderkoog` | [neufelderkoog](https://dev.sh-netz.energiemonitor.de/neufelderkoog) |
| Neukirchen | `01054086` | `neukirchen` | [neukirchen](https://dev.sh-netz.energiemonitor.de/neukirchen) |
| Neukirchen | `01055031` | `neukirchen` | [neukirchen](https://dev.sh-netz.energiemonitor.de/neukirchen) |
| Neumünster | `01004000` | `neumuenster` | [neumuenster](https://dev.sh-netz.energiemonitor.de/neumuenster) |
| Neuwittenbek | `01058112` | `neuwittenbek` | [neuwittenbek](https://dev.sh-netz.energiemonitor.de/neuwittenbek) |
| Neversdorf | `01060062` | `neversdorf` | [neversdorf](https://dev.sh-netz.energiemonitor.de/neversdorf) |
| Nieblum | `01054087` | `nieblum` | [nieblum](https://dev.sh-netz.energiemonitor.de/nieblum) |
| Nieby | `01059147` | `nieby` | [nieby](https://dev.sh-netz.energiemonitor.de/nieby) |
| Niebüll | `01054088` | `niebuell` | [niebuell](https://dev.sh-netz.energiemonitor.de/niebuell) |
| Nienborstel | `01058113` | `nienborstel` | [nienborstel](https://dev.sh-netz.energiemonitor.de/nienborstel) |
| Nienbüttel | `01061076` | `nienbuettel` | [nienbuettel](https://dev.sh-netz.energiemonitor.de/nienbuettel) |
| Niendorf/ Stecknitz | `01053095` | `niendorf/-stecknitz` | [niendorf/-stecknitz](https://dev.sh-netz.energiemonitor.de/niendorf/-stecknitz) |
| Nienwohld | `01062051` | `nienwohld` | [nienwohld](https://dev.sh-netz.energiemonitor.de/nienwohld) |
| Niesgrau | `01059148` | `niesgrau` | [niesgrau](https://dev.sh-netz.energiemonitor.de/niesgrau) |
| Nindorf (bei Hohenwestedt) | `01058115` | `nindorf-bei-hohenwestedt` | [nindorf-bei-hohenwestedt](https://dev.sh-netz.energiemonitor.de/nindorf-bei-hohenwestedt) |
| Nindorf (bei Meldorf) | `01051078` | `nindorf-bei-meldorf` | [nindorf-bei-meldorf](https://dev.sh-netz.energiemonitor.de/nindorf-bei-meldorf) |
| Noer | `01058116` | `noer` | [noer](https://dev.sh-netz.energiemonitor.de/noer) |
| Norddeich | `01051079` | `norddeich` | [norddeich](https://dev.sh-netz.energiemonitor.de/norddeich) |
| Norddorf auf Amrum | `01054089` | `norddorf-auf-amrum` | [norddorf-auf-amrum](https://dev.sh-netz.energiemonitor.de/norddorf-auf-amrum) |
| Norderbrarup | `01059063` | `norderbrarup` | [norderbrarup](https://dev.sh-netz.energiemonitor.de/norderbrarup) |
| Norderfriedrichskoog | `01054090` | `norderfriedrichskoog` | [norderfriedrichskoog](https://dev.sh-netz.energiemonitor.de/norderfriedrichskoog) |
| Norderheistedt | `01051080` | `norderheistedt` | [norderheistedt](https://dev.sh-netz.energiemonitor.de/norderheistedt) |
| Nordermeldorf | `01051137` | `nordermeldorf` | [nordermeldorf](https://dev.sh-netz.energiemonitor.de/nordermeldorf) |
| Norderwöhrden | `01051081` | `norderwoehrden` | [norderwoehrden](https://dev.sh-netz.energiemonitor.de/norderwoehrden) |
| Nordhackstedt | `01059149` | `nordhackstedt` | [nordhackstedt](https://dev.sh-netz.energiemonitor.de/nordhackstedt) |
| Nordhastedt | `01051082` | `nordhastedt` | [nordhastedt](https://dev.sh-netz.energiemonitor.de/nordhastedt) |
| Nordstrand | `01054091` | `nordstrand` | [nordstrand](https://dev.sh-netz.energiemonitor.de/nordstrand) |
| Norstedt | `01054092` | `norstedt` | [norstedt](https://dev.sh-netz.energiemonitor.de/norstedt) |
| Nortorf (Amt Wilstermarsch) | `01061077` | `nortorf-(amt-wilstermarsch)` | [nortorf-(amt-wilstermarsch)](https://dev.sh-netz.energiemonitor.de/nortorf-(amt-wilstermarsch)) |
| Nottfeld | `01059065` | `nottfeld` | [nottfeld](https://dev.sh-netz.energiemonitor.de/nottfeld) |
| Nutteln | `01061078` | `nutteln` | [nutteln](https://dev.sh-netz.energiemonitor.de/nutteln) |
| Nübbel | `01058118` | `nuebbel` | [nuebbel](https://dev.sh-netz.energiemonitor.de/nuebbel) |
| Nübel | `01059098` | `nuebel` | [nuebel](https://dev.sh-netz.energiemonitor.de/nuebel) |
| Nützen | `01060064` | `nuetzen` | [nuetzen](https://dev.sh-netz.energiemonitor.de/nuetzen) |
| Ockholm | `01054093` | `ockholm` | [ockholm](https://dev.sh-netz.energiemonitor.de/ockholm) |
| Odderade | `01051083` | `odderade` | [odderade](https://dev.sh-netz.energiemonitor.de/odderade) |
| Oelixdorf | `01061079` | `oelixdorf` | [oelixdorf](https://dev.sh-netz.energiemonitor.de/oelixdorf) |
| Oering | `01060065` | `oering` | [oering](https://dev.sh-netz.energiemonitor.de/oering) |
| Oersberg | `01059067` | `oersberg` | [oersberg](https://dev.sh-netz.energiemonitor.de/oersberg) |
| Oeschebüttel | `01061080` | `oeschebuettel` | [oeschebuettel](https://dev.sh-netz.energiemonitor.de/oeschebuettel) |
| Oesterdeichstrich | `01051084` | `oesterdeichstrich` | [oesterdeichstrich](https://dev.sh-netz.energiemonitor.de/oesterdeichstrich) |
| Oesterwurth | `01051140` | `oesterwurth` | [oesterwurth](https://dev.sh-netz.energiemonitor.de/oesterwurth) |
| Oevenum | `01054094` | `oevenum` | [oevenum](https://dev.sh-netz.energiemonitor.de/oevenum) |
| Oeversee | `01059184` | `oeversee` | [oeversee](https://dev.sh-netz.energiemonitor.de/oeversee) |
| Offenbüttel | `01051085` | `offenbuettel` | [offenbuettel](https://dev.sh-netz.energiemonitor.de/offenbuettel) |
| Oldenborstel | `01061081` | `oldenborstel` | [oldenborstel](https://dev.sh-netz.energiemonitor.de/oldenborstel) |
| Oldenbüttel | `01058119` | `oldenbuettel` | [oldenbuettel](https://dev.sh-netz.energiemonitor.de/oldenbuettel) |
| Oldenhütten | `01058120` | `oldenhuetten` | [oldenhuetten](https://dev.sh-netz.energiemonitor.de/oldenhuetten) |
| Oldenswort | `01054095` | `oldenswort` | [oldenswort](https://dev.sh-netz.energiemonitor.de/oldenswort) |
| Oldersbek | `01054096` | `oldersbek` | [oldersbek](https://dev.sh-netz.energiemonitor.de/oldersbek) |
| Olderup | `01054097` | `olderup` | [olderup](https://dev.sh-netz.energiemonitor.de/olderup) |
| Oldsum | `01054098` | `oldsum` | [oldsum](https://dev.sh-netz.energiemonitor.de/oldsum) |
| Osdorf | `01058121` | `osdorf` | [osdorf](https://dev.sh-netz.energiemonitor.de/osdorf) |
| Ostenfeld (Husum) | `01054099` | `ostenfeld-husum` | [ostenfeld-husum](https://dev.sh-netz.energiemonitor.de/ostenfeld-husum) |
| Ostenfeld (Rendsburg) | `01058122` | `ostenfeld-rendsburg` | [ostenfeld-rendsburg](https://dev.sh-netz.energiemonitor.de/ostenfeld-rendsburg) |
| Oster-Ohrstedt | `01054101` | `oster-ohrstedt` | [oster-ohrstedt](https://dev.sh-netz.energiemonitor.de/oster-ohrstedt) |
| Osterby | `01058123` | `osterby` | [osterby](https://dev.sh-netz.energiemonitor.de/osterby) |
| Osterby (Amt Schafflund) | `01059151` | `osterby-amt-schafflund` | [osterby-amt-schafflund](https://dev.sh-netz.energiemonitor.de/osterby-amt-schafflund) |
| Osterhever | `01054100` | `osterhever` | [osterhever](https://dev.sh-netz.energiemonitor.de/osterhever) |
| Osterhorn | `01056038` | `osterhorn` | [osterhorn](https://dev.sh-netz.energiemonitor.de/osterhorn) |
| Osterrade | `01051086` | `osterrade` | [osterrade](https://dev.sh-netz.energiemonitor.de/osterrade) |
| Osterrönfeld | `01058124` | `osterroenfeld` | [osterroenfeld](https://dev.sh-netz.energiemonitor.de/osterroenfeld) |
| Osterstedt | `01058125` | `osterstedt` | [osterstedt](https://dev.sh-netz.energiemonitor.de/osterstedt) |
| Ostrohe | `01051087` | `ostrohe` | [ostrohe](https://dev.sh-netz.energiemonitor.de/ostrohe) |
| Ottenbüttel | `01061083` | `ottenbuettel` | [ottenbuettel](https://dev.sh-netz.energiemonitor.de/ottenbuettel) |
| Owschlag | `01058127` | `owschlag` | [owschlag](https://dev.sh-netz.energiemonitor.de/owschlag) |
| Padenstedt | `01058128` | `padenstedt` | [padenstedt](https://dev.sh-netz.energiemonitor.de/padenstedt) |
| Pahlen | `01051088` | `pahlen` | [pahlen](https://dev.sh-netz.energiemonitor.de/pahlen) |
| Panker | `01057055` | `panker` | [panker](https://dev.sh-netz.energiemonitor.de/panker) |
| Passade | `01057056` | `passade` | [passade](https://dev.sh-netz.energiemonitor.de/passade) |
| Peissen | `01061084` | `peissen` | [peissen](https://dev.sh-netz.energiemonitor.de/peissen) |
| Pellworm | `01054103` | `pellworm` | [pellworm](https://dev.sh-netz.energiemonitor.de/pellworm) |
| Plön | `01057057` | `ploen` | [ploen](https://dev.sh-netz.energiemonitor.de/ploen) |
| Pohnsdorf | `01057058` | `pohnsdorf` | [pohnsdorf](https://dev.sh-netz.energiemonitor.de/pohnsdorf) |
| Pommerby | `01059152` | `pommerby` | [pommerby](https://dev.sh-netz.energiemonitor.de/pommerby) |
| Poppenbüll | `01054104` | `poppenbuell` | [poppenbuell](https://dev.sh-netz.energiemonitor.de/poppenbuell) |
| Postfeld | `01057059` | `postfeld` | [postfeld](https://dev.sh-netz.energiemonitor.de/postfeld) |
| Poyenberg | `01061086` | `poyenberg` | [poyenberg](https://dev.sh-netz.energiemonitor.de/poyenberg) |
| Prasdorf | `01057060` | `prasdorf` | [prasdorf](https://dev.sh-netz.energiemonitor.de/prasdorf) |
| Prinzenmoor | `01058129` | `prinzenmoor` | [prinzenmoor](https://dev.sh-netz.energiemonitor.de/prinzenmoor) |
| Probsteierhagen | `01057063` | `probsteierhagen` | [probsteierhagen](https://dev.sh-netz.energiemonitor.de/probsteierhagen) |
| Pronstorf | `01060067` | `pronstorf` | [pronstorf](https://dev.sh-netz.energiemonitor.de/pronstorf) |
| Puls | `01061087` | `puls` | [puls](https://dev.sh-netz.energiemonitor.de/puls) |
| Pöschendorf | `01061085` | `poeschendorf` | [poeschendorf](https://dev.sh-netz.energiemonitor.de/poeschendorf) |
| Quarnstedt | `01061088` | `quarnstedt` | [quarnstedt](https://dev.sh-netz.energiemonitor.de/quarnstedt) |
| Quickborn (Dithmarschen) | `01051089` | `quickborn-dithmarschen` | [quickborn-dithmarschen](https://dev.sh-netz.energiemonitor.de/quickborn-dithmarschen) |
| Rabel | `01059154` | `rabel` | [rabel](https://dev.sh-netz.energiemonitor.de/rabel) |
| Rabenholz | `01059155` | `rabenholz` | [rabenholz](https://dev.sh-netz.energiemonitor.de/rabenholz) |
| Rabenkirchen-Faulück | `01059068` | `rabenkirchen-faulueck` | [rabenkirchen-faulueck](https://dev.sh-netz.energiemonitor.de/rabenkirchen-faulueck) |
| Rade | `01061089` | `rade` | [rade](https://dev.sh-netz.energiemonitor.de/rade) |
| Rade b. Hohenwestedt | `01058131` | `rade-b-hohenwestedt` | [rade-b-hohenwestedt](https://dev.sh-netz.energiemonitor.de/rade-b-hohenwestedt) |
| Rade b. Rendsburg | `01058132` | `rade-b-rendsburg` | [rade-b-rendsburg](https://dev.sh-netz.energiemonitor.de/rade-b-rendsburg) |
| Ramhusen | `01051090` | `ramhusen` | [ramhusen](https://dev.sh-netz.energiemonitor.de/ramhusen) |
| Ramstedt | `01054105` | `ramstedt` | [ramstedt](https://dev.sh-netz.energiemonitor.de/ramstedt) |
| Rantrum | `01054106` | `rantrum` | [rantrum](https://dev.sh-netz.energiemonitor.de/rantrum) |
| Rantzau | `01057065` | `rantzau` | [rantzau](https://dev.sh-netz.energiemonitor.de/rantzau) |
| Rathjensdorf | `01057067` | `rathjensdorf` | [rathjensdorf](https://dev.sh-netz.energiemonitor.de/rathjensdorf) |
| Rausdorf | `01062058` | `rausdorf` | [rausdorf](https://dev.sh-netz.energiemonitor.de/rausdorf) |
| Reher | `01061091` | `reher` | [reher](https://dev.sh-netz.energiemonitor.de/reher) |
| Rehm-Flehde-Bargen | `01051092` | `rehm-flehde-bargen` | [rehm-flehde-bargen](https://dev.sh-netz.energiemonitor.de/rehm-flehde-bargen) |
| Reinsbüttel | `01051093` | `reinsbuettel` | [reinsbuettel](https://dev.sh-netz.energiemonitor.de/reinsbuettel) |
| Rellingen | `01056043` | `rellingen` | [rellingen](https://dev.sh-netz.energiemonitor.de/rellingen) |
| Remmels | `01058134` | `remmels` | [remmels](https://dev.sh-netz.energiemonitor.de/remmels) |
| Rendsburg | `01058135` | `rendsburg` | [rendsburg](https://dev.sh-netz.energiemonitor.de/rendsburg) |
| Rendswühren | `01057068` | `rendswuehren` | [rendswuehren](https://dev.sh-netz.energiemonitor.de/rendswuehren) |
| Rethwisch | `01061092` | `rethwisch` | [rethwisch](https://dev.sh-netz.energiemonitor.de/rethwisch) |
| Reußenköge | `01054108` | `reussenkoege` | [reussenkoege](https://dev.sh-netz.energiemonitor.de/reussenkoege) |
| Rickert | `01058136` | `rickert` | [rickert](https://dev.sh-netz.energiemonitor.de/rickert) |
| Rickling | `01060068` | `rickling` | [rickling](https://dev.sh-netz.energiemonitor.de/rickling) |
| Riepsdorf | `01055036` | `riepsdorf` | [riepsdorf](https://dev.sh-netz.energiemonitor.de/riepsdorf) |
| Rieseby | `01058137` | `rieseby` | [rieseby](https://dev.sh-netz.energiemonitor.de/rieseby) |
| Ringsberg | `01059157` | `ringsberg` | [ringsberg](https://dev.sh-netz.energiemonitor.de/ringsberg) |
| Risum-Lindholm | `01054109` | `risum-lindholm` | [risum-lindholm](https://dev.sh-netz.energiemonitor.de/risum-lindholm) |
| Rodenbek | `01058138` | `rodenbek` | [rodenbek](https://dev.sh-netz.energiemonitor.de/rodenbek) |
| Rodenäs | `01054110` | `rodenaes` | [rodenaes](https://dev.sh-netz.energiemonitor.de/rodenaes) |
| Rohlstorf | `01060069` | `rohlstorf` | [rohlstorf](https://dev.sh-netz.energiemonitor.de/rohlstorf) |
| Rosdorf | `01061093` | `rosdorf` | [rosdorf](https://dev.sh-netz.energiemonitor.de/rosdorf) |
| Roseburg | `01053104` | `roseburg` | [roseburg](https://dev.sh-netz.energiemonitor.de/roseburg) |
| Ruhwinkel | `01057069` | `ruhwinkel` | [ruhwinkel](https://dev.sh-netz.energiemonitor.de/ruhwinkel) |
| Rumohr | `01058139` | `rumohr` | [rumohr](https://dev.sh-netz.energiemonitor.de/rumohr) |
| Rügge | `01059070` | `ruegge` | [ruegge](https://dev.sh-netz.energiemonitor.de/ruegge) |
| Rümpel | `01062065` | `ruempel` | [ruempel](https://dev.sh-netz.energiemonitor.de/ruempel) |
| Sahms | `01053106` | `sahms` | [sahms](https://dev.sh-netz.energiemonitor.de/sahms) |
| Sankt Annen | `01051096` | `sankt-annen` | [sankt-annen](https://dev.sh-netz.energiemonitor.de/sankt-annen) |
| Sankt Margarethen | `01061095` | `sankt-margarethen` | [sankt-margarethen](https://dev.sh-netz.energiemonitor.de/sankt-margarethen) |
| Sankt Michaelisdonn | `01051097` | `sankt-michaelisdonn` | [sankt-michaelisdonn](https://dev.sh-netz.energiemonitor.de/sankt-michaelisdonn) |
| Sankt Peter-Ording | `01054113` | `sankt-peter-ording` | [sankt-peter-ording](https://dev.sh-netz.energiemonitor.de/sankt-peter-ording) |
| Sarlhusen | `01061096` | `sarlhusen` | [sarlhusen](https://dev.sh-netz.energiemonitor.de/sarlhusen) |
| Sarzbüttel | `01051098` | `sarzbuettel` | [sarzbuettel](https://dev.sh-netz.energiemonitor.de/sarzbuettel) |
| Saustrup | `01059072` | `saustrup` | [saustrup](https://dev.sh-netz.energiemonitor.de/saustrup) |
| Schaalby | `01059073` | `schaalby` | [schaalby](https://dev.sh-netz.energiemonitor.de/schaalby) |
| Schacht-Audorf | `01058140` | `schacht-audorf` | [schacht-audorf](https://dev.sh-netz.energiemonitor.de/schacht-audorf) |
| Schackendorf | `01060070` | `schackendorf` | [schackendorf](https://dev.sh-netz.energiemonitor.de/schackendorf) |
| Schafflund | `01059158` | `schafflund` | [schafflund](https://dev.sh-netz.energiemonitor.de/schafflund) |
| Schafstedt | `01051099` | `schafstedt` | [schafstedt](https://dev.sh-netz.energiemonitor.de/schafstedt) |
| Schalkholz | `01051100` | `schalkholz` | [schalkholz](https://dev.sh-netz.energiemonitor.de/schalkholz) |
| Schashagen | `01055037` | `schashagen` | [schashagen](https://dev.sh-netz.energiemonitor.de/schashagen) |
| Scheggerott | `01059074` | `scheggerott` | [scheggerott](https://dev.sh-netz.energiemonitor.de/scheggerott) |
| Schellhorn | `01057070` | `schellhorn` | [schellhorn](https://dev.sh-netz.energiemonitor.de/schellhorn) |
| Schenefeld | `01061097` | `schenefeld` | [schenefeld](https://dev.sh-netz.energiemonitor.de/schenefeld) |
| Schieren | `01060071` | `schieren` | [schieren](https://dev.sh-netz.energiemonitor.de/schieren) |
| Schierensee | `01058141` | `schierensee` | [schierensee](https://dev.sh-netz.energiemonitor.de/schierensee) |
| Schillsdorf | `01057071` | `schillsdorf` | [schillsdorf](https://dev.sh-netz.energiemonitor.de/schillsdorf) |
| Schinkel | `01058142` | `schinkel` | [schinkel](https://dev.sh-netz.energiemonitor.de/schinkel) |
| Schlesen | `01057072` | `schlesen` | [schlesen](https://dev.sh-netz.energiemonitor.de/schlesen) |
| Schlichting | `01051102` | `schlichting` | [schlichting](https://dev.sh-netz.energiemonitor.de/schlichting) |
| Schlotfeld | `01061098` | `schlotfeld` | [schlotfeld](https://dev.sh-netz.energiemonitor.de/schlotfeld) |
| Schmalensee | `01060072` | `schmalensee` | [schmalensee](https://dev.sh-netz.energiemonitor.de/schmalensee) |
| Schmalfeld | `01060073` | `schmalfeld` | [schmalfeld](https://dev.sh-netz.energiemonitor.de/schmalfeld) |
| Schmedeswurth | `01051103` | `schmedeswurth` | [schmedeswurth](https://dev.sh-netz.energiemonitor.de/schmedeswurth) |
| Schnarup-Thumby | `01059076` | `schnarup-thumby` | [schnarup-thumby](https://dev.sh-netz.energiemonitor.de/schnarup-thumby) |
| Schretstaken | `01053113` | `schretstaken` | [schretstaken](https://dev.sh-netz.energiemonitor.de/schretstaken) |
| Schrum | `01051104` | `schrum` | [schrum](https://dev.sh-netz.energiemonitor.de/schrum) |
| Schuby | `01059077` | `schuby` | [schuby](https://dev.sh-netz.energiemonitor.de/schuby) |
| Schulendorf | `01053115` | `schulendorf` | [schulendorf](https://dev.sh-netz.energiemonitor.de/schulendorf) |
| Schwabstedt | `01054116` | `schwabstedt` | [schwabstedt](https://dev.sh-netz.energiemonitor.de/schwabstedt) |
| Schwartbuck | `01057076` | `schwartbuck` | [schwartbuck](https://dev.sh-netz.energiemonitor.de/schwartbuck) |
| Schwarzenbek | `01053116` | `schwarzenbek` | [schwarzenbek](https://dev.sh-netz.energiemonitor.de/schwarzenbek) |
| Schwedeneck | `01058150` | `schwedeneck` | [schwedeneck](https://dev.sh-netz.energiemonitor.de/schwedeneck) |
| Schwesing | `01054118` | `schwesing` | [schwesing](https://dev.sh-netz.energiemonitor.de/schwesing) |
| Schwissel | `01060074` | `schwissel` | [schwissel](https://dev.sh-netz.energiemonitor.de/schwissel) |
| Schönbek | `01058144` | `schoenbek` | [schoenbek](https://dev.sh-netz.energiemonitor.de/schoenbek) |
| Schönberg | `01057073` | `schoenberg` | [schoenberg](https://dev.sh-netz.energiemonitor.de/schoenberg) |
| Schönhorst | `01058145` | `schoenhorst` | [schoenhorst](https://dev.sh-netz.energiemonitor.de/schoenhorst) |
| Schönkirchen | `01057074` | `schoenkirchen` | [schoenkirchen](https://dev.sh-netz.energiemonitor.de/schoenkirchen) |
| Schönwalde am Bungsberg | `01055038` | `schoenwalde-am-bungsberg` | [schoenwalde-am-bungsberg](https://dev.sh-netz.energiemonitor.de/schoenwalde-am-bungsberg) |
| Schülldorf | `01058146` | `schuelldorf` | [schuelldorf](https://dev.sh-netz.energiemonitor.de/schuelldorf) |
| Schülp | `01051105` | `schuelp` | [schuelp](https://dev.sh-netz.energiemonitor.de/schuelp) |
| Schülp b. Nortorf | `01058147` | `schuelp-b-nortorf` | [schuelp-b-nortorf](https://dev.sh-netz.energiemonitor.de/schuelp-b-nortorf) |
| Schülp b. Rendsburg | `01058148` | `schuelp-b-rendsburg` | [schuelp-b-rendsburg](https://dev.sh-netz.energiemonitor.de/schuelp-b-rendsburg) |
| Seedorf | `01060075` | `seedorf` | [seedorf](https://dev.sh-netz.energiemonitor.de/seedorf) |
| Seefeld | `01058151` | `seefeld` | [seefeld](https://dev.sh-netz.energiemonitor.de/seefeld) |
| Seeth | `01054119` | `seeth` | [seeth](https://dev.sh-netz.energiemonitor.de/seeth) |
| Sehestedt | `01058152` | `sehestedt` | [sehestedt](https://dev.sh-netz.energiemonitor.de/sehestedt) |
| Selent | `01057077` | `selent` | [selent](https://dev.sh-netz.energiemonitor.de/selent) |
| Selk | `01059078` | `selk` | [selk](https://dev.sh-netz.energiemonitor.de/selk) |
| Seth | `01060076` | `seth` | [seth](https://dev.sh-netz.energiemonitor.de/seth) |
| Siebeneichen | `01053119` | `siebeneichen` | [siebeneichen](https://dev.sh-netz.energiemonitor.de/siebeneichen) |
| Siek | `01062069` | `siek` | [siek](https://dev.sh-netz.energiemonitor.de/siek) |
| Sierksdorf | `01055039` | `sierksdorf` | [sierksdorf](https://dev.sh-netz.energiemonitor.de/sierksdorf) |
| Sievershütten | `01060077` | `sievershuetten` | [sievershuetten](https://dev.sh-netz.energiemonitor.de/sievershuetten) |
| Sieverstedt | `01059159` | `sieverstedt` | [sieverstedt](https://dev.sh-netz.energiemonitor.de/sieverstedt) |
| Silberstedt | `01059079` | `silberstedt` | [silberstedt](https://dev.sh-netz.energiemonitor.de/silberstedt) |
| Silzen | `01061100` | `silzen` | [silzen](https://dev.sh-netz.energiemonitor.de/silzen) |
| Simonsberg | `01054120` | `simonsberg` | [simonsberg](https://dev.sh-netz.energiemonitor.de/simonsberg) |
| Sollerup | `01059162` | `sollerup` | [sollerup](https://dev.sh-netz.energiemonitor.de/sollerup) |
| Sollwitt | `01054123` | `sollwitt` | [sollwitt](https://dev.sh-netz.energiemonitor.de/sollwitt) |
| Sommerland | `01061101` | `sommerland` | [sommerland](https://dev.sh-netz.energiemonitor.de/sommerland) |
| Sophienhamm | `01058154` | `sophienhamm` | [sophienhamm](https://dev.sh-netz.energiemonitor.de/sophienhamm) |
| Sprakebüll | `01054124` | `sprakebuell` | [sprakebuell](https://dev.sh-netz.energiemonitor.de/sprakebuell) |
| Stadt Garding | `01054036` | `stadt-garding` | [stadt-garding](https://dev.sh-netz.energiemonitor.de/stadt-garding) |
| Stadt Glückstadt | `01061029` | `glueckstadt` | [glueckstadt](https://dev.sh-netz.energiemonitor.de/glueckstadt) |
| Stadt Schenefeld | `01056044` | `stadt-schenefeld` | [stadt-schenefeld](https://dev.sh-netz.energiemonitor.de/stadt-schenefeld) |
| Stadt Wesselburen | `01051127` | `stadt-wesselburen` | [stadt-wesselburen](https://dev.sh-netz.energiemonitor.de/stadt-wesselburen) |
| Stadum | `01054125` | `stadum` | [stadum](https://dev.sh-netz.energiemonitor.de/stadum) |
| Stafstedt | `01058155` | `stafstedt` | [stafstedt](https://dev.sh-netz.energiemonitor.de/stafstedt) |
| Stakendorf | `01057078` | `stakendorf` | [stakendorf](https://dev.sh-netz.energiemonitor.de/stakendorf) |
| Stangheck | `01059163` | `stangheck` | [stangheck](https://dev.sh-netz.energiemonitor.de/stangheck) |
| Stapel | `01059188` | `stapel` | [stapel](https://dev.sh-netz.energiemonitor.de/stapel) |
| Stapelfeld | `01062071` | `stapelfeld` | [stapelfeld](https://dev.sh-netz.energiemonitor.de/stapelfeld) |
| Stedesand | `01054126` | `stedesand` | [stedesand](https://dev.sh-netz.energiemonitor.de/stedesand) |
| Steenfeld | `01058156` | `steenfeld` | [steenfeld](https://dev.sh-netz.energiemonitor.de/steenfeld) |
| Stein | `01057079` | `stein` | [stein](https://dev.sh-netz.energiemonitor.de/stein) |
| Steinberg | `01059164` | `steinberg` | [steinberg](https://dev.sh-netz.energiemonitor.de/steinberg) |
| Steinbergkirche | `01059186` | `steinbergkirche` | [steinbergkirche](https://dev.sh-netz.energiemonitor.de/steinbergkirche) |
| Steinfeld | `01059080` | `steinfeld` | [steinfeld](https://dev.sh-netz.energiemonitor.de/steinfeld) |
| Stelle-Wittenwurth | `01051107` | `stelle-wittenwurth` | [stelle-wittenwurth](https://dev.sh-netz.energiemonitor.de/stelle-wittenwurth) |
| Sterup | `01059167` | `sterup` | [sterup](https://dev.sh-netz.energiemonitor.de/sterup) |
| Stipsdorf | `01060079` | `stipsdorf` | [stipsdorf](https://dev.sh-netz.energiemonitor.de/stipsdorf) |
| Stocksee | `01060080` | `stocksee` | [stocksee](https://dev.sh-netz.energiemonitor.de/stocksee) |
| Stolk | `01059081` | `stolk` | [stolk](https://dev.sh-netz.energiemonitor.de/stolk) |
| Stolpe | `01057080` | `stolpe` | [stolpe](https://dev.sh-netz.energiemonitor.de/stolpe) |
| Stoltebüll | `01059168` | `stoltebuell` | [stoltebuell](https://dev.sh-netz.energiemonitor.de/stoltebuell) |
| Stoltenberg | `01057081` | `stoltenberg` | [stoltenberg](https://dev.sh-netz.energiemonitor.de/stoltenberg) |
| Strande | `01058157` | `strande` | [strande](https://dev.sh-netz.energiemonitor.de/strande) |
| Struckum | `01054128` | `struckum` | [struckum](https://dev.sh-netz.energiemonitor.de/struckum) |
| Strukdorf | `01060081` | `strukdorf` | [strukdorf](https://dev.sh-netz.energiemonitor.de/strukdorf) |
| Struvenhütten | `01060082` | `struvenhuetten` | [struvenhuetten](https://dev.sh-netz.energiemonitor.de/struvenhuetten) |
| Struxdorf | `01059082` | `struxdorf` | [struxdorf](https://dev.sh-netz.energiemonitor.de/struxdorf) |
| Strübbel | `01051108` | `struebbel` | [struebbel](https://dev.sh-netz.energiemonitor.de/struebbel) |
| Stuvenborn | `01060084` | `stuvenborn` | [stuvenborn](https://dev.sh-netz.energiemonitor.de/stuvenborn) |
| Stördorf | `01061102` | `stoerdorf` | [stoerdorf](https://dev.sh-netz.energiemonitor.de/stoerdorf) |
| Störkathen | `01061103` | `stoerkathen` | [stoerkathen](https://dev.sh-netz.energiemonitor.de/stoerkathen) |
| Sönnebüll | `01054121` | `soennebuell` | [soennebuell](https://dev.sh-netz.energiemonitor.de/soennebuell) |
| Sörup | `01059161` | `soerup` | [soerup](https://dev.sh-netz.energiemonitor.de/soerup) |
| Süderau | `01061104` | `suederau` | [suederau](https://dev.sh-netz.energiemonitor.de/suederau) |
| Süderbrarup | `01059083` | `suederbrarup` | [suederbrarup](https://dev.sh-netz.energiemonitor.de/suederbrarup) |
| Süderdeich | `01051109` | `suederdeich` | [suederdeich](https://dev.sh-netz.energiemonitor.de/suederdeich) |
| Süderdorf | `01051139` | `suederdorf` | [suederdorf](https://dev.sh-netz.energiemonitor.de/suederdorf) |
| Süderende | `01054129` | `suederende` | [suederende](https://dev.sh-netz.energiemonitor.de/suederende) |
| Süderfahrenstedt | `01059084` | `suederfahrenstedt` | [suederfahrenstedt](https://dev.sh-netz.energiemonitor.de/suederfahrenstedt) |
| Süderhackstedt | `01059169` | `suederhackstedt` | [suederhackstedt](https://dev.sh-netz.energiemonitor.de/suederhackstedt) |
| Süderhastedt | `01051110` | `suederhastedt` | [suederhastedt](https://dev.sh-netz.energiemonitor.de/suederhastedt) |
| Süderheistedt | `01051141` | `suederheistedt` | [suederheistedt](https://dev.sh-netz.energiemonitor.de/suederheistedt) |
| Süderhöft | `01054130` | `suederhoeft` | [suederhoeft](https://dev.sh-netz.energiemonitor.de/suederhoeft) |
| Süderlügum | `01054131` | `suederluegum` | [suederluegum](https://dev.sh-netz.energiemonitor.de/suederluegum) |
| Südermarsch | `01054132` | `suedermarsch` | [suedermarsch](https://dev.sh-netz.energiemonitor.de/suedermarsch) |
| Sülfeld | `01060085` | `suelfeld` | [suelfeld](https://dev.sh-netz.energiemonitor.de/suelfeld) |
| Süsel | `01055041` | `suesel` | [suesel](https://dev.sh-netz.energiemonitor.de/suesel) |
| Taarstedt | `01059086` | `taarstedt` | [taarstedt](https://dev.sh-netz.energiemonitor.de/taarstedt) |
| Tackesdorf | `01058158` | `tackesdorf` | [tackesdorf](https://dev.sh-netz.energiemonitor.de/tackesdorf) |
| Talkau | `01053125` | `talkau` | [talkau](https://dev.sh-netz.energiemonitor.de/talkau) |
| Tangstedt | `01062076` | `tangstedt` | [tangstedt](https://dev.sh-netz.energiemonitor.de/tangstedt) |
| Tappendorf | `01058159` | `tappendorf` | [tappendorf](https://dev.sh-netz.energiemonitor.de/tappendorf) |
| Tarbek | `01060086` | `tarbek` | [tarbek](https://dev.sh-netz.energiemonitor.de/tarbek) |
| Tarp | `01059171` | `tarp` | [tarp](https://dev.sh-netz.energiemonitor.de/tarp) |
| Tasdorf | `01057083` | `tasdorf` | [tasdorf](https://dev.sh-netz.energiemonitor.de/tasdorf) |
| Tating | `01054134` | `tating` | [tating](https://dev.sh-netz.energiemonitor.de/tating) |
| Techelsdorf | `01058160` | `techelsdorf` | [techelsdorf](https://dev.sh-netz.energiemonitor.de/techelsdorf) |
| Tellingstedt | `01051114` | `tellingstedt` | [tellingstedt](https://dev.sh-netz.energiemonitor.de/tellingstedt) |
| Tensbüttel-Röst | `01051138` | `tensbuettel-roest` | [tensbuettel-roest](https://dev.sh-netz.energiemonitor.de/tensbuettel-roest) |
| Tensfeld | `01060087` | `tensfeld` | [tensfeld](https://dev.sh-netz.energiemonitor.de/tensfeld) |
| Tetenbüll | `01054135` | `tetenbuell` | [tetenbuell](https://dev.sh-netz.energiemonitor.de/tetenbuell) |
| Tetenhusen | `01059087` | `tetenhusen` | [tetenhusen](https://dev.sh-netz.energiemonitor.de/tetenhusen) |
| Thaden | `01058161` | `thaden` | [thaden](https://dev.sh-netz.energiemonitor.de/thaden) |
| Thumby | `01058162` | `thumby` | [thumby](https://dev.sh-netz.energiemonitor.de/thumby) |
| Tielen | `01059088` | `tielen` | [tielen](https://dev.sh-netz.energiemonitor.de/tielen) |
| Tielenhemme | `01051117` | `tielenhemme` | [tielenhemme](https://dev.sh-netz.energiemonitor.de/tielenhemme) |
| Timmaspe | `01058163` | `timmaspe` | [timmaspe](https://dev.sh-netz.energiemonitor.de/timmaspe) |
| Tinningstedt | `01054136` | `tinningstedt` | [tinningstedt](https://dev.sh-netz.energiemonitor.de/tinningstedt) |
| Todenbüttel | `01058164` | `todenbuettel` | [todenbuettel](https://dev.sh-netz.energiemonitor.de/todenbuettel) |
| Todesfelde | `01060088` | `todesfelde` | [todesfelde](https://dev.sh-netz.energiemonitor.de/todesfelde) |
| Tolk | `01059090` | `tolk` | [tolk](https://dev.sh-netz.energiemonitor.de/tolk) |
| Tramm | `01053126` | `tramm` | [tramm](https://dev.sh-netz.energiemonitor.de/tramm) |
| Trappenkamp | `01060089` | `trappenkamp` | [trappenkamp](https://dev.sh-netz.energiemonitor.de/trappenkamp) |
| Travenbrück | `01062092` | `travenbrueck` | [travenbrueck](https://dev.sh-netz.energiemonitor.de/travenbrueck) |
| Travenhorst | `01060090` | `travenhorst` | [travenhorst](https://dev.sh-netz.energiemonitor.de/travenhorst) |
| Traventhal | `01060091` | `traventhal` | [traventhal](https://dev.sh-netz.energiemonitor.de/traventhal) |
| Treia | `01059092` | `treia` | [treia](https://dev.sh-netz.energiemonitor.de/treia) |
| Tremsbüttel | `01062081` | `tremsbuettel` | [tremsbuettel](https://dev.sh-netz.energiemonitor.de/tremsbuettel) |
| Trennewurth | `01051118` | `trennewurth` | [trennewurth](https://dev.sh-netz.energiemonitor.de/trennewurth) |
| Trittau | `01062082` | `trittau` | [trittau](https://dev.sh-netz.energiemonitor.de/trittau) |
| Tröndel | `01057082` | `troendel` | [troendel](https://dev.sh-netz.energiemonitor.de/troendel) |
| Twedt | `01059097` | `twedt` | [twedt](https://dev.sh-netz.energiemonitor.de/twedt) |
| Tönning | `01054138` | `toenning` | [toenning](https://dev.sh-netz.energiemonitor.de/toenning) |
| Tümlauer Koog | `01054140` | `tuemlauer-koog` | [tuemlauer-koog](https://dev.sh-netz.energiemonitor.de/tuemlauer-koog) |
| Tüttendorf | `01058165` | `tuettendorf` | [tuettendorf](https://dev.sh-netz.energiemonitor.de/tuettendorf) |
| Uelsby | `01059093` | `uelsby` | [uelsby](https://dev.sh-netz.energiemonitor.de/uelsby) |
| Uelvesbüll | `01054141` | `uelvesbuell` | [uelvesbuell](https://dev.sh-netz.energiemonitor.de/uelvesbuell) |
| Uetersen | `01056049` | `uetersen` | [uetersen](https://dev.sh-netz.energiemonitor.de/uetersen) |
| Ulsnis | `01059094` | `ulsnis` | [ulsnis](https://dev.sh-netz.energiemonitor.de/ulsnis) |
| Uphusum | `01054142` | `uphusum` | [uphusum](https://dev.sh-netz.energiemonitor.de/uphusum) |
| Utersum | `01054143` | `utersum` | [utersum](https://dev.sh-netz.energiemonitor.de/utersum) |
| Vaale | `01061105` | `vaale` | [vaale](https://dev.sh-netz.energiemonitor.de/vaale) |
| Vaalermoor | `01061106` | `vaalermoor` | [vaalermoor](https://dev.sh-netz.energiemonitor.de/vaalermoor) |
| Viöl | `01054144` | `vioel` | [vioel](https://dev.sh-netz.energiemonitor.de/vioel) |
| Vollerwiek | `01054145` | `vollerwiek` | [vollerwiek](https://dev.sh-netz.energiemonitor.de/vollerwiek) |
| Vollstedt | `01054146` | `vollstedt` | [vollstedt](https://dev.sh-netz.energiemonitor.de/vollstedt) |
| Volsemenhusen | `01051119` | `volsemenhusen` | [volsemenhusen](https://dev.sh-netz.energiemonitor.de/volsemenhusen) |
| Waabs | `01058166` | `waabs` | [waabs](https://dev.sh-netz.energiemonitor.de/waabs) |
| Wacken | `01061107` | `wacken` | [wacken](https://dev.sh-netz.energiemonitor.de/wacken) |
| Wagersrott | `01059095` | `wagersrott` | [wagersrott](https://dev.sh-netz.energiemonitor.de/wagersrott) |
| Wahlstedt | `01060092` | `wahlstedt` | [wahlstedt](https://dev.sh-netz.energiemonitor.de/wahlstedt) |
| Wahlstorf | `01057084` | `wahlstorf` | [wahlstorf](https://dev.sh-netz.energiemonitor.de/wahlstorf) |
| Wakendorf I | `01060093` | `wakendorf-i` | [wakendorf-i](https://dev.sh-netz.energiemonitor.de/wakendorf-i) |
| Wakendorf II | `01060094` | `wakendorf-ii` | [wakendorf-ii](https://dev.sh-netz.energiemonitor.de/wakendorf-ii) |
| Wallen | `01051120` | `wallen` | [wallen](https://dev.sh-netz.energiemonitor.de/wallen) |
| Wallsbüll | `01059173` | `wallsbuell` | [wallsbuell](https://dev.sh-netz.energiemonitor.de/wallsbuell) |
| Wanderup | `01059174` | `wanderup` | [wanderup](https://dev.sh-netz.energiemonitor.de/wanderup) |
| Wangels | `01055043` | `wangels` | [wangels](https://dev.sh-netz.energiemonitor.de/wangels) |
| Wankendorf | `01057085` | `wankendorf` | [wankendorf](https://dev.sh-netz.energiemonitor.de/wankendorf) |
| Wapelfeld | `01058167` | `wapelfeld` | [wapelfeld](https://dev.sh-netz.energiemonitor.de/wapelfeld) |
| Warder | `01058168` | `warder` | [warder](https://dev.sh-netz.energiemonitor.de/warder) |
| Warnau | `01057086` | `warnau` | [warnau](https://dev.sh-netz.energiemonitor.de/warnau) |
| Warwerort | `01051121` | `warwerort` | [warwerort](https://dev.sh-netz.energiemonitor.de/warwerort) |
| Wasbek | `01058169` | `wasbek` | [wasbek](https://dev.sh-netz.energiemonitor.de/wasbek) |
| Wattenbek | `01058170` | `wattenbek` | [wattenbek](https://dev.sh-netz.energiemonitor.de/wattenbek) |
| Weddelbrook | `01060095` | `weddelbrook` | [weddelbrook](https://dev.sh-netz.energiemonitor.de/weddelbrook) |
| Weddingstedt | `01051122` | `weddingstedt` | [weddingstedt](https://dev.sh-netz.energiemonitor.de/weddingstedt) |
| Weede | `01060096` | `weede` | [weede](https://dev.sh-netz.energiemonitor.de/weede) |
| Wees | `01059176` | `wees` | [wees](https://dev.sh-netz.energiemonitor.de/wees) |
| Weesby | `01059177` | `weesby` | [weesby](https://dev.sh-netz.energiemonitor.de/weesby) |
| Welmbüttel | `01051125` | `welmbuettel` | [welmbuettel](https://dev.sh-netz.energiemonitor.de/welmbuettel) |
| Welt | `01054148` | `welt` | [welt](https://dev.sh-netz.energiemonitor.de/welt) |
| Wendtorf | `01057087` | `wendtorf` | [wendtorf](https://dev.sh-netz.energiemonitor.de/wendtorf) |
| Wennbüttel | `01051126` | `wennbuettel` | [wennbuettel](https://dev.sh-netz.energiemonitor.de/wennbuettel) |
| Wensin | `01060097` | `wensin` | [wensin](https://dev.sh-netz.energiemonitor.de/wensin) |
| Wesselburener Deichhausen | `01051128` | `wesselburener-deichhausen` | [wesselburener-deichhausen](https://dev.sh-netz.energiemonitor.de/wesselburener-deichhausen) |
| Wesselburenerkoog | `01051129` | `wesselburenerkoog` | [wesselburenerkoog](https://dev.sh-netz.energiemonitor.de/wesselburenerkoog) |
| Wesseln | `01051130` | `wesseln` | [wesseln](https://dev.sh-netz.energiemonitor.de/wesseln) |
| Westensee | `01058171` | `westensee` | [westensee](https://dev.sh-netz.energiemonitor.de/westensee) |
| Wester-Ohrstedt | `01054152` | `wester-ohrstedt` | [wester-ohrstedt](https://dev.sh-netz.energiemonitor.de/wester-ohrstedt) |
| Westerborstel | `01051131` | `westerborstel` | [westerborstel](https://dev.sh-netz.energiemonitor.de/westerborstel) |
| Westerdeichstrich | `01051132` | `westerdeichstrich` | [westerdeichstrich](https://dev.sh-netz.energiemonitor.de/westerdeichstrich) |
| Westerhever | `01054150` | `westerhever` | [westerhever](https://dev.sh-netz.energiemonitor.de/westerhever) |
| Westerholz | `01059178` | `westerholz` | [westerholz](https://dev.sh-netz.energiemonitor.de/westerholz) |
| Westerhorn | `01056051` | `westerhorn` | [westerhorn](https://dev.sh-netz.energiemonitor.de/westerhorn) |
| Westermoor | `01061109` | `westermoor` | [westermoor](https://dev.sh-netz.energiemonitor.de/westermoor) |
| Westerrade | `01060098` | `westerrade` | [westerrade](https://dev.sh-netz.energiemonitor.de/westerrade) |
| Westerrönfeld | `01058172` | `westerroenfeld` | [westerroenfeld](https://dev.sh-netz.energiemonitor.de/westerroenfeld) |
| Westre | `01054154` | `westre` | [westre](https://dev.sh-netz.energiemonitor.de/westre) |
| Wewelsfleth | `01061110` | `wewelsfleth` | [wewelsfleth](https://dev.sh-netz.energiemonitor.de/wewelsfleth) |
| Wiemersdorf | `01060099` | `wiemersdorf` | [wiemersdorf](https://dev.sh-netz.energiemonitor.de/wiemersdorf) |
| Wiemerstedt | `01051133` | `wiemerstedt` | [wiemerstedt](https://dev.sh-netz.energiemonitor.de/wiemerstedt) |
| Wiershop | `01053131` | `wiershop` | [wiershop](https://dev.sh-netz.energiemonitor.de/wiershop) |
| Willenscharen | `01061112` | `willenscharen` | [willenscharen](https://dev.sh-netz.energiemonitor.de/willenscharen) |
| Windbergen | `01051134` | `windbergen` | [windbergen](https://dev.sh-netz.energiemonitor.de/windbergen) |
| Windeby | `01058173` | `windeby` | [windeby](https://dev.sh-netz.energiemonitor.de/windeby) |
| Winnemark | `01058174` | `winnemark` | [winnemark](https://dev.sh-netz.energiemonitor.de/winnemark) |
| Winnert | `01054156` | `winnert` | [winnert](https://dev.sh-netz.energiemonitor.de/winnert) |
| Winseldorf | `01061114` | `winseldorf` | [winseldorf](https://dev.sh-netz.energiemonitor.de/winseldorf) |
| Winsen | `01060100` | `winsen` | [winsen](https://dev.sh-netz.energiemonitor.de/winsen) |
| Wisch (Holstein) | `01057088` | `wisch-holstein` | [wisch-holstein](https://dev.sh-netz.energiemonitor.de/wisch-holstein) |
| Wisch (Nordfriesland) | `01054157` | `wisch-nordfriesland` | [wisch-nordfriesland](https://dev.sh-netz.energiemonitor.de/wisch-nordfriesland) |
| Witsum | `01054158` | `witsum` | [witsum](https://dev.sh-netz.energiemonitor.de/witsum) |
| Wittbek | `01054159` | `wittbek` | [wittbek](https://dev.sh-netz.energiemonitor.de/wittbek) |
| Wittdün auf Amrum | `01054160` | `wittduen-auf-amrum` | [wittduen-auf-amrum](https://dev.sh-netz.energiemonitor.de/wittduen-auf-amrum) |
| Wittenbergen | `01061115` | `wittenbergen` | [wittenbergen](https://dev.sh-netz.energiemonitor.de/wittenbergen) |
| Wittenborn | `01060101` | `wittenborn` | [wittenborn](https://dev.sh-netz.energiemonitor.de/wittenborn) |
| Wittmoldt | `01057089` | `wittmoldt` | [wittmoldt](https://dev.sh-netz.energiemonitor.de/wittmoldt) |
| Witzeeze | `01053132` | `witzeeze` | [witzeeze](https://dev.sh-netz.energiemonitor.de/witzeeze) |
| Witzhave | `01062086` | `witzhave` | [witzhave](https://dev.sh-netz.energiemonitor.de/witzhave) |
| Witzwort | `01054161` | `witzwort` | [witzwort](https://dev.sh-netz.energiemonitor.de/witzwort) |
| Wobbenbüll | `01054162` | `wobbenbuell` | [wobbenbuell](https://dev.sh-netz.energiemonitor.de/wobbenbuell) |
| Wohlde | `01059096` | `wohlde` | [wohlde](https://dev.sh-netz.energiemonitor.de/wohlde) |
| Wolmersdorf | `01051135` | `wolmersdorf` | [wolmersdorf](https://dev.sh-netz.energiemonitor.de/wolmersdorf) |
| Woltersdorf | `01053134` | `woltersdorf` | [woltersdorf](https://dev.sh-netz.energiemonitor.de/woltersdorf) |
| Worth | `01053135` | `worth` | [worth](https://dev.sh-netz.energiemonitor.de/worth) |
| Wrist | `01061116` | `wrist` | [wrist](https://dev.sh-netz.energiemonitor.de/wrist) |
| Wrixum | `01054163` | `wrixum` | [wrixum](https://dev.sh-netz.energiemonitor.de/wrixum) |
| Wrohm | `01051136` | `wrohm` | [wrohm](https://dev.sh-netz.energiemonitor.de/wrohm) |
| Wulfsmoor | `01061117` | `wulfsmoor` | [wulfsmoor](https://dev.sh-netz.energiemonitor.de/wulfsmoor) |
| Wyk auf Föhr | `01054164` | `wyk-auf-foehr` | [wyk-auf-foehr](https://dev.sh-netz.energiemonitor.de/wyk-auf-foehr) |
| Wöhrden | `01051113` | `woehrden` | [woehrden](https://dev.sh-netz.energiemonitor.de/woehrden) |
### VSE — VSE AG (`tenantId=5030`)

Dashboard-Basis: `https://dev.vse.energiemonitor.de/<regionUrlKey>` — **1** Regionen.

| Gemeinde / Region | `region_code` | URL-Slug | Dashboard |
|---|---|---|---|
| Oberthal (Saarland) | `10046116` | `oberthal` | [oberthal](https://dev.vse.energiemonitor.de/oberthal) |
### WHITELABEL — E.ON Grid Solutions GmbH (`tenantId=4711`)

Dashboard-Basis: `https://energiemonitor.de/<regionUrlKey>` — **36** Regionen.

| Gemeinde / Region | `region_code` | URL-Slug | Dashboard |
|---|---|---|---|
| Adelshofen | `09179111` | `adelshofen` | [adelshofen](https://energiemonitor.de/adelshofen) |
| Alling | `09179113` | `alling` | [alling](https://energiemonitor.de/alling) |
| Althegnenberg | `09179114` | `althegnenberg` | [althegnenberg](https://energiemonitor.de/althegnenberg) |
| Alzenau | `09671111` | `eva-alzenau` | [eva-alzenau](https://energiemonitor.de/eva-alzenau) |
| Burgdorf | `03241003` | `burgdorf` | [burgdorf](https://energiemonitor.de/burgdorf) |
| Eching am Ammersee | `09181115` | `eching-am-ammersee` | [eching-am-ammersee](https://energiemonitor.de/eching-am-ammersee) |
| Energiemonitor für Erlenbach, Obernburg und Wörth | `09676000` | `ezv-energie` | [ezv-energie](https://energiemonitor.de/ezv-energie) |
| Eresing | `09181118` | `eresing` | [eresing](https://energiemonitor.de/eresing) |
| Geltendorf | `09181122` | `geltendorf` | [geltendorf](https://energiemonitor.de/geltendorf) |
| Gilching | `09188121` | `gilching` | [gilching](https://energiemonitor.de/gilching) |
| Grafrath | `09179125` | `grafrath` | [grafrath](https://energiemonitor.de/grafrath) |
| Greifenberg | `09181123` | `greifenberg` | [greifenberg](https://energiemonitor.de/greifenberg) |
| Hattenhofen | `09179128` | `hattenhofen` | [hattenhofen](https://energiemonitor.de/hattenhofen) |
| Inning am Ammersee | `09188126` | `inning` | [inning](https://energiemonitor.de/inning) |
| Jesenwang | `09179130` | `jesenwang` | [jesenwang](https://energiemonitor.de/jesenwang) |
| Kelheim | `49273137` | `kelheim` | [kelheim](https://energiemonitor.de/kelheim) |
| Kottgeisering | `09179131` | `kottgeisering` | [kottgeisering](https://energiemonitor.de/kottgeisering) |
| Kreis Steinfurt | `05566` | `kreis-steinfurt` | [kreis-steinfurt](https://energiemonitor.de/kreis-steinfurt) |
| Landkreis Aschaffenburg | `09671` | `landkreis-aschaffenburg` | [landkreis-aschaffenburg](https://energiemonitor.de/landkreis-aschaffenburg) |
| Landsberied | `09179132` | `landsberied` | [landsberied](https://energiemonitor.de/landsberied) |
| Mammendorf | `09179136` | `mammendorf` | [mammendorf](https://energiemonitor.de/mammendorf) |
| Moorenweis | `09179138` | `moorenweis` | [moorenweis](https://energiemonitor.de/moorenweis) |
| Pullach | `09184139` | `pullach` | [pullach](https://energiemonitor.de/pullach) |
| Schwarzwald-Baar-Kreis | `08326` | `schwarzwald-baar-kreis` | [schwarzwald-baar-kreis](https://energiemonitor.de/schwarzwald-baar-kreis) |
| Schöngeising | `09179147` | `schoengeising` | [schoengeising](https://energiemonitor.de/schoengeising) |
| Stadt Fürstenfeldbruck | `09179121` | `fuerstenfeldbruck` | [fuerstenfeldbruck](https://energiemonitor.de/fuerstenfeldbruck) |
| Stadtwerke Altdorf | `09574112` | `stadtwerke-altdorf` | [stadtwerke-altdorf](https://energiemonitor.de/stadtwerke-altdorf) |
| Stadtwerke Dorfen | `09177777` | `stadtwerkedorfen` | [stadtwerkedorfen](https://energiemonitor.de/stadtwerkedorfen) |
| Stadtwerke Fürstenfeldbruck | `09179999` | `stadtwerke-fuerstenfeldbruck` | [stadtwerke-fuerstenfeldbruck](https://energiemonitor.de/stadtwerke-fuerstenfeldbruck) |
| Stadtwerke Soest | `05974040` | `stadtwerke-soest` | [stadtwerke-soest](https://energiemonitor.de/stadtwerke-soest) |
| Steindorf | `09771168` | `steindorf-eresried` | [steindorf-eresried](https://energiemonitor.de/steindorf-eresried) |
| strotög | `40111111` | `strotoeg` | [strotoeg](https://energiemonitor.de/strotoeg) |
| Türkenfeld | `09179149` | `tuerkenfeld` | [tuerkenfeld](https://energiemonitor.de/tuerkenfeld) |
| Windach | `09181146` | `windach` | [windach](https://energiemonitor.de/windach) |
| Windpark Wörth Simulation | `09676999` | `ezv-energie-plus-windpark` | [ezv-energie-plus-windpark](https://energiemonitor.de/ezv-energie-plus-windpark) |
| Wörthsee | `09188145` | `woerthsee` | [woerthsee](https://energiemonitor.de/woerthsee) |
### WN — Westenergie AG (`tenantId=2200`)

Dashboard-Basis: `https://dev.westenergie.energiemonitor.de/<regionUrlKey>` — **50** Regionen.

| Gemeinde / Region | `region_code` | URL-Slug | Dashboard |
|---|---|---|---|
| Aldenhoven | `05358004` | `aldenhoven` | [aldenhoven](https://dev.westenergie.energiemonitor.de/aldenhoven) |
| Anröchte | `05974004` | `anroechte` | [anroechte](https://dev.westenergie.energiemonitor.de/anroechte) |
| Arnsberg | `05958004` | `arnsberg` | [arnsberg](https://dev.westenergie.energiemonitor.de/arnsberg) |
| Attendorn | `05966004` | `attendorn` | [attendorn](https://dev.westenergie.energiemonitor.de/attendorn) |
| Bad Wünnenberg | `05774040` | `bad-wuennenberg` | [bad-wuennenberg](https://dev.westenergie.energiemonitor.de/bad-wuennenberg) |
| Balve | `05962008` | `balve` | [balve](https://dev.westenergie.energiemonitor.de/balve) |
| Bergheim | `05362008` | `bergheim` | [bergheim](https://dev.westenergie.energiemonitor.de/bergheim) |
| Bissendorf | `03459012` | `bissendorf` | [bissendorf](https://dev.westenergie.energiemonitor.de/bissendorf) |
| Büren | `05774016` | `bueren` | [bueren](https://dev.westenergie.energiemonitor.de/bueren) |
| Drolshagen | `05966008` | `drolshagen` | [drolshagen](https://dev.westenergie.energiemonitor.de/drolshagen) |
| Düren | `05358008` | `dueren` | [dueren](https://dev.westenergie.energiemonitor.de/dueren) |
| Ense | `05974012` | `ense` | [ense](https://dev.westenergie.energiemonitor.de/ense) |
| Finnentrop | `05966012` | `finnentrop` | [finnentrop](https://dev.westenergie.energiemonitor.de/finnentrop) |
| Gemeinde Erndtebrück | `05970012` | `erndtebrueck` | [erndtebrueck](https://dev.westenergie.energiemonitor.de/erndtebrueck) |
| Gemeinde Wenden | `05966028` | `wenden` | [wenden](https://dev.westenergie.energiemonitor.de/wenden) |
| Hürtgenwald | `05358016` | `huertgenwald` | [huertgenwald](https://dev.westenergie.energiemonitor.de/huertgenwald) |
| Inden | `05358020` | `inden` | [inden](https://dev.westenergie.energiemonitor.de/inden) |
| Jülich | `05358024` | `juelich` | [juelich](https://dev.westenergie.energiemonitor.de/juelich) |
| Kirchhundem | `05966016` | `kirchhundem` | [kirchhundem](https://dev.westenergie.energiemonitor.de/kirchhundem) |
| Kreis Düren | `05358` | `kreis-dueren` | [kreis-dueren](https://dev.westenergie.energiemonitor.de/kreis-dueren) |
| Kreis Soest | `05974` | `kreis-soest` | [kreis-soest](https://dev.westenergie.energiemonitor.de/kreis-soest) |
| Kreuzau | `05358028` | `kreuzau` | [kreuzau](https://dev.westenergie.energiemonitor.de/kreuzau) |
| Langenberg | `05754024` | `langenberg` | [langenberg](https://dev.westenergie.energiemonitor.de/langenberg) |
| Langerwehe | `05358032` | `langerwehe` | [langerwehe](https://dev.westenergie.energiemonitor.de/langerwehe) |
| Lennestadt | `05966020` | `lennestadt` | [lennestadt](https://dev.westenergie.energiemonitor.de/lennestadt) |
| Lichtenau | `05774028` | `lichtenau` | [lichtenau](https://dev.westenergie.energiemonitor.de/lichtenau) |
| Linnich | `05358036` | `linnich` | [linnich](https://dev.westenergie.energiemonitor.de/linnich) |
| Lippetal | `05974024` | `lippetal` | [lippetal](https://dev.westenergie.energiemonitor.de/lippetal) |
| Marienheide | `05374024` | `marienheide` | [marienheide](https://dev.westenergie.energiemonitor.de/marienheide) |
| Merzenich | `05358040` | `merzenich` | [merzenich](https://dev.westenergie.energiemonitor.de/merzenich) |
| Neuenrade | `05962048` | `neuenrade` | [neuenrade](https://dev.westenergie.energiemonitor.de/neuenrade) |
| Nideggen | `05358044` | `nideggen` | [nideggen](https://dev.westenergie.energiemonitor.de/nideggen) |
| Niederzier | `05358048` | `niederzier` | [niederzier](https://dev.westenergie.energiemonitor.de/niederzier) |
| Nörvenich | `05358052` | `noervenich` | [noervenich](https://dev.westenergie.energiemonitor.de/noervenich) |
| OIE EnergieMonitor | `07136363` | `oie` | [oie](https://dev.westenergie.energiemonitor.de/oie) |
| Olpe | `05966024` | `olpe` | [olpe](https://dev.westenergie.energiemonitor.de/olpe) |
| Porta Westfalica | `05770032` | `portawestfalica` | [portawestfalica](https://dev.westenergie.energiemonitor.de/portawestfalica) |
| Reken | `05554044` | `reken` | [reken](https://dev.westenergie.energiemonitor.de/reken) |
| Saarburg-Kell | `072355008` | `saarburg-kell` | [saarburg-kell](https://dev.westenergie.energiemonitor.de/saarburg-kell) |
| Saerbeck | `05566080` | `saerbeck` | [saerbeck](https://dev.westenergie.energiemonitor.de/saerbeck) |
| Schöppingen | `05554052` | `schoeppingen` | [schoeppingen](https://dev.westenergie.energiemonitor.de/schoeppingen) |
| Siegen-Wittgenstein | `05970` | `siegen-wittgenstein` | [siegen-wittgenstein](https://dev.westenergie.energiemonitor.de/siegen-wittgenstein) |
| Stadt Horstmar | `05566024` | `stadt-horstmar` | [stadt-horstmar](https://dev.westenergie.energiemonitor.de/stadt-horstmar) |
| Steinfurt | `05566084` | `steinfurt` | [steinfurt](https://dev.westenergie.energiemonitor.de/steinfurt) |
| Timmendorfer Strand | `01055042` | `timmendorfer-strand` | [timmendorfer-strand](https://dev.westenergie.energiemonitor.de/timmendorfer-strand) |
| Titz | `05358056` | `titz` | [titz](https://dev.westenergie.energiemonitor.de/titz) |
| Uedem | `05154056` | `uedem` | [uedem](https://dev.westenergie.energiemonitor.de/uedem) |
| Verl | `05754044` | `verl` | [verl](https://dev.westenergie.energiemonitor.de/verl) |
| Vettweiß | `05358060` | `vettweiss` | [vettweiss](https://dev.westenergie.energiemonitor.de/vettweiss) |
| Welver | `05974048` | `welver` | [welver](https://dev.westenergie.energiemonitor.de/welver) |
### enviaM — envia Mitteldeutsche Energie AG (`tenantId=2700`)

*Keine Regionen in der API (Stand 2026-05-31).*

