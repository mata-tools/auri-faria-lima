"""Gera o HTML do e-mail Auri Faria Lima (corretores) — fonte única para prévia e publicação.

Uso:
  python3 build.py preview   -> preview.html com imagens incorporadas (abre localmente)
  python3 build.py publish https://<projeto>.pages.dev -> index.html com URLs HTTPS absolutas
"""
import base64, sys, pathlib, urllib.parse

ROOT = pathlib.Path(__file__).parent
MODE = sys.argv[1] if len(sys.argv) > 1 else "preview"
BASE = sys.argv[2].rstrip("/") if len(sys.argv) > 2 else ""

# ---- Parâmetros da campanha -------------------------------------------------
DIA, MES = "14", "outubro"            # data de ENVIO (a confirmar)
CAMPAIGN = "auri_corretores_email_03"
PREHEADER = ("Fit-out completo instalado: uma laje entra em operação em 1 a 2 meses. "
             "Argumentos prontos para levar ao seu cliente.")
WHATS = "5511994174021"

def utm(url, content):
    q = urllib.parse.urlencode({"utm_source": "rd_station", "utm_medium": "email",
                                "utm_campaign": CAMPAIGN, "utm_content": content})
    return f"{url}{'&' if '?' in url else '?'}{q}"

def wa(msg, content):
    return utm(f"https://wa.me/{WHATS}?text={urllib.parse.quote_plus(msg)}", content)

SITE = "https://www.aurifarialima.com.br/"
MSG_VISITA = (f"Olá, recebi o e-mail do dia {DIA} de {MES} do Auri Faria Lima para corretores e "
              "parceiros e gostaria de agendar uma visita para apresentar as lajes prontas a um cliente.")
MSG_MATERIAIS = (f"Olá, recebi o e-mail do dia {DIA} de {MES} do Auri Faria Lima para corretores e "
                 "parceiros e gostaria de receber fotos e materiais de apresentação do empreendimento.")

def img(name):
    p = ROOT / "assets" / name
    if MODE == "preview":
        mime = "image/png" if name.endswith(".png") else "image/jpeg"
        return f"data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"
    return f"{BASE}/assets/{name}"

# ---- Tokens (paleta oficial) -------------------------------------------------
BROWN, COFFEE, GRAPHITE = "#4A2616", "#2A1710", "#3A332E"
CHAMPAGNE, BRONZE, WHITE = "#F3E9D5", "#C69A4C", "#FFFFFF"
FF = "'Raleway',Arial,Helvetica,sans-serif"

def p(text, size=16, lh=26, color=GRAPHITE, extra=""):
    return (f'<p style="margin:0;font-family:{FF};font-size:{size}px;line-height:{lh}px;'
            f'color:{color};font-weight:400;text-align:left;{extra}">{text}</p>')

def label(text, color=BROWN, extra=""):
    return p(text, 12, 20, color, f"letter-spacing:1.5px;{extra}")

def row(inner, pad="0 42px 32px", bg=WHITE, cls="px"):
    return (f'<tr><td bgcolor="{bg}" class="{cls}" style="padding:{pad};background-color:{bg};">'
            f'{inner}</td></tr>')

# ---- Blocos -----------------------------------------------------------------
stats = [("1 a 2 meses", "para uma laje entrar em operação"),
         ("1.940 m²", "laje típica BOMA, sem pilares internos"),
         ("100%", "da carga coberta por geradores, inclusive ar-condicionado")]
stat_cells = "".join(
    f'<td class="stack" valign="top" width="33.33%" style="width:33.33%;padding:0 {0 if i == 2 else 14}px 0 0;vertical-align:top;">'
    f'<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr>'
    f'<td style="border-top:2px solid {BRONZE};padding:14px 0 18px;">'
    f'<p style="margin:0 0 6px;font-family:{FF};font-size:26px;line-height:30px;font-weight:700;color:{BROWN};'
    f'letter-spacing:-.4px;white-space:nowrap;">{n}</p>'
    f'{p(t, 13, 20, GRAPHITE)}</td></tr></table></td>'
    for i, (n, t) in enumerate(stats))

installed = [
    ("Cabeamento CAT-6A e rack em cada andar", "Sem passar cabo nem montar patch panel."),
    ("Nobreak (UPS) por andar", "Na sala técnica de cada pavimento, para a continuidade de TI."),
    ("Piso elevado de aço", "Elétrica e dados pelo entrepiso: mudar o layout não exige obra."),
    ("Climatização com controle por sala", "Com renovação total do ar a cada 47 minutos."),
    ("Automação integrada (BMS)", "Protocolo aberto para iluminação, persianas, climatização e acesso."),
    ("Submedição de energia por andar", "Cada ocupante paga o próprio consumo, medido."),
]
installed_rows = "".join(
    f'<tr><td style="border-top:1px solid {CHAMPAGNE};padding:14px 0;">'
    f'<p style="margin:0;font-family:{FF};font-size:16px;line-height:26px;color:{GRAPHITE};">'
    f'<span style="color:{BROWN};font-weight:700;">{a}</span><br>{b}</p></td></tr>'
    for a, b in installed)

args = [
    ("PARA O CFO", "Compare custo total de ocupação, não o aluguel nominal. Obra de implantação, "
     "CAPEX de infraestrutura e meses de espera já estão resolvidos no imóvel."),
    ("PARA FACILITIES E TI", "Geradores para 100% da carga, com autonomia mínima de 24 horas, "
     "nobreak por andar e automação central em protocolo aberto."),
    ("PARA RH E ESG", "LEED Platinum e Healthy Building Certificate: desempenho auditado, "
     "com ciclovia da Faria Lima a 20 metros e restaurante com terraço no edifício."),
]
arg_rows = "".join(
    f'<tr><td style="padding:0 0 {0 if i == 2 else 22}px;">'
    f'{label(k, BROWN, "margin-bottom:4px;")}{p(v, 16, 26, COFFEE)}</td></tr>'
    for i, (k, v) in enumerate(args))

commission = [("1,25 aluguel", "em contratos de até 59 meses"),
              ("2 aluguéis", "em contratos de 60 meses ou mais"),
              ("+ 0,25 aluguel", "de bonificação para contratos assinados até 31/12/2026")]
comm_rows = "".join(
    f'<tr><td style="border-top:1px solid {BRONZE};padding:14px 0;">'
    f'<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr>'
    f'<td class="stack" width="42%" valign="top" style="width:42%;vertical-align:top;padding-right:12px;">'
    f'<p style="margin:0;font-family:{FF};font-size:20px;line-height:26px;font-weight:700;color:{BROWN};white-space:nowrap;">{a}</p></td>'
    f'<td class="stack" valign="top" style="vertical-align:top;">{p(b, 16, 26, GRAPHITE)}</td>'
    f'</tr></table></td></tr>'
    for a, b in commission)

def button(text, href):
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr>'
            f'<td align="center" bgcolor="{BROWN}" style="background:{BROWN};border-radius:6px;padding:0;">'
            f'<!--[if mso]><v:rect xmlns:v="urn:schemas-microsoft-com:vml" href="{href}" style="height:52px;v-text-anchor:middle;width:516px;" stroked="f" fillcolor="{BROWN}"><center style="color:#FFFFFF;font-family:Arial,sans-serif;font-size:13px;letter-spacing:1px;">{text}</center></v:rect><![endif]-->'
            f'<!--[if !mso]><!--><a href="{href}" target="_blank" style="display:block;background:{BROWN};'
            f'border-radius:6px;padding:17px 16px;font-family:{FF};font-size:13px;line-height:18px;'
            f'letter-spacing:1px;color:#FFFFFF;text-decoration:none;text-align:center;font-weight:400;">{text}</a><!--<![endif]-->'
            f'</td></tr></table>')

H = f"""<!DOCTYPE html>
<html lang="pt-BR" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="x-apple-disable-message-reformatting">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>Auri Faria Lima: pronto para operar</title>
<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;700&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0;padding:0;-webkit-text-size-adjust:100%;}}
table{{border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt;}}
img{{border:0;-ms-interpolation-mode:bicubic;}}
a{{color:inherit;}}
@media (max-width:620px){{
 .outer{{padding:0!important;}}
 .container{{width:100%!important;}}
 .px{{padding-left:24px!important;padding-right:24px!important;}}
 .stack{{display:block!important;width:100%!important;padding-right:0!important;}}
 .h1{{font-size:36px!important;line-height:40px!important;}}
 .gal td{{padding:2px!important;}}
}}
</style>
<!--[if mso]><style>p,h1,a,span,td{{font-family:Arial,Helvetica,sans-serif!important;}}</style>
<xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
</head>
<body style="margin:0;padding:0;background:#FFFFFF;color:{COFFEE};">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:#FFFFFF;">{PREHEADER}{" &#847; &zwnj; &nbsp;" * 40}</div>
<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;background:#FFFFFF;">
<tr><td align="center" class="outer" style="padding:24px 0;">
<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0"><tr><td><![endif]-->
<table role="presentation" cellpadding="0" cellspacing="0" width="600" class="container" style="width:100%;max-width:600px;background:#FFFFFF;">

<!-- Header -->
<tr><td bgcolor="{CHAMPAGNE}" align="center" style="padding:26px 0;background-color:{CHAMPAGNE};">
<a href="{utm(SITE, 'header_site')}" target="_blank" style="text-decoration:none;display:inline-block;">
<img src="{img('logo-auri.png')}" width="144" alt="Auri Faria Lima" style="display:block;width:144px;max-width:144px;height:auto;border:0;margin:0 auto;"></a>
</td></tr>
<tr><td style="padding:0;line-height:0;font-size:0;">
<a href="{utm(SITE, 'header_site')}" target="_blank" style="display:block;line-height:0;">
<img src="{img('recepcao.jpg')}" width="600" alt="Recepção corporativa do Auri Faria Lima, com painéis de LED na entrada" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a>
</td></tr>

<!-- Abertura -->
{row(label("PARA CORRETORES E PARCEIROS", BROWN) +
     f'<h1 class="h1" style="margin:14px 0 22px;font-family:{FF};font-size:44px;line-height:48px;letter-spacing:-1.5px;font-weight:700;color:{COFFEE};text-align:left;">Pronto para operar.</h1>' +
     p("No Auri Faria Lima, a laje que o seu cliente visita é a laje em que ele vai trabalhar. "
       "O edifício está concluído e o fit-out está instalado: sem obra de implantação, "
       "uma laje entra em operação em 1 a 2 meses.", 16, 26, GRAPHITE),
     "40px 42px 30px")}

<!-- Números -->
{row(f'<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr>{stat_cells}</tr></table>', "0 42px 34px")}

<!-- O que já está instalado -->
{row(label("O QUE O SEU CLIENTE NÃO PRECISA CONSTRUIR", BROWN, "margin-bottom:6px;") +
     f'<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;">{installed_rows}'
     f'<tr><td style="border-top:1px solid {CHAMPAGNE};font-size:0;line-height:0;">&nbsp;</td></tr></table>',
     "0 42px 30px")}

<!-- Galeria 13º -->
{row(f'<table role="presentation" cellpadding="0" cellspacing="0" width="100%" class="gal" style="width:100%;table-layout:fixed;"><tr>'
     f'<td width="50%" style="padding:0 3px 0 0;"><img src="{img("rooftop-terraco.jpg")}" width="255" alt="Terraço do 13º pavimento com jardim vertical" style="display:block;width:100%;height:auto;border:0;"></td>'
     f'<td width="50%" style="padding:0 0 0 3px;"><img src="{img("rooftop-interno.jpg")}" width="255" alt="Salão do 13º pavimento em travertino e madeira" style="display:block;width:100%;height:auto;border:0;"></td>'
     f'</tr></table>' +
     p("13º pavimento: travertino em piso e paredes, jardim vertical e bares de apoio entregues. "
       "O que se vê na visita é o que o ocupante recebe.", 13, 20, GRAPHITE, "margin-top:12px;"),
     "0 42px 38px")}

<!-- Argumentos por decisor -->
{row(f'<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;border-collapse:separate;background:{CHAMPAGNE};border-radius:14px;">'
     f'<tr><td class="px" style="padding:30px 32px;">'
     f'<p style="margin:0 0 20px;font-family:{FF};font-size:20px;line-height:28px;font-weight:700;color:{COFFEE};">Como apresentar ao seu cliente</p>'
     f'<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;">{arg_rows}</table>'
     f'</td></tr></table>', "0 24px 36px", WHITE, "")}

<!-- Comissionamento -->
{row(label("POLÍTICA DE COMISSIONAMENTO", BROWN, "margin-bottom:6px;") +
     f'<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;">{comm_rows}'
     f'<tr><td style="border-top:1px solid {BRONZE};font-size:0;line-height:0;">&nbsp;</td></tr></table>' +
     p("Política válida até 31/12/2026.", 13, 20, GRAPHITE, "margin-top:10px;"),
     "0 42px 38px")}

<!-- CTA -->
{row(p("Tem um cliente em crescimento ou com contrato vencendo nos próximos anos? "
       "Leve-o para ver a laje pronta. O time comercial da Nexland organiza a visita com você.", 16, 26, GRAPHITE),
     "0 42px 22px")}
{row(button("AGENDAR VISITA PELO WHATSAPP", wa(MSG_VISITA, "cta_whatsapp_comercial")), "0 42px 8px")}
{row(f'<a href="{wa(MSG_MATERIAIS, "cta_whatsapp_materiais")}" target="_blank" style="display:block;padding:12px 0;font-family:{FF};font-size:12px;line-height:20px;letter-spacing:1px;color:{BROWN};text-align:center;text-decoration:underline;">SOLICITAR MATERIAIS DO EMPREENDIMENTO</a>', "0 42px 26px")}

<!-- Fechamento -->
{row(p("Se preferir falar por e-mail:", 13, 20, GRAPHITE, "text-align:center;") +
     p(f'<a href="mailto:comercialsp@nexland.com.br" style="color:{BROWN};text-decoration:underline;">comercialsp@nexland.com.br</a>', 13, 20, BROWN, "text-align:center;margin-top:4px;") +
     p(f'Saiba mais sobre o empreendimento: <a href="{utm(SITE, "link_site")}" target="_blank" style="color:{BROWN};text-decoration:underline;">aurifarialima.com.br</a>', 13, 20, GRAPHITE, "text-align:center;margin-top:18px;") +
     p("Equipe Comercial Nexland · Auri Faria Lima", 13, 20, COFFEE, "text-align:center;margin-top:18px;") +
     p("Rua Elvira Ferraz, 440 · Nova Faria Lima · São Paulo", 13, 20, GRAPHITE, "text-align:center;"),
     "0 42px 34px")}

<!-- Rodapé -->
<tr><td bgcolor="{CHAMPAGNE}" style="padding:32px 24px;background-color:{CHAMPAGNE};">
<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;table-layout:fixed;"><tr>
<td width="33.33%" align="center" valign="middle" style="padding:0 10px;vertical-align:middle;"><a href="{utm(SITE, 'footer_site')}" target="_blank" style="display:block;"><img src="{img('logo-auri-preto.png')}" width="110" alt="Auri Faria Lima" style="display:block;width:110px;max-width:100%;height:auto;border:0;margin:0 auto;"></a></td>
<td width="33.33%" align="center" valign="middle" style="padding:0 10px;vertical-align:middle;"><a href="{utm('https://nexland.com.br/', 'footer_nexland')}" target="_blank" style="display:block;"><img src="{img('logo-nexland-preto.png')}" width="154" alt="Nexland Properties" style="display:block;width:154px;max-width:100%;height:auto;border:0;margin:0 auto;"></a></td>
<td width="33.33%" align="center" valign="middle" style="padding:0 10px;vertical-align:middle;"><a href="{utm('https://aurinova.com.br/', 'footer_aurinova')}" target="_blank" style="display:block;"><img src="{img('logo-aurinova-preto.png')}" width="148" alt="Aurinova" style="display:block;width:148px;max-width:100%;height:auto;border:0;margin:0 auto;"></a></td>
</tr></table>
</td></tr>

</table>
<!--[if mso]></td></tr></table><![endif]-->
</td></tr>
</table>
</body>
</html>
"""

out = ROOT / ("preview.html" if MODE == "preview" else "index.html")
out.write_text(H, encoding="utf-8")
print(out, len(H))
