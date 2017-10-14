#!/bin/bash

#colors
LIGHTBLUE='\033[1;34m'
GREEN='\033[1;32m'
NC='\033[0m'

echo -e "${GREEN}Reseting Test Database $NC"
mysql -uroot -proot cartonBotTest < ./schema-test.sql

echo -e "${GREEN}Testing Centurion $NC"
python3 ../PyMods/Tests/test-centurion.py

echo -e "${GREEN}Testing Centurion Add/Remove $NC"
python3 ../PyMods/Tests/test-centurion-add-remove.py

echo -e "${GREEN}Reseting Test Database $NC"
mysql -uroot -proot cartonBotTest < ./schema-test.sql

echo -e "${GREEN}Testing Ganon $NC"
python3 ../PyMods/Tests/test-ganon.py

echo -e "${GREEN}Reseting Test Database $NC"
mysql -uroot -proot cartonBotTest < ./schema-test.sql

echo -e "${GREEN}Testing Hammer $NC"
python3 ../PyMods/Tests/test-hammer.py

echo -e "${GREEN}Testing Scribe $NC"
python3 ../PyMods/Tests/test-scribe.py
