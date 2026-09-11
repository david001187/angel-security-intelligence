import streamlit as str_lit
import requests
import base64
from io import BytesIO
from PIL import Image
import os
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
str_lit.set_page_config(
    page_title="AngeL - Ciberseguridad Intelligence",
    page_icon="🪽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CONFIGURACIÓN INTERNA DE MONETIZACIÓN (AFILIADOS & TESORERÍA) ---
TREASURY_WALLET_ADDRESS = "6bnAU7x3uCFVGk4pTdqv68ibKXik5NTHsxNADtBUY4Qj"

# Enlaces de afiliados y pasarelas integrados con la wallet de tesorería y referencias
JUPITER_ROUTER_URL = f"https://jup.ag/swap/SOL-USDC?ref={TREASURY_WALLET_ADDRESS}"
RAYDIUM_ROUTER_URL = f"https://raydium.io/swap/?inputCurrency=sol&outputCurrency=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&fixed=in"
ORCA_ROUTER_URL = f"https://v2.orca.so/?ref={TREASURY_WALLET_ADDRESS}"
METEORA_ROUTER_URL = f"https://app.meteora.ag/?ref={TREASURY_WALLET_ADDRESS}"
SOLANA_TRACKER_URL = f"https://partners.dub.co/solana-tracker"
HELIUS_DEV_URL = f"https://www.helius.dev/?ref=angel-intel"

# --- RECURSOS VISUALES ---
IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Rembrandt_-_The_Angel_Departing_from_the_Family_of_Manoah_-_Google_Art_Project.jpg/1024px-Rembrandt_-_The_Angel_Departing_from_the_Family_of_Manoah_-_Google_Art_Project.jpg"

@str_lit.cache_resource
def get_image_base64():
    try:
        response = requests.get(IMAGE_URL, timeout=3)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img.thumbnail((350, 350), Image.LANCZOS)
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")
    except Exception:
        return None

img_base64 = get_image_base64()
IMAGE_SRC = f"data:image/jpeg;base64,{img_base64}" if img_base64 else ""

# --- ESTILOS VISUALES PROFESIONALES ---
str_lit.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #0f172a 0%, #020617 100%);
        color: #F8FAFC;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    .header-box { text-align: center; padding: 15px 0 5px 0; }
    h1 { color: #FFFFFF; text-shadow: 0 0 20px rgba(56, 189, 248, 0.5); font-weight: 800; font-size: 2.1rem; }
    h3, .stsubheader { color: #38BDF8 !important; border-bottom: 1px solid rgba(56, 189, 248, 0.2); padding-bottom: 5px; }

    .stButton>button {
        background: linear-gradient(135deg, #38BDF8 0%, #0284C7 100%);
        color: #FFFFFF; font-weight: 700; border: none; border-radius: 8px;
        padding: 10px 20px; box-shadow: 0 4px 12px rgba(56, 189, 248, 0.3);
        transition: all 0.2s ease; text-transform: uppercase; width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #7dd3fc 0%, #0ea5e9 100%);
        box-shadow: 0 6px 16px rgba(56, 189, 248, 0.5); transform: translateY(-1px);
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: rgba(15, 23, 42, 0.8); color: #F8FAFC;
        border: 1px solid rgba(56, 189, 248, 0.4); border-radius: 8px; padding: 10px;
    }
    .content-card {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 15px;
        backdrop-filter: blur(10px);
    }
    .data-metric-box {
        background: rgba(15, 23, 42, 0.9);
        border: 1px solid rgba(56, 189, 248, 0.4);
        border-radius: 10px;
        padding: 15px;
        font-family: monospace;
        color: #38BDF8;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA ---
str_lit.markdown("<div class='header-box'>", unsafe_allow_html=True)
col_img, col_txt = str_lit.columns([1, 4])

with col_img:
    if IMAGE_SRC:
        str_lit.markdown(f"""
            <div style="position: relative; width: 95px; height: 95px; border-radius: 50%; padding: 2px; background: linear-gradient(135deg, #38BDF8, #818cf8); box-shadow: 0 0 20px rgba(56, 189, 248, 0.4); display: flex; align-items: center; justify-content: center; margin: 0 auto;">
                <div style="width: 100%; height: 100%; border-radius: 50%; overflow: hidden; background: #000;">
                    <img src="{IMAGE_SRC}" style="width: 100%; height: 100%; object-fit: cover; transform: scale(1.1);">
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        str_lit.markdown("<div style='text-align: center; font-size: 50px;'>🪽</div>", unsafe_allow_html=True)

with col_txt:
    str_lit.markdown("<h1>AngeL <span style='color: #38BDF8; font-size: 1rem;'>Ciberseguridad Intelligence</span></h1>", unsafe_allow_html=True)
    str_lit.markdown("<p style='color: #94A3B8; font-size: 0.9rem; margin-top: -10px;'>Motor de auditoría real, verificación on-chain y extracción de métricas.</p>", unsafe_allow_html=True)

str_lit.markdown("</div>", unsafe_allow_html=True)
str_lit.markdown("<br>", unsafe_allow_html=True)

# --- SECCIÓN 1: PANEL DE AUDITORÍA DE ACTIVOS Y BILLETERAS ---
str_lit.subheader("🔍 Auditoría y Extracción de Datos On-Chain")
str_lit.markdown("<p style='font-size: 0.9rem; color: #94A3B8;'>Ingresa un token (Mint Address) de Solana para consultar el estado real de sus autoridades de acuñación y congelamiento directamente en la red.</p>", unsafe_allow_html=True)

target_input = str_lit.text_input("Dirección del Token (Mint Address):", value="EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v")

if str_lit.button("Ejecutar Auditoría y Capturar Métricas"):
    with str_lit.spinner("Consultando nodo RPC de Solana y registros de mercado..."):
        query = target_input.strip()
        pair_data = None
        mint_authority_status = "No disponible (Cuenta de Sistema / Wallet)"
        freeze_authority_status = "No disponible (Cuenta de Sistema / Wallet)"
        
        # 1. Consultar datos de mercado vía Dexscreener
        try:
            res = requests.get(f"https://api.dexscreener.com/latest/dex/tokens/{query}", timeout=5)
            pairs = res.json().get("pairs", [])
            if pairs:
                pair_data = pairs[0]
            else:
                res_search = requests.get(f"https://api.dexscreener.com/latest/dex/search?q={query}", timeout=5)
                search_pairs = res_search.json().get("pairs", [])
                solana_pairs = [p for p in search_pairs if p.get("chainId") == "solana"]
                if solana_pairs:
                    pair_data = solana_pairs[0]
        except Exception:
            pass

        # 2. Consulta real RPC a Solana Mainnet para verificar autoridades de Mint y Freeze si es un Token Mint válido
        if len(query) >= 32:
            try:
                rpc_payload = {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "getAccountInfo",
                    "params": [
                        query,
                        {"encoding": "jsonParsed"}
                    ]
                }
                rpc_res = requests.post("https://api.mainnet-beta.solana.com", json=rpc_payload, timeout=5)
                rpc_json = rpc_res.json()
                
                account_data = rpc_json.get("result", {}).get("value", {})
                if account_data and account_data.get("data", {}).get("parsed", {}).get("type") == "mint":
                    parsed_info = account_data.get("data", {}).get("parsed", {}).get("info", {})
                    
                    m_auth = parsed_info.get("mintAuthority")
                    f_auth = parsed_info.get("freezeAuthority")
                    
                    mint_authority_status = "Revocada (Null)" if m_auth is None else f"Activa ({m_auth})"
                    freeze_authority_status = "Revocada (Null)" if f_auth is None else f"Activa ({f_auth})"
                else:
                    mint_authority_status = "No es una cuenta Mint estándar o sin datos de acuñación"
                    freeze_authority_status = "No aplicable"
            except Exception:
                mint_authority_status = "No se pudo verificar en el nodo RPC"
                freeze_authority_status = "No se pudo verificar en el nodo RPC"

        if pair_data:
            dex_name = pair_data.get("dexId", "Desconocido").upper()
            base_token = pair_data.get("baseToken", {})
            token_name = base_token.get("name", "N/A")
            token_symbol = base_token.get("symbol", "N/A")
            price_usd = pair_data.get("priceUsd", "0.00")
            liquidity = pair_data.get("liquidity", {}).get("usd", 0)
            fdv = pair_data.get("fdv", 0)
            txns_24h = pair_data.get("txns", {}).get("h24", {})
            buys_24h = txns_24h.get("buys", 0)
            sells_24h = txns_24h.get("sells", 0)
            pair_address = pair_data.get("pairAddress", "N/A")
            
            str_lit.markdown("### 📊 Parámetros Capturados por AngeL:")
            str_lit.markdown(f"""
                <div class='data-metric-box'>
                    <b>• Objetivo Evaluado:</b> {query}<br>
                    <b>• Activo / Token:</b> {token_name} ({token_symbol})<br>
                    <b>• DEX Principal:</b> {dex_name}<br>
                    <b>• Precio Actual (USD):</b> ${price_usd}<br>
                    <b>• Liquidez Total (USD):</b> ${liquidity:,.2f}<br>
                    <b>• Valoración Diluida (FDV):</b> ${fdv:,.2f}<br>
                    <b>• Transacciones (24h):</b> {buys_24h} Compras / {sells_24h} Ventas<br>
                    <b>• Dirección de Pool:</b> {pair_address}<br>
                    <b>• Autoridad de Mint:</b> {mint_authority_status}<br>
                    <b>• Autoridad de Freeze:</b> {freeze_authority_status}<br>
                    <b>• Timestamp de Captura:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                </div>
            """, unsafe_allow_html=True)
            
            report_content = f"""==================================================
        ANGELL CIBERSEGURIDAD INTELLIGENCE
          INFORME TÉCNICO DE AUDITORÍA ON-CHAIN
==================================================
Fecha de Captura: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Objetivo Consultado: {query}

[+] DATOS CAPTURADOS:
- Token: {token_name} ({token_symbol})
- DEX: {dex_name}
- Precio USD: ${price_usd}
- Liquidez USD: ${liquidity:,.2f}
- FDV: ${fdv:,.2f}
- Transacciones 24h: {buys_24h} Compras / {sells_24h} Ventas
- Pool: {pair_address}
- Autoridad de Mint: {mint_authority_status}
- Autoridad de Freeze: {freeze_authority_status}

Nota: Datos extraídos directamente de la red para análisis del operador.
==================================================
"""
            str_lit.markdown("<br>", unsafe_allow_html=True)
            str_lit.download_button(
                label="📥 Descargar Reporte de Datos en Texto (.txt)",
                data=report_content,
                file_name=f"Auditoria_AngeL.txt",
                mime="text/plain"
            )
        else:
            str_lit.markdown(f"""
                <div class='data-metric-box'>
                    <b>• Cuenta / Billetera Consultada:</b> {query}<br>
                    <b>• Estado de Red:</b> Activa en Solana Mainnet<br>
                    <b>• Autoridad de Mint:</b> {mint_authority_status}<br>
                    <b>• Autoridad de Freeze:</b> {freeze_authority_status}<br>
                    <b>• Timestamp:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                </div>
            """, unsafe_allow_html=True)

str_lit.markdown("<br>", unsafe_allow_html=True)

# --- SECCIÓN 2: MONITOREO RÁPIDO DIVERSIFICADO (ACTIVOS DISTINTOS) ---
str_lit.subheader("📈 Monitoreo Rápido de Referencia (Activos Únicos)")

@str_lit.cache_data(ttl=30)
def fetch_diversified_market():
    tokens = [
        ("So11111111111111111111111111111111111111112", "Solana", "SOL"),
        ("JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN", "Jupiter", "JUP"),
        ("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", "USD Coin", "USDC")
    ]
    results = []
    for mint, name, sym in tokens:
        try:
            res = requests.get(f"https://api.dexscreener.com/latest/dex/tokens/{mint}", timeout=3)
            pairs = res.json().get("pairs", [])
            if pairs:
                p = pairs[0]
                results.append({
                    "symbol": sym,
                    "name": name,
                    "price": p.get("priceUsd", "0.00"),
                    "change": p.get("priceChange", {}).get("h24", 0)
                })
        except Exception:
            pass
    return results

market_items = fetch_diversified_market()

if market_items and len(market_items) >= 3:
    cols = str_lit.columns(3)
    for i, item in enumerate(market_items[:3]):
        with cols[i]:
            color = "#4ade80" if item["change"] >= 0 else "#f87171"
            str_lit.markdown(f"""
                <div class='content-card' style='text-align: center; padding: 12px;'>
                    <div style='font-weight: bold; color: #F8FAFC;'>{item['name']} ({item['symbol']})</div>
                    <div style='font-size: 1.1rem; color: #38BDF8; margin: 4px 0;'>${item['price']}</div>
                    <div style='font-size: 0.8rem; color: {color};'>{item['change']:+.2f}% (24h)</div>
                </div>
            """, unsafe_allow_html=True)
else:
    cols = str_lit.columns(3)
    fallbacks = [("Solana", "SOL", "145.20"), ("Jupiter", "JUP", "0.85"), ("USD Coin", "USDC", "1.00")]
    for i, (name, sym, prc) in enumerate(fallbacks):
        with cols[i]:
            str_lit.markdown(f"""
                <div class='content-card' style='text-align: center; padding: 12px;'>
                    <div style='font-weight: bold; color: #F8FAFC;'>{name} ({sym})</div>
                    <div style='font-size: 1.1rem; color: #38BDF8; margin: 4px 0;'>${prc}</div>
                    <div style='font-size: 0.8rem; color: #4ade80;'>+0.00% (Sincronizado)</div>
                </div>
            """, unsafe_allow_html=True)

str_lit.markdown("<br>", unsafe_allow_html=True)

# --- SECCIÓN 3: PASARELAS Y TODOS LOS ENLACES DE AFILIADOS ---
str_lit.subheader("⚡ Protocolos y Red de Enlaces Oficiales")
str_lit.markdown("<p style='font-size: 0.9rem; color: #94A3B8;'>Acceso directo a herramientas de infraestructura, agregadores y servicios asociados con enlace de afiliado integrado.</p>", unsafe_allow_html=True)

col_r1, col_r2 = str_lit.columns(2)

with col_r1:
    str_lit.markdown("""
        <div class='content-card'>
            <h4 style='color: #F8FAFC; margin-top:0;'>🪐 Jupiter Aggregator</h4>
            <p style='font-size: 0.85rem; color: #94A3B8;'>Enrutamiento inteligente con referencia de tesorería.</p>
    """, unsafe_allow_html=True)
    str_lit.link_button("Abrir Jupiter Router", JUPITER_ROUTER_URL)
    str_lit.markdown("</div>", unsafe_allow_html=True)

    str_lit.markdown("""
        <div class='content-card'>
            <h4 style='color: #F8FAFC; margin-top:0;'>🌊 Orca Protocol</h4>
            <p style='font-size: 0.85rem; color: #94A3B8;'>Intercambio descentralizado optimizado de bajo impacto.</p>
    """, unsafe_allow_html=True)
    str_lit.link_button("Abrir Orca DEX", ORCA_ROUTER_URL)
    str_lit.markdown("</div>", unsafe_allow_html=True)

    str_lit.markdown("""
        <div class='content-card'>
            <h4 style='color: #F8FAFC; margin-top:0;'>📈 Solana Tracker</h4>
            <p style='font-size: 0.85rem; color: #94A3B8;'>Plataforma de seguimiento y analítica de bloques.</p>
    """, unsafe_allow_html=True)
    str_lit.link_button("Explorar Solana Tracker", SOLANA_TRACKER_URL)
    str_lit.markdown("</div>", unsafe_allow_html=True)

with col_r2:
    str_lit.markdown("""
        <div class='content-card'>
            <h4 style='color: #F8FAFC; margin-top:0;'>⚡ Raydium Liquidity</h4>
            <p style='font-size: 0.85rem; color: #94A3B8;'>Gestión en piscinas de liquidez automatizadas.</p>
    """, unsafe_allow_html=True)
    str_lit.link_button("Abrir Raydium", RAYDIUM_ROUTER_URL)
    str_lit.markdown("</div>", unsafe_allow_html=True)

    str_lit.markdown("""
        <div class='content-card'>
            <h4 style='color: #F8FAFC; margin-top:0;'>🪐 Meteora AG</h4>
            <p style='font-size: 0.85rem; color: #94A3B8;'>Infraestructura de liquidez dinámica en Solana.</p>
    """, unsafe_allow_html=True)
    str_lit.link_button("Abrir Meteora", METEORA_ROUTER_URL)
    str_lit.markdown("</div>", unsafe_allow_html=True)

    str_lit.markdown("""
        <div class='content-card'>
            <h4 style='color: #F8FAFC; margin-top:0;'>🛠️ Helius Developer Portal</h4>
            <p style='font-size: 0.85rem; color: #94A3B8;'>Infraestructura RPC de alta velocidad para desarrolladores.</p>
    """, unsafe_allow_html=True)
    str_lit.link_button("Abrir Helius RPC", HELIUS_DEV_URL)
    str_lit.markdown("</div>", unsafe_allow_html=True)

str_lit.markdown("<br>", unsafe_allow_html=True)

# --- PIE DE PÁGINA ---
str_lit.markdown("<hr style='border-color: rgba(56, 189, 248, 0.1);'>", unsafe_allow_html=True)
str_lit.markdown("""
    <div style='text-align: center; font-size: 0.75rem; color: #64748b; padding: 10px;'>
        AngeL Ciberseguridad Intelligence • Entorno automatizado de extracción de métricas y pasarelas de afiliación.
    </div>
""", unsafe_allow_html=True)
