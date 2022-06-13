# Cisco SD-WAN bug CSCvz87812 fix

# Problem

Cisco ISR1100s are provisioned as vedge and not cedge which is causing issues with registration in vManage

## This script

The script gets all devices from the vManage API and changes all ISR1100s to Cedge type.

## Usage

- Clone the repo
- Run **python3 migrate_to_xe.py \<vManage IP\> \<vManageUser\> \<vManage Password\>**