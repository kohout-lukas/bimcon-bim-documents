# GEOMETRICKÁ PODROBNOST PRVKŮ
**Projekt**: `[Název projektu]`

**Objednatel**: `[Název objednatele]`

**Verze**: V.01

# Obsah

- [1. Obecné požadavky](#1-obecné-požadavky)
- [2. Úrovně podrobnosti](#2-úrovně-podrobnosti)
   - [2.1. Symbolická podrobnost](#21-symbolická-podrobnost)
   - [2.2. Obecná podrobnost (Objemová reprezentace)](#22-obecná-podrobnost-objemová-reprezentace)
   - [2.3. Detailní podrobnost](#23-detailní-podrobnost)
   - [2.4. Výrobní podrobnost](#24-výrobní-podrobnost)
- [3. Geometrická podrobnost – stavební část](#3-geometrická-podrobnost--stavební-část)
   - [3.1 Zaměřený terén](#31-zaměřený-terén)
   - [3.2 Zemní práce](#32-zemní-práce)
   - [3.3 Základové konstrukce: základové pasy, desky, podkladní beton](#33-základové-konstrukce-základové-pasy-desky-podkladní-beton)
   - [3.4 Základové konstrukce: piloty](#34-základové-konstrukce-piloty)
   - [3.5 Vodorovné nosné konstrukce: desky](#35-vodorovné-nosné-konstrukce-desky)
   - [3.6 Svislé nosné konstrukce](#36-svislé-nosné-konstrukce)
   - [3.7 Svislé nenosné konstrukce: příčky, předstěny](#37-svislé-nenosné-konstrukce-příčky-předstěny)
   - [3.8 Omítky, malby a nátěry](#38-omítky-malby-a-nátěry)
   - [3.9 Obklady](#39-obklady)
   - [3.10 Trámy](#310-trámy)
   - [3.11 Překlady](#311-překlady)
   - [3.12 Sloupy, hlavice sloupů](#312-sloupy-hlavice-sloupů)
   - [3.13 Podlahy](#313-podlahy)
   - [3.14 Podhledy](#314-podhledy)
   - [3.15 Výplně otvorů (dveře, okna)](#315-výplně-otvorů-dveře-okna)
   - [3.16 Výrobky (zámečnické, klempířské, truhlářské a jiné)](#316-výrobky-zámečnické-klempířské-truhlářské-a-jiné)
   - [3.17 Střechy](#317-střechy)
   - [3.18 Prostupy](#318-prostupy)
- [4. Geometrická podrobnost – profese](#4-geometrická-podrobnost--profese)
   - [4.1 Potrubní a trubní vedení](#41-potrubní-a-trubní-vedení)
   - [4.2 Mechanické zařízení a koncové elementy](#42-mechanické-zařízení-a-koncové-elementy)
   - [4.3 Zdravotně technické instalace](#43-zdravotně-technické-instalace)
   - [4.4 Kabelové vedení](#44-kabelové-vedení)

# 1. Obecné požadavky

Každý prvek modelu je vztažen ke konkrétnímu podlaží, kterému funkčně či prostorově přísluší. Požadavky nastavení podlaží viz [7.3 Podlaží](EIR.md#73-podlaží). Podlahové a stropní konstrukce jsou vždy součástí podlaží, ve kterém se nachází jejich horní povrch (konstrukce, po kterých se ve skutečnosti bude chodit, náleží vždy do příslušného podlaží); jsou-li součástí takových konstrukcí samostatně modelované trámy, průvlaky či hlavice, jsou vztaženy do nižšího podlaží. Konstrukce procházející přes více podlaží jsou modelovány a exportovány po jednotlivých podlažích. Možný je přesah nepodstatné části konstrukce do navazujícího podlaží (například protažení stěny pod úroveň čisté podlahy na horní úroveň hrubé podlahy, okno nacházející se na rozhraní dvou podlaží atd.). U prvků, kde by dělení po podlažích mohlo působit problémy v rámci vykazování po jednotlivých systémech (stoupací potrubí atd.), je nutno předem odsouhlasit a zaznamenat výjimky z jednotlivých požadavků (hrozí nebezpečí nezahrnutí takových prvků například při detekci kolizí v případě zobrazení modelu filtrovaného v rozsahu konkrétního podlaží, do prvek není vztažen).

Každý prvek modelu obsahuje informaci o stavebním a/nebo povrchovém materiálu. U konstrukcí, kde je více materiálů (výplně otvorů apod.) bude každá položka rozdělena zvlášť. U prvků, kde je na straně Dodavatele pochybnost o způsobu dělení, musí Dodavatel předložit návrh na rozdělení ke schválení.

# 2. Úrovně podrobnosti

## 2.1. Symbolická podrobnost

Geometrie obsahuje základní tvary nebo značky, které reprezentují funkci bez ohledu na přesný tvar nebo rozměr. Geometrie je zjednodušená, používá se v raných fázích projektu.

## 2.2. Obecná podrobnost (Objemová reprezentace)

Geometrie udává přibližný tvar, velikost, umístění, orientaci, počet, funkci a chování prvků bez vykreslení podrobností (např. bez vykreslení omítek, překladů, jednotlivých vrstev podlah a podhledů). Geometrie nemusí odpovídat skutečnému výrobku, ale prvek je v modelu již konkrétně identifikovatelný. V modelu mohou být využívány zástupné prvky.

## 2.3. Detailní podrobnost

Geometrie velikostí a tvarem zaručuje, že později modelované či realizované prvky budou v rámci či kolem vymezeného prostoru (dle povahy prvku) a budou navazovat na sousední či napojené prvky. Tvar, velikost, umístění, orientace, počet, funkce a chování prvků mohou být stanoveny z modelu, ale může u nich dojít k dalšímu zpřesnění.

V případě modelů skutečného provedení či existujícího stavu je stanovena úroveň přesnosti ≤ 25 mm.

## 2.4. Výrobní podrobnost

Geometrie slouží k jednoznačnému a přesnému určení tvaru, rozměrů a provedení stavebních prvků, a její přesnost musí odpovídat nárokům daného výrobního nebo montážního procesu tak, aby bylo zajištěno správné provedení a návaznost jednotlivých dílů při realizaci stavby. Geometrie velikostí a tvarem zaručuje, že realizované prvky budou navazovat na sousední či napojené prvky. Tvar, velikost, umístění, orientace, počet, funkce a chování prvků je modelováno v nejvyšší podrobnosti.

V případě modelů výrobní dokumentace je podrobnost obdobná jako podrobnost požadovaná pro 2D výrobní dokumentaci a odpovídá aktuálně platným normovým tolerancím a přesnostem stanoveným pro jednotlivé typy konstrukcí.

# 3. Geometrická podrobnost – stavební část

## 3.1 Zaměřený terén
Model obsahuje geodetické zaměření terénu v podobě jednolité plochy, nebo objemu.

## 3.2	Zemní práce

Model obsahuje základní prostorové nároky na výkopy dle návrhu daného stupně.

## 3.3	Základové konstrukce: základové pasy, desky, podkladní beton

Model obsahuje konstrukce v návrhové tloušťce a půdorysném rozměru.

## 3.4	Základové konstrukce: piloty

V modelu musí být možno identifikovat horní a dolní hranu konstrukce. Model obsahuje konstrukce v návrhových rozměrech. Horní hrana piloty je ukončena na spodní hraně návazné konstrukce (patka, deska apod.).

## 3.5	Vodorovné nosné konstrukce: desky

Model obsahuje konstrukce v návrhové tloušťce a půdorysném rozměru.

#### Požadavky pro detailní a výrobní podrobnost

U konstrukcí sestávajících z více vrstev model obsahuje samostatné vrstvy s uvedením požadovaných informací (materiál, nosná/nenosná konstrukce); v případě, kdy modelovací nástroj umožňuje vytvářet konstrukce sestávající z jednotlivých vrstev, kterým lze přiřadit vlastnosti a toto rozdělení zohlednit při exportu do formátu `.ifc`, lze konstrukce modelovat jako sendvičové.

## 3.6	Svislé nosné konstrukce

Model obsahuje konstrukce v návrhové tloušťce a půdorysném rozměru.

#### Požadavky pro detailní a výrobní podrobnost

Usazení stěn odpovídá skutečnému osazení na konstrukce. U konstrukcí sestávajících z více vrstev model obsahuje samostatné vrstvy s uvedením požadovaných informací (materiál, nosná/nenosná konstrukce atd.); v případě, kdy modelovací nástroj umožňuje vytvářet konstrukce sestávající z jednotlivých vrstev, kterým lze přiřadit vlastnosti a toto rozdělení zohlednit při exportu do formátu `.ifc`, lze konstrukce modelovat jako sendvičové.

## 3.7	Svislé nenosné konstrukce: příčky, předstěny

Svislé nenosné konstrukce musí být modelovány po podlažích.

#### Požadavky pro detailní a výrobní podrobnost

Usazení příček odpovídá skutečnému osazení na konstrukce. U konstrukcí sestávajících z více vrstev model obsahuje samostatné vrstvy s uvedením požadovaných informací (materiál, nosná/nenosná konstrukce); v případě, kdy modelovací nástroj umožňuje vytvářet konstrukce sestávající z jednotlivých vrstev, kterým lze přiřadit vlastnosti a toto rozdělení zohlednit při exportu do formátu `.ifc`, lze konstrukce modelovat jako sendvičové.

## 3.8	Omítky, malby a nátěry

#### Požadavky pro symbolickou a obecnou podrobnost

Model nemusí obsahovat omítky, malby a nátěry.

#### Požadavky pro detailní a výrobní podrobnost

Z digitálního modelu stavby musí být možno automaticky vykazovat omítky, malby a nátěry. Konkrétní způsob vykazování (modelování vrstev omítek, vykazování pomocí povrchové úpravy konstrukcí atd.) bude navržen dodavatelem a odsouhlasen objednatelem a uveden v dodatcích a změnách projektových metod a postupů pro vytváření informací v rámci `Plán realizace BIM (BEP)`.

## 3.9	Obklady

#### Požadavky pro symbolickou a obecnou podrobnost

Model nemusí obsahovat obklady.

#### Požadavky pro detailní a výrobní podrobnost

Model obsahuje obklady jako samostatnou vrstvu. Není nutné zobrazit spárořez. V případě, kdy modelovací nástroj umožňuje vytvářet konstrukce sestávající z jednotlivých vrstev, kterým lze přiřadit vlastnosti a toto rozdělení zohlednit při exportu do formátu `.ifc`, lze modelovat jako sendvičovou konstrukci včetně obkladu.

## 3.10	Trámy

Pokud je trám v průniku s nosnou deskou, horní hrana trámu je ukončena s horní hranou desky. Objem trámu bude odečten od objemu všech navazujících konstrukcí.

## 3.11	Překlady

#### Požadavky pro symbolickou a obecnou podrobnost

Model nemusí obsahovat překlady ve stěnách.

#### Požadavky pro detailní a výrobní podrobnost

Model obsahuje překlad v reálných vnějších rozměrech a ve skutečném umístění (včetně přesahů na uložení). Objem překladu je odečten od konstrukcí, ve kterých se nachází.

## 3.12	Sloupy, hlavice sloupů

Model obsahuje sloupy včetně hlavic v návrhových rozměrech. V návaznosti na stropní konstrukci bude horní hrana hlavice sloupů shodná s horní hranou desky. Objem hlavice bude odečten od objemu stropní desky.

## 3.13	Podlahy

#### Požadavky pro symbolickou a obecnou podrobnost

Model nemusí obsahovat podlahy, obsahuje stropní desky v tloušťce včetně podlahy.

#### Požadavky pro detailní a výrobní podrobnost

Podlaha musí být dělena po místnostech a půdorysně umístěna dle skutečného provedení (pod dveřmi, v nikách apod.) U konstrukcí sestávajících z více vrstev model obsahuje samostatné vrstvy s uvedením požadovaných informací (materiál, nosná/nenosná konstrukce atd.); v případě, kdy modelovací nástroj umožňuje vytvářet konstrukce sestávající z jednotlivých vrstev, kterým lze přiřadit vlastnosti a toto rozdělení zohlednit při exportu do formátu `.ifc`, lze konstrukce modelovat jako sendvičové.

## 3.14	Podhledy

#### Požadavky pro symbolickou a obecnou podrobnost

Model nemusí obsahovat podhledy, obsahuje stropní desky v tloušťce včetně podhledů.

#### Požadavky pro detailní a výrobní podrobnost

Model obsahuje vlastní podhled a vodorovnou nosná konstrukci podhledu (není nutné modelovat závěsy). Model neobsahuje vzduchovou mezeru nad podhledem (ve formě materiálu); vzduchová mezera není modelovaná nebo je zanedbaná při exportu do formátu `.ifc`.

## 3.15	Výplně otvorů (dveře, okna)

Prvky musí odpovídat skutečným reálným stavebním rozměrům otvorů. Členění výplně bude odpovídat skutečnosti.

#### Požadavky pro detailní a výrobní podrobnost

Hlavní rozměry rámů budou odpovídají skutečnosti. Vnější a vnitřní parapety, stínicí prvky a další doplňky mohou být součástí prvků výplní otvorů, avšak výplně otvorů musí umožňovat vykázání a navázání informací týkajících se doplňků. Některé doplňkové části výplně otvorů nemusí být součástí modelu (vložky dveří apod.), avšak geometrický významné položky, které jsou důležité pro vykazování, vzhled a funkci (kukátko, madlo, klika apod.), musí být součástí prvků a dle skutečnosti.

## 3.16	Výrobky (zámečnické, klempířské, truhlářské a jiné)

Všechny délkové výrobky jsou modelovány ve skutečných velikostech (např. oplechování apod.). Kusové výrobky jsou modelovány ve zjednodušených vnějších geometrických rozměrech.
U výrobků neexportovaných do formátu `.ifc` a vykazovaných přímo z návrhové aplikace mohou být použity zástupné 2D symboly. 

## 3.17	Střechy

Střecha je v požadované tloušťce, rozměru a spádu. 

#### Požadavky pro detailní a výrobní podrobnost

Jsou modelovány všechny návazné vrstvy (např. zateplení apod.). U konstrukcí sestávajících z více vrstev model obsahuje samostatné vrstvy s uvedením požadovaných informací (materiál, nosná/nenosná konstrukce atd.); v případě, kdy modelovací nástroj umožňuje vytvářet konstrukce sestávající z jednotlivých vrstev, kterým lze přiřadit vlastnosti a toto rozdělení zohlednit při exportu do formátu `.ifc`, lze konstrukce modelovat jako sendvičové.

## 3.18	Prostupy

#### Požadavky pro detailní podrobnost

Jsou modelovány svislé a vodorovné prostupy nosnými konstrukcemi v reálných pozicích a velikostech. Prostupy musí jasně definovat statický a stavební otvor.

#### Požadavky pro výrobní podrobnost

Jsou modelovány svislé a vodorovné prostupy nosnými i nenosnými konstrukcemi v reálných pozicích a velikostech. Prostupy musí jasně definovat statický a stavební otvor.

# 4. Geometrická podrobnost – profese

## 4.1	Potrubní a trubní vedení

Součástí modelu jsou všechny potrubní systémy, které jsou na sebe napojeny dle vnitřních standardů modelovacího programu. Není přípustné mít napojení jednotlivých prvků „na sraz“, tzn., musí být využito principu napojení modelovacího nástroje. Zařízení umístěné na potrubí může být modelováno zjednodušeně, musí ale mít reálné vnější rozměry a musí být definován servisní prostor, který musí zůstat volný pro přístup k zařízení (stanovení servisního prostoru je důležité pro vyhodnocení bezkolizního stavu). 

Vedení je možné modelovat bez přírub s výjimkou kolizních bodů. Model obsahuje potrubí bez izolace a izolaci samostatně. Model nemusí obsahovat závěsy a další kotvicí a vynášecí prvky.

## 4.2	Mechanické zařízení a koncové elementy

Mechanická zařízení (např. VZT jednotky) mohou být modelovány zjednodušeně, ale v reálných vnějších rozměrech. Součástí prvku zařízení je i vyznačení servisního prostoru. Toto vyznačení servisního přístupu musí být součástí definice prvku pro potřeby ověření, že do servisního prostoru nezasahuje jiné vedení aj.

Koncové prvky mohou být modelovány zjednodušeně, ale v reálných vnějších rozměrech a jejich součástí musí být definice servisního prostoru, který musí zůstat volný pro přístup k zařízení. Koncové prvky jsou obsahem modelu příslušné profese; nejsou přípustné duplicitní prvky ve více profesích.

Mechanická zařízení jsou příkladem uzavírací a ovládací armatury, regulační a měřící prvky, ventily, filtry, jednotky systému (např. VZT jednotka), fancoil, topný trám, akumulační nádrž, servopohony, vyústky, čistící kusy, atd.

## 4.3	Zdravotně technické instalace

Splňují výše uvedené podmínky pro potrubí a trubní vedení a mechanická zařízení a koncové prvky. Zařizovací prvky se v modelech profesí nachází v reálných geometrických rozměrech, a do modelu stavebního jsou převzaty. Není přípustné mít duplicitu zařizovacích elementů ve stavebním modelu a v modelech ostatních profesí. 

## 4.4	Kabelové vedení

Samostatné dílčí modely budou odpovídat profesím a struktuře modelu. Modely budou obsahovat hlavní kabelové trasy, všechny osazené prvky (např. rozvodné skříně, zásuvky, vypínače, krabice apod.) a kabelové chráničky. 
Schéma zapojení není třeba řešit v modelovacím nástroji.