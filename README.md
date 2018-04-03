# bioinfo-scripts



##gene_id_conversion.py 

This script mainly used MyGeneInfo to convert gene symbols to gene Entrez IDs.

Returns only gene symbols and their corresponding IDs if thier Entrez IDs are available.

If there are more than one Entrez IDs for a given gene symbol, only the first one found will be output.

sys.argv[1] is for input gene list (symbol), i.e., your_path/genelist.txt

sys.argv[2] is for output gene list (symbol and ID), i.e., your_path/gene_symbol_to_id.txt
