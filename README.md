# SamacharAI Bot

A Telegram-based AI assistant that helps UPSC aspirants by classifying articles into GS Mains Papers and generating structured Q&A in UPSC answer format.

## 🔍 Features

- Classifies any article into GS1, GS2, GS3, GS4
- Uses LLaMA and Gemma models with fallback logic
- Smart chunking of long texts
- Generates UPSC-style question and structured answer (Intro–Body–Conclusion)
- Works directly inside Telegram

## 🚀 Usage

1. Visit the bot: [t.me/SamacharAIBot](https://t.me/SamacharAIBot)
2. Use `/classify [article]` to tag GS papers and topics
3. Use `/ask` to generate questions and answers

**To use the bot, run the script locally, and access the Telegram bot from any device. Uploading to the cloud soon.**

## 🎥 Demo

https://github.com/user-attachments/assets/1cb0dfb1-39e0-49a9-ab92-2461fe582fd8

## 🛠 Setup

```bash
git clone https://github.com/aeryanarora/SamacharAIBot.git
cd SamacharAIBot
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
