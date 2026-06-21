import streamlit as st

# إعدادات الصفحة والعنوان
st.set_page_config(page_title="Cyber Risk Predictor", page_icon="🛡️", layout="centered")

st.title("Cyber Risk Predictor 🛡️")
st.markdown("### محاكي التنبؤ بمخاطر الأمن السيبراني باستخدام الذكاء الاصطناعي")
st.write("أدخل سيناريو الحادثة الأمنية أو التقرير السيبراني بالأسفل لتحليله ومحاكاته:")

# صندوق نصي لإدخال السيناريو من قبل المستخدم
user_input = st.text_area("وصف السيناريو السيبراني:", height=150, placeholder="مثال: تم رصد محاولات دخول فاشلة متكررة عبر منفذ SSH...")

# زر تشغيل التنبؤ
if st.button("🚨 تحليل ومحاكاة السيناريو"):
    if user_input:
        text_lower = user_input.lower()
        
        # فحص الكلمات الدلالية كمحاكاة ذكية للعرض (Demo)
        if any(word in text_lower for word in ["brute force", "اختراق", "ssh", "attack", "هجوم"]):
            st.error("### 🔴 النتيجة المتوقعة: خطر عالٍ جداً (High Risk)\n**التوصية:** تفعيل جدار الحماية فوراً وحظر عنوان الـ IP المهاجم.")
        elif any(word in text_lower for word in ["phishing", "تصيد", "رابط", "link", "email"]):
            st.warning("### 🟡 النتيجة المتوقعة: خطر متوسط (Medium Risk)\n**التوصية:** عزل الجهاز المتأثر وتوعية الموظف بعدم فتح الروابط المجهولة.")
        else:
            st.success("### 🟢 النتيجة المتوقعة: خطر منخفض / نشاط طبيعي (Low Risk)\n**التوصية:** لا توجد مؤشرات اختراق، النشاط طبيعي ضمن الصيانة الدورية.")
    else:
        st.info("الرجاء كتابة سيناريو أو التقرير الأمني أولاً في الصندوق أعلاه لتشغيل المحاكاة.")
