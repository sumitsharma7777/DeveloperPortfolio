#!/bin/bash

# Author: Sumit Sharma
# Purpose: Generate System Information Report

echo "=========================================="
echo "       SYSTEM INFORMATION REPORT"
echo "=========================================="

echo "Name: Sumit Sharma"
echo "Roll Number: Add Your Roll Number"
echo "Date: $(date)"

echo ""
echo "---------- CPU INFORMATION ----------"

CPU_MODEL=$(sysctl -n machdep.cpu.brand_string)
CPU_CORES=$(sysctl -n hw.ncpu)

echo "CPU Model: $CPU_MODEL"
echo "CPU Cores: $CPU_CORES"

echo ""
echo "---------- MEMORY INFORMATION ----------"

TOTAL_BYTES=$(sysctl -n hw.memsize)
TOTAL_GB=$(awk -v b="$TOTAL_BYTES" 'BEGIN {printf "%.1f GB", b/1073741824}')

FREE_PERCENT=$(memory_pressure | awk -F': ' '/System-wide memory free percentage/ {gsub("%","",$2); print $2}')

USED_GB=$(awk -v t="$TOTAL_BYTES" -v f="$FREE_PERCENT" 'BEGIN {printf "%.1f GB", t*(100-f)/100/1073741824}')

echo "Total Memory: $TOTAL_GB"
echo "Estimated Used Memory: $USED_GB"

echo ""
echo "---------- TOP 3 PROCESSES ----------"

ps -A -o %cpu=,comm= | sort -nr | head -3

echo ""
echo "=========================================="
echo "Report generated successfully."
echo "=========================================="

