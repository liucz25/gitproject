#!/bin/bash

a=20
b=40

val=`expr $a + $b`
echo "a+b : $val"

val=`expr $a - $b`
echo "a-b : $val"

val=`expr $a \* $b`
echo "a*b : $val"

val=`expr $a / $b`
echo "a/b : $val"

val=`expr $a % $b`
echo "a%b : $val"

if [ $a == $b ]
then 
   echo "a == b"
fi


if [ $a != $b ]
then 
   echo "a != b"
fi

