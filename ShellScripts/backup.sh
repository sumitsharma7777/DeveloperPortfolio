#!/bin/bash

# Author: Sumit Sharma
# Purpose: Create compressed folder backups

if [ -z "$1" ]; then
    echo "Usage: ./backup.sh <folder>"
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Error: Folder does not exist."
    exit 1
fi

BACKUP_DIR="$HOME/DeveloperPortfolio_Backups"

mkdir -p "$BACKUP_DIR"

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

FOLDER_NAME=$(basename "$1")

BACKUP_FILE="$BACKUP_DIR/backup_${TIMESTAMP}.tar.gz"

tar -czf "$BACKUP_FILE" -C "$(dirname "$1")" "$FOLDER_NAME"

if [ $? -eq 0 ]; then
    SIZE=$(du -h "$BACKUP_FILE" | awk '{print $1}')

    echo "Backup created successfully!"
    echo "Backup filename: $BACKUP_FILE"
    echo "Backup size: $SIZE"

    echo "$TIMESTAMP - SUCCESS - $BACKUP_FILE - $SIZE" >> "$BACKUP_DIR/backup.log"
else
    echo "Error: Backup failed."

    echo "$TIMESTAMP - FAILED - $1" >> "$BACKUP_DIR/backup.log"
    exit 1
fi

