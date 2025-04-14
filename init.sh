#!/bin/bash
echo "🔄 Creating virtual environment..."
python3 -m venv .venv

echo "🐍 Activating virtual environment..."
source .venv/bin/activate

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "📦 Installing Node/Yarn dependencies..."
yarn install

echo "🌬️ Starting TailwindCSS watcher..."
yarn tailwindcss &

echo "🚀 Launching Flask app..."
python main.py
