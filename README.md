## 🧠 Quizzler — Aplicação de Quiz de Verdadeiro/Falso

Um quiz interativo que utiliza perguntas de cultura geral obtidas online e apresenta-as numa interface gráfica simples e intuitiva. O utilizador responde **True/False**, acompanha a sua pontuação em tempo real e recebe feedback imediato após cada resposta.

---

## 🎯 Objetivo

O projeto oferece uma experiência leve e dinâmica para testar conhecimentos gerais, combinando:

- **Interface gráfica** para interação direta  
- **Perguntas dinâmicas** obtidas de uma API pública  
- **Feedback visual** para respostas certas e erradas  
- **Pontuação em tempo real**  
- **Progressão automática** até ao fim do quiz  

---

## 🧩 Como funciona

- As perguntas são carregadas a partir de uma **API de trivia**, garantindo variedade e atualização constante.  
- Cada pergunta é convertida num objeto estruturado que contém texto e resposta correta.  
- A aplicação apresenta uma pergunta de cada vez e regista a resposta do utilizador.  
- O fundo muda de cor para indicar se a resposta foi correta ou incorreta.  
- Quando já não existem mais perguntas, o utilizador vê uma mensagem final e os botões são desativados.

---

## 🖥️ Componentes principais

- **Sistema de perguntas** — gere o texto, respostas e avanço no quiz  
- **Lógica do quiz** — controla pontuação, validação e fluxo  
- **Interface gráfica** — apresenta perguntas, botões e feedback visual  
- **Integração com API** — obtém perguntas atualizadas automaticamente  

---

## 🏁 Funcionalidades

- **Perguntas booleanas** (True/False)  
- **Atualização automática da pontuação**  
- **Feedback visual imediato**  
- **Interface limpa e responsiva**  
- **Mensagem final de conclusão**  

---

## 📦 Estrutura do projeto

- **Módulo de dados** — obtém e prepara as perguntas  
- **Modelo de pergunta** — representa cada pergunta individual  
- **Motor do quiz** — gere pontuação e fluxo  
- **Interface gráfica** — apresenta o quiz ao utilizador  
