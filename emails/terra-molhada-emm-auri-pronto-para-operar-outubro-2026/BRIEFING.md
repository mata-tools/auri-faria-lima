# Auri Faria Lima · E-mail 03 para corretores · "Pronto para operar"

Status: **rascunho, HTML de prévia para aprovação**. Nada foi publicado, registrado no Marketing Hub, enviado ou agendado.

## Estratégia

- **Objetivo:** gerar visitas de corretores com clientes às lajes prontas.
- **Público:** corretores e parceiros que já conhecem o Auri e receberam o e-mail de 30/09 (multiusuário + comissão).
- **Mensagem central (pilar prontidão):** fit-out completo instalado e edifício concluído, então uma laje entra em operação em 1 a 2 meses, sem obra de implantação.
- **Apoio 1:** argumentos por decisor (CFO, facilities/TI, RH/ESG) que o corretor repassa ao cliente, com o custo total de ocupação no lugar do aluguel nominal.
- **Apoio 2:** lembrete da política de comissionamento, citada uma única vez e completa.
- **Ação:** agendar visita pelo WhatsApp (principal) · solicitar materiais (secundário) · e-mail comercial como alternativa.
- **Preço:** não citado. O e-mail não disputa localização com os ícones da avenida.

## Assunto e preheader

| # | Abordagem | Assunto | Preheader |
|---|---|---|---|
| **1 (recomendado)** | Benefício | Auri Faria Lima: pronto para operar | Fit-out completo instalado: uma laje entra em operação em 1 a 2 meses. |
| **2 (A/B)** | Oportunidade comercial | O que seu cliente não precisa construir no Auri | Cabeamento, nobreak, piso elevado e automação já instalados, laje a laje. |
| 3 | Novidade | Lajes prontas no Auri: argumentos para o seu cliente | Como apresentar o Auri ao CFO, ao facilities e ao RH, com dados verificáveis. |
| 4 | Benefício | Da visita à operação em 1 a 2 meses | No Auri Faria Lima, a laje que o cliente visita é a laje em que ele vai trabalhar. |
| 5 | Oportunidade comercial | Seu cliente troca de escritório nos próximos anos? | Leve-o ao Auri: sede Triple A com fit-out instalado e comissão de até 2 aluguéis. |

**Hipótese do A/B (1 × 2):** o assunto 1 é direto e reconhecível pela marca. O 2 aposta na curiosidade prática do corretor sobre o que ele pode usar na conversa com o cliente. Medir pela taxa de cliques em `cta_whatsapp_comercial`, não só pela abertura.

O HTML já leva o preheader do par 1, acrescido de "Argumentos prontos para levar ao seu cliente."

## Imagens (acervo oficial "Imagens Auri Faria Lima Corporate")

| Uso | Arquivo de origem | Pasta | Tratamento |
|---|---|---|---|
| Foto principal | `Recepção Auri Faria Lima.jpeg` | Recepção | Corte 5:3, 1200 × 720 (2x) |
| Galeria (esquerda) | `_DSC3251.JPG` (foto @AndreStefano) | Rooftop - 13º pavimento | Corte 4:5, 560 × 700 |
| Galeria (direita) | `_DSC3512.JPG` (foto @AndreStefano) | Rooftop - 13º pavimento | Corte 4:5, 560 × 700 |
| Logos | pacote aprovado de 30/09 | EXAMPLES | Sem alteração |

Motivo: a recepção corporativa mostra a chegada ao edifício pronto (e difere da entrada usada no e-mail 02). O 13º comprova "entregue com acabamento" com travertino, jardim vertical e bares instalados. Por limitação do conector do Drive, que não baixa arquivos acima de ~5 MB, não consegui inspecionar as fotos dos pavimentos tipo e as do 11º em alta resolução.

## Dados usados e cuidados

- 1.940 m² (laje típica 6º–9º): consistente entre o deck e o Plano Comercial.
- 1 a 2 meses para operar: Plano Comercial set/2026.
- Geradores com 100% da carga, inclusive HVAC, e 24 h de autonomia; LEED Platinum; HBC; ar renovado a cada 47 min; ciclovia a 20 m: consistentes entre as fontes.
- **Não citados, por conflito entre fontes:** CAPEX (US$ 50 mi × R$ 250 MM), kVA do gerador do Multiúso (500 × 565), áreas do 5º, 10º, 11º e 13º, cadeiras do Multiúso.

## UTMs · `utm_campaign=auri_corretores_email_03`

| Posição | Destino | utm_content |
|---|---|---|
| Logo e foto do topo | aurifarialima.com.br | header_site |
| Botão principal | wa.me/5511994174021 (visita) | cta_whatsapp_comercial |
| Link secundário | wa.me/5511994174021 (materiais) | cta_whatsapp_materiais |
| Link final | aurifarialima.com.br | link_site |
| Rodapé Auri | aurifarialima.com.br | footer_site |
| Rodapé Nexland | nexland.com.br | footer_nexland |
| Rodapé Aurinova | aurinova.com.br | footer_aurinova |

utm_source=rd_station · utm_medium=email

Mensagens WhatsApp (decodificadas):
- Visita: "Olá, recebi o e-mail do dia 14 de outubro do Auri Faria Lima para corretores e parceiros e gostaria de agendar uma visita para apresentar as lajes prontas a um cliente."
- Materiais: "Olá, recebi o e-mail do dia 14 de outubro do Auri Faria Lima para corretores e parceiros e gostaria de receber fotos e materiais de apresentação do empreendimento."

## Pendências antes do pacote final

1. **Confirmar a data de envio.** Usei 14/10/2026 (quarta, duas semanas após o e-mail 02) como proposta. Ela está nas mensagens de WhatsApp. Depois de confirmada, o projeto passa a se chamar `terra-molhada-emm-auri-pronto-para-operar-{dia}-outubro-2026`.
2. **Confirmar a vigência da comissão:** 1,25 / 2 aluguéis / + 0,25 até 31/12/2026, conforme o e-mail aprovado de 30/09.
3. **Confirmar o WhatsApp 5511994174021** como canal vigente desta frente.
4. Registrar os links no Marketing Hub (aba Links parametrizados). Este ambiente não tem ferramenta de edição de células de planilha, então o registro segue pendente.
5. Após a aprovação: gerar o ZIP para o Cloudflare Pages (`python3 build.py publish https://<projeto>.pages.dev`), publicar, testar URL e assets sem login, importar no RD e fazer envio de teste.

## Verificações executadas

- HTML começa com `<!DOCTYPE html>` e não traz avisos internos nem placeholders.
- Renderizado no Chromium a ~600 px e a 375 px. A fonte web não carregou no ambiente, então a renderização valeu como teste de fallback em Arial/Helvetica (ver os PNGs).
- Todos os hrefs extraídos e decodificados; UTMs e mensagens conferidos.
- **Não verificado:** renderização em clientes de e-mail reais (Outlook, Gmail, Apple Mail) e a prévia do RD.
