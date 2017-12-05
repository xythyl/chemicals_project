from flask import jsonify
import pubchempy as pcp

import json
'''
def create_json(cid):
  c = pcp.Compound.from_cid(cid)
  output_json = {}
  cas-number = 'CAS-NUMBER'
  pubchem_id = 'PubChem ID'
  canonical_smiles = 'Canonical SMILES'
  isomeric_smiles = 'Isomeric SMILES'
  name = 'name'
  un-number = 'un-number'
  inchi-key = 'InChl-key'
  molecular-formula = 'molecular-formula'
  molecular-weight = 'molecular-weight'
  mesh_synonyms = 'MeSH synonyms'
  h_bond_donor_count = 'Hydrogen Bond Donor Count'
  h_bond_acceptor_count = 'Hydrogen Bond Acceptor Count'
  exact_mass = 'Exact Mass'
  heavy_atom_count = 'Heavy Atom Count'
  formal_charge = 'Formal Charge'
  complexity = 'Complexity'
  covalently_bonded_unit_count = 'Covalently-Bonded Unit Count'
  melting_point = 'Melting Point'
  boiling_point = 'Boiling Point'
  freezing_point = 'Freezing Point'
  chemical_compound = 'Chemical/Compound'
  reaction_group_id = 'Reaction Group ID'

  output_json[cas_number] = get_cas(cid)
  output_json[pubchem_id] =  c.cid
  output_json[canonical_smiles] = c.canonical_smiles
  output_json[isomeric_smiles] = c.isomeric_smiles
  output_json[name] = c.iupac_name
  output_json[un-number] = get_un(cid)
  output_json[ichi-key] =  c.inchikey
  output_json[molecular-formula] = c.molecular_formula
  output_json[molecular-weight] = c.molecular_weight
  output_json[mesh_synonyms] = get_mesh(cid)
  output_json[h_bond_donor_count] = c.h_bond_donor_count
  output_json[h_bond_acceptor_count] =  c.h_bond_acceptor_count
  output_json[exact_mass] = c.exact_mass
  output_json[heavy_atom_count] = c.heavy_atom_count
  output_json[formal_charge] = c.charge
  output_json[complexity] = c.complexity
  output_json[covalently_bonded_unit_count] =  c.covalent_unit_count
  output_json[melting_point] =
  output_json[boiling_point] =
  output_json[freezing_point] =
  output_json[chemical_compound] = 'compound'
  output_json[reaction_group_id] =

  c = pcp.Compound.from_cid(cid)
  output_json[cas-number_label] = c.
'''
list_of_cids = [9032, 11000, 517653, 11590]

data = []
for i in list_of_cids:
  data.append(pcp.Compound.from_cid(i).to_dict(properties=['cid','canonical_smiles',
  'isomeric_smiles','iupac_name','inchikey', 'molecular_formula',
  'molecular_weight','h_bond_donor_count', 'h_bond_acceptor_count',
  'rotatable_bond_count', 'exact_mass', 'heavy_atom_count', 'charge', 'complexity',
  'covalent_unit_count']))

with open ('test.json', 'w') as f:
  f.write(json.dumps(data, sort_keys=True, indent=4))
  '''json.dump(data, f)'''

'''
  json.dumps(output, sort_keys=True, indent=4, separators=(',',':'))\
'''

'''
def format_json():
  output_json = {}
  cas-number_label = 'CAS-NUMBER'
  pubchem_id_label = 'PubChem ID'
'''
