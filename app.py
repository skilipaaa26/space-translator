import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from deep_translator import GoogleTranslator

st.set_page_config(page_title="مترجم فيديوهات يوتيوب", page_icon="🚀")
st.title("🚀 مترجم فيديوهات يوتيوب الفضائي")

# إدخال رابط اليوتيوب
youtube_url = st.text_input("ضعي رابط فيديو يوتيوب هنا:")

if youtube_url:
    try:
        # استخراج معرف الفيديو من الرابط
        video_id = youtube_url.split("v=")[-1]
        
        # استخراج الترجمة
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'it', 'ar'])
        full_text = " ".join([i['text'] for i in transcript])
        
        st.success("تم استخراج النص من الفيديو!")
        
        # خيارات الترجمة
        target_lang = st.selectbox("ترجمة إلى:", ["ar", "en", "it", "fr"])
        
        if st.button("بدء الترجمة"):
            with st.spinner('جاري الترجمة...'):
                translated_text = GoogleTranslator(source='auto', target=target_lang).translate(full_text)
                st.text_area("النص المترجم:", translated_text, height=300)
                
    except Exception as e:
        st.error(f"عذراً، لم أتمكن من العثور على ترجمة للفيديو. تأكدي أن الفيديو يحتوي على نص صوتي أو ترجمة مصاحبة.")
