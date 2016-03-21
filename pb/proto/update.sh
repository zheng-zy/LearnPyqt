#!/usr/bin/sh

protoc --python_out=/home/otdev/code/python   *.proto
r=`echo $?`
if [ $r -eq 0 ]
then
  cp *.proto ~/code/ly/aba/code/comm/pb/
  cd ~/code/ly/aba/code/comm/pb/
  svn up
  svn ci -m "update define"
  cd /home/otdev/code/ly/ot/code/comm/pb
else
    echo 'proto file error'
fi
