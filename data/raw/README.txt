#
# This file is: http://www.voynich.nu/data/000_README.txt
# Latest update: 13/06/2021
#

The files in this directory, and the subdirectory /beta , are 
related to a general reformating of transliteration files of the 
Voynich MS text.

A new format, called IVTFF (Intermediate Voynich Transliteration
File Format) has been defined, such that it can represent all
existing and publicly available transliteration files in their own 
representation alphabet, in a consistent manner.

For general information see:
http://www.voynich.nu/transcr.html

For more specific information see:
http://www.voynich.nu/extra/transcr_new.html

Reasonably stable files are in the present directory.
Files that are still subject to change, and are being beta-tested,
may be found in subdirectory /beta , which also has its own
README file.

Two tool called 'bitrans' and 'ivtt' are able to read and process all 
files in this format. For these tools see:
http://www.voynich.nu/software/


--------------------------
Contents of this directory
--------------------------

FSG_ivtff_1c.txt
----------------
The original FSG transcription, in IVTFF 1.7 format.
This file is compatible with format version 1.6 and does not yet use the
extensions of format version 1.7.
The file uses the FSG transcription alphabet.


GC_ivtff_0c.txt
----------------
A version of GC's v101 transcription file in the IVTFF 1.7 format.
This file is compatible with format version 1.6 and does not yet use the
extensions of format version 1.7.
Locus ordering is according to the IVTFF convention.


IT_ivtff_0d.txt
---------------
The transcription by Takeshi Takahashi, as included in the interlinear 
file by Jorge Stolfi in 1999, in the IVTFF 1.7 format. 
This file is compatible with format version 1.6 and does not yet use the
extensions of format version 1.7.
It does not use capitalised Eva.


ivtff.xlsx
----------
This excel file provides a count of all locus types per page of the
Voynich MS (first worksheet). On the second worksheet this information
is summarised per quire.
The defintion of the locus types may be found in the IVTFF format
definition (see PDF file described below).
The numbers for the generic types (P, L, C, R) are summed from the
numbers for the complete locus types.


page_vars_ivtff.txt
-------------------
This text file lists all page headers with the definition of the standard
variables. For the meaning of these lines, see the IVTFF format definition.


ThP_folios.txt
--------------
This text file gives the relationship between 'Th.Petersen' page numbers
and the page names. The format is:
 1 space character
 3-character integer: the Petersen page number
 1 space character
 1-character integer: the length (n) of the page name field
 2 space characters
 n-character word: the page name without the leading f.


voyn_101.txt
------------
The original and unmodified v101 transcription file by GC.


ZL_ivtff_1r.txt
---------------
The latest release of the Zandbergen-Landini transcription of 1999 
in the IVTFF 1.7 format. 
This file is compatible with format version 1.6 and does not yet use the
extensions of format version 1.7.
It is a complete transcription, including all 5389 loci that have 
been identified in the MS. It uses the Eva alphabet, including the 
high-ascii extensions.
The file has been corrected in numerous places.
Some parts of the text inside folds of the pages still need to be
added.

