#!/bin/sh

ROOT_DIR=`pwd`

cd $ROOT_DIR/NCG
sed -n -o '/{.*}/p' outChunk.txt
# cat outChunk.txt | grep -o -i '{*}'

# sed -n '/Solution.*starts/,/Solution.*ends/p' parser.log
# sed 's/Solution.*starts/0/g'
# sed 's/Solution.*ends/1/g'
# sed  's/\*//g'
# sed 's/[A-Z]\?[>{}/\]\?//g'
# sed 's/</ /'
# sed 's/  / /g'
# sed 's/ //g'
# sed 's/--/\n/g' > sed_output_dump.txt	