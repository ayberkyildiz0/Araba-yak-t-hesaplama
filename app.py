import streamlit as st

# Sayfa Başlığı ve Tasarımı
st.set_page_config(
    page_title="Araba Yakıt Hesaplama",
    page_icon="🚗",
    layout="centered"
)

# Ana Başlık
st.title("🚗 ARABA YAKIT HESAPLAMA YILDIZ ARGE")
st.write("Gideceğiniz mesafe ve araç tüketim değerlerini girerek toplam maliyeti hesaplayın.")

st.divider()

# Kullanıcı Giriş Alanları (Streamlit Form Elemanları)
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
        help="Fabrika verisi veya ortalama yakıt tüketiminiz."
    )

with col2:
    fiyat = st.number_input(
        "Yakıtın litre fiyatı kaç TL?",
        min_value=0.0,
        value=42.50,
        step=0.50,
        help="Güncel litre fiyatını girin."
    )

st.divider()

# Hesapla Butonu ve Mantığı
if st.button("HESAPLA 🧮", use_container_width=True, type="primary"):
    if km > 0 and tuketim > 0 and fiyat > 0:
        toplam_maliyet = (km / 100) * tuketim * fiyat
        toplam_litre = (km / 100) * tuketim

        # Sonuç Gösterimi
        st.success("Hesaplama Başarıyla Tamamlandı!")

        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.metric(label="Toplam Harcanan Yakıt", value=f"{toplam_litre:.2f} Litre")
        with res_col2:
            st.metric(label="Toplam Yakıt Maliyeti", value=f"{toplam_maliyet:.2f} TL")

    else:
        st.warning("Lütfen tüm değerleri 0'dan büyük girin.")
