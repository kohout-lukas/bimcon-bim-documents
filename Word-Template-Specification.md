# Specifikace Word šablony pro BIM dokumentaci

**Účel**: Jednotná šablona pro vytváření BIM dokumentů (EIR, PRE-BEP, BIM protokol, Přílohy)

**Verze**: 1.0

**Datum**: 2026-02-14

---

## 1. Základní nastavení stránky

### Formát a okraje
- **Formát papíru**: A4 (210 × 297 mm)
- **Orientace**: Na výšku (portrait)
- **Okraje**:
  - Horní: 2.5 cm
  - Dolní: 2.5 cm
  - Levý: 2.0 cm
  - Pravý: 2.0 cm
  - Záhlaví: 1.25 cm
  - Zápatí: 1.25 cm

### Sekce
- **Titulní stránka**: Vlastní sekce bez záhlaví/zápatí
- **Hlavní obsah**: Standardní záhlaví a zápatí

---

## 2. Titulní stránka

### Struktura

```
[LOGO společnosti - vpravo nahoře]

[Vertikální mezera]

NÁZEV DOKUMENTU
[18pt, Bold, Barva: #003B5C, Zarovnání: střed]

[Mezera]

Projekt: [Název projektu]
[12pt, Bold]

Objednatel: [Název objednatele]
[11pt]

[Vertikální mezera]

Vytvořil: BIM Consulting s.r.o.
Verze: XX
Datum: DD.MM.RRRR

[Dole stránky]
_______________________________________________________
© BIM Consulting s.r.o. | Důvěrné
```

### Formátování titulní stránky
- Žádné záhlaví ani zápatí
- Veškerý text zarovnán na střed kromě loga (vpravo)
- Verze a datum: 10pt, Regular, Barva: #666666

---

## 3. Záhlaví a zápatí

### Záhlaví (kromě titulní stránky)
```
[Název dokumentu nebo projektový kód]          [Stránka X z Y]
_________________________________________________________
```
- **Font**: 9pt, Regular
- **Barva**: #666666
- **Levá část**: Název dokumentu
- **Pravá část**: Číslo stránky (automatické pole)
- **Oddělení**: Tenká čára 0.5pt, #CCCCCC

### Zápatí
```
[BIM Consulting s.r.o.]  [Verze X.X | DD.MM.RRRR]  [Strana X]
```
- **Font**: 9pt, Regular
- **Barva**: #666666
- **Levá část**: Název společnosti + malé logo (volitelně)
- **Střed**: Verze a datum
- **Pravá část**: Číslo stránky

---

## 4. Styly nadpisů

### Nadpis 1 (Heading 1)
```
Nastavení:
- Font: Calibri nebo Arial
- Velikost: 18pt
- Styl: Bold
- Barva: #003B5C (tmavě modrá)
- Mezera před: 18pt
- Mezera za: 12pt
- Číslování: 1., 2., 3.
- Nová stránka: Ne (ponechat za sebou)
```

### Nadpis 2 (Heading 2)
```
Nastavení:
- Font: Calibri nebo Arial
- Velikost: 14pt
- Styl: Bold
- Barva: #005A8C (středně modrá)
- Mezera před: 12pt
- Mezera za: 6pt
- Číslování: 1.1, 1.2, atd.
- Odsazení: 0 cm
```

### Nadpis 3 (Bold text - ne nadpis)
```
Nastavení:
- Font: Calibri nebo Arial
- Velikost: 11pt
- Styl: Bold
- Barva: #333333 (tmavě šedá)
- Mezera před: 6pt
- Mezera za: 3pt
- BEZ číslování
- Odsazení: 0 cm
```

---

## 5. Základní text

### Normální text (Normal)
```
Nastavení:
- Font: Calibri nebo Arial
- Velikost: 11pt
- Styl: Regular
- Barva: #000000
- Řádkování: 1.15
- Zarovnání: Do bloku (justify)
- Mezera před: 0pt
- Mezera za: 6pt
- První řádek: Bez odsazení
```

### Kód / Zástupné symboly (Code)
```
Nastavení:
- Font: Consolas nebo Courier New
- Velikost: 10pt
- Styl: Regular
- Barva: #000000
- Pozadí: #F5F5F5 (světle šedá)
- Okraje: 3pt všude
- Řádkování: 1.0
```

---

## 6. Seznamy

### Odrážkový seznam (Bullet List)
```
Nastavení:
- Symbol: • (modrý kruh #005A8C)
- Odsazení: 1.27 cm
- Řádkování: 1.15
- Mezera mezi položkami: 3pt
```

### Číslovaný seznam (Numbered List)
```
Nastavení:
- Formát: 1., 2., 3. (pro první úroveň)
- Formát: 1.1, 1.2 (pro druhou úroveň)
- Formát: 1.1.1, 1.1.2 (pro třetí úroveň)
- Odsazení: 1.27 cm (první úroveň), +0.64 cm pro každou další
- Řádkování: 1.15
```

---

## 7. Tabulky

### Tabulka - Záhlaví
```
Nastavení:
- Pozadí: #003B5C (tmavě modrá)
- Text: Bílá (#FFFFFF)
- Font: 11pt, Bold
- Zarovnání: Na střed svisle i vodorovně
- Výplň buňky: 5pt všude
```

### Tabulka - Řádky
```
Nastavení:
- Střídání barev:
  - Lichý řádek: Bílá (#FFFFFF)
  - Sudý řádek: Světle šedá (#F8F8F8)
- Text: 10pt, Regular, Barva: #000000
- Okraje buňky: 5pt všude
- Zarovnání: Vlevo (text), Vpravo (čísla)
- Okraje tabulky: 1pt, #CCCCCC
```

### Tabulka - Popisek
```
Nastavení:
- Text: "Tabulka X: [Název]"
- Font: 10pt, Italic
- Barva: #666666
- Umístění: Nad tabulkou
- Mezera za: 6pt
- Automatické číslování: Ano
```

---

## 8. Obsah (Table of Contents)

### Nastavení
```
- Styly: Heading 1, Heading 2, Heading 3 (volitelně)
- Maximální úroveň: 2 nebo 3
- Tečkovaná linka: Ano
- Čísla stránek: Zarovnané vpravo
- Hyperlinky: Ano (aktivní odkazy)
- Formát čísel stránek: Arabské (1, 2, 3)
```

### Formátování obsahu
```
Úroveň 1:
- Font: 12pt, Bold
- Barva: #003B5C
- Odsazení: 0 cm

Úroveň 2:
- Font: 11pt, Regular
- Barva: #000000
- Odsazení: 0.5 cm

Úroveň 3:
- Font: 10pt, Regular
- Barva: #666666
- Odsazení: 1.0 cm
```

---

## 9. Odkazy a křížové odkazy

### Hyperlinky
```
Nastavení:
- Barva: #0078D4 (světle modrá)
- Podtržené: Ano
- Navštívený odkaz: #551A8B (fialová)
```

### Křížové odkazy
```
Formát:
- "viz kapitola X"
- "viz bod X.X"
- "viz Tabulka X"
- "viz Obrázek X"

Styl: Modrý (#0078D4), podtržený, automaticky aktualizovaný
```

---

## 10. Obrázky a schémata

### Obrázek - Popisek
```
Nastavení:
- Text: "Obrázek X: [Název]"
- Font: 10pt, Italic
- Barva: #666666
- Umístění: Pod obrázkem
- Mezera před: 6pt
- Automatické číslování: Ano
- Zarovnání: Na střed
```

### Obrázek - Nastavení
```
- Obtékání textem: Zarovnáno (In line with text)
- Zarovnání: Na střed
- Maximální šířka: 16 cm (ponechat okraje)
```

---

## 11. Barevná paleta

### Primární barvy
```
Tmavě modrá (hlavní):    #003B5C   RGB(0, 59, 92)
Středně modrá:           #005A8C   RGB(0, 90, 140)
Světle modrá (odkazy):   #0078D4   RGB(0, 120, 212)
```

### Sekundární barvy
```
Zelená (úspěch):         #107C10   RGB(16, 124, 16)
Oranžová (upozornění):   #FFB900   RGB(255, 185, 0)
Červená (chyba):         #D13438   RGB(209, 52, 56)
```

### Neutrální barvy
```
Černá (text):            #000000   RGB(0, 0, 0)
Tmavě šedá:              #333333   RGB(51, 51, 51)
Šedá (sekundární text):  #666666   RGB(102, 102, 102)
Světle šedá (pozadí):    #F5F5F5   RGB(245, 245, 245)
Okraje:                  #CCCCCC   RGB(204, 204, 204)
Bílá:                    #FFFFFF   RGB(255, 255, 255)
```

---

## 12. Speciální bloky

### Upozornění / Poznámka
```
Struktur:
┌────────────────────────────────────┐
│ ⚠ POZNÁMKA                         │
│                                    │
│ Text upozornění nebo poznámky...   │
└────────────────────────────────────┘

Nastavení:
- Ohraničení: 2pt, #FFB900 (oranžová)
- Pozadí: #FFF8E1 (velmi světle oranžová)
- Výplň: 10pt všude
- Font: 10pt, Regular
- Ikona: ⚠ (U+26A0)
```

### Důležité informace
```
Struktur:
┌────────────────────────────────────┐
│ ⓘ DŮLEŽITÉ                         │
│                                    │
│ Důležitá informace...              │
└────────────────────────────────────┘

Nastavení:
- Ohraničení: 2pt, #0078D4 (modrá)
- Pozadí: #E3F2FD (velmi světle modrá)
- Výplň: 10pt všude
- Font: 10pt, Regular
- Ikona: ⓘ (U+24D8)
```

---

## 13. Implementace v Microsoft Word

### Postup vytvoření šablony:

1. **Vytvořit nový dokument**
   - Soubor → Nový → Prázdný dokument

2. **Nastavit okraje**
   - Rozložení → Okraje → Vlastní okraje
   - Zadat hodnoty podle specifikace

3. **Vytvořit styly nadpisů**
   - Domů → Styly → Spravovat styly
   - Upravit Heading 1, 2, 3 podle specifikace
   - Nastavit číslování víceúrovňového seznamu

4. **Vytvořit styl Normal**
   - Upravit styl Normal podle specifikace

5. **Vytvořit vlastní styly**
   - Nový styl: "Code" pro kódové bloky
   - Nový styl: "Note" pro poznámky
   - Nový styl: "Important" pro důležité informace

6. **Nastavit záhlaví a zápatí**
   - Vložit → Záhlaví a zápatí
   - Různé záhlaví pro první stránku (titulní list)
   - Vložit pole čísla stránek

7. **Vytvořit styly tabulky**
   - Návrh tabulky → Styly tabulky → Nový styl tabulky
   - Nastavit formátování podle specifikace

8. **Uložit jako šablonu**
   - Soubor → Uložit jako
   - Typ souboru: Word šablona (*.dotx)
   - Název: "BIM_Document_Template.dotx"

---

## 14. Kontrolní seznam

Po vytvoření šablony zkontrolovat:

- [ ] Okraje stránky správně nastaveny
- [ ] Všechny styly nadpisů vytvořeny a formátovány
- [ ] Číslování nadpisů funguje správně (víceúrovňový seznam)
- [ ] Záhlaví a zápatí nastaveny včetně polí
- [ ] Titulní stránka bez záhlaví/zápatí
- [ ] Obsah se generuje automaticky z nadpisů
- [ ] Tabulkové styly vytvořeny
- [ ] Křížové odkazy fungují
- [ ] Barevná schémata odpovídají specifikaci
- [ ] Styly pro seznamy (odrážkové i číslované)
- [ ] Styl pro kódové bloky
- [ ] Styly pro poznámky a upozornění
- [ ] Šablona uložena jako .dotx soubor

---

## 15. Použití šablony

### Pro nový dokument:
1. Otevřít šablonu BIM_Document_Template.dotx
2. Soubor → Uložit jako → Zadat nový název
3. Vyplnit titulní stranu (projekt, objednatel, verze)
4. Začít psát obsah pomocí stylů

### Klávesové zkratky:
- **Nadpis 1**: Ctrl + Alt + 1
- **Nadpis 2**: Ctrl + Alt + 2
- **Normal**: Ctrl + Shift + N
- **Odrážky**: Ctrl + Shift + L
- **Aktualizovat obsah**: Pravý klik na obsah → Aktualizovat pole

---

## 16. Údržba šablony

### Verze šablony:
- Udržovat changelog změn v šabloně
- Verzování: X.Y (major.minor)
- Datum poslední revize

### Aktualizace existujících dokumentů:
1. Otevřít dokument
2. Vývojář → Šablony dokumentu
3. Připojit novou šablonu
4. Aktualizovat styly automaticky

---

**Konec specifikace**

