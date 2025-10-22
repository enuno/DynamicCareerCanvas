#!/bin/bash
# Validate YAML files in _data directory

echo "🔍 Validating YAML files..."

# Check if yamllint is installed
if ! command -v yamllint &> /dev/null; then
    echo "⚠️  yamllint not found. Checking with Jekyll build instead..."
    bundle exec jekyll build --verbose 2>&1 | grep -i "yaml\|error"
    exit $?
fi

# Validate with yamllint
yamllint _data/*.yml

if [ $? -eq 0 ]; then
    echo "✅ All YAML files are valid!"
else
    echo "❌ YAML validation failed!"
    exit 1
fi
