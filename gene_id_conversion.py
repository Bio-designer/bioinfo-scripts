# -*- coding: utf-8 -*-
"""
 @author: Min Dai
 @created on 03,Apr, 2018
 @ide: PyCharm Community Edition
"""


import mygene
import sys

##This script mainly used MyGeneInfo to convert gene symbols to gene Entrez IDs.
##Returns only gene symbols and their corresponding IDs if thier Entrez IDs are available.
##If there are more than one Entrez IDs for a given gene symbol, only the first one found will be output.
##sys.argv[1] is for input gene list (symbol), i.e., your_path/genelist.txt
##sys.argv[2] is for output gene list (symbol and ID), i.e., your_path/gene_symbol_to_id.txt


mg = mygene.MyGeneInfo()


###Open the list including gene symbols you want to convert
f = open(sys.argv[1])
line = f.readline()
gen_list = []
while line:
    gen_list.append(line.rstrip())
    line=f.readline()
f.close()


print(len(gen_list))
print(gen_list[0:10])

mgRes=mg.querymany(gen_list, scopes='symbol', fields='entrezgene,symbol',
                   species=9606)

###Set the last symbol converted, in order to delete duplicated symbols.
last_symbol=""

##Your output 
with open(sys.argv[2], 'w') as f4:
    for res in mgRes:
        if('entrezgene' in res):
            ##Judge whether the symbol has already been output once, since there might be more than one entrez gene id for a
            ## given gene symbol. For instance, try 'TEC'
            if(res['query']!=last_symbol):
                f4.write(res['query'])
                f4.write('\t')
                f4.write(str(res['entrezgene']))
                f4.write('\n')
            last_symbol=res['query']

        # else:
        #     print (res['query']+ " not found.")
        # print(query['query'])
        # print(query['_id'])
