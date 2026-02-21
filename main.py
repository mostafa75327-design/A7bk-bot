import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# تفعيل التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# دالة الرد على أي رسالة
async def reply_love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("احبك 💕")

def main():
    # التوكن الخاص بالبوت (مضمن مباشرة)
    TOKEN = "8555031080:AAHKv_xFrNa2POPRPN9eI4TMjXAmEw1XLTw"
    
    # إنشاء التطبيق
    application = Application.builder().token(TOKEN).build()
    
    # إضافة معالج لجميع الرسائل النصية
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_love))
    
    # بدء البوت
    print("البوت يعمل الآن...")
    application.run_polling()

if __name__ == "__main__":
    main()
