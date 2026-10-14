# Prompts do projeto — Prompt em Pauta

Este arquivo reúne modelos e decisões do processo. Um modelo de prompt não deve ser apresentado como se tivesse sido usado literalmente se isso não ocorreu.

## 1. Planejamento do episódio

> Ajude a planejar um episódio curto de podcast educativo, em português brasileiro, para estudantes e iniciantes em Tecnologia da Informação. O tema é “Como usar a IA generativa para estudar tecnologia com mais eficiência”. Sugira uma estrutura clara, uma promessa realista para o ouvinte, três pontos principais e um encerramento. Evite exageros, jargão desnecessário e afirmações sem suporte.

**Situação:** modelo de planejamento; registre adaptações feitas durante o processo.

## 2. Criação do roteiro

> Escreva um roteiro narrado para um podcast de 3 a 5 minutos, em português brasileiro, com o título “Como usar a IA generativa para estudar tecnologia com mais eficiência”. O público são estudantes e iniciantes em TI. Estruture em abertura, desenvolvimento, demonstração de um prompt, cuidados com respostas incorretas e encerramento. Use linguagem natural, frases fáceis de falar em voz alta e transições claras. Inclua uma demonstração prática com um tutor de Linux para iniciantes. Não invente estatísticas nem apresente a IA como fonte infalível.

**Situação:** modelo de referência. O roteiro final está em `../roteiro/episodio-01.md`.

## 3. Revisão editorial e factual

> Revise o roteiro abaixo como editor de um podcast introdutório sobre IA generativa. Verifique clareza, fluidez oral, coerência, repetição, termos técnicos e adequação ao público iniciante. Sinalize afirmações que precisam ser verificadas em fontes confiáveis; não invente fontes nem fatos para preencher lacunas. Preserve o objetivo e a linguagem acessível. Entregue problemas encontrados, sugestões e uma versão revisada. Roteiro: [colar roteiro].

**Situação:** modelo de revisão.

## 4. Narração com ElevenLabs

**Estilo desejado:** narração em português brasileiro, clara, natural, direta, acolhedora e profissional; ritmo conversacional moderado, dicção nítida e pausas naturais.

**Planejamento inicial:** The Professional Instructor foi considerada durante a preparação do projeto.  
**Voz presente no arquivo exportado:** Davi Andrei, modelo Eleven v4, gerado no ElevenLabs Studio.

A voz efetivamente usada é registrada conforme o arquivo exportado, sem afirmar que The Professional Instructor foi utilizada.

> Narre o roteiro aprovado em português brasileiro com voz clara, natural, acolhedora e profissional. Mantenha um tom instrutivo e conversacional, com articulação precisa, ritmo moderado e pausas curtas entre as ideias. Dê ênfase discreta às perguntas e aos exemplos. Evite entonação publicitária, dramatização e pressa. Pronuncie termos técnicos com clareza. Não altere o texto aprovado.

**Atribuição:** ElevenLabs — https://elevenlabs.io. Se o áudio foi gerado no plano gratuito, mantenha o uso não comercial e a atribuição ao publicar.

## 5. Capa — Nano Banana

> Crie uma capa quadrada para um podcast educativo chamado “Prompt em Pauta”, sobre como usar a IA generativa para estudar tecnologia com mais eficiência. Use estilo contemporâneo, tecnológico e limpo, com um microfone como elemento central e referências visuais discretas a diálogo, aprendizado e inteligência artificial. Use fundo azul-marinho, detalhes em ciano e violeta, alto contraste e composição organizada. Use apenas “Prompt em Pauta” como texto principal, sem logotipos de marcas, marcas-d'água ou texto pequeno ilegível.

**Situação:** o conceito visual foi criado com Nano Banana. A capa vetorial SVG está no GitHub; a capa PNG está incluída no pacote local e ainda precisa ser enviada ao GitHub caso seja solicitada.

## 6. Registro da geração de áudio efetivamente realizada

- **Ferramenta:** eSpeak, síntese local de voz.
- **Voz:** `pt-br`.
- **Velocidade:** 135.
- **Pitch:** 48.
- **Amplitude:** 90.
- **Síntese:** uma única passagem contínua, para reduzir emendas entre trechos.
- **Pós-processamento:** filtro leve de frequências e normalização de volume.
- **Exportação:** MP3 mono, 44,1 kHz, 160 kbps; pico medido de aproximadamente -2,4 dBFS.
- **Duração medida:** aproximadamente 4:43.

Não foi utilizado ElevenLabs nesta versão. A síntese contínua reduz a possibilidade de emendas e saturação, mas a voz eSpeak continua sintética e pode soar robótica. A análise automática não substitui a escuta humana. Se for substituída por outra ferramenta, atualize o registro.

## 7. Revisão final do áudio

> Com base no áudio fornecido, verifique se a fala é compreensível do início ao fim, se o volume é consistente e se existem cortes abruptos, ruídos excessivos, trechos duplicados ou música que prejudique a voz. Compare o conteúdo com o roteiro e indique os problemas e correções recomendadas. Não afirme ter ouvido ou analisado um arquivo que não tenha sido fornecido.

**Situação:** a análise técnica automática foi feita; a escuta humana integral ainda está pendente.
