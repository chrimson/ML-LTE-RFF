#!/bin/bash

MAC=33-04-E7-92-52-BD

for rep in 10 15 20 25 30 35
do
    for str in 10 15 20 25 30 35
    do 

         matlab -nodisplay -nodesktop -nosplash -r "s1_LTE_RWF_dataset($rep, $str); exit;"

         python3 s2_BuildTrainCNN.py $rep $str

         PARMS=$(grep ${MAC} ${rep}x${str}_ue_rwf_parm.asc | awk '{ print $2 "," $3 "," $4 "," $5 "," $6 "," $7 }')
         matlab -nodisplay -nodesktop -nosplash -r "s3_LTE_RWF_test($rep, $str, $PARMS); exit;"

         python3 s4_MatchUEbyRWF.py $rep $str > ${rep}x${str}_ue_rwf_match.log

    done
done

