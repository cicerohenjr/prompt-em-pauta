# Registro de produção e uso de IA

| Etapa | Ferramenta ou método | Situação | Observações |
|---|---|---|---|
| Organização do roteiro | ChatGPT | Realizada | Linguagem acessível a estudantes e iniciantes em TI. |
| Capa | Nano Banana | Realizada | Capa PNG incluída no projeto. |
| Síntese da narração | ElevenLabs Studio | Realizada | Voz Davi Andrei, modelo Eleven v4, texto em português brasileiro. |
| Ajuste de volume e metadados | FFmpeg | Realizada | Alvo de −19 LUFS e pico verdadeiro alvo de −1,5 dBTP. |
| Verificação técnica | ffprobe e filtro loudnorm | Realizada | Aproximadamente 3:25; mono, 44,1 kHz, 192 kbps; loudness medido próximo de −19,4 LUFS. |
| Revisão auditiva | Reprodução em segmentos | Realizada | O arquivo foi percorrido em segmentos; não foram identificados cortes abruptos evidentes. A conferência final da pronúncia pelo autor é recomendada. |
| Upload do MP3 binário ao GitHub | Interface do GitHub | Pendente | O pacote ZIP contém o áudio atualizado; o arquivo binário ainda precisa ser enviado ao repositório. |
| Entrega na DIO | Plataforma DIO | Pendente | Enviar o link do repositório após conferir o MP3 público. |

## Decisões editoriais

- Priorizar linguagem acessível para iniciantes em TI.
- Usar um exemplo de prompt para aprender o comando ls, pronunciado como “éle ésse”.
- Reforçar a verificação de informações e a prática independente.
- Não incluir música de fundo; o episódio usa somente narração.

## Transparência sobre a voz

O planejamento inicial mencionava The Professional Instructor, mas o arquivo recebido para revisão foi exportado com Davi Andrei e o modelo Eleven v4. A documentação descreve a voz realmente usada.

**Atribuição:** ElevenLabs — https://elevenlabs.io. A licença depende do plano usado para gerar o áudio; confira as condições da conta antes de publicar.
