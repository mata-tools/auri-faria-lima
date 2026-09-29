# Auri Faria Lima · Plano do filme (v0 para discussão)

Status (Motion Master): **Estudo → pré-animatic**. Nada aqui é copy final nem seleção de imagem aprovada.
Data: 29/09/2026 · Autoria: MATA (Caroline + Claude)

---

## 1. O desafio, como eu entendi

1. Fazer **um filme premium do Auri Faria Lima** misturando **foto com motion** (as fotos são o melhor ativo) e **vídeo real** (fraco como conjunto, mas necessário para mostrar movimento).
2. Referência de nível: os filmes da **Maison Flamboyant** (horizontal e vertical, produzidos pela Aliv).
3. Regra de ouro do cliente: **cada informação dita precisa estar provada pela imagem que está na tela naquele momento.** Se falamos "pé-direito de 7,83 m", a imagem é o 11º andar com o pé-direito duplo visível, e não um hall qualquer.
4. Depois do filme, **derivar uma skill** que reproduza o processo (fontes, checagem de fatos, casamento entre afirmação e imagem, gramática de motion, QA).

---

## 2. O que eu estudei e o que ainda não consegui ver

| Fonte | Status |
|---|---|
| Skill **Motion Master** (Drive `[BASE] MOTION MASTER/skill.md`) | Lida. Gates 1–5, estados de entrega e direção verificável por trecho |
| Skill **Design Master** (Drive `[BASE] DESIGN MASTER/skill.md`) | Lida |
| **Design System Auri Faria Lima V1.1** (`[TERRA MOLHADA] DESIGN SYSTEM - AURI FARIA LIMA.md`, 28/09/2026) | Lido: paleta, Raleway, logos, 60·30·10, fotografia |
| **Apresentação Comercial vigente** (`[AURI FARIA LIMA CORPORATIVO] APRESENTAÇÃO COMERCIAL COMPLETA.pdf`, v4 MULTIUSUÁRIO) | Lida por inteiro (texto) |
| Briefing **Motion para Telas de LED** v3 (regras editoriais e terminologia) | Lido |
| Feedbacks de motion da Caroline (25–28/09) | Lidos (entrada de texto por foco, sem zoom contínuo em peça estática, arco musical) |
| TEXTOS_AURI (anúncios e WhatsApp) | Lido |
| Skill `auri-comercial` | Lida, mas **está desatualizada** (ver §3) |
| **E-mail da Bárbara para o Douglas** | **Não acessei.** Não há conector de Gmail nesta sessão. Localizei os filmes da Maison no Drive pelo nome (abaixo) |
| **Filmes Maison Flamboyant** (Horizontal Final, Horizontal Final para corretores, Vertical Nexland, Vertical Parceiros) | **Localizados, mas não assistidos.** Por aqui o Drive só me devolve metadados de vídeo/imagem |
| **Fotos do kit e vídeos da Terra Molhada** | **Inventariados por pasta e nome de arquivo. Ainda não vi o conteúdo** |
| Site aurifarialima.com.br | **Bloqueado** pela rede desta sessão |

> Consequência prática: a lista de cenas abaixo está amarrada a **pastas e arquivos candidatos**, não a frames que eu tenha visto. A curadoria final exige que eu veja o material (ver §9, "O que preciso de você").

### Mapa de ativos visuais (inventário)

**Fotos: `[KIT LAJES CORPORATIVAS] AURI FARIA LIMA/FOTOS_AURI FARIA LIMA/`**
- `Recepção/`: 12 (F1601, F1701, Auri-030/039, painéis LED Blas 0017–0022, "Recepção Auri Faria Lima.jpeg")
- `Pavimentos especiais - 11° e 13º/`: 43 (F30xx–F44xx, painéis LED Blas 0038–0085)
- `Rooftop - 13º pavimento/`: 6 (_DSC3251/3401/3485/3560, 11, 12)
- `Restaurante e Terraço/`: 11 (F33xx–F36xx, "Terraco Restaurante_Painel LED")
- `Espaço Multiúso e Eventos/`: 85 (F101–F115, F403, F80x, Blas 0002–0155, painéis LED Blas 0023–0033)
- `IMAGENS 3D/`: 43 renders EFE (fachadas, acessos, hall, pavimentos, foyer, teatro, restaurante)

**Terra Molhada: `2-IMAGENS E VIDEOS/`**
- `2026/`: Corporativo (Guilherme Pucci e Sandra Blas), Espaço Multiúso (Pucci e Blas), "Fachada e interna teatro" (fotos e vídeos), fotos de celular da equipe, plantas humanizadas, "Foto painel LED restaurante + logo Auri"
- `ÁURI EVENTOS/`: Trio Core (27–30/08, IMG_75xx + vídeos), Trio Sonova (19/08, fotógrafo e equipe interna), Nutty Bavarian 30 anos (07/08), Argosy, Corporativo CORE, aniversário
- `VIDEO/` e `VIDEOS YOUTUBE/`: filmes de 2023–2024 e do YouTube (**antigos**: "Corporate Tower", monousuário, fase de obra)
- Descartar por coerência: tudo que for Aurinova 2017–2018, "Auri Corporate Tower 2023", "Completo - Old" e qualquer material que mostre marca de locatário anterior

---

## 3. Travamento de fatos (antes de qualquer animação)

As fontes se contradizem. O filme só usa o que estiver **travado**. Minha proposta é seguir a **Apresentação Comercial v4 (MULTIUSUÁRIO)** como fonte vigente e confirmar os itens marcados.

| Item | Divergência encontrada | Proposta para o filme |
|---|---|---|
| CAPEX | US$ 50 mi (skill antiga, anúncios) × **R$ 250 mi** (deck v4, briefing LED "definido") | **R$ 250 milhões em CAPEX e fit out instalados**. Confirmar |
| Modelo de ocupação | "monousuário / único proprietário" (skill, anúncios) × **multiusuário, um ou mais locatários** (deck v4, briefing LED) | Não usar "monousuário". Falar em lajes/andares disponíveis |
| Laje típica | 1.950,45 m² (skill) × 1.940,06 m² (deck v4) | Usar "lajes de até ~2.000 m² BOMA" (padrão do deck) ou omitir número |
| 13º pavimento | 769,11 m² × 842,95 m² | Não citar área; citar travertino e pé-direito 7,83 m |
| Gerador do espaço multiúso | 565 kVA (deck) × 500 kVA (dado validado no briefing) | Não citar kVA. Usar "100% da carga, 24 h de autonomia" |
| Vagas | 401 × 335 (site, segundo o briefing) | Omitir, ou confirmar 401 |
| Cabeamento | CAT6 × CAT-6A | Não citar em tela |

Regras editoriais que valem para o filme (briefing LED, skill e design system):
- Dado concreto no lugar de adjetivo. Sem superlativo, buzzword ou frase de efeito. Sem travessão no texto de tela. Escrever pelo positivo ("pronto para operar", e não "sem obras").
- O nome é sempre **Auri Faria Lima**.
- **"Espaço multiúso"**, nunca "auditório/teatro" para capacidade. **Não usar o nome do teatro reservado pela família.** "Painel de LED imersivo" é o do palco; "video walls" só para lobby e bar.
- Fachada de LED e painéis RGBW são **infraestrutura do edifício**, não benefício exclusivo de locatário.
- Nenhuma referência ao ocupante anterior (cuidado com logos e telas nas fotos e vídeos).
- "Triple A" é permitido no corte corporativo/institucional e não no de eventos.

---

## 4. Conceito proposto: "Do térreo ao rooftop"

A estrutura do filme é **uma subida pelo edifício**, parada a parada, seguindo a jornada do deck (Módulo 05). O filme ganha um fio narrativo que o espectador entende sem locução.

**Dispositivo central (a "assinatura" do motion):** um **indicador de pavimento** discreto (filete bronze vertical + rótulo em Raleway, por exemplo `TÉRREO`, `11º`, `13º`). Ele sobe entre as cenas como um elevador. Tem três funções:
1. **Resolve a regra do cliente estruturalmente:** toda afirmação fica ancorada ao andar onde a imagem foi feita. Se o rótulo diz 11º, a foto tem que ser do 11º.
2. Dá a transição-mãe do filme: um *wipe* vertical que segue as linhas da arquitetura, sem whoosh e sem efeito gratuito.
3. Traduz para motion o "organismo vivo", ordenado e clássico, do edifício.

**Quando usar foto, vídeo ou motion (regra de meio)**
| A afirmação fala de... | Meio | Exemplo |
|---|---|---|
| Espaço, material, escala, luz | **Foto** com movimento de câmera arquitetônico (push-in reto, pan lento, parallax 2.5D leve) | Travertino do 13º, pé-direito de 10,15 m |
| Algo que **muda / se move** | **Vídeo real** (obrigatório, a foto não prova) | Arquibancada recolhendo, painel LED acendendo, fachada RGBW mudando de cor, vidro que opaca |
| Algo **invisível** (desempenho, certificação) | **Motion tipográfico** sobre detalhe arquitetônico neutro | Ar renovado a cada 47 min, geradores 100%/24 h, LEED Platinum |

---

## 5. Roteiro / mapa de cenas (master 16:9, ~60 s, sem locução)

> Tempos provisórios, até existir trilha (a Motion Master proíbe declarar sincronismo sem a música). Copy de tela como **referência**, a validar. Títulos em CAIXA ALTA, Raleway Light.

| # | Tempo | Andar | Texto de tela (ref.) | Imagem que **prova** a afirmação | Candidatos (pasta/arquivo) | Meio |
|---|---|---|---|---|---|---|
| 1 | 0–5 s | Fachada | *(sem texto)* → logo | Fachada de Lew Oliver, de preferência à noite com RGBW | Vídeos "2026 Fachada e interna teatro"; 3D `EFE_01_Fachada_Frontal` (fallback) | Vídeo |
| 2 | 5–9 s | — | AURI FARIA LIMA · NOVA FARIA LIMA | Continua a fachada | idem | Vídeo + logo oficial PNG |
| 3 | 9–14 s | Térreo | PÉ-DIREITO DE 10,15 M | Hall/recepção com a altura legível no quadro (pessoa ou elevador como escala) | `Recepção/F1601`, `F1701`, "Recepção Auri Faria Lima" | Foto: tilt vertical |
| 4 | 14–20 s | 6º–9º | LAJES COLUMN-FREE · ATÉ ~2.000 M² BOMA | Laje com vão livre **sem pilar visível** no quadro | "2026 Corporativo fotos Guilherme Pucci / Sandra Blas" | Foto: dolly lateral |
| 5 | 20–25 s | 6º–9º | FIT OUT COMPLETO, PRONTO PARA OPERAR | Andar entregue com piso elevado, forro, salas e workcafé instalados | idem | Foto |
| 6 | 25–31 s | 11º | PÉ-DIREITO DE 7,83 M · TRAVERTINO ROMANO E NOGUEIRA AMERICANA | 11º com pé-direito duplo + detalhe de pedra/madeira | `Pavimentos especiais/F30xx–F44xx` | Foto: push-in + detalhe |
| 7 | 31–34 s | 11º | VIDRO QUE OPACA NO TOQUE DE UM BOTÃO | **Vidro passando de transparente a opaco** | Não localizado → **captar** (10 s de celular com gimbal) | Vídeo |
| 8 | 34–39 s | 4º | RESTAURANTE E TERRAÇO DE 389 M² | Terraço com vista para São Paulo | `Restaurante e Terraço/F33xx–F36xx` | Foto |
| 9 | 39–46 s | 1º–3º | 391 LUGARES · ATÉ 600 PESSOAS NA ÁREA LIVRE | Plateia montada → área livre (**match-cut** do mesmo ângulo ou vídeo da arquibancada recolhendo) | `Espaço Multiúso/F101–F115`, Blas; vídeos Trio/Nutty | Foto-par ou vídeo |
| 10 | 46–50 s | 1º | PAINEL DE LED IMERSIVO · 8,96 × 5,28 M | Palco com o painel **aceso** | `Auri_paineis_led@blas 0023–0033` | Foto ou vídeo |
| 11 | 50–53 s | — | AR RENOVADO A CADA 47 MIN · ENERGIA PARA 100% DA CARGA, 24 H | Detalhe arquitetônico neutro (forro, fachada) | a definir | Motion tipográfico |
| 12 | 53–57 s | 13º | ROOFTOP EM TRAVERTINO · VISTA DE SÃO PAULO | 13º com terraço e vista | `Rooftop/_DSC3251, 3401, 3485, 3560` | Foto: push-in lento, grand finale |
| 13 | 57–60 s | — | LEED PLATINUM · 5 PRÊMIOS INTERNATIONAL PROPERTY AWARDS / PRONTO PARA RECEBER A SUA EMPRESA | Fundo Café, logo dourado, contato | Logo oficial | Assinatura |

**Cortes derivados:** 30 s (cenas 1, 3, 4, 6, 9, 12, 13) e 15 s (1, 6, 12, 13). O **vertical 9:16** é **recomposto**, não recortado: foto em cima, dado no centro, assinatura embaixo. As fotos horizontais ganham *pan* vertical e o indicador de andar passa para a lateral.

**Variações por público** (se o e-mail pedir): corte **Corporativo** (cenas 3–7, 11), corte **Eventos** (8–10, sem "Triple A") e **Institucional** (este mapa completo).

---

## 6. Direção visual e de movimento

**Marca** (Design System V1.1)
- Base 60% **Café #2A1710** (telas de texto) · estrutura 30% **Marrom #4A2616 / Preto** · acento 10% **Dourado #E3BA65**. Filetes em **Bronze #C69A4C**. O gradiente Champagne→Dourado→Bronze só em títulos e filetes.
- **Raleway** Light 300 em títulos (caixa alta, tracking positivo) e Regular 400 em dado de apoio. Logo apenas como **PNG oficial**, com área de proteção, sem efeito e sem gradiente.
- Fotografia: manter a luz original, sem filtro fora da paleta, sem moldura nem caixa. **Ocultar rostos** sem autorização e **marcas de terceiros** nos vídeos de evento.

**Gramática de movimento** (poucos gestos e coerentes)
- Câmera sobre foto: push-in **reto** de 3–5%, pan lento seguindo linhas horizontais ou verticais da arquitetura. Sem rotação, sem zoom contínuo exagerado e sem Ken Burns aleatório.
- Transição-mãe: **wipe vertical "elevador"** alinhado a uma linha arquitetônica, com 0,6–0,8 s de easing suave. Corte seco só no *match-cut* plateia → área livre (cena 9), porque ali o corte **é** a informação.
- Texto: entrada **por foco** (desfocado → nítido, deslocamento curto, ~1,1 s, `power3.out`) e saída por fade curto. Esse padrão foi aprovado nos feedbacks de 28/09.
- Hold mínimo de 3 s por linha curta e 2 s por número isolado.

**Perfil de energia:** contido e crescente. Respira no térreo e nas lajes, ganha escala no 11º, faz o pico no espaço multiúso (cena 9, um acento musical) e resolve com calma no rooftop, seguido da assinatura.

**Som:** música como estrutura (condução, pico e resolução). Sem whoosh em cada entrada. Aguardo a trilha para marcar os timecodes reais de acentos.

---

## 7. O que eu faria diferente / proponho somar

1. **Matriz de prova aprovada antes do animatic.** Uma tabela "afirmação → imagem exata → andar → fonte do dado", validada pelo cliente. Como eles são muito criteriosos, é mais barato errar na tabela do que no render. A tabela da §5 é o rascunho dela.
2. **Travar os fatos primeiro** (§3). Hoje há pelo menos 5 números conflitantes entre as fontes, e o filme não pode herdar isso.
3. **Micro-captação dirigida** de 4 a 6 takes curtos (celular com gimbal, 4K, 10–15 s cada) para as afirmações que só o movimento prova: vidro opacando, arquibancada recolhendo, painel LED do palco acendendo, fachada RGBW à noite e persianas motorizadas. Isso resolve o problema de "os vídeos são ruins" sem depender deles.
4. **Master + cortes:** entregar 60 s, 30 s e 15 s, em 16:9 e 9:16, já compostos. Não fazer crop automático.
5. **Não usar IA generativa** para ambientes do Auri (o design system proíbe inventar ambiente). Parallax 2.5D sobre foto real é permitido.
6. **Atualizar a skill `auri-comercial`**, que ainda diz monousuário e US$ 50 mi. Ela contamina qualquer peça futura.

---

## 8. Esqueleto da skill que vamos derivar (`auri-video`)

Vamos registrar enquanto produzimos:
1. **Fontes de verdade** e ordem de precedência (deck vigente > briefing validado > skill comercial), com a lista de dados travados e de dados proibidos.
2. **Matriz de prova** (template) e a regra de meio foto / vídeo / motion.
3. **Inventário de ativos** por andar, com o status de cada item (protagonista, suporte, inadequado, ausente), vindo da curadoria real.
4. **Gramática de motion** do Auri: indicador de andar, wipe elevador, entrada por foco, holds.
5. **Templates** de mapa de cenas (60/30/15, 16:9/9:16, versões Corporativo, Eventos e Institucional).
6. **QA** (Motion Master qa-video + checklist do design system + checklist editorial) e **log de feedback** do cliente.

---

## 9. O que preciso de você para seguir

1. **O e-mail da Bárbara:** encaminhar o texto (ou salvar no Drive). Não tenho acesso ao Gmail aqui. Quero ver o que eles elogiaram ou pediram no filme da Maison: duração, locução ou só lettering, trilha, ritmo.
2. **Ver o material:** o Drive só me entrega metadados de mídia. Opções:
   (a) exportar **proxies leves** (720p) dos filmes da Maison e dos vídeos candidatos + **contact sheets** das pastas de foto, e subir numa pasta que eu possa baixar; ou
   (b) liberar `drive.google.com` / `drive.usercontent.google.com` no network policy do ambiente (o download ainda precisa de link com permissão).
   Obs.: este repositório é **público**, então não subir material do cliente aqui.
3. **Confirmar** CAPEX R$ 250 mi, discurso multiusuário, vagas (401?) e se o filme é institucional, corporativo ou eventos, e para qual canal.
4. **A música**, para eu fazer o mapa de acentos e o animatic.

Próximo gate: com (1)–(3) em mãos, faço a curadoria real de fotos e vídeos, fecho a matriz de prova e monto o **animatic** com copy real e holds reais.
