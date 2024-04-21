#!/bin/sh -e

echo "Setting configuration options..."
mkdir -p ~/.config/gdfuse/default
cat gdrive-ocamlfuse-config.ini > ~/.config/gdfuse/default/config

echo "Setting up Google Drive Auth..."
source ./.env
python sus.py | google-drive-ocamlfuse -xdgbd -headless -id $GOOGLE_CLIENT_ID -secret $GOOGLE_CLIENT_SECRET

echo "Mouting the folder to harbour/..."
google-drive-ocamlfuse harbour/
