#!/bin/bash
# Run this locally from the repository root to remove duplicate directories and files created by previous iterations.
set -e

# List of duplicate dirs to remove
DUP_DIRS=("alembic1" "dashboard1" "auth1" "docs1" "templates1")
for d in "${DUP_DIRS[@]}"; do
  if [ -d "$d" ]; then
    echo "Removing $d"
    git rm -r "$d" || true
  else
    echo "$d not present, skipping"
  fi
done

# Remove README_FIRST1.md if present
if [ -f "README_FIRST1.md" ]; then
  git rm README_FIRST1.md || true
fi

# Commit removal
git commit -m "chore: remove duplicate *1 folders and README_FIRST1.md" || true

echo "Duplicates removed. Push branch and open PR to merge." 
