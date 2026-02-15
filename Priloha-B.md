# GEOMETRICKÁ PODROBNOST PRVKŮ
**Projekt**: `[Název projektu]`

**Objednatel**: `[Název objednatele]`

**Verze**: V.01

# Obsah

- [Obecné požadavky](#1-obecné-požadavky)
- [Geometrická podrobnost - stavební část](#2-geometrická-podrobnost---stavební-část)
   - [2.1 Zaměřený terén](#21-zaměřený-terén)
   - [2.2 Zemní práce](#22-zemní-práce)
   - [2.3 Základové konstrukce: základové pasy, desky, podkladní beton](#23-základové-konstrukce-základové-pasy-desky-podkladní-beton)
   - [2.4 Základové konstrukce: piloty](#24-základové-konstrukce-piloty)
   - [2.5 Vodorovné nosné konstrukce: desky](#25-vodorovné-nosné-konstrukce-desky)
   - [2.6 Svislé nosné konstrukce](#26-svislé-nosné-konstrukce)
   - [2.7 Svislé nenosné konstrukce: příčky, předstěny](#27-svislé-nenosné-konstrukce-příčky-předstěny)
   - [2.8 Omítky, malby a nátěry](#28-omítky-malby-a-nátěry)
   - [2.9 Obklady](#29-obklady)
   - [2.10 Trámy](#210-trámy)
   - [2.11 Překlady](#211-překlady)
   - [2.12 Sloupy, hlavice sloupů](#212-sloupy-hlavice-sloupů)
   - [2.13 Podlahy](#213-podlahy)
   - [2.14 Podhledy](#214-podhledy)
   - [2.15 Výplně otvorů (dveře, okna)](#215-výplně-otvorů-dveře-okna)
   - [2.16 Výrobky (zámečnické, klempířské, truhlářské a jiné)](#216-výrobky-zámečnické-klempířské-truhlářské-a-jiné)
   - [2.17 Střechy](#217-střechy)
   - [2.18 Prostupy](#218-prostupy)
- [Geometrická podrobnost - stavební část](#3-geometrická-podrobnost---stavební-část)
   - [3.1 Potrubní a trubní vedení](#31-potrubní-a-trubní-vedení)
   - [3.2 Mechanické zařízení a koncové elementy](#32-mechanické-zařízení-a-koncové-elementy)
   - [3.3 Zdravotně technické instalace](#33-zdravotně-technické-instalace)
   - [3.4 Kabelové vedení](#34-kabelové-vedení)

# 1. Obecné požadavky

Každý prvek modelu je vztažen ke konkrétnímu podlaží, kterému funkčně či prostorově přísluší. Požadavky nastavení podlaží viz [7.3 Podlaží](EIR.md#73-podlaží). Podlahové a stropní konstrukce jsou vždy součástí podlaží, ve kterém se nachází jejich horní povrch (konstrukce, po kterých se ve skutečnosti bude chodit, náleží vždy do příslušného podlaží); jsou-li součástí takových konstrukcí samostatně modelované trámy, průvlaky či hlavice, jsou vztaženy do nižšího podlaží. Konstrukce procházející přes více podlaží jsou modelovány a exportovány po jednotlivých podlažích. Možný je přesah nepodstatné části konstrukce do navazujícího podlaží (například protažení stěny pod úroveň čisté podlahy na horní úroveň hrubé podlahy, okno nacházející se na rozhraní dvou podlaží atd.). U prvků, kde by dělení po podlažích mohlo působit problémy v rámci vykazování po jednotlivých systémech (stoupací potrubí atd.), je nutno předem odsouhlasit a zaznamenat výjimky z jednotlivých požadavků (hrozí nebezpečí nezahrnutí takových prvků například při detekci kolizí v případě zobrazení modelu filtrovaného v rozsahu konkrétního podlaží, do prvek není vztažen).

Každý prvek modelu obsahuje informaci o stavebním a/nebo povrchovém materiálu. U konstrukcí, kde je více materiálů (výplně otvorů apod.) bude každá položka rozdělena zvlášť. U prvků, kde je na straně Dodavatele pochybnost o způsobu dělení, musí Dodavatel předložit návrh na rozdělení ke schválení.

# 2. Geometrická podrobnost – stavební část

## 2.1 Zaměřený terén
Model obsahuje geodetické zaměření terénu v podobě jednolité plochy, nebo objemu.

## 2.2	Zemní práce

Model obsahuje základní prostorové nároky na výkopy dle návrhu daného stupně.

## 2.3	Základové konstrukce: základové pasy, desky, podkladní beton

Model obsahuje konstrukce v návrhové tloušťce a půdorysném rozměru.

## 2.4	Základové konstrukce: piloty

V modelu musí být možno identifikovat horní a dolní hranu konstrukce. Model obsahuje konstrukce v návrhových rozměrech. Horní hrana piloty je ukončena na spodní hraně návazné konstrukce (patka, deska apod.).

## 2.5	Vodorovné nosné konstrukce: desky

Model obsahuje konstrukce v návrhové tloušťce a půdorysném rozměru.

**Požadavky pro detailní a výrobní podrobnost**

U konstrukcí sestávajících z více vrstev model obsahuje samostatné vrstvy s uvedením požadovaných informací (materiál, nosná/nenosná konstrukce); v případě, kdy modelovací nástroj umožňuje vytvářet konstrukce sestávající z jednotlivých vrstev, kterým lze přiřadit vlastnosti a toto rozdělení zohlednit při exportu do formátu `.ifc`, lze konstrukce modelovat jako sendvičové.

## 2.6	Svislé nosné konstrukce

Model obsahuje konstrukce v návrhové tloušťce a půdorysném rozměru.

**Požadavky pro detailní a výrobní podrobnost**

Usazení stěn odpovídá skutečnému osazení na konstrukce. U konstrukcí sestávajících z více vrstev model obsahuje samostatné vrstvy s uvedením požadovaných informací (materiál, nosná/nenosná konstrukce atd.); v případě, kdy modelovací nástroj umožňuje vytvářet konstrukce sestávající z jednotlivých vrstev, kterým lze přiřadit vlastnosti a toto rozdělení zohlednit při exportu do formátu `.ifc`, lze konstrukce modelovat jako sendvičové.

## 2.7	Svislé nenosné konstrukce: příčky, předstěny

Svislé nenosné konstrukce musí být modelovány po podlažích.

**Požadavky pro detailní a výrobní podrobnost**

Usazení příček odpovídá skutečnému osazení na konstrukce. U konstrukcí sestávajících z více vrstev model obsahuje samostatné vrstvy s uvedením požadovaných informací (materiál, nosná/nenosná konstrukce); v případě, kdy modelovací nástroj umožňuje vytvářet konstrukce sestávající z jednotlivých vrstev, kterým lze přiřadit vlastnosti a toto rozdělení zohlednit při exportu do formátu `.ifc`, lze konstrukce modelovat jako sendvičové.

## 2.8	Omítky, malby a nátěry

**Požadavky pro symbolickou a obecnou podrobnost**

Model nemusí obsahovat omítky, malby a nátěry.

**Požadavky pro detailní a výrobní podrobnost**

Z digitálního modelu stavby musí být možno automaticky vykazovat omítky, malby a nátěry. Konkrétní způsob vykazování (modelování vrstev omítek, vykazování pomocí povrchové úpravy konstrukcí atd.) bude navržen dodavatelem a odsouhlasen objednatelem a uveden v dodatcích a změnách projektových metod a postupů pro vytváření informací v rámci `Plán realizace BIM (BEP)`.

## 2.9	Obklady

**Požadavky pro symbolickou a obecnou podrobnost**

Model nemusí obsahovat obklady.

**Požadavky pro detailní a výrobní podrobnost**

Model obsahuje obklady jako samostatnou vrstvu. Není nutné zobrazit spárořez. V případě, kdy modelovací nástroj umožňuje vytvářet konstrukce sestávající z jednotlivých vrstev, kterým lze přiřadit vlastnosti a toto rozdělení zohlednit při exportu do formátu `.ifc`, lze modelovat jako sendvičovou konstrukci včetně obkladu.

## 2.10	Trámy

Pokud je trám v průniku s nosnou deskou, horní hrana trámu je ukončena s horní hranou desky. Objem trámu bude odečten od objemu všech navazujících konstrukcí.

## 2.11	Překlady

**Požadavky pro symbolickou a obecnou podrobnost**

Model nemusí obsahovat překlady ve stěnách.

**Požadavky pro detailní a výrobní podrobnost**

Model obsahuje překlad v reálných vnějších rozměrech a ve skutečném umístění (včetně přesahů na uložení). Objem překladu je odečten od konstrukcí, ve kterých se nachází.

## 2.12	Sloupy, hlavice sloupů

Model obsahuje sloupy včetně hlavic v návrhových rozměrech. V návaznosti na stropní konstrukci bude horní hrana hlavice sloupů shodná s horní hranou desky. Objem hlavice bude odečten od objemu stropní desky.

## 2.13	Podlahy

**Požadavky pro symbolickou a obecnou podrobnost**

Model nemusí obsahovat podlahy, obsahuje stropní desky v tloušťce včetně podlahy.

**Požadavky pro detailní a výrobní podrobnost**

Podlaha musí být dělena po místnostech a půdorysně umístěna dle skutečného provedení (pod dveřmi, v nikách apod.) U konstrukcí sestávajících z více vrstev model obsahuje samostatné vrstvy s uvedením požadovaných informací (materiál, nosná/nenosná konstrukce atd.); v případě, kdy modelovací nástroj umožňuje vytvářet konstrukce sestávající z jednotlivých vrstev, kterým lze přiřadit vlastnosti a toto rozdělení zohlednit při exportu do formátu `.ifc`, lze konstrukce modelovat jako sendvičové.

## 2.14	Podhledy

**Požadavky pro symbolickou a obecnou podrobnost**

Model nemusí obsahovat podhledy, obsahuje stropní desky v tloušťce včetně podhledů.

**Požadavky pro detailní a výrobní podrobnost**

Model obsahuje vlastní podhled a vodorovnou nosná konstrukci podhledu (není nutné modelovat závěsy). Model neobsahuje vzduchovou mezeru nad podhledem (ve formě materiálu); vzduchová mezera není modelovaná nebo je zanedbaná při exportu do formátu `.ifc`.

## 2.15	Výplně otvorů (dveře, okna)

Prvky musí odpovídat skutečným reálným stavebním rozměrům otvorů. Členění výplně bude odpovídat skutečnosti.

**Požadavky pro detailní a výrobní podrobnost**

Hlavní rozměry rámů budou odpovídají skutečnosti. Vnější a vnitřní parapety, stínicí prvky a další doplňky mohou být součástí prvků výplní otvorů, avšak výplně otvorů musí umožňovat vykázání a navázání informací týkajících se doplňků. Některé doplňkové části výplně otvorů nemusí být součástí modelu (vložky dveří apod.), avšak geometrický významné položky, které jsou důležité pro vykazování, vzhled a funkci (kukátko, madlo, klika apod.), musí být součástí prvků a dle skutečnosti.

## 2.16	Výrobky (zámečnické, klempířské, truhlářské a jiné)

Všechny délkové výrobky jsou modelovány ve skutečných velikostech (např. oplechování apod.). Kusové výrobky jsou modelovány ve zjednodušených vnějších geometrických rozměrech.
U výrobků neexportovaných do formátu `.ifc` a vykazovaných přímo z návrhové aplikace mohou být použity zástupné 2D symboly. 

## 2.17	Střechy

Střecha je v požadované tloušťce, rozměru a spádu. 

**Požadavky pro detailní a výrobní podrobnost**

Jsou modelovány všechny návazné vrstvy (např. zateplení apod.). U konstrukcí sestávajících z více vrstev model obsahuje samostatné vrstvy s uvedením požadovaných informací (materiál, nosná/nenosná konstrukce atd.); v případě, kdy modelovací nástroj umožňuje vytvářet konstrukce sestávající z jednotlivých vrstev, kterým lze přiřadit vlastnosti a toto rozdělení zohlednit při exportu do formátu `.ifc`, lze konstrukce modelovat jako sendvičové.

## 2.18	Prostupy

**Požadavky pro detailní podrobnost**

Jsou modelovány svislé a vodorovné prostupy nosnými konstrukcemi v reálných pozicích a velikostech. Prostupy musí jasně definovat statický a stavební otvor.

**Požadavky pro výrobní podrobnost**

Jsou modelovány svislé a vodorovné prostupy nosnými i nenosnými konstrukcemi v reálných pozicích a velikostech. Prostupy musí jasně definovat statický a stavební otvor.

# 3. Geometrická podrobnost – profese

## 3.1	Potrubní a trubní vedení

Součástí modelu jsou všechny potrubní systémy, které jsou na sebe napojeny dle vnitřních standardů modelovacího programu. Není přípustné mít napojení jednotlivých prvků „na sraz“, tzn., musí být využito principu napojení modelovacího nástroje. Zařízení umístěné na potrubí může být modelováno zjednodušeně, musí ale mít reálné vnější rozměry a musí být definován servisní prostor, který musí zůstat volný pro přístup k zařízení (stanovení servisního prostoru je důležité pro vyhodnocení bezkolizního stavu). 

Vedení je možné modelovat bez přírub s výjimkou kolizních bodů. Model obsahuje potrubí bez izolace a izolaci samostatně. Model nemusí obsahovat závěsy a další kotvicí a vynášecí prvky.

## 3.2	Mechanické zařízení a koncové elementy

Mechanická zařízení (např. VZT jednotky) mohou být modelovány zjednodušeně, ale v reálných vnějších rozměrech. Součástí prvku zařízení je i vyznačení servisního prostoru. Toto vyznačení servisního přístupu musí být součástí definice prvku pro potřeby ověření, že do servisního prostoru nezasahuje jiné vedení aj.

Koncové prvky mohou být modelovány zjednodušeně, ale v reálných vnějších rozměrech a jejich součástí musí být definice servisního prostoru, který musí zůstat volný pro přístup k zařízení. Koncové prvky jsou obsahem modelu příslušné profese; nejsou přípustné duplicitní prvky ve více profesích.

Mechanická zařízení jsou příkladem uzavírací a ovládací armatury, regulační a měřící prvky, ventily, filtry, jednotky systému (např. VZT jednotka), fancoil, topný trám, akumulační nádrž, servopohony, vyústky, čistící kusy, atd.

## 3.3	Zdravotně technické instalace

Splňují výše uvedené podmínky pro potrubí a trubní vedení a mechanická zařízení a koncové prvky. Zařizovací prvky se v modelech profesí nachází v reálných geometrických rozměrech, a do modelu stavebního jsou převzaty. Není přípustné mít duplicitu zařizovacích elementů ve stavebním modelu a v modelech ostatních profesí. 

## 3.4	Kabelové vedení

Samostatné dílčí modely budou odpovídat profesím a struktuře modelu. Modely budou obsahovat hlavní kabelové trasy, všechny osazené prvky (např. rozvodné skříně, zásuvky, vypínače, krabice apod.) a kabelové chráničky. 
Schéma zapojení není třeba řešit v modelovacím nástroji.