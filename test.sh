#!/bin/bash
rm -rf frames
rm -rf slides
rm answer.txt

mkdir frames
mkdir slides

cd ~/DSAA_PROJECT/Data/Dataset
string=.jpg
declare -a slidearr
declare -a framearr
declare -a dirarr
declare -a donearr
CNT=0
for Dir in *
do
	# echo $Dir
	cd $Dir
	for F in *
	do
		if [[ $F != answer.txt ]]
		then
			fgg=ppt.jpg
			if [[ $F = $fgg ]]
			then
				echo -n ""
			else
				slidearr+=($CNT)
				framearr+=($F)
				dirarr+=($Dir)	
				donearr+=(0)
			fi
		fi	
	done
	CNT=`expr $CNT + 1`
	cd ..
done



C=0
Ci=0
for((i=1;i<=50;i++))
do 
	c=0
	val=$RANDOM
	val=$(($val % 400))
	dg=$((val/4))
	v=~/DSAA_PROJECT/Data/Dataset/
	x=${framearr[$val]}
	y=${dirarr[$val]}
	sl=/
	dot=~
	d=frames
	e=slides
	po=${slidearr[$val]}
	dr=ppt
	cp $v$y$sl$x  $dot$sl$d$sl$C$string
	cp $v$y$sl$dr$string $dot$sl$e$sl$dr$po$string
	echo $C$string $dr$po$string >> ~/answer.txt
	C=`expr $C + 1`
done	

echo $Ci
