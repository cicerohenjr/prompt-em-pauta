# Áudio final — Episódio 01

**Arquivo:** episodio-01-prompt-em-pauta.mp3  
**Duração:** aproximadamente 3 minutos e 25 segundos  
**Formato:** MP3, mono, 44,1 kHz, 192 kbps  
**Voz:** Davi Andrei  
**Modelo:** Eleven v4, no ElevenLabs Studio  
**Pós-processamento:** normalização de loudness com FFmpeg  
**Atribuição:** ElevenLabs — https://elevenlabs.io

## Tratamento aplicado

- Normalização para alvo próximo de −19 LUFS.
- Pico verdadeiro alvo de −1,5 dBTP para manter margem contra clipping.
- Metadados preenchidos com o título do episódio e o nome do podcast.

## Conferência técnica

- [x] Codec MP3 confirmado.
- [x] Duração de aproximadamente 3:25 confirmada.
- [x] Taxa de amostragem de 44,1 kHz confirmada.
- [x] Áudio mono e bitrate de 192 kbps confirmados.
- [x] Loudness final medido próximo de −19,4 LUFS.
- [x] Pico verdadeiro medido próximo de −1,7 dBTP, sem clipping.
- [x] Arquivo percorrido em segmentos ao longo da duração; não foram identificados cortes abruptos evidentes.

## Transparência

Esta versão usa Davi Andrei + Eleven v4. O planejamento inicial mencionava The Professional Instructor, mas essa voz não foi usada no arquivo exportado. A avaliação técnica detalhada está em docs/avaliacao-audio.md.

O pacote ZIP de entrega contém o MP3 atualizado. O arquivo binário ainda precisa ser adicionado a este repositório para ficar disponível no caminho acima.
