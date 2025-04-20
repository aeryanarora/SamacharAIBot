import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from classifier.utility import classify_chunks
from classifier.qa import generate_qa_for_all_papers, format_qa_markdown

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
user_last_article = {}


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    intro = (
        "🧠 *Welcome to the UPSC GS Classifier & QnA Bot!* 🇮🇳\n\n"
        "Paste any article, report, or editorial — and I will:\n"
        "1. 🔍 Classify it into UPSC GS Mains Papers and Topics\n"
        "2. ✍️ Generate model Q&A in structured UPSC answer format\n\n"
        "Commands:\n"
        "• `/classify [article]` – Tag GS Paper + Topics\n"
        "• `/ask` – Get high-quality UPSC-style Q&A\n\n"
        "Use it for daily answer writing, newspaper practice, and beyond!"
    )
    await update.message.reply_text(intro, parse_mode="Markdown")


async def classify_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""
    text = text.replace("/classify", "", 1).strip()

    if not text:
        await update.message.reply_text("❗️Please paste your article after the /classify command.")
        return

    user_last_article[update.effective_user.id] = text

    try:
        result = classify_chunks(text)

        reply = "🧾 *GS Paper Classification:*\n"
        for paper, topics in result.items():
            if topics:
                reply += f"*{paper}*: {', '.join(topics)}\n"

        await update.message.reply_text(reply, parse_mode="Markdown")

    except:
        await update.message.reply_text("Something went wrong while classifying the article.")


async def ask_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = user_last_article.get(user_id)

    if not text:
        await update.message.reply_text("❗️Please classify an article first using /classify.")
        return

    try:
        gs_map = classify_chunks(text)
        qas = generate_qa_for_all_papers(text, gs_map)

        for paper, qa in qas.items():
            msg = format_qa_markdown(qa, paper)
            await update.message.reply_text(msg)

    except:
        await update.message.reply_text("Something went wrong while generating questions and answers.")


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("classify", classify_command))
    app.add_handler(CommandHandler("ask", ask_command))
    app.run_polling()
