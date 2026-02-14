import openpyxl
import xml.etree.ElementTree as ET
from xml.dom import minidom
from collections import defaultdict

# Load the Excel file
wb = openpyxl.load_workbook('input/excel/EIR_Příloha A_Projektový datový standard.xlsx', data_only=True)
ws = wb['Projektový datový standard']

# Read data starting from row 3 (after headers) - process all rows
data = []
for row in ws.iter_rows(min_row=3, values_only=True):  # All data rows
    if row[0]:  # If first column has value
        data.append(row)

print(f"Processing {len(data)} rows from Excel...")

# Group properties by ElementCode and IFC class
element_properties = defaultdict(list)

for row in data:
    element_code = row[5]  # ElementCode (Třídicí kód)
    parent_element_name = row[2]  # ParentElementName (Třída stavebního prvku)
    element_name = row[4]  # ElementName (Podtřída stavebního prvku)
    param_group = row[6]   # ParameterGroup (Skupina)
    param_name = row[7]    # ParameterName
    param_desc = row[8]    # ParameterDescription
    data_type = row[9]     # ParameterDataType
    ifc_value_type = row[11]  # IfcValueType
    dsp = row[13]          # DSP:ASR
    dps = row[14]          # DPS:ASR
    dsps = row[15]         # DSPS:ASR
    cafm = row[16]         # CAFM:ASR
    ifc_class = row[17]    # IfcBuildingElement
    ifc_type_class = row[18]  # IfcBuildingElementType
    ifc_predefined_raw = row[19]  # IfcPredefinedType
    ifc_user_defined_raw = row[20]  # IfcUserDefinedType (ObjectType)
    
    # Parse PredefinedType - handle array format [VALUE1;VALUE2;...]
    ifc_predefined = None
    if ifc_predefined_raw:
        predefined_str = str(ifc_predefined_raw).strip()
        # Check if it's an array format
        if predefined_str.startswith('[') and predefined_str.endswith(']'):
            # Multiple values - we'll omit PredefinedType (means any is acceptable)
            ifc_predefined = None
        else:
            # Single value - clean it up
            ifc_predefined = predefined_str.strip()
            # Fix common issues
            if ifc_predefined == 'PADFOOTING':
                ifc_predefined = 'PAD_FOOTING'
            elif ifc_predefined == 'STRIPFOOTING':
                ifc_predefined = 'STRIP_FOOTING'
            elif ifc_predefined == 'CURTAINPANEL':
                ifc_predefined = 'CURTAIN_PANEL'
            elif ifc_predefined == 'FLATROOF':
                ifc_predefined = 'FLAT_ROOF'
    
    # Parse ObjectType (for USERDEFINED PredefinedTypes)
    ifc_object_type = None
    if ifc_user_defined_raw:
        ifc_object_type = str(ifc_user_defined_raw).strip()
        if not ifc_object_type:  # Empty string
            ifc_object_type = None
    
    if element_code and param_name and ifc_class:
        element_properties[element_code].append({
            'parent_element_name': parent_element_name,
            'element_name': element_name,
            'param_name': param_name,
            'param_desc': param_desc,
            'param_group': param_group,
            'data_type': data_type,
            'ifc_value_type': ifc_value_type,
            'ifc_class': ifc_class,
            'ifc_type_class': ifc_type_class,
            'ifc_predefined': ifc_predefined,
            'ifc_object_type': ifc_object_type,
            'milestones': {'DSP': dsp, 'DPS': dps, 'DSPS': dsps, 'CAFM': cafm}
        })

print(f"Found {len(element_properties)} unique ElementCodes")
for code in sorted(element_properties.keys())[:5]:
    print(f"  - {code}: {len(element_properties[code])} properties")

# Create IDS XML structure
ids = ET.Element('ids', {
    'xmlns': 'http://standards.buildingsmart.org/IDS',
    'xmlns:xs': 'http://www.w3.org/2001/XMLSchema',
    'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'xsi:schemaLocation': 'http://standards.buildingsmart.org/IDS http://standards.buildingsmart.org/IDS/1.0/ids.xsd'
})

# Add info section
info = ET.SubElement(ids, 'info')
ET.SubElement(info, 'title').text = 'EIR Projektový datový standard'
ET.SubElement(info, 'copyright').text = 'BIM Consulting s.r.o.'
ET.SubElement(info, 'version').text = '1.0'
ET.SubElement(info, 'description').text = 'Information Delivery Specification generated from EIR_Příloha A_Projektový datový standard.xlsx'
ET.SubElement(info, 'author').text = 'auto-generated'
ET.SubElement(info, 'date').text = '2026-02-14'

# Add specifications
specifications = ET.SubElement(ids, 'specifications')

# Create one specification per ElementCode
for element_code in sorted(element_properties.keys()):
    props = element_properties[element_code]
    
    # Get the IFC class (should be same for all properties of this element)
    ifc_class = props[0]['ifc_class']
    ifc_predefined = props[0]['ifc_predefined']
    ifc_object_type = props[0]['ifc_object_type']
    parent_element_name = props[0]['parent_element_name']
    element_name = props[0]['element_name']
    
    # Create specification name: ElementCode - ParentElementName ElementName
    spec_name = f'{element_code} - {parent_element_name} {element_name}'
    
    spec = ET.SubElement(specifications, 'specification', {
        'name': spec_name,
        'ifcVersion': 'IFC4X3',
        'minOccurs': '0',
        'maxOccurs': 'unbounded'
    })
    
    # Add description
    desc_text = f'Property requirements for element code {element_code}'
    ET.SubElement(spec, 'description').text = desc_text
    
    # Applicability: Filter by ElementCode property (Třídicí kód)
    applicability = ET.SubElement(spec, 'applicability')
    
    # Filter entities that have the ElementCode property with specific value
    property_filter = ET.SubElement(applicability, 'property')
    prop_name = ET.SubElement(property_filter, 'name')
    ET.SubElement(prop_name, 'simpleValue').text = 'Třídicí kód'
    prop_value = ET.SubElement(property_filter, 'value')
    ET.SubElement(prop_value, 'simpleValue').text = element_code
    
    # Requirements: Entity type and properties
    requirements = ET.SubElement(spec, 'requirements')
    
    # Add entity type as requirement
    entity_req = ET.SubElement(requirements, 'entity')
    entity_name = ET.SubElement(entity_req, 'name')
    ET.SubElement(entity_name, 'simpleValue').text = ifc_class
    
    # Add PredefinedType only if it's a single value (not array/multiple options)
    if ifc_predefined:
        predefined = ET.SubElement(entity_req, 'predefinedType')
        ET.SubElement(predefined, 'simpleValue').text = ifc_predefined
    
    # Add ObjectType when PredefinedType is USERDEFINED and ObjectType is specified
    if ifc_predefined == 'USERDEFINED' and ifc_object_type:
        object_type = ET.SubElement(entity_req, 'objectType')
        ET.SubElement(object_type, 'simpleValue').text = ifc_object_type
    
    # Add property requirements
    for prop in props:
        param_name = prop['param_name']
        param_group = prop['param_group']
        data_type = prop['data_type']
        ifc_value_type = prop['ifc_value_type']
        
        # Check if property is required in any milestone
        has_requirement = any(prop['milestones'].get(m) == 'x' for m in ['DSP', 'DPS', 'DSPS', 'CAFM'])
        
        if has_requirement:
            property_elem = ET.SubElement(requirements, 'property', {
                'minOccurs': '0',  # Optional by default, can be made required per project phase
                'maxOccurs': 'unbounded'
            })
            
            # Property name
            prop_name = ET.SubElement(property_elem, 'name')
            ET.SubElement(prop_name, 'simpleValue').text = param_name
            
            # Property set from ParameterGroup column
            if param_group:
                prop_set = ET.SubElement(property_elem, 'propertySet')
                ET.SubElement(prop_set, 'simpleValue').text = param_group
            
            # Value type
            if ifc_value_type:
                value = ET.SubElement(property_elem, 'value')
                ET.SubElement(value, 'simpleValue').text = ifc_value_type

# Convert to string with pretty formatting
def prettify(elem):
    """Return a pretty-printed XML string for the Element without minidom."""
    import xml.etree.ElementTree as ET
    ET.indent(elem, space="  ", level=0)
    return ET.tostring(elem, encoding='unicode', xml_declaration=True)

# Write to file
xml_string = prettify(ids)
output_file = 'output/EIR_Priloha_A_Projektovy_datovy_standard.ids'

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(xml_string)

print(f"\n✓ IDS file created: {output_file}")
print(f"  - Specifications: {len(element_properties)}")
print(f"  - Total properties: {sum(len(props) for props in element_properties.values())}")

# Show sample specification
print("\n" + "="*80)
print("SAMPLE SPECIFICATION (first ElementCode):")
print("="*80)
first_code = sorted(element_properties.keys())[0]
first_props = element_properties[first_code][0]
spec_name = f"{first_code} - {first_props['parent_element_name']} {first_props['element_name']}"
print(f"Specification: {spec_name}")
print(f"ElementCode: {first_code}")
print(f"IFC Class: {first_props['ifc_class']}")
print(f"Properties ({len(element_properties[first_code])}):")
for prop in element_properties[first_code][:8]:
    milestones = ', '.join([k for k, v in prop['milestones'].items() if v == 'x'])
    pset = prop.get('param_group', 'N/A')
    print(f"  - {prop['param_name']} ({prop['data_type']}) - Pset: {pset} - Required in: {milestones}")
