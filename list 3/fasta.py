import argparse
import json
import pickle
import requests
import unittest
import sys

class ProteinSequence:
    """
    Represents a single protein sequence with its identifier.
    """
    def __init__(self, identifier, sequence):
        if not isinstance(identifier, str) or not isinstance(sequence, str):
            raise TypeError("Identifier and sequence must be strings.")
        
        self.identifier = identifier
        self.sequence = sequence

def fasta_id_to_dict(identifier):
    """
    Parses FASTA identifier to extract accession, full_name, and organism.
    """
    if not isinstance(identifier, str):
        raise TypeError("Identifier must be a string.")
    
    try:
        parts = identifier.split("|")
        accession = parts[1]
        
        rest = parts[2]
        name_part = rest.split(" OS=")[0]
        full_name = name_part.split(" ", 1)[1]
        
        os_part = rest.split(" OS=")[1]
        organism = os_part.split(" OX=")[0]
        
        return {
            "accession": accession,
            "full_name": full_name,
            "organism": organism
        }
    except IndexError:
        raise ValueError("Invalid FASTA identifier format.")

def fasta_to_prot_seq(fasta_file):
    """
    Opens a FASTA file and returns a list of ProteinSequence objects.
    """
    if not isinstance(fasta_file, str):
        raise TypeError("File name must be a string.")
    
    sequences = []
    with open(fasta_file, "r") as f:
        lines = f.readlines()
        
    current_id = ""
    current_seq = []
    
    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            if current_id:
                sequences.append(ProteinSequence(current_id, "".join(current_seq)))
            current_id = line
            current_seq = []
        else:
            current_seq.append(line)
            
    if current_id:
        sequences.append(ProteinSequence(current_id, "".join(current_seq)))
        
    return sequences


class TestFasta(unittest.TestCase):
    
    def test_fasta_id_to_dict_valid(self):
        header = ">sp|P02768|ALBU_HUMAN Serum albumin OS=Homo sapiens OX=9606 GN=ALB PE=1 SV=2"
        result = fasta_id_to_dict(header)
        
        self.assertEqual(result["accession"], "P02768")
        self.assertEqual(result["full_name"], "Serum albumin")
        self.assertEqual(result["organism"], "Homo sapiens")
        
    def test_fasta_id_to_dict_invalid_type(self):
        with self.assertRaises(TypeError):
            fasta_id_to_dict(12345)
            
    def test_fasta_id_to_dict_invalid_format(self):
        with self.assertRaises(ValueError):
            fasta_id_to_dict(">zly_format_bez_kresek")

    def test_protein_sequence_creation(self):
        header = ">sp|P02768|ALBU_HUMAN Serum albumin OS=Homo sapiens OX=9606"
        seq = "MKWVTFISLLFLFSSAYSRGVFRR"
        
        obj = ProteinSequence(header, seq)
        self.assertEqual(obj.identifier, header)
        self.assertEqual(obj.sequence, seq)
        
    def test_protein_sequence_invalid_type(self):
        with self.assertRaises(TypeError):
            ProteinSequence(123, "MKWVT")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        unittest.main()
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("--fasta", type=str)
        parser.add_argument("--protein", type=str)
        parser.add_argument("--max_seq", type=int)
        parser.add_argument("--pickle", type=str)
        parser.add_argument("--json", type=str)
        parser.add_argument("--xml", type=str)
        
        args = parser.parse_args()
        
        sequences = []
        
        if args.protein and args.max_seq:
            url = f"https://rest.uniprot.org/uniprotkb/search?query={args.protein}&format=fasta&size={args.max_seq}"
            response = requests.get(url)
            
            with open("temp.fasta", "w") as f:
                f.write(response.text)
                
            sequences = fasta_to_prot_seq("temp.fasta")
            
        elif args.fasta:
            sequences = fasta_to_prot_seq(args.fasta)
            
        data_to_save = []
        for seq in sequences:
            info = fasta_id_to_dict(seq.identifier)
            info["sequence"] = seq.sequence
            data_to_save.append(info)
            
        if args.json:
            with open(args.json, "w") as f:
                json.dump(data_to_save, f, indent=4)
                
        if args.pickle:
            with open(args.pickle, "wb") as f:
                pickle.dump(data_to_save, f)
                
        if args.xml:
            with open(args.xml, "w") as f:
                f.write("<proteins>\n")
                for item in data_to_save:
                    f.write("  <protein>\n")
                    f.write(f"    <accession>{item['accession']}</accession>\n")
                    f.write(f"    <full_name>{item['full_name']}</full_name>\n")
                    f.write(f"    <sequence>{item['sequence']}</sequence>\n")
                    f.write(f"    <organism>{item['organism']}</organism>\n")
                    f.write("  </protein>\n")
                f.write("</proteins>\n")
