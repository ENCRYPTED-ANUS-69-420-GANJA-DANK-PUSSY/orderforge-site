#!/bin/bash
# Orderforge Reddit Poster
# Usage: ./post-to-reddit.sh "Title" "Body" subreddit

# Note: This requires the 'reddito' tool or PRAW setup
# For now, outputs formatted post for manual copy-paste

echo "=== REDDIT POST READY ==="
echo ""
echo "Subreddit: $3"
echo ""
echo "--- TITLE ---"
echo "$1"
echo ""
echo "--- BODY ---"
echo "$2"
echo ""
echo "=========================="
echo "Copy and paste into Reddit"
