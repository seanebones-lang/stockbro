#!/bin/bash
# Script to run the financial dashboard locally

cd "$(dirname "$0")"
source venv/bin/activate

echo "=========================================="
echo "Starting Financial Dashboard"
echo "=========================================="
echo ""
echo "The dashboard will be available at:"
echo "  http://127.0.0.1:8050"
echo ""
echo "Press Ctrl+C to stop the server"
echo "=========================================="
echo ""

python financial_dashboard.py
