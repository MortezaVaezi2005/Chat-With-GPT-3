import openai
import time

# تنظیم کلید API شرکت OpenAI
openai.api_key = "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"

# تنظیم پارامترهای مدل
model_engine = "text-davinci-002"  # موتور مدل
temperature = 0.5  # دمای دخیل در تولید متن
max_tokens = 2048  # حداکثر تعداد توکن‌های تولید شده توسط مدل

# تعریف تابع برای دریافت پاسخ از OpenAI
def ask_gpt(prompt):
    # ایجاد درخواست برای OpenAI API
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    # بازگرداندن پاسخ
    return response.choices[0].text.strip()

# ایجاد فضای چت
print("Chatting with OpenAI's GPT-3!")
while True:
    prompt = input("You: ")
    # در صورتی که کاربر خروجی مدل را بخواهد متن زیر را اجرا کند
    if prompt.lower() in ["exit", "quit", "bye", "goodbye"]:
        break
    # دریافت پاسخ از OpenAI و چاپ آن
    response = ask_gpt(prompt)
    print("AI: " + response)
    time.sleep(1)
