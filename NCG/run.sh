#!/bin/sh

# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

# the directory of this script is the "source tree".
RT_DIR=`pwd`
ROOT_DIR=$RT_DIR/NCG
BIN_DIR=$ROOT_DIR/bin
RES_DIR=$ROOT_DIR/res

config_file='config.xml'
input='input'

#the directory of the dependent packages.
PKG_VAR=np.org.mpp
ALIGN=$PKG_VAR.wordaligner.WordAligner

#-------------------------------------------------------------------------------
# utility functions
#-------------------------------------------------------------------------------

WordAligner() {
	#$input
#     cat $input
#     cp $input $BIN_DIR
    cd $BIN_DIR
    java $PKG_VAR.wordaligner.WordAligner -i $ROOT_DIR/$input -o ./../res/Aligner/output
}

PopTokenizer(){
  cd $BIN_DIR
# java $PKG_VAR.poptokenizer.PopTokenizer -i ./../res/Aligner/output -pop $RES_DIR/PopTokenizer/popList -exp $RES_DIR/PopTokenizer/exceptionWordFile -o $RES_DIR/PopTokenizer/out
java $PKG_VAR.poptokenizer.PopTokenizer ./../res/Aligner/output $RES_DIR/PopTokenizer/popList $RES_DIR/PopTokenizer/exceptionWordFile $RES_DIR/PopTokenizer/out
}

# TnT: Trigrams'n'Tags - Statistical Trigram Tagging - Version 2.2
# (C) 1993 - 2001 Thorsten Brants, thorsten@brants.net

TntCorpus(){
  cd $BIN_DIR/tnt
  ./tnt TntCorpus $RES_DIR/PopTokenizer/out > tntOut.txt  2>/dev/null 
 #  2>&1  is making 2 output and 1 input same
}

Tnt2General(){
  cd $BIN_DIR
  java $PKG_VAR.tnttogeneral.TntToMppFormatConverter -i $BIN_DIR/tnt/tntOut.txt -o $RES_DIR/Chunker/chunkip.txt
}

Chunker() {
  cd $BIN_DIR
  java $PKG_VAR.chunker.Chunker -i $RES_DIR/Chunker/chunkip.txt -r $RES_DIR/Chunker/chunkRules.txt -o $RES_DIR/Chunker/outChunk.txt
  cp $RES_DIR/Chunker/outChunk.txt $ROOT_DIR/outChunk
  cp $RES_DIR/Chunker/chunkip.txt $ROOT_DIR/output
  cat $ROOT_DIR/outChunk >> $ROOT_DIR/tests/chunkOP.txt 
  # cat $RES_DIR/Chunker/chunkip.txt >> $ROOT_DIR/tests/chunkOP.txt 
}

parser(){
	cd $BIN_DIR
	#echo $config_file
	java $PKG_VAR.parser.ConstraintBasedParser -c $ROOT_DIR/$1 -i $ROOT_DIR/outChunk.txt >./../log/waste.log 2>/dev/null 
}

# echo parsing started
WordAligner $1
PopTokenizer
TntCorpus
Tnt2General
Chunker
parser $config_file
# echo parsing ended
# echo 
#echo Note: Look at the parser.log file inside the log directory for complete parse analysis of the given input sentence. 
# echo image files have been generated
