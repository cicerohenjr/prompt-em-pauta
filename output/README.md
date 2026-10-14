# Áudio final — Episódio 01

**Arquivo esperado:** `episodio-01-prompt-em-pauta.mp3`  
**Duração do MP3 gerado localmente:** aproximadamente 4 minutos e 43 segundos  
**Formato:** MP3, mono, 44,1 kHz, 160 kbps  
**Voz:** eSpeak `pt-br` (voz sintética básica)  
**Status:** áudio refeito em uma única síntese contínua; escuta humana final e envio ao GitHub ainda pendentes.

## Como o áudio foi produzido

A narração foi sintetizada em uma única passagem com eSpeak `pt-br`, velocidade 135, pitch 48 e amplitude 90. O tratamento leve de frequências e a normalização foram aplicados no FFmpeg. O arquivo foi exportado em MP3 mono a 44,1 kHz e 160 kbps.

## Conferência técnica

- [x] O arquivo MP3 foi gerado.
- [x] O codec foi identificado como MP3.
- [x] A duração foi conferida: aproximadamente 4:43.
- [x] A taxa de amostragem foi conferida: 44,1 kHz.
- [x] O áudio é mono e tem bitrate de 160 kbps.
- [x] O nível de áudio foi analisado automaticamente; o pico medido ficou em aproximadamente -2,4 dBFS.
- [ ] Ouvir o MP3 integralmente em um reprodutor para verificar pronúncia, ritmo e possíveis artefatos.
- [ ] Adicionar o arquivo `output/episodio-01-prompt-em-pauta.mp3` ao GitHub.

## Observação importante

A síntese contínua e o tratamento leve foram aplicados para reduzir a possibilidade de emendas e saturação, mas não transformam eSpeak em uma voz neural natural. A voz ainda pode soar robótica. Para se aproximar de leitores modernos de navegador, é necessário usar um serviço TTS neural, como ElevenLabs ou outro equivalente. Não declare que este áudio foi produzido com ElevenLabs: esta versão continua usando eSpeak.
