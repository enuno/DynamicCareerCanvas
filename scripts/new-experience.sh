#!/bin/bash
# Quick script to add new experience entry template

echo "📝 Add New Work Experience"
echo "=========================="
echo ""

read -p "Company: " company
read -p "Title: " title
read -p "Location: " location
read -p "Start Date (YYYY-MM): " start_date
read -p "End Date (YYYY-MM or leave empty if current): " end_date
read -p "Is current position? (yes/no): " is_current

if [ "$is_current" = "yes" ]; then
    current="true"
    end_date="null"
else
    current="false"
fi

echo ""
echo "✏️  Copy this template to _data/experience.yml:"
echo ""
echo "- company: \"$company\""
echo "  title: \"$title\""
echo "  location: \"$location\""
echo "  start_date: \"$start_date\""
echo "  end_date: \"$end_date\""
echo "  current: $current"
echo "  description: |"
echo "    Add your description here"
echo "  highlights:"
echo "    - \"Highlight 1\""
echo "    - \"Highlight 2\""
echo "  technologies:"
echo "    - \"Tech 1\""
echo "    - \"Tech 2\""
echo ""
