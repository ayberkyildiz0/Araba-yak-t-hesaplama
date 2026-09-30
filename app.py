import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Araba Yakıt Hesaplama YILDIZ ARGE *",
    page_icon="🚗",
    layout="centered"
)

# Siyah-Beyaz & Modern CSS Stilleri
st.markdown("""
    <style>
    /* Ana Arka Planı Simsiyah Yap */
    .stApp {
        background-color: #0d0d0d;
        color: #ffffff;
    }
    
    /* Üst Menü / Header Şeffaflaştırma */
    header {
        background-color: transparent !important;
    }
    
    /* Başlıklar ve Metinler */
    h1, h2, h3, p, label {
        color: #ffffff !important;
    }
    
    /* Girdi Kutuları (Input Fields) Modernizasyonu */
    div[data-baseweb="input"] {
        background-color: #1a1a1a !important;
        border: 1px solid #333333 !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        transition: all 0.3s ease;
    }
    
    div[data-baseweb="input"]:focus-within {
        border-color: #ffffff !important;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
    }
    
    input {
        color: #ffffff !important;
    }

    /* Artırma/Azaltma Butonları (Number Input Controls) */
    button[aria-label="Decrease value"], button[aria-label="Increase value"] {
        background-color: #262626 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
    }
    
    /* Modern Tasarımlı Ana Buton */
    div.stButton > button {
        background: linear-gradient(135deg, #ffffff 0%, #cccccc 100%) !important;
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 24px !important;
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.15) !important;
        transition: all 0.3s ease-in-out !important;
    }
    
    /* Buton Hover (Üzerine Gelince) Efekti */
    div.stButton > button:hover {
        background: linear-gradient(135deg, #ffffff 0%, #ffffff 100%) !important;
        transform: translateY(-2px) scale(1.01) !important;
        box-shadow: 0 6px 20px rgba(255, 255, 255, 0.3) !important;
    }
    
    /* Metric Kartları (Sonuç Kutuları) */
    div[data-testid="stMetric"] {
        background-color: #161616 !important;
        border: 1px solid #2a2a2a !important;
        border-radius: 14px !important;
        padding: 16px !important;
        text-align: center;
    }
    
    div[data-testid="stMetricLabel"] {
        color: #a0a0a0 !important;
    }
    
    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Ana Başlık
st.title("🚗 ARABA YAKIT HESAPLAMA YILDIZ ARGE")
st.caption("Mesafe ve yakıt verilerini girerek toplam maliyeti anında hesaplayın.")

st.markdown("---")

# Kullanıcı Giriş Alanları
col1, col2 = st.columns(2)

with col1:
    km = st.number_input(
        "Kaç km yol gittiniz?", 
        min_value=0.0, 
        value=100.0, 
        step=10.0,
        help="Gidilen toplam mesafeyi kilometre cinsinden girin."
    )
    
    tuketim = st.number_input(
        "Araç 100 km'de kaç litre yakıyor?", 
        min_value=0.0, 
        value=6.5, 
        step=0.1,
        help="Ortalama yakıt tüketiminiz."
    )

with col2:
    fiyat = st.number_input(
        "Yakıtın litre fiyatı kaç TL?", 
        min_value=0.0, 
        value=42.50, 
        step=0.50,
        help="Güncel litre fiyatını girin."
    )

st.markdown("---")

# Modern Hesapla Butonu ve Hesaplama
if st.button("HESAPLA 🧮", use_container_width=True):
    if km > 0 and tuketim > 0 and fiyat > 0:
        toplam_maliyet = (km / 100) * tuketim * fiyat
        toplam_litre = (km / 100) * tuketim

        st.success("Hesaplama başarıyla tamamlandı!")
        
        # Sonuç Kartları
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.metric(label="Toplam Harcanan Yakıt", value=f"{toplam_litre:.2f} L")
        with res_col2:
            st.metric(label="Toplam Yakıt Maliyeti", value=f"{toplam_maliyet:.2f} TL")
            
    else:
        st.warning("Lütfen tüm değerleri 0'dan büyük girin.")
