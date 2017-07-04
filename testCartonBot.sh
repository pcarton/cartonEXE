#!/bin/bash

#colors
LIGHTBLUE='\033[1;34m'
GREEN='\033[1;32m'
NC='\033[0m'

echo -e "${GREEN}Reseting Test Database $NC"
mysql -uroot -proot cartonBotTest < schema-test.sql

echo -e "${GREEN}Testing Centurion $NC"
python3 test-centurion.py
