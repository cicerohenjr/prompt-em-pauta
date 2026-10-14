# Registro de produção e uso de IA

Atualize este documento quando uma etapa mudar. Não declare como utilizada uma ferramenta que não foi usada.

| Etapa | Ferramenta ou método | Situação | Observações |
|---|---|---|---|
| Organização do projeto e elaboração inicial do roteiro | ChatGPT | Realizada | Documentação e roteiro organizados com apoio de IA; revisão humana recomendada. |
| Capa | Nano Banana | Realizada anteriormente | A capa vetorial SVG está no GitHub; a versão PNG está no pacote de entrega e ainda precisa ser enviada ao repositório se solicitada. |
| Síntese de voz | eSpeak, voz `pt-br` | Realizada e refeita | Uma única passagem contínua; velocidade 135, pitch 48, amplitude 90. Voz sintética básica. |
| Pós-processamento e exportação | FFmpeg | Realizada | Filtro leve de frequências e normalização; MP3 mono, 44,1 kHz, 160 kbps. |
| Verificação técnica do arquivo | ffprobe e análise de volume | Realizada | Duração aproximada de 4:43; pico medido no MP3 de aproximadamente -2,4 dBFS. |
| Escuta humana integral | Reprodutor de áudio | Pendente | Ouvir do início ao fim e confirmar pronúncia, ritmo e eventuais artefatos. |
| Envio dos arquivos finais ao GitHub | Interface do GitHub | Pendente | O pacote local contém o MP3 e o PNG; ainda é necessário adicionar esses arquivos binários ao repositório. |
| Entrega na plataforma DIO | Plataforma DIO | Pendente | Enviar o link do repositório após a revisão final. |

## Decisões editoriais

- Priorizar linguagem acessível a estudantes e iniciantes em TI.
- Usar um exemplo de prompt para aprender o comando `ls`, pronunciado no áudio como “éle ésse”.
- Reforçar a verificação de informações e a prática independente.
- Não incluir música de fundo; o episódio usa somente narração.

## Transparência sobre a voz

O MP3 atual foi gerado com eSpeak, não com ElevenLabs. A nova versão usa uma única síntese contínua e tratamento leve para reduzir emendas e saturação; a voz continua sintética e pode soar robótica. A análise técnica automática não substitui a escuta humana. Se uma versão neural mais natural for produzida, registre a ferramenta e os parâmetros reais.
