#!/bin/bash

#colors
LIGHTBLUE='\033[1;34m'
GREEN='\033[1;32m'
NC='\033[0m'

echo -e "${LIGHTBLUE}PCarton Normal $NC"
echo "PCarton Normal" | python3 ganon.py

echo -e "${LIGHTBLUE}PCarton Follower $NC"
echo "PCarton Follower" | python3 ganon.py

echo -e "${LIGHTBLUE}PCarton Sub $NC"
echo "PCarton Sub" | python3 ganon.py

echo -e "${LIGHTBLUE}PCarton Mod $NC"
echo "PCarton Mod" | python3 ganon.py

echo -e "${LIGHTBLUE}PCarton Caster $NC"
echo "PCarton Caster" | python3 ganon.py
