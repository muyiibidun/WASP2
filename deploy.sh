#!/bin/sh
python vmanager.py -c WASP2/waspmq.sh -a create waspmq
python vmanager.py -c WASP2/frontend.sh -a create waspmq-frontend
python vmanager.py -c WASP2/backend.sh -a create waspmq-backend
