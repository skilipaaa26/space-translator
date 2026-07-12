import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from deep_translator import GoogleTranslator

st.title("🎬 مترجم الفيديوهات الفضائي")

# طلب الرابط
url = st.text_input("ضعي رابط فيديو يوتيوب هنا:")

if st.button("استخراج وترجمة"):
    if url:
        try:
            # استخراج معرف الفيديو
            video_id = url.split("v=")[-1]
            
            # جلب النص
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ar', 'en', 'it', 'fr'])
            text = " ".join([i['text'] for i in transcript])
            
            # الترجمة
            st.write("جاري الترجمة...")
            translation = GoogleTranslator(source='auto', target='ar').translate(text)
            
            st.success("الترجمة جاهزة:")
            st.write(translation)
            
        except Exception as e:
            st.error("خطأ: تأكدي أن الفيديو يحتوي على نص (Subtitles). الفيديوهات الموسيقية لا يمكن ترجمتها بهذه الطريقة.")
