#!/bin/bash
# Serve Jekyll site locally with live reload

echo "🚀 Starting Jekyll server with live reload..."
echo "📱 Open http://localhost:4000 in your browser"
echo "🔄 Changes will auto-reload"
echo ""
echo "Press Ctrl+C to stop"
echo ""

bundle exec jekyll serve --livereload
