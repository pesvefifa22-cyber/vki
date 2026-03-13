import streamlit as st
import math

st.set_page_config(
    page_title="VKİ Hesaplayıcı",
    page_icon="⚖️",
    layout="centered",
)

st.markdown("""
    <style>
        .main-title {
            font-size: 2.8rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 0.2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            text-align: center;
            color: #6b7280;
            font-size: 1.05rem;
            margin-bottom: 2rem;
        }
        .result-box {
            border-radius: 16px;
            padding: 2rem;
            text-align: center;
            margin-top: 1.5rem;
        }
        .bmi-value {
            font-size: 4rem;
            font-weight: 900;
            line-height: 1;
        }
        .bmi-label {
            font-size: 1.5rem;
            font-weight: 700;
            margin-top: 0.5rem;
        }
        .bmi-desc {
            font-size: 0.95rem;
            margin-top: 0.5rem;
            opacity: 0.85;
        }
        .category-card {
            border-radius: 10px;
            padding: 0.6rem 1rem;
            margin: 0.3rem 0;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Vücut Kitle İndeksi</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Kilonuzun sağlığınıza uygunluğunu hemen öğrenin</div>', unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2, gap="large")

with col1:
    kilo = st.number_input(
        "Kilonuz (kg)",
        min_value=1.0, max_value=300.0,
        value=70.0, step=0.5, format="%.1f"
    )

with col2:
    boy = st.number_input(
        "Boyunuz (metre)",
        min_value=0.5, max_value=2.5,
        value=1.75, step=0.01, format="%.2f"
    )

hesapla = st.button("VKİ Hesapla", use_container_width=True, type="primary")

if hesapla:
    vki = kilo / (boy ** 2)

    if vki < 18.5:
        renk, bg_renk, durum, emoji_durum = "#3b82f6", "#eff6ff", "Zayıf", "🔵"
        aciklama = "Kilonuz normal aralığın altında. Dengeli beslenmeye özen gösterin."
    elif vki < 25.0:
        renk, bg_renk, durum, emoji_durum = "#16a34a", "#f0fdf4", "Normal", "🟢"
        aciklama = "Tebrikler! Kilonuz sağlıklı aralıkta. Bu dengeyi koruyun."
    elif vki < 30.0:
        renk, bg_renk, durum, emoji_durum = "#ca8a04", "#fefce8", "Fazla Kilolu", "🟡"
        aciklama = "Kilonuz normalin biraz üzerinde. Düzenli egzersiz önerilir."
    else:
        renk, bg_renk, durum, emoji_durum = "#dc2626", "#fef2f2", "Obez", "🔴"
        aciklama = "Sağlığınız için bir uzmanla görüşmenizi öneririz."

    st.markdown(f"""
        <div class="result-box" style="background-color:{bg_renk}; border: 2px solid {renk}22;">
            <div class="bmi-value" style="color:{renk};">{vki:.1f}</div>
            <div class="bmi-label" style="color:{renk};">{emoji_durum} {durum}</div>
            <div class="bmi-desc" style="color:#374151;">{aciklama}</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("#### VKİ Kategorileri")
    kategoriler = [
        ("🔵 Zayıf", "< 18.5", "#3b82f6", "#eff6ff"),
        ("🟢 Normal", "18.5 – 24.9", "#16a34a", "#f0fdf4"),
        ("🟡 Fazla Kilolu", "25.0 – 29.9", "#ca8a04", "#fefce8"),
        ("🔴 Obez", "≥ 30.0", "#dc2626", "#fef2f2"),
    ]
    for kat_adi, aralik, renk_k, bg_k in kategoriler:
        secili = (
            (kat_adi.startswith("🔵") and vki < 18.5) or
            (kat_adi.startswith("🟢") and 18.5 <= vki < 25.0) or
            (kat_adi.startswith("🟡") and 25.0 <= vki < 30.0) or
            (kat_adi.startswith("🔴") and vki >= 30.0)
        )
        border = f"2px solid {renk_k}" if secili else "1px solid #e5e7eb"
        bg = bg_k if secili else "#f9fafb"
        st.markdown(f"""
            <div class="category-card" style="background:{bg}; border:{border}; color:#1f2937;">
                <span style="color:{renk_k}; font-weight:700;">{kat_adi}</span>
                <span style="float:right; color:#6b7280;">{aralik}</span>
            </div>
        """, unsafe_allow_html=True)

    st.info("Bu hesaplayıcı yalnızca genel bilgi amaçlıdır. Sağlık kararları için bir uzmana danışın.", icon="ℹ️")

st.markdown("---")
st.markdown('<div style="text-align:center; color:#d1d5db; font-size:0.8rem;">VKİ Hesaplayıcı © 2026</div>', unsafe_allow_html=True)
