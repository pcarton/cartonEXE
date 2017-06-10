#!/bin/bash

#colors
LIGHTBLUE='\033[1;34m'
GREEN='\033[1;32m'
NC='\033[0m'

echo -e $GREEN Testing !add, !remove, and database commands $NC
echo "PCarton Mod !add !test Mod Hello World"
echo "PCarton Mod !add !test Mod Hello World" | python3 centurion.py

echo "PCarton Mod !test"
echo "PCarton Mod !test" | python3 centurion.py

echo "PCarton Mod !remove !test"
echo "PCarton Mod !remove !test" | python3 centurion.py

echo "PCarton Mod !test"
echo "PCarton Mod !test" | python3 centurion.py


echo "PCarton Mod !add !testingInvalidArgs Mod"
echo "PCarton Mod !add !testingInvalidArgs Mod" | python3 centurion.py

echo "PCarton Mod !add !testingInvalidArgs Hello World"
echo "PCarton Mod !add !testingInvalidArgs Hello World" | python3 centurion.py

echo "PCarton Mod !add"
echo "PCarton Mod !add" | python3 centurion.py

echo -e $GREEN Testing !purge, !timeout, !ban, !unban commands $NC
echo "PCarton Mod !purge PCarton"
echo "PCarton Mod !purge PCarton" | python3 centurion.py

echo "PCarton Mod !purge"
echo "PCarton Mod !purge" | python3 centurion.py

echo "PCarton Mod !timeout PCarton"
echo "PCarton Mod !timeout PCarton" | python3 centurion.py

echo "PCarton Mod !timeout"ban
echo "PCarton Mod !timeout" | python3 centurion.py

echo "PCarton Mod !ban PCarton"
echo "PCarton Mod !ban PCarton" | python3 centurion.py

echo "PCarton Mod !ban"
echo "PCarton Mod !ban" | python3 centurion.py

echo "PCarton Mod !unban PCarton"
echo "PCarton Mod !unban PCarton" | python3 centurion.py

echo "PCarton Mod !unban"
echo "PCarton Mod !unban" | python3 centurion.py
