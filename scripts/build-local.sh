#!/bin/bash
# Local build script for DynamicCareerCanvas

echo "🔨 Building Jekyll site..."
bundle exec jekyll build

if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    echo "📁 Output in _site/"
else
    echo "❌ Build failed!"
    exit 1
fi
