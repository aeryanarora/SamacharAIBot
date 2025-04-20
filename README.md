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

## 🛠 Setup

```bash
git clone https://github.com/aeryanarora/SamacharAIBot.git
cd SamacharAIBot
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
