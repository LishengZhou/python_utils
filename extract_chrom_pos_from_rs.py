## Created by:	Lisheng Zhou
## Date:		15JUN2018
## Purpose:		Extract chrom/pos from rs # 
##              dbsnp144, build 38
## =================================================

## ************* NOTE ******************************
## This script should be run in virtualenv with these installed:
# pip install six
# pip install cruzdb
# pip install sqlalchemy
# pip install mysql-python
## *************************************************

from cruzdb import Genome
import sys

fname = "variants_rs.csv"
outfile = open('chrom_pos.table', 'w')

lines = [line.rstrip('\r\n') for line in open(fname, "r")]
for rs in lines:
	if rs.startswith("rs"):
		var_info = Genome('hg38').snp144.filter_by(name=rs).first()
		if var_info is not None:
			outputstring = str(var_info.chrom.split("chr")[1]) + "\t" + str(var_info.chromStart+1) + "\n"
			outfile.write(outputstring)
		else:
			outfile.write(str("Caution:"+rs+"\n"))

outfile.close()
