#!/bin/bash

MAC=33-04-E7-92-52-BD

for rep in 10 15 20 25 30 35
do
    for str in 10 15 20 25 30 35
    do 

         matlab -nodisplay -nodesktop -nosplash -r "s1_LTE_RWF_dataset($rep, $str); exit;"

         python3 s2_BuildTrainCNN.py $rep $str

         A=$(grep ${MAC} ${rep}x${str}_ue_rwf_parm.asc | awk '{ print $2 }')
         B=$(grep ${MAC} ${rep}x${str}_ue_rwf_parm.asc | awk '{ print $3 }')
         C=$(grep ${MAC} ${rep}x${str}_ue_rwf_parm.asc | awk '{ print $4 }')
         D=$(grep ${MAC} ${rep}x${str}_ue_rwf_parm.asc | awk '{ print $5 }')
         J=$(grep ${MAC} ${rep}x${str}_ue_rwf_parm.asc | awk '{ print $6 }')
         K=$(grep ${MAC} ${rep}x${str}_ue_rwf_parm.asc | awk '{ print $7 }')

         matlab -nodisplay -nodesktop -nosplash -r "s3_LTE_RWF_test($rep, $str, $A, $B, $C, $D, $J, $K); exit;"

         python3 s4_MatchUEbyRWF.py $rep $str > ${rep}x${str}_ue_rwf_match.log

    done
done

