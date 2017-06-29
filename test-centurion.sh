#!/bin/bash

#colors
LIGHTBLUE='\033[1;34m'
GREEN='\033[1;32m'
NC='\033[0m'

echo -e "${GREEN}Testing !add, !remove, and database commands $NC"
echo -e "${LIGHTBLUE}PCarton Mod !add !test Mod Hello World $NC"
echo "PCarton Mod !add !test Mod Hello World" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !test $NC"
echo "PCarton Mod !test" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !remove !test $NC"
echo "PCarton Mod !remove !test" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !test $NC"
echo "PCarton Mod !test" | python3 centurion.py


echo -e "${LIGHTBLUE}PCarton Mod !add !testingInvalidArgs Mod $NC"
echo "PCarton Mod !add !testingInvalidArgs Mod" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !add !testingInvalidArgs Hello World $NC"
echo "PCarton Mod !add !testingInvalidArgs Hello World" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !add $NC"
echo "PCarton Mod !add" | python3 centurion.py

echo -e "${GREEN}Testing !purge, !timeout, !ban, !unban commands $NC"
echo -e "${LIGHTBLUE}PCarton Mod !purge PCarton $NC"
echo "PCarton Mod !purge PCarton" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !purge $NC"
echo "PCarton Mod !purge" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !timeout PCarton $NC"
echo "PCarton Mod !timeout PCarton" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !timeout $NC"
echo "PCarton Mod !timeout" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !ban PCarton $NC"
echo "PCarton Mod !ban PCarton" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !ban $NC"
echo "PCarton Mod !ban" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !unban PCarton $NC"
echo "PCarton Mod !unban PCarton" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !unban $NC"
echo "PCarton Mod !unban" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !permit PCarton $NC"
echo "PCarton Mod !permit PCarton" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !permit $NC"
echo "PCarton Mod !permit" | python3 centurion.py

echo -e "${GREEN}Testing database commands cooldown $NC"
echo -e "${LIGHTBLUE}PCarton Normal !add !test2 Mod Hello World $NC"
echo "PCarton Mod !add !test2 Normal Hello World" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Normal !test2 $NC"
echo "PCarton Normal !test2" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !test2 $NC"
echo "PCarton Mod !test2" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Normal !test2 $NC"
echo "PCarton Normal !test2" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !test2 $NC"
echo "PCarton Mod !test2" | python3 centurion.py
