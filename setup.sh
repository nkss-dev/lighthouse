#!/bin/sh -e

echo "Setting up Google Drive Auth..."
echo "Please check your browser"
google-drive-ocamlfuse -xdgbd

echo "Setting configuration options..."
crudini --merge ~/.config/gdfuse/default/config < gdrive-ocamlfuse-config.ini

echo "Mouting the folder to harbour/..."
google-drive-ocamlfuse harbour/
