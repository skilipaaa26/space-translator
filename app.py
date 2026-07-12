import streamlit as st
import whisper
import os
import base64

# إعداد الصفحة
st.set_page_config(page_title="محطة الترجمة الفضائية", layout="centered")

# دالة لتحويل الصورة لـ Base64 لضمان عرضها كخلفية
def get_bg_image(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# تنسيق الخلفية (الصورة كواجهة)
try:
    img_base64 = get_bg_image('space.jpg') # تأكد من وجود ملف باسم space.jpg
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        /* جعل خلفية الحاويات شفافة قليلاً لتظهر الصورة خلفها */
        [data-testid="stAppViewContainer"] {{
            background: rgba(0, 0, 0, 0.5) !important;
        }}
        h1, label, .stMarkdown, .stSuccess, .stWarning {{
            color: #ffffff !important;
            text-shadow: 2px 2px 10px #000000;
        }}
        div.stButton > button {{
            background-color: #00d2ff !important;
            color: #000000 !important;
            font-weight: bold;
            border-radius: 20px !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
except:
    st.error("خطأ: يرجى وضع صورة باسم 'space.jpg' في مجلد المشروع.")

# محتوى الصفحة
st.title("🌌 محطة الترجمة الفضائية")

lang_option = st.selectbox("حدد كوكب اللغة المستهدف:", ["إيطاليا (it)", "إنجلترا (en)", "فرنسا (fr)"])
lang_code = lang_option.split("(")[1].replace(")", "")

uploaded_file = st.file_uploader("ارفع ملف الفيديو للترجمة (mp4):", type=["mp4"])

if st.button("بدء المهمة الفضائية 🚀"):
    if uploaded_file is not None:
        with open("temp_video.mp4", "wb") as f:
            f.write(uploaded_file.read())
        try:
            with st.spinner('جاري سحب البيانات من الثقب الأسود...'):
                model = whisper.load_model("base")
                result = model.transcribe("temp_video.mp4")
                translator = Translator()
                translated = translator.translate(result["text"], dest=lang_code)
                st.success("تمت المهمة بنجاح!")
                st.text_area("النص المترجم:", translated.text, height=300)
        except Exception as e:
            st.error(f"حدث خلل في المهمة: {e}")
        finally:
            if os.path.exists("temp_video.mp4"): os.remove("temp_video.mp4")
    else:
        st.warning("الرجاء رفع فيديو أولاً قبل الإقلاع!")
