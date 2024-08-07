#!/bin/bash

# Ensure the script is run from the root of the git repository
if [ ! -d ".git" ]; then
  echo "This script must be run from the root of a git repository."
  exit 1
fi

# Check if feature branch name is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <feature-branch>"
  exit 1
fi

FEATURE_BRANCH="$1"

# Check if the feature branch exists
if ! git show-ref --verify --quiet "refs/heads/$FEATURE_BRANCH"; then
  echo "Feature branch '$FEATURE_BRANCH' does not exist."
  exit 1
fi

# Check out the feature branch
echo "Switching to feature branch '$FEATURE_BRANCH'..."
git checkout "$FEATURE_BRANCH" || exit 1

# Make changes (you can modify this part to suit your needs)
echo "Making changes to text.txt..."
echo "hesdasdallo" > text.txt

# Stage and commit changes
echo "Staging changes..."
git add text.txt || exit 1

echo "Committing changes..."
git commit -m "Add a descriptive message about your changes" || exit 1

# Push changes to the remote feature branch
echo "Pushing changes to remote feature branch..."
git push origin "$FEATURE_BRANCH" || exit 1

# Switch to the main branch
echo "Switching to main branch..."
git checkout main || exit 1

# Pull the latest changes from the remote main branch
echo "Pulling latest changes from remote main branch..."
git pull origin main || exit 1

# Merge the feature branch into the main branch
echo "Merging feature branch '$FEATURE_BRANCH' into main..."
git merge "$FEATURE_BRANCH" || exit 1

# Handle merge conflicts if necessary
if [ -n "$(git status --porcelain)" ]; then
  echo "Merge conflicts detected. Please resolve them manually and then commit the changes."
  exit 1
fi

# Push the merged changes to the remote main branch
echo "Pushing merged changes to remote main branch..."
git push origin main || exit 1

echo "Merge process completed successfully."

