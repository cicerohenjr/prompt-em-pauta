# Plano de produção — Prompt em Pauta

## 1. Escopo

Produzir um episódio introdutório de podcast sobre o uso responsável de IA generativa no estudo de tecnologia, para o desafio “Criando um Podcast com IAs Generativas”, da DIO.

## 2. Definição editorial

- **Série:** Prompt em Pauta
- **Episódio:** 01
- **Tema:** Como usar a IA generativa para estudar tecnologia com mais eficiência
- **Público:** estudantes e pessoas iniciantes em TI
- **Idioma:** português brasileiro
- **Duração-alvo:** 3 a 5 minutos
- **Tom:** didático, respeitoso, acessível e prático
- **Mensagem central:** prompts claros ajudam a obter apoio mais útil, mas respostas da IA precisam de verificação e prática humana.

## 3. Etapas de produção e estado

1. **Planejamento e roteiro:** primeira versão concluída; revisar antes de entregar.
2. **Capa:** SVG está no repositório. O PNG de 1024 × 1024 está no pacote local e pode ser enviado ao GitHub.
3. **Narração:** MP3 gerado localmente com eSpeak, voz `pt-br`, velocidade 145, pitch 48 e amplitude 175.
4. **Pós-processamento:** normalização e compressão dinâmica leve; exportação em MP3 mono, 44,1 kHz, 128 kbps.
5. **Verificação técnica:** codec, duração, taxa de amostragem, canais, bitrate e nível de pico conferidos automaticamente.
6. **Verificação humana:** ouvir o áudio completo, conferir pronúncia, ritmo e possíveis artefatos.
7. **Publicação e entrega:** adicionar o MP3 ao diretório `output/` e, se necessário, a capa PNG ao GitHub; conferir links e enviar o link do repositório à DIO.

## 4. Critérios de qualidade

- O episódio responde ao tema anunciado no título.
- O exemplo de prompt é concreto e compreensível.
- O roteiro não promete resultados garantidos nem apresenta a IA como infalível.
- A fala é compreensível e o volume é consistente.
- Não há cortes abruptos, trechos duplicados ou ruídos que prejudiquem a compreensão.
- A duração final fica dentro da meta ou qualquer desvio é intencional.
- O arquivo exportado é ouvido integralmente antes de publicar.

## 5. Organização dos arquivos

- `prompts/README.md` — modelos de prompts e transparência.
- `roteiro/episodio-01.md` — roteiro e nota sobre a narração.
- `capa/capa-prompt-em-pauta.svg` — capa vetorial.
- `capa/README.md` — orientações para a capa.
- `output/README.md` — orientação e estado do áudio.
- `docs/registro-de-producao.md` — ferramentas e etapas realmente executadas.
- `docs/checklist-entrega.md` — verificação final.

## 6. Transparência

O MP3 gerado localmente usa eSpeak, uma voz sintética básica que pode soar robótica. A página pública do desafio cita ElevenLabs como ferramenta sugerida para uma voz mais humanizada. Se outra voz for gerada, registre a ferramenta e os parâmetros reais, substitua o arquivo e repita a verificação.
