#!/bin/bash
myname="shi yanlou"
echo $myname
echo ${myname}
echo ${myname}Good
echo $myname Good

readonly myname
myname="miao"
echo ${myname}
