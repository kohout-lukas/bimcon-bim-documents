# PŘEDBĚŽNÝ PLÁN REALIZACE BIM (PRE-BEP)
**Projekt**: `[Název projektu]`

**Objednatel**: `[Název objednatele]`

**Dodavatel**: `[Název dodavatele]`

**Verze**: V.01

# Obsah

- [1. Úvod](#1-úvod)
  - [1.1. Pojmy a zkratky](#11-pojmy-a-zkratky)
  - [1.2. Použité normy](#12-použité-normy)
- [2. Funkce a odpovědnosti při managementu informací BIM](#2-funkce-a-odpovědnosti-při-managementu-informací-bim)
  - [2.1. Funkce a odpovědnosti na straně objednatele](#21-funkce-a-odpovědnosti-na-straně-objednatele)
  - [2.2. Funkce a odpovědnosti na straně dodavatele](#22-funkce-a-odpovědnosti-na-straně-dodavatele)
- [3. Strategie sdružování a struktura členění](#3-strategie-sdružování-a-struktura-členění)
  - [3.1. Stavební objekty (provozní soubory, inženýrské objekty)](#31-stavební-objekty-provozní-soubory-inženýrské-objekty)
  - [3.2. Profesní části projektu](#32-profesní-části-projektu)
- [4. Vysokoúrovňová matice odpovědnosti](#4-vysokoúrovňová-matice-odpovědnosti)
- [5. Přístup realizačního týmu k plnění požadavků EIR](#5-přístup-realizačního-týmu-k-plnění-požadavků-eir)
  - [5.1. Základní bod digitálních modelů stavby](#51-základní-bod-digitálních-modelů-stavby)
- [6. Dodatky a změny projektového informačního standardu](#6-dodatky-a-změny-projektového-informačního-standardu)
- [7. Dodatky a změny projektových metod a postupů pro vytváření informací](#7-dodatky-a-změny-projektových-metod-a-postupů-pro-vytváření-informací)
- [8. Rozpis nasazení software](#8-rozpis-nasazení-software)
  - [8.1. Řešení pro společné datové prostředí (CDE)](#81-řešení-pro-společné-datové-prostředí-cde)
  - [8.2. Ostatní digitální nástroje](#82-ostatní-digitální-nástroje)

# 1. Úvod

Tento dokument je určen k řízení tvorby projektu metodou BIM, k popsání konkrétních kroků k naplnění cílů a očekávání. Dokument navazuje na [dokument EIR](EIR.md) a popisuje konkrétní kroky k jejich naplnění na straně dodavatele.

Předběžný plán realizace BIM (PRE-BEP) obsahuje:

- jména osob, kteří budou plnit funkce při managementu informací jménem realizačního týmu;
- strategii předávání informací realizačního týmu obsahující:
  - přístup realizačního týmu k plnění požadavků na výměnu informací;
  - přehled o složení realizačního týmu ve formě jednoho nebo více úkolových týmů;
- strategii sdružování, kterou bude realizační tým uplatňovat;
- vysokoúrovňovou matici odpovědnosti realizačního týmu obsahující rozdělení odpovědností za každou součást informačního modelu a klíčové výstupy spojené s těmito součástmi;
- jakékoliv navržené dodatky nebo změny projektových metod a postupů pro vytváření informací, které realizační tým požaduje pro umožnění efektivity při:
  - zachycení existujících informací o aktivu;
  - tvoření, přezkoumávání, schvalování nebo autorizování informací;
  - zabezpečení a distribuci informací; a
  - předávání informací;
- jakékoliv navržené dodatky nebo změny projektového informačního standardu, které realizační tým požaduje pro umožnění efektivity při:
  - výměně informací mezi úkolovými týmy;
  - distribuci informací externím stranám; nebo
- navržený rozpis nasazení software (včetně verzí), hardware a IT infrastruktury, které realizační tým zamýšlí používat.

## 1.1. Pojmy a zkratky

| **Pojem / Zkratka** | **Definice** |
|---|---|
| **Dodavatel** | Strana uvedená ve smlouvě, která nabízí poskytnutí dodávek, služeb nebo stavebních prací a je Dodavatelem dle zákona. Dodavatel je vedoucí pověřenou stranou dle ČSN EN ISO 19650. |
| **Objednatel** | Strana uvedená ve smlouvě, která přijala nabídku zhotovitele a je zadavatelem podle zákona o zadávání veřejných zakázek. Objednatel je pověřující stranou dle ČSN EN ISO 19650. |
| **Koordinátor BIM** | Osoba na straně dodavatele odpovědná za kontrolu plnění požadavků na informace v rámci managementu informací s využitím metody BIM. |
| **Projektový manažer BIM** | Osoba na straně objednatele odpovědná za kontrolu plnění požadavků na informace v rámci managementu informací s využitím metody BIM. |
| **Projektový tým** | Všechny osoby účastnící se projektu na straně objednatele, dodavatele a subdodavatelů. |
| **Realizační tým** | Všechny osoby účastnící se na projektu na straně zhotovitele a jeho subdodavatelů. V rámci projektového týmu je jeden nebo více realizačních týmů. |
| **Správce datového prostředí** | Osoba na straně objednatele odpovědná za správu a provoz společného datového prostředí (CDE). |
| **Subdodavatel / Podzhotovitel** | Strana poskytující dodávky Dodavateli. Subdodavatel je pověřenou stranou podle ČSN EN ISO 19650. |
| **Úkolový tým** | Všechny osoby účastnící se na projektu na straně jednoho subdodavatele. V rámci realizačního týmu je zpravidla jeden nebo více úkolových týmů. |
| **BEP** | Plán realizace BIM (BIM Execution Plan). |
| **BIM** | Informační modelování staveb (Building Information Modeling). |
| **BIM protokol** | Dokument, který stanovuje pravidla pro zajištění efektivní výměny dat prostřednictvím digitální platformy CDE v rámci BIM projektu a upravuje práva a povinnosti objednatele, dodavatele a dalších uživatelů. |
| **CDE** | Společné datové prostředí (Common Data Environment). |
| **EIR** | Požadavky na výměnu informací (Exchange Information Requirements); pojem nahradil starší Požadavky objednatele na informace (Employer¨s Information Requirements). |

## 1.2. Použité normy

Tento dokument vychází z částí níže uvedených norem. Je-li se v tomto dokumentu odvoláváno na ustanovení normy, týká se to pouze přímo uvedeného ustanovení, nikoliv celého znění normy.

| **Norma** | **Název** |
|---|---|
| **ČSN EN ISO 19650** | Organizace a digitalizace informací o budovách a inženýrských stavbách včetně informačního modelování staveb (BIM) (soubor norem). |
| **ČSN EN 17817-1** | Informační modelování staveb – Úroveň informačních potřeb – Část 1: Pojmy a principy. |
| **ČSN EN ISO 16739** | Datový formát Industry Foundation Classes (IFC) pro sdílení dat ve stavebnictví a facility managementu. |
| **ČSN EN ISO 12006** | Budovy a inženýrské stavby – Organizace informací o stavbách. |

# 2. Funkce a odpovědnosti při managementu informací BIM

## 2.1. Funkce a odpovědnosti na straně objednatele

| **Role BIM** | **Funkce a odpovědnosti** |
|---|---|
| **Projektový manažer objednatele** | Odpovědnost za dohled nad plněním závazků vyplývajících ze smluvních vztahů se dodavatelem. |
| **Projektový manažer BIM** | Odpovědnost za:<br>- odsouhlasení BEP vytvořeného dodavatelem, odsouhlasení změn BEP;<br>- kontrolu dodržování dokumentu EIR a BEP v rámci projektového týmu;<br>- kontrola předávaných dat dodavatelem dle BEP včetně finální kontroly před předáním;<br>Související služby, jejichž potřeba vznikne v návaznosti na úpravu BEP v průběhu realizace projektu.<br>Aktivní účast při řešení vzniklých problémů a návrh jejich řešení.<br>Zodpovídá přímo projektovému řízení na straně objednatele.<br>Neschvaluje a neprojednává dotazy zhotovitele týkající se technického řešení z hlediska řešení projektu. |
| **Správce datového prostředí** | Správa společného datového prostředí pro celý projektový tým v celém průběhu projektu.<br>Školení uživatelů související s používáním CDE.<br>Odpovědnost za vytváření procesních matic v prostředí CDE. |

#### Kontaktní osoby na straně objednatele

| **Role BIM** | **Organizace** | **Jméno** | **E-mail** |
|---|---|---|---|
| **Projektový manažer BIM** |  |  |  |
| **Správce datového prostředí** |  |  |  |
| **Správce stavby** |  |  |  |

## 2.2. Funkce a odpovědnosti na straně dodavatele

| **Role BIM** | **Funkce a odpovědnosti** |
|---|---|
| **Hlavní inženýr projektu (HIP)** | Řízení projektu na straně dodavatele.<br>Vypracovává projektové standardy, které doplňují chybějící standardy v BEP a předkládá je k odsouhlasení Koordinátorovi BIM.<br>Zodpovídá za správnost projektové dokumentace. |
| **Koordinátor BIM** | Vypracovává BEP dle šablony objednatele;<br>vede projektové týmy dle odsouhlaseného EIR a BEP.<br>Kontroluje naplnění informačních modelů, vyhodnocuje správnosti dat obsažených v informačním modelu a předává projektovému manažerovi BIM.<br>Aktivně předkládá návrhy změn BEP, kontroluje naplňování cílů projektu k milníkům projektu.<br> Odpovídá za propojení jednotlivých modelů na datové bázi a koordinaci informačních modelů. |
| **Vedoucí modelář** | Řídí modeláře v rozsahu definovaném dle BEP.<br>Vytváří projektové standardy, které doplňují chybějící standardy v BEP a předkládá je k odsouhlasení Koordinátorovi BIM.<br>Zodpovídá za správnost informačního modelu za dané profesní části. |
| **Modelář** | Osoba, která vytváří informační model dle vnitřních směrnic dodavatele/subdodavatele a dle BEP. |

#### Kontaktní osoby na straně dodavatele

| **Role BIM** | **Organizace** | **Jméno** | **E-mail** |
|---|---|---|---|
| **Koordinátor BIM** |  |  |  |
| **Hlavní inženýr projektu (HIP)** |  |  |  |

# 3. Strategie sdružování a struktura členění

Dílčí model bude zpracován pro každý stavební objekt (resp. inženýrský objekt, případně provozní soubor) a každou profesní část projektu podle níže uvedené struktury projektu. Další členění v rámci jedné profese na více modelů není nijak limitováno. Modely budou mezi sebou plně zkoordinovány podle [dokumentu EIR](EIR.md).

## 3.1. Stavební objekty (provozní soubory, inženýrské objekty)

| **SO/PS/IO** | **Popis** |
|---|---|
| **SO01** | Hlavní objekt |
|  |  |
|  |  |

*POZN. 1: Tabulku doplní dodavatel dle struktury projektu.*

## 3.2. Profesní části projektu

| **Označení** | **Popis** |
|---|---|
| **AST** | Architektonicko-stavební část |
| **STA** | Stavebně-konstrukční část |
| **VZT** | Vzduchotechnika |
| **RTC** | Rozvody tepla a chladu |
| **ZTI** | Zdravotně-technické instalace |
| **SIL** | Silnoproudá elektrotechnika |
| **SLP** | Slaboproudá elektrotechnika |
| **EPS** | Elektronická požární signalizace |
| **EZS** | Poplachové zabezpečovací a tísňové systémy |
| **EKV** | Vstupní systémy |
| **KAM** | Kamerové systémy |
| **MAR** | Měření a regulace |
| **PBR** | Požárně bezpečnostní řešení stavby |
| **SOZ** | Samočinné odvětrávací zařízení, odvod tepla a kouře |
| **SHZ** | Stabilní hasící systém (nebo GHZ – plynový systém) |
| **POP** | Potrubní pošta |
| **MED** | Medicínské plyny |

*POZN. 1: Tabulku profesních částí projektu aktualizuje dodavatel dle struktury projektu.*

*POZN. 2: V případě chybející zkratky pro označení profesní části v [dokumentu EIR](EIR.md) je nutné o této skutečnosti informovat projektového manažera BIM, který chybějící zkratku doplní.*

# 4. Vysokoúrovňová matice odpovědnosti

Vysokoúrovňová matice odpovědnosti obsahuje odpovědnost jednotlivých úkolových týmů za jednotlivé části dle navržené struktury.

**R** – tým, který úkol vykonává

**A** – tým, který nese konečnou odpovědnost za úkol

**C** – tým, který se podílí na úkolu konzultacemi a poskytuje odborné rady

**I** – tým, který musí být informován

|  | Úkolový tým 1 | Úkolový tým 2 | Úkolový tým 3 | Úkolový tým 4 |
|---|---|---|---|---|
| **SO01** |  |  |  |  |
| ASR | R |  |  |  |
| STA |  | R |  |  |
| VZT |  |  | R |  |
| RTC |  |  | R |  |
| ZTI |  |  |  |  |
| SIL |  |  |  |  |
| SLP |  |  |  |  |
| EPS |  |  |  |  |
| EZS |  |  |  |  |
| **SO02** |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

*POZN. 1: Chybějící matice pro provozní soubory a inženýrské objekty doplní zhotovitel.*

# 5. Přístup realizačního týmu k plnění požadavků EIR

## 5.1. Základní bod digitálních modelů stavby

Základní bod (body) je (jsou) umístěn(y) v *[Zde uvést popis umístění bodu]*

| Označení bodu | Souřadnice X | Souřadnice Y | Souřadnice Z |
|---|---|---|---|
| Základní bod |  |  |  |
|  |  |  |  |
|  |  |  |  |

*POZN. 1: Souřadnice jsou uvedeny v metrech, viz. [kapitola 7.5. dokumentu EIR](EIR.md#75-jednotky-hodnot-veličin).*

# 6. Dodatky a změny projektového informačního standardu

Níže uvedené odsouhlasené dodatky a změny projektového informačního standardu doplňují a nahrazují příslušné znění projektového informačního standardu v [dokumentu EIR](EIR.md).

*[Zde uvést případné dodatky a změny]*

# 7. Dodatky a změny projektových metod a postupů pro vytváření informací

Níže uvedené odsouhlasené dodatky a změny projektových metod a postupů pro vytváření informací doplňují a nahrazují příslušné znění projektových metod a postupů pro vytváření informací v [dokumentu EIR](EIR.md).

*[Zde uvést případné dodatky a změny]*

# 8. Rozpis nasazení software

## 8.1. Řešení pro společné datové prostředí (CDE)

Společné datové prostředí je implementováno na straně objednatele.

*[Zde uvést zvolené řešení CDE.]*

## 8.2. Ostatní digitální nástroje

V průběhu projektu budou používány verze projekčních a modelovacích aplikací, ve kterých byla zahájena práce. V případě potřeby je možné provést aktualizaci na vyšší verze a migraci modelů. Tato aktualizace musí být projednána mezi proejtovým maanžerem BIM koordinátorem BIM a zanesena a schválena v nové verzi tohoto dokumentu.

| **Název aplikace** | **Verze** | **Účel použití** | **Formát** |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |