import streamlit as st
from deep_translator import GoogleTranslator

# إعداد الصفحة
st.set_page_config(page_title="محطة الترجمة الفضائية", page_icon="🚀")

st.title("🚀 محطة الترجمة الفضائية")
st.write("قومي بلصق النص الذي تريدين ترجمته في الأسفل:")

# واجهة المستخدم
text_to_translate = st.text_area("النص:", height=150)
target_lang = st.selectbox("اختاري اللغة المستهدفة:", 
                           options=["en", "it", "ar", "fr", "es"],
                           format_func=lambda x: {"en": "إنجليزي", "it": "إيطالي", "ar": "عربي", "fr": "فرنسي", "es": "إسباني"}[x])

# زر الترجمة
if st.button("بدء المهمة الفضائية"):
    if text_to_translate:
        try:
            with st.spinner('جاري الترجمة عبر المجرات...'):
                translated = GoogleTranslator(source='auto', target=target_lang).translate(text_to_translate)
                st.success("الترجمة جاهزة:")
                st.write(translated)
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
    else:
        st.warning("الرجاء إدخال نص للترجمة أولاً.")
