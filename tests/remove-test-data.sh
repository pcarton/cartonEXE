#!/bin/bash

#colors
LIGHTBLUE='\033[1;34m'
GREEN='\033[1;32m'
NC='\033[0m'

echo -e "${LIGHTBLUE}PCarton Mod !remove !test $NC"
echo "PCarton Mod !remove !test" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !remove !test2 $NC"
echo "PCarton Mod !remove !test2" | python3 centurion.py

echo -e "${LIGHTBLUE}PCarton Mod !remove !testQuotes $NC"
echo "PCarton Mod !remove !testQuotes" | python3 centurion.py
