import streamlit as str_lit
import requests
import base64
from io import BytesIO
from PIL import Image
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
str_lit.set_page_config(
    page_title="AngeL - Ciberseguridad Intelligence & SOC 24/7",
    page_icon="🪽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CONFIGURACIÓN DE MONETIZACIÓN GLOBAL Y TESORERÍA ---
TREASURY_WALLET_ADDRESS = "6bnAU7x3uCFVGk4pTdqv68ibKXik5NTHsxNADtBUY4Qj"
PAYPAL_ME_LINK = f"https://paypal.me/angelciberseguridad"

# Enlaces de pasarelas, afiliados y herramientas con tu wallet y referencias integradas
JUPITER_ROUTER_URL = f"https://jup.ag/swap/SOL-USDC?ref={TREASURY_WALLET_ADDRESS}"
RAYDIUM_ROUTER_URL = f"https://raydium.io/swap/?inputCurrency=sol&outputCurrency=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&fixed=in"
ORCA_ROUTER_URL = f"https://v2.orca.so/?ref={TREASURY_WALLET_ADDRESS}"
METEORA_ROUTER_URL = f"https://app.meteora.ag/?ref={TREASURY_WALLET_ADDRESS}"
SOLANA_TRACKER_URL = f"https://partners.dub.co/solana-tracker"
HELIUS_DEV_URL = f"https://www.helius.dev/?ref=angel-intel"

# --- ENLACES DE PATROCINIO Y MONETIZACIÓN DIARIA (REFERIDOS Y AFILIADOS) ---
PHANTOM_AFFILIATE_URL = f"https://phantom.app/?ref={TREASURY_WALLET_ADDRESS}"
SOLANAFLEX_URL = f"https://solana.com/?ref={TREASURY_WALLET_ADDRESS}"
BANANA_GUN_BOT_URL = f"https://t.me/Banana_Gun_Bot?start=ref_{TREASURY_WALLET_ADDRESS}"
MAESTRO_BOT_URL = f"https://t.me/MaestroSniperBot?start={TREASURY_WALLET_ADDRESS}"
BULKR_TRADING_URL = f"https://bullx.io/?ref={TREASURY_WALLET_ADDRESS}"
METAPLEX_URL = f"https://metaplex.com/?ref={TREASURY_WALLET_ADDRESS}"

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

# --- ESTILOS VISUALES ---
str_lit.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #1e293b 0%, #0f172a 100%) !important;
        color: #F8FAFC;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    .header-box { text-align: center; padding: 15px 0 5px 0; }
    h1 { color: #FFFFFF; text-shadow: 0 0 20px rgba(56, 189, 248, 0.5); font-weight: 800; font-size: 2.1rem; }
    h3, .stsubheader { color: #38BDF8 !important; border-bottom: 1px solid rgba(56, 189, 248, 0.2); padding-bottom: 5px; }

    .stButton>button, .stDownloadButton>button, .stLinkButton>a {
        background: #38BDF8 !important;
        color: #0F172A !important; 
        font-weight: 900 !important; 
        border: 2px solid #0EA5E9 !important; 
        border-radius: 8px !important;
        padding: 10px 20px !important; 
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.6) !important;
        transition: all 0.2s ease !important; 
        text-transform: uppercase !important; 
        width: 100% !important;
        opacity: 1 !important;
        text-align: center !important;
        text-decoration: none !important;
        display: inline-block !important;
        box-sizing: border-box !important;
    }
    .stButton>button:hover, .stDownloadButton>button:hover, .stLinkButton>a:hover {
        background: #7DD3FC !important;
        color: #0F172A !important;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.9) !important; 
        transform: translateY(-1px) !important;
        text-decoration: none !important;
    }

    .gold-code-box div {
        background-color: rgba(20, 24, 39, 0.95) !important;
        border: 2px solid #FACC15 !important;
        border-radius: 6px !important;
        box-shadow: 0 0 12px rgba(250, 204, 21, 0.5) !important;
    }
    .gold-code-box code {
        color: #FDE047 !important;
        font-weight: 800 !important;
        text-shadow: 0 0 8px rgba(250, 204, 21, 0.6);
    }

    .stTextInput>div>div>input {
        background-color: rgba(15, 23, 42, 0.8); color: #F8FAFC;
        border: 2px solid #eab308 !important; border-radius: 8px; padding: 10px;
        font-weight: bold;
        box-shadow: 0 0 10px rgba(234, 179, 8, 0.4);
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
    .price-tag {
        font-size: 1.4rem;
        font-weight: 800;
        color: #38BDF8;
        margin: 5px 0;
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
    str_lit.markdown("<h1>AngeL <span style='color: #38BDF8; font-size: 1rem;'>Ciberseguridad Intelligence & SOC 24/7</span></h1>", unsafe_allow_html=True)
    str_lit.markdown("<p style='color: #94A3B8; font-size: 0.9rem; margin-top: -10px;'>Plataforma integral enfocada en auditoría de contratos, tokens, firmas en el ecosistema de Solana, seguridad Web/Android y monitorización defensiva corporativa.</p>", unsafe_allow_html=True)

str_lit.markdown("</div>", unsafe_allow_html=True)
str_lit.markdown("<br>", unsafe_allow_html=True)

# --- SECCIÓN 1: BUSCADOR UNIVERSAL Y AUDITORÍA AVANZADA DE SOLANA (100% REAL EN VIVO & INFORMATIVO) ---
str_lit.subheader("🔍 Buscador Universal y Auditoría On-Chain (Información y Significado)")
str_lit.markdown("<p style='font-size: 0.9rem; color: #94A3B8;'>Inspecciona de forma real cualquier Token, Wallet, Contrato o Firma en la blockchain de Solana. Obtén todos los datos técnicos, su significado exacto y la cartola de movimientos para tu propio análisis.</p>", unsafe_allow_html=True)

target_input = str_lit.text_input("Ingresa Mint de Token, Wallet o Firma de Transacción (TXID):", value="EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v")

if str_lit.button("Consultar Información On-Chain con AngeL"):
    with str_lit.spinner("Extrayendo datos directos de la blockchain de Solana en tiempo real..."):
        query = target_input.strip()
        
        # 1. Consulta si es una Firma de Transacción (TXID)
        if len(query) >= 80:
            str_lit.markdown("### 📌 Información de Firma de Transacción (TXID)")
            str_lit.code(query, language="text")
            try:
                rpc_payload = {
                    "jsonrpc": "2.0", "id": 1,
                    "method": "getTransaction",
                    "params": [query, {"encoding": "jsonParsed", "maxSupportedTransactionVersion": 0}]
                }
                res = requests.post("https://api.mainnet-beta.solana.com", json=rpc_payload, timeout=8)
                tx_data = res.json().get("result")
                
                if tx_data:
                    err = tx_data.get("meta", {}).get("err")
                    status_text = "Transacción Fallida / Con errores" if err else "Transacción Exitosa y Confirmada en Bloque"
                    fee = tx_data.get("meta", {}).get("fee", 0) / 1e9
                    slot = tx_data.get("slot")
                    block_time = tx_data.get("blockTime")
                    time_str = datetime.fromtimestamp(block_time).strftime('%Y-%m-%d %H:%M:%S') if block_time else "N/A"
                    
                    str_lit.markdown(f"""
                        <div class='data-metric-box'>
                            <b>DETALLES DE LA TRANSACCIÓN:</b><br>
                            • <b>Estado en Red:</b> {status_text} <i>(Indica si la operación se ejecutó correctamente o falló).</i><br>
                            • <b>Número de Bloque (Slot):</b> {slot}<br>
                            • <b>Fecha y Hora:</b> {time_str}<br>
                            • <b>Comisión Pagada (Fee):</b> {fee} SOL <i>(Costo cobrado por la red para procesar la transacción).</i>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    str_lit.error("La firma ingresada no se encuentra registrada o no ha sido propagada en la red principal.")
            except Exception as e:
                str_lit.error(f"Error de conexión RPC: {e}")

        # 2. Si es cuenta, wallet o token mint (32-44 caracteres)
        elif len(query) >= 32 and len(query) <= 44:
            str_lit.markdown("### 🛡️ Información Técnica y Cartola de Movimientos On-Chain")
            str_lit.code(query, language="text")
            
            mint_authority_status = "No aplicable (Cuenta de Usuario / Sistema)"
            freeze_authority_status = "No aplicable (Cuenta de Usuario / Sistema)"
            account_owner = "Desconocido"
            balance_sol = 0.0
            
            # Consulta RPC nativa real
            try:
                rpc_payload = {
                    "jsonrpc": "2.0", "id": 1,
                    "method": "getAccountInfo",
                    "params": [query, {"encoding": "jsonParsed"}]
                }
                rpc_res = requests.post("https://api.mainnet-beta.solana.com", json=rpc_payload, timeout=6)
                account_info = rpc_res.json().get("result", {}).get("value")
                
                if account_info:
                    balance_sol = account_info.get("lamports", 0) / 1e9
                    account_owner = account_info.get("owner", "N/A")
                    data_parsed = account_info.get("data", {}).get("parsed", {})
                    
                    if isinstance(data_parsed, dict) and data_parsed.get("type") == "mint":
                        info = data_parsed.get("info", {})
                        m_auth = info.get("mintAuthority")
                        f_auth = info.get("freezeAuthority")
                        
                        mint_authority_status = f"REVOCADO (Ninguna dirección controla la emisión de nuevos tokens). Detalle: {m_auth}" if m_auth is None else f"ACTIVO (La dirección {m_auth} puede crear más tokens)."
                        freeze_authority_status = f"REVOCADO (Nadie puede congelar fondos en las cuentas). Detalle: {f_auth}" if f_auth is None else f"ACTIVO (La dirección {f_auth} puede congelar fondos)."
            except Exception:
                pass

            # Consulta de mercado real vía Dexscreener
            pair_data = None
            try:
                res = requests.get(f"https://api.dexscreener.com/latest/dex/tokens/{query}", timeout=5)
                pairs = res.json().get("pairs", [])
                if pairs:
                    pair_data = pairs[0]
                else:
                    res_search = requests.get(f"https://api.dexscreener.com/latest/dex/search?q={query}", timeout=5)
                    solana_pairs = [p for p in res_search.json().get("pairs", []) if p.get("chainId") == "solana"]
                    if solana_pairs:
                        pair_data = solana_pairs[0]
            except Exception:
                pass

            if pair_data:
                token_name = pair_data.get("baseToken", {}).get("name", "Desconocido")
                token_symbol = pair_data.get("baseToken", {}).get("symbol", "TOKEN")
                price_usd = pair_data.get("priceUsd", "0.00")
                liquidity = pair_data.get("liquidity", {}).get("usd", 0)
                volume_h24 = pair_data.get("volume", {}).get("h24", 0)
                fdv = pair_data.get("fdv", 0)
                dex_name = pair_data.get("dexId", "DEX").upper()
                
                str_lit.markdown(f"""
                    <div class='data-metric-box'>
                        <b>📊 DATOS DE MERCADO Y CONTRATO:</b><br>
                        • <b>Nombre del Token:</b> {token_name} ({token_symbol})<br>
                        • <b>Plataforma DEX:</b> {dex_name}<br>
                        • <b>Precio Actual:</b> ${price_usd} USD<br>
                        • <b>Liquidez Total en Pool:</b> ${liquidity:,.2f} USD <i>(Significado: Dinero disponible en el fondo común para facilitar compra y venta).</i><br>
                        • <b>Volumen (24h):</b> ${volume_h24:,.2f} USD <i>(Significado: Monto total negociado por los usuarios en el último día).</i><br>
                        • <b>FDV (Valor Total Diluido):</b> ${fdv:,.2f} USD<br><br>
                        
                        <b>🔒 ESTADO DE AUTORIDADES:</b><br>
                        • <b>Mint Authority (Autoridad de Emisión):</b> {mint_authority_status}<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;<i>Significado: Define si se pueden acuñar más monedas en el futuro. Si está revocado, la cantidad máxima es fija. Si está activo, el creador puede emitir más oferta.</i><br><br>
                        • <b>Freeze Authority (Autoridad de Congelamiento):</b> {freeze_authority_status}<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;<i>Significado: Define si una entidad externa puede bloquear los tokens en tu billetera. Si está revocado, las cuentas operan con total libertad.</i>
                    </div>
                """, unsafe_allow_html=True)
            else:
                str_lit.markdown(f"""
                    <div class='data-metric-box'>
                        <b>👤 INFORMACIÓN DE CUENTA / WALLET:</b><br>
                        • <b>Dirección Analizada:</b> {query}<br>
                        • <b>Propietario del Programa (Owner):</b> {account_owner} <i>(Significado: Identifica si es una cuenta del sistema, un token o un programa inteligente).</i><br>
                        • <b>Balance Actual en Wallet:</b> {balance_sol:,.4f} SOL<br>
                        • <b>Mint Authority:</b> {mint_authority_status}<br>
                        • <b>Freeze Authority:</b> {freeze_authority_status}<br>
                        • <b>Nota Informativa:</b> Corresponde a una dirección de cuenta o contrato interno sin pares comerciales públicos directos en DEXes principales.
                    </div>
                """, unsafe_allow_html=True)

            # --- CARTOLA DE MOVIMIENTOS RECIENTES (HISTORIAL ON-CHAIN) ---
            str_lit.markdown("#### 📜 Cartola de Movimientos Recientes (Historial On-Chain)")
            str_lit.markdown("<p style='font-size: 0.85rem; color: #94A3B8;'>Registro cronológico de las últimas transacciones confirmadas en la blockchain asociadas a esta dirección:</p>", unsafe_allow_html=True)
            
            try:
                sig_payload = {
                    "jsonrpc": "2.0", "id": 1,
                    "method": "getSignaturesForAddress",
                    "params": [query, {"limit": 5}]
                }
                sig_res = requests.post("https://api.mainnet-beta.solana.com", json=sig_payload, timeout=6)
                signatures_list = sig_res.json().get("result", [])
                
                if signatures_list:
                    for idx, tx_item in enumerate(signatures_list, 1):
                        sig = tx_item.get("signature", "N/A")
                        slot = tx_item.get("slot", "N/A")
                        err = tx_item.get("err")
                        status_str = "Fallida / Con error" if err else "Exitosa"
                        block_time = tx_item.get("blockTime")
                        time_str = datetime.fromtimestamp(block_time).strftime('%Y-%m-%d %H:%M:%S') if block_time else "Registrada"
                        
                        str_lit.markdown(f"""
                            <div style='background: rgba(15, 23, 42, 0.6); border-left: 3px solid #38BDF8; padding: 10px; margin-bottom: 8px; border-radius: 4px; font-size: 0.85rem;'>
                                <b>Movimiento #{idx}</b> | Estado: {status_str}<br>
                                <b>Fecha y Hora:</b> {time_str} (Bloque/Slot: {slot})<br>
                                <b>Firma de Transacción (TXID):</b> <code style='color:#FDE047;'>{sig}</code>
                            </div>
                        """, unsafe_allow_html=True)
                else:
                    str_lit.info("No se registran transacciones recientes públicas para este objetivo.")
            except Exception as e:
                str_lit.warning(f"No se pudo cargar la cartola de movimientos: {e}")

            if pair_data:
                token_symbol = pair_data.get("baseToken", {}).get("symbol", "TOKEN")
                price_usd = pair_data.get("priceUsd", "0.00")
                liquidity = pair_data.get("liquidity", {}).get("usd", 0)
                report_content = f"""==================================================
        ANGELL CIBERSEGURIDAD INTELLIGENCE
          INFORME INFORMATIVO ON-CHAIN
==================================================
Objetivo: {query}
Token: {token_name} ({token_symbol})
Precio USD: ${price_usd}
Liquidez: ${liquidity:,.2f}
Mint Authority: {mint_authority_status}
Freeze Authority: {freeze_authority_status}
==================================================
"""
                str_lit.markdown("<br>", unsafe_allow_html=True)
                str_lit.download_button(
                    label="📥 Descargar Informe y Cartola en TXT",
                    data=report_content,
                    file_name=f"Informe_{token_symbol}.txt",
                    mime="text/plain"
                )
        else:
            str_lit.error("Formato no reconocido. Ingrese una dirección válida de Solana (32-44 caracteres) o una firma de transacción completa.")

str_lit.markdown("<br>", unsafe_allow_html=True)

# --- SECCIÓN 2: MONITOREO EN VIVO ---
str_lit.subheader("📈 Monitoreo de Referencia - Red Solana")
str_lit.markdown("<p style='font-size: 0.9rem; color: #94A3B8;'>Panel de referencia con precios y datos actualizados para evaluar transacciones y operaciones en el ecosistema.</p>", unsafe_allow_html=True)

if str_lit.button("⚡ Actualizar Valores de Mercado"):
    str_lit.toast("¡Valores de mercado sincronizados con la Red Principal!", icon="🚀")

def fetch_live_solana_market():
    tokens = [
        ("So11111111111111111111111111111111111111112", "Solana", "SOL"),
        ("JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN", "Jupiter", "JUP"),
        ("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", "USD Coin", "USDC"),
        ("EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm", "Dogwifhat", "WIF"),
        ("DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263", "Bonk", "BONK"),
        ("jito4APyf642JPZPx3hGc6WWJ8zPKtU84PczSPYnQ6A", "Jito", "JTO")
    ]
    results = []
    for mint, name, sym in tokens:
        try:
            res = requests.get(f"https://api.dexscreener.com/latest/dex/tokens/{mint}", timeout=3)
            pairs = res.json().get("pairs", [])
            if pairs:
                p = pairs[0]
                results.append({
                    "mint": mint, "symbol": sym, "name": name,
                    "price": p.get("priceUsd", "0.00"),
                    "change": p.get("priceChange", {}).get("h24", 0),
                    "volume": p.get("volume", {}).get("h24", 0)
                })
            else:
                results.append({"mint": mint, "symbol": sym, "name": name, "price": "0.00", "change": 0.0, "volume": 0})
        except Exception:
            results.append({"mint": mint, "symbol": sym, "name": name, "price": "0.00", "change": 0.0, "volume": 0})
    return results

live_data = fetch_live_solana_market()
if live_data:
    cols = str_lit.columns(3)
    for i, item in enumerate(live_data):
        with cols[i % 3]:
            color = "#4ade80" if item["change"] >= 0 else "#f87171"
            str_lit.markdown(f"""
                <div class='content-card' style='text-align: center; padding: 12px;'>
                    <div><b style='color:#38BDF8;'>{item['name']} ({item['symbol']})</b></div>
                    <div style='font-size: 1.1rem; color: #F8FAFC; margin: 4px 0;'>${item['price']}</div>
                    <div style='font-size: 0.8rem; color: {color};'>{item['change']:+.2f}% (24h)</div>
                    <div style='font-size: 0.75rem; color: #94A3B8; margin-top: 4px;'>Vol: ${item['volume']:,.0f} USD</div>
                </div>
            """, unsafe_allow_html=True)
            str_lit.markdown("<div class='gold-code-box'>", unsafe_allow_html=True)
            str_lit.code(item['mint'], language="text")
            str_lit.markdown("</div>", unsafe_allow_html=True)

str_lit.markdown(f"<p style='text-align: right; font-size: 0.75rem; color: #64748b;'>Última consulta: {datetime.now().strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)
str_lit.markdown("<br>", unsafe_allow_html=True)

# --- SECCIÓN 3: SERVICIOS PROFESIONALES Y SOC 24/7 (PRECIOS DE OFERTA COMPETITIVOS) ---
str_lit.subheader("🛡️ Servicios de Ciberseguridad Defensiva y SOC 24/7")
str_lit.markdown("<p style='font-size: 0.9rem; color: #94A3B8;'>Protege tu infraestructura corporativa, aplicaciones móviles y sitios web frente a brechas con tarifas especiales de oferta adaptadas al mercado actual y disponibilidad 24/7.</p>", unsafe_allow_html=True)

col_s1, col_s2, col_s3 = str_lit.columns(3)

with col_s1:
    str_lit.markdown("""
        <div class='content-card'>
            <h4 style='color: #F8FAFC; margin-top:0;'>🛡️ SOC 24/7 (Contrato)</h4>
            <p style='font-size: 0.85rem; color: #94A3B8;'>Monitoreo continuo de red, detección de intrusiones y respuesta a incidentes.</p>
            <div style='text-decoration: line-through; color: #94A3B8; font-size: 0.9rem;'>$1,500 USD</div>
            <div class='price-tag'>$1000 USD <span style='font-size:0.7rem; color:#38BDF8;'>/ mes (Oferta)</span></div>
    """, unsafe_allow_html=True)
    if str_lit.button("Contratar SOC 24/7"):
        str_lit.success(f"Redirigiendo a pasarela de pago segura. Tesorería: {TREASURY_WALLET_ADDRESS}")
    str_lit.markdown("</div>", unsafe_allow_html=True)

with col_s2:
    str_lit.markdown("""
        <div class='content-card'>
            <h4 style='color: #F8FAFC; margin-top:0;'>🌐 Auditoría Web</h4>
            <p style='font-size: 0.85rem; color: #94A3B8;'>Pruebas de penetración OWASP Top 10 y análisis de vulnerabilidades.</p>
            <div style='text-decoration: line-through; color: #94A3B8; font-size: 0.9rem;'>$850 USD</div>
            <div class='price-tag'>$500 USD <span style='font-size:0.7rem; color:#38BDF8;'>/ único (Oferta)</span></div>
    """, unsafe_allow_html=True)
    if str_lit.button("Contratar Auditoría Web"):
        str_lit.success(f"Iniciando solicitud de auditoría web vía enlace oficial.")
    str_lit.markdown("</div>", unsafe_allow_html=True)

with col_s3:
    str_lit.markdown("""
        <div class='content-card'>
            <h4 style='color: #F8FAFC; margin-top:0;'>📱 Auditoría Android</h4>
            <p style='font-size: 0.85rem; color: #94A3B8;'>Ingeniería inversa, análisis de APK, cifrado y validación de APIs móviles.</p>
            <div style='text-decoration: line-through; color: #94A3B8; font-size: 0.9rem;'>$850 USD</div>
            <div class='price-tag'>$500 USD <span style='font-size:0.7rem; color:#38BDF8;'>/ único (Oferta)</span></div>
    """, unsafe_allow_html=True)
    if str_lit.button("Contratar Auditoría Android"):
        str_lit.success(f"Preparando entorno de análisis móvil para tu app.")
    str_lit.markdown("</div>", unsafe_allow_html=True)

str_lit.markdown("<br>", unsafe_allow_html=True)

# --- SECCIÓN 4: PASARELAS DE PAGO Y MEDIOS MULTIPLES (Actualizado a 2 columnas) ---
str_lit.subheader("💳 Medios de Pago")
str_lit.markdown("<p style='font-size: 0.9rem; color: #94A3B8;'>Paga tus servicios de ciberseguridad con criptomonedas instantáneas, pasarelas DeFi o PayPal.</p>", unsafe_allow_html=True)

col_p1, col_p2 = str_lit.columns(2)

with col_p1:
    str_lit.markdown("""
        <div class='content-card' style='text-align: center;'>
            <h4 style='color: #F8FAFC;'>🟡 Pagar con PayPal</h4>
            <p style='font-size: 0.8rem; color: #94A3B8;'>Tarjetas y saldo PayPal.</p>
    """, unsafe_allow_html=True)
    str_lit.link_button("Pagar vía PayPal", PAYPAL_ME_LINK)
    str_lit.markdown("</div>", unsafe_allow_html=True)

with col_p2:
    str_lit.markdown("""
        <div class='content-card' style='text-align: center;'>
            <h4 style='color: #F8FAFC;'>🪐 Pagar con Solana</h4>
            <p style='font-size: 0.8rem; color: #94A3B8;'>Transferencia a tesorería.</p>
    """, unsafe_allow_html=True)
    str_lit.code(TREASURY_WALLET_ADDRESS, language="text")
    str_lit.link_button("Pagar en DEX (Jupiter)", JUPITER_ROUTER_URL)
    str_lit.markdown("</div>", unsafe_allow_html=True)

str_lit.markdown("<br>", unsafe_allow_html=True)

# --- SECCIÓN 5: PROTOCOLOS Y RED DE ENLACES OFICIALES ---
str_lit.subheader("⚡ Protocolos, Patrocinios Diarios y Red de Afiliados Masivos")
str_lit.markdown("<p style='font-size: 0.9rem; color: #94A3B8;'>Acceso directo a herramientas de infraestructura, agregadores, bots de trading y servicios de patrocinio diario integrados con tu cuenta y referidos para ingresos recurrentes.</p>", unsafe_allow_html=True)

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

    str_lit.markdown("""
        <div class='content-card'>
            <h4 style='color: #F8FAFC; margin-top:0;'>🦊 Phantom Wallet </h4>
            <p style='font-size: 0.85rem; color: #94A3B8;'>Billetera oficial de Solana con comisiones de referido diarias.</p>
    """, unsafe_allow_html=True)
    str_lit.link_button("Instalar Phantom (Ref)", PHANTOM_AFFILIATE_URL)
    str_lit.markdown("</div>", unsafe_allow_html=True)

    str_lit.markdown("""
        <div class='content-card'>
            <h4 style='color: #F8FAFC; margin-top:0;'>🤖 Banana Gun Sniper Bot</h4>
            <p style='font-size: 0.85rem; color: #94A3B8;'>Bot de francotirador para tokens con comisiones compartidas.</p>
    """, unsafe_allow_html=True)
    str_lit.link_button("Abrir Banana Gun Bot", BANANA_GUN_BOT_URL)
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

    str_lit.markdown("""
        <div class='content-card'>
            <h4 style='color: #F8FAFC; margin-top:0;'>🐂 BullX Terminal</h4>
            <p style='font-size: 0.85rem; color: #94A3B8;'>Terminal de trading profesional para memecoins en Solana.</p>
    """, unsafe_allow_html=True)
    str_lit.link_button("Abrir BullX Terminal", BULKR_TRADING_URL)
    str_lit.markdown("</div>", unsafe_allow_html=True)

    str_lit.markdown("""
        <div class='content-card'>
            <h4 style='color: #F8FAFC; margin-top:0;'>⚡ Maestro Sniper Bot</h4>
            <p style='font-size: 0.85rem; color: #94A3B8;'>Automatización de compra y venta rápida con referidos.</p>
    """, unsafe_allow_html=True)
    str_lit.link_button("Abrir Maestro Bot", MAESTRO_BOT_URL)
    str_lit.markdown("</div>", unsafe_allow_html=True)

str_lit.markdown("<br>", unsafe_allow_html=True)

# --- PIE DE PÁGINA ---
str_lit.markdown("<hr style='border-color: rgba(56, 189, 248, 0.1);'>", unsafe_allow_html=True)
str_lit.markdown(f"""
    <div style='text-align: center; font-size: 0.75rem; color: #64748b; padding: 10px;'>
        AngeL Ciberseguridad Intelligence • Servicios profesionales SOC 24/7 y pasarelas de afiliación global.<br>
        Wallet Tesorería Principal (Phantom): <code>{TREASURY_WALLET_ADDRESS}</code>
    </div>
""", unsafe_allow_html=True)
