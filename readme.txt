sudo /usr/local/bin/singularity build --sandbox --force Casync casync.def

sudo /usr/local/bin/singularity build Casync.img Casync/

casync make app.caibx ProteinPrepare
casync extract gerard@computer05:/home/gerard/test/test/app.caibx ProteinPrepare
