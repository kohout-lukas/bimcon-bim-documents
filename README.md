# BIM Documents Repository

This repository contains BIM (Building Information Modeling) documentation templates and tools for Czech construction projects following ČSN EN ISO 19650 standards.

## Documents

### Main Documentation
- **PRE-BEP.md** - Předběžný plán realizace BIM (Pre-BIM Execution Plan)
- **EIR.md** - Požadavky na výměnu informací (Exchange Information Requirements)
- **BIM protokol.md** - BIM Protocol document
- **Priloha-B.md** - Geometrická podrobnost prvků specification

### Templates
- **input/word/PRE_BEP_template.docx** - PRE-BEP Word template
- **input/word/EIR_template.docx** - EIR Word template
- **input/word/PROTOKOL_template.docx** - BIM Protocol Word template

### Supporting Files
- **input/excel/** - Excel data standards for IDS generation
- **images/** - Project diagrams and schemas
- **output/** - Generated Word documents and IDS files

## Tools

### Python Scripts (`scripts/`)

#### Markdown to Word Converter
- `convert_markdown_to_word.py` - Converts markdown documents to Word format using templates
  - Supports headings with automatic bookmarks
  - Internal links and cross-references
  - Tables with custom styling
  - Bullet lists and numbered lists
  - Images and formatting (bold, italic, code)
  - Custom metadata (project name, version, etc.)

#### IDS Validation Tools
- `create_ids.py` - Generates IDS (Information Delivery Specification) files from Excel data standards
  - Validates element classification codes (Třídící kód) with pattern [A-Z]{2}[0-9]{2}
  - Validates identification codes (Identifikační kód) with pattern [A-Z]{2}[0-9]{2}\.[0-9]{2}\.[0-9]{4}
  - Creates specifications for IFC4X3 entities with properties and requirements

## Requirements

```bash
pip install python-docx openpyxl
```

## Usage

### Convert Markdown to Word

```bash
python scripts/convert_markdown_to_word.py
```

This will convert all markdown documents (PRE-BEP.md, EIR.md, BIM protokol.md, Priloha-B.md) to Word format using their respective templates.

### Generate IDS Files

```bash
python scripts/create_ids.py
```

This generates IDS files from the Excel data standard located in `input/excel/`.

## Standards Compliance

All documents follow:
- ČSN EN ISO 19650 - Information management using BIM
- ČSN EN 17817-1 - Level of information need
- ČSN EN ISO 16739 - IFC data format
- ČSN EN ISO 12006 - Organization of information about construction works

## License

Internal use - BIM Consulting s.r.o. project documentation
