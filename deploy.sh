#!/bin/bash

set -e  # Exit on error

echo "🚀 Starting Deployment..."

cd /var/www/html/
echo "📥 Pulling latest changes from GitHub..."
git pull origin main

echo "💡 Activating Virtual Environment..."
source /var/www/html/venv/bin/activate

cd /var/www/html/my_project/  # Ensure we are in the right directory

echo "📦 Installing dependencies..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt  
else
    echo "❌ ERROR: 'requirements.txt' not found!"
    exit 1
fi

echo "🔄 Running migrations..."
python manage.py migrate

echo "♻️ Restarting Gunicorn..."
sudo systemctl restart gunicorn

deactivate

echo "✅ Deployment completed successfully!"

