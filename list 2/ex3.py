class BaseSequence:
    """
    Represents a base biological sequence.

    Attributes:
        identifier (int): Unique identifier of the sequence.
        valid_chars (set): A set of characters allowed in the sequence (defined in subclasses).
    """

    def __init__(self, identifier, data):
        """
        Initializes the base sequence.

        Args:
            identifier (int): Identifier of the sequence.
            data (str): Actual sequence data.

        Raises:
            TypeError: If identifier is not an int or data is not a string.
        """
        if not isinstance(identifier, int):
            raise TypeError("'identifier' must be an int.")
        if not isinstance(data, str):
            raise TypeError("'data' must be a string.")

        self.identifier = identifier
        self.data = data.upper()
        
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        """
        Checks if the character is valid for the sequence.
        """
        for char in value:
            if char not in self.valid_chars:
                raise ValueError("Invalid character in sequence.")
        self._data = value

    def __len__(self):
        """
        Returns the length of the sequence (int).
        """
        return len(self.data)

    def __str__(self):
        """
        Returns the sequence representation in a FASTA-like format.

        Returns:
            str: Formatted sequence string starting with '>' and identifier.
        """
        return f">{self.identifier}\n{self.data}"

    def mutate(self, position, value):
        """
        Modifies sequence data at the given position to the specified value.

        Args:
            position (int): The index at which the sequence will be mutated.
            value (str): The new character to insert at the position.
            
        Raises:
            ValueError: If the new value is not in valid_chars (handled by setter).
        """
        data_list = list(self.data)
        data_list[position] = value
        self.data = "".join(data_list)
        
    def find_motif(self, motif):
        """
        Finds all starting positions of a given motif in the sequence.

        Args:
            motif (str): The substring to search for.

        Returns:
            list: A list of integers representing the starting indices of the motif.
        """
        motifs_list = []
        for i in range(len(self.data) - len(motif) + 1):
            if self.data[i: i + len(motif)] == motif:
                motifs_list.append(i)
        return motifs_list
                
            
class DNASequence(BaseSequence):
    """
    Represents a DNA sequence.
    """
    valid_chars = {"A", "T", "C", "G"}
    
    def complement(self):
        """
        Generates the complementary DNA sequence.

        Returns:
            str: The complementary sequence data.
        """
        DNA_pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}
        
        complement = ""
        for base in self.data:
            complement = complement + DNA_pairs[base]       
            
        return complement 
    
    def transcribe(self):
        """
        Transcribes the DNA sequence into an RNA sequence.

        Returns:
            RNASequence: A new instance representing the transcribed RNA.
        """
        new_rna = self.data.replace("T", "U")
        return RNASequence(self.identifier, new_rna)
    

class RNASequence(BaseSequence):
    """
    Represents an RNA sequence.
    """
    valid_chars = {"A", "U", "C", "G"}
    
    def complement(self):
        """
        Generates the complementary RNA sequence.

        Returns:
            str: The complementary sequence data.
        """
        RNA_pairs = {"A": "U", "U": "A", "C": "G", "G": "C"}
        
        complement = ""
        for base in self.data:
            complement = complement + RNA_pairs[base]       
            
        return complement
        
    def translate(self):
        """
        Translates the RNA sequence into a protein sequence.

        Returns:
            ProteinSequence: A new instance representing the translated protein.
        """
        codons = {
            "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
            "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
            "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
            "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
            "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
            "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
            "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
            "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
            "UAU": "Y", "UAC": "Y", "UAA": "", "UAG": "",
            "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
            "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
            "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
            "UGU": "C", "UGC": "C", "UGA": "", "UGG": "W",
            "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
            "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
            "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
        }
        
        amino_acids = ""
        for i in range(0, len(self.data), 3):
            codon = self.data[i: i+3]
            if codon in codons:
                amino_acids = amino_acids + codons[codon]
                
        return ProteinSequence(self.identifier, amino_acids)
            

class ProteinSequence(BaseSequence):
    """
    Represents a Protein sequence.
    """
    valid_chars = {"A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"}
    

def test_sequences():
    """
    Tests functionality of all functions from sequence classes.
    """
    
    try:
        DNASequence("one", "ATCG")
        assert False
    except TypeError:
        pass
    
    try:
        DNASequence(2, 321)
        assert False
    except TypeError:
        pass
    
    try:
        DNASequence(3, "ABCD")
        assert False
    except ValueError:
        pass
    
    try:
        RNASequence(4, "ATCG")
        assert False
    except ValueError:
        pass
    
    dna1 = DNASequence(5, "ATCGGT")
    assert len(dna1) == 6
    assert str(dna1) == ">5\nATCGGT"
    
    dna1.mutate(5, "A")
    assert dna1.data == "ATCGGA"
    assert dna1.find_motif("TCG") == [1]
    assert dna1.complement() == "TAGCCT"
    
    rna1 = RNASequence(6, "AUCG")
    assert rna1.complement() == "UAGC"
    
    rna2 = RNASequence(7, "AUGGCUUAA")
    protein_test = rna2.translate()
    assert isinstance(protein_test, ProteinSequence)
    assert protein_test.data == "MA"
    
    print("All tests for sequences passed.")
    

if __name__ == "__main__":
    test_sequences()
