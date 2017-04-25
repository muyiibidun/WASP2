#!/bin/sh
python vmanager.py -c WASP2/vm-init1.sh -a create waspymq1
python vmanager.py -c WASP2/vm-init2.sh -a create waspymq2
python vmanager.py -c WASP2/vm-init3.sh -a create waspymq3
