# Nova narração com ElevenLabs — Episódio 01

## Objetivo

Preparar uma versão mais clara e natural do episódio **“Como usar a IA generativa para estudar tecnologia com mais eficiência”**, mantendo o roteiro aprovado e usando a voz **The Professional Instructor** com texto em português do Brasil.

**Importante:** o MP3 atualmente incluído no pacote continua sendo a versão eSpeak. Este guia e o script preparam a geração com ElevenLabs, mas não significam que o novo áudio já tenha sido gerado.

## Voz e modelo recomendados

- **Voz escolhida:** The Professional Instructor.
- **Idioma do texto:** português brasileiro.
- **Modelo de síntese:** Eleven Multilingual v2, opção indicada para narração longa e consistente.
- **Estilo desejado:** instrutivo, claro, direto, acolhedor e profissional; ritmo conversacional moderado, articulação nítida e pausas naturais.
- **Texto-fonte:** `roteiro/narracao-utilizada.txt`. Não reescreva o roteiro durante a geração.

A página oficial da biblioteca permite testar **Portuguese (Brazil)** com The Professional Instructor: https://elevenlabs.io/pt/voice-library/straightforward. A descrição dessa voz menciona um sotaque americano; por isso, ouça a amostra em português antes de aprovar a narração integral. A disponibilidade do seletor de idioma não garante, por si só, que a pronúncia de cada termo técnico ficará perfeita.

## Opção A — Gerar pela interface web

1. Abra a [biblioteca de vozes diretas da ElevenLabs](https://elevenlabs.io/pt/voice-library/straightforward).
2. Selecione **Portuguese (Brazil)** e **The Professional Instructor** no gerador da página.
3. Teste primeiro este trecho curto:

   > Você já fez uma pergunta para uma ferramenta de inteligência artificial e recebeu uma resposta tão genérica que quase não ajudou? Às vezes, a diferença está na forma como pedimos ajuda. Está começando o Prompt em Pauta, um podcast sobre inteligência artificial generativa e aprendizado em tecnologia.

4. Se a pronúncia e o ritmo forem adequados, gere a narração completa usando o texto de `roteiro/narracao-utilizada.txt`. Se a interface limitar o tamanho de texto, use a opção de API abaixo.
5. Baixe o MP3 e ouça-o do início ao fim. Confira principalmente “Linux”, “L S”, “prompts”, “inteligência artificial” e as pausas entre parágrafos.

## Opção B — Gerar pelo script do projeto

O script usa a API oficial da ElevenLabs, sem dependências Python adicionais. É necessário ter acesso à API e saldo/créditos suficientes na conta.

1. Copie `.env.example` para `.env` na pasta raiz do projeto.
2. No arquivo `.env`, preencha `ELEVENLABS_API_KEY` com sua chave da API e `ELEVENLABS_VOICE_ID` com o ID correspondente à voz **The Professional Instructor** disponível na sua conta.
3. Não compartilhe a chave de API nem a envie para o GitHub. O arquivo `.env` já está ignorado pelo `.gitignore`.
4. Execute, na pasta raiz do projeto:

   ```bash
   python scripts/generate_audio_elevenlabs.py
   ```

5. O script lê o texto aprovado e grava uma cópia de avaliação em `output/episodio-01-prompt-em-pauta-elevenlabs.mp3`. Ele não sobrescreve o MP3 eSpeak existente.

Configurações iniciais do script: modelo `eleven_multilingual_v2`, saída MP3 a 44,1 kHz/128 kbps, estabilidade 0,55, similaridade 0,78, estilo 0,10 e reforço de locutor ativado. São pontos de partida, não garantias de resultado; ajuste depois de ouvir a amostra.

Documentação oficial do endpoint: https://elevenlabs.io/docs/pt/api-reference/text-to-speech/convert

## Critérios para aprovar e substituir o áudio

- [ ] Voz inteligível e natural em português brasileiro.
- [ ] Pronúncia clara de termos técnicos, incluindo o exemplo “L S”.
- [ ] Ritmo conversacional, sem pressa nem entonação publicitária exagerada.
- [ ] Texto falado conferido com `roteiro/narracao-utilizada.txt`, sem omissões ou acréscimos.
- [ ] Volume consistente, sem cortes abruptos ou artefatos audíveis.
- [ ] Escuta humana integral concluída.

Só depois de aprovar a nova versão, substitua `output/episodio-01-prompt-em-pauta.mp3` pelo áudio neural e atualize `output/README.md`, `docs/registro-de-producao.md`, o checklist e o README. Até essa confirmação, descreva o áudio atual como eSpeak e o uso do ElevenLabs como preparado, mas pendente.
