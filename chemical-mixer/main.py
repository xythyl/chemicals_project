#!/usr/bin/env python3

from flask import Flask, request, render_template, jsonify
import pubchempy as pcp
import chempy
import json
import wolframalpha as wra

app_id = "42Y669-3A4V8JE46Y"
client = wra.Client(app_id)

app = Flask(__name__)

@app.route('/')
def index():
  #return 'This is the homepage'
  return render_template('index.html')

@app.route('/script', methods=['POST'])
def script():
  return "SCRIPT OK"

@app.route('/search', methods=['GET'])
def search():
  input = request.args.get('cid')
  #something = pcp.Compound.from_cid(input)

  out = jsonify(pcp.Compound.from_cid(input).to_dict(properties=['cid', 'canonical_smiles','isomeric_smiles','iupac_name','inchikey','molecular_formula','molecular_weight','h_bond_donor_count','h_bond_acceptor_count','rotatable_bond_count','exact_mass','heavy_atom_count','charge','complexity','covalent_unit_count']))
  #append chempy result to dict above 
  #out = pcp.Compound.from_cid(input).canonical_smiles

  return out

@app.route('/mix', methods=['GET'])
def mix():
  r1 = request.args.get('chem1')
  r2 = request.args.get('chem2')

  c1 = pcp.Compound.from_cid(r1).molecular_formula
  c2 = pcp.Compound.from_cid(r2).molecular_formula
  
  res = client.query(c1 + " + " + c2)

  out = "Error"

  for pod in res.pods:
    if (pod.title == "Sample reactions"):
      print(c1 + " + "+ c2)
      for sub in pod.subpods:
        out = sub.plaintext
        print(sub.plaintext)
  out = out.replace('\n',"<br>")
  print(out)
  return out

if __name__ == "__main__":
  app.run(debug=True)
