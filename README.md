# 🤖 DIO Agent

> Seu mentor de Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar com mais clareza, destravar desafios e entender qualquer conceito.

E você não precisa instalar nada complicado. Em **3 passos simples**, o seu mentor de IA estará pronto para usar.

---

## 📌 Descrição do projeto

O **DIO Agent** é um agente de IA que acompanha estudantes da [DIO](https://dio.me) na aprendizagem de tecnologia — sem dar respostas prontas, mas conduzindo o estudante ao raciocínio.

Ele conhece os formatos da DIO (Bootcamps, Formações, Cursos, Desafios, Lives, Mentorias etc.) e usa **skills passo a passo** para:

- **Plano de estudos**: organiza o que estudar, em que ordem e em quanto tempo, ancorado no conteúdo real da DIO;
- **Destravar desafio**: conduz o raciocínio de um Desafio de Código, Projeto ou Criativo, sem entregar a solução pronta;
- **Explicar conceito**: explica termos e tecnologias de forma simples, com analogia e exemplo;
- **Análise de vulnerabilidades** (nova especialização): orienta a análise de segurança, classificando risco por impacto, probabilidade e severidade — sempre perguntando o contexto antes de sugerir qualquer ação;
- **Pesquisa na web** (nova): fundamenta respostas em busca atual com fontes citadas.

O coração do projeto é o padrão aberto `AGENTS.md`: qualquer harness compatível (Antigravity, Claude Code, Codex, Cursor, Gemini CLI e Hermes) lê o arquivo e recruta o agente. O mesmo mentor pode "dar aula" em qualquer um deles.

---

## ✨ Antes de começar: dois conceitos rápidos

Para usar o DIO Agent, basta entender duas palavras. As duas estão no [Glossário completo](docs/glossary.md), mas aqui vai a versão rápida:

- 🧠 **Agente de IA:** um chatbot comum responde perguntas, como um buscador mais esperto. Um *agente* de IA vai além: ele lê, planeja e executa passos para te ajudar a alcançar um objetivo. É a diferença entre alguém que te explica o caminho e alguém que caminha junto com você. O DIO Agent é um agente desse tipo: um tutor particular que acompanha a sua evolução.
- 🖥️ **Harness:** é o programa onde a conversa com o agente acontece. Vale a comparação: o agente é o professor, e o harness é a sala de aula. O mesmo professor pode dar aula em salas diferentes. Por isso o DIO Agent funciona em qualquer harness: você escolhe a "sala" no Passo 1, e o seu mentor continua o mesmo.

Pronto. Com isso já dá para começar.

---

## 🎯 Especialização do agente: Análise de Vulnerabilidades (AppSec)

O DIO Agent partiu como um mentor de tecnologia genérico: plano de estudos, destravar desafios e explicar conceitos. O aperfeiçoamento escolhido foi **especializá-lo em Análise de Vulnerabilidades** — ensinar o estudante a pensar em segurança, a classificar riscos e a corrigir falhas, sem nunca entregar respostas prontas ou scripts de exploração.

Por que essa especialização?

- **Segurança é um dos temas mais pedidos — e o mais descuidado.** Quem pergunta por um login, formulário ou endpoint quase nunca pergunta "como atacar", pergunta "isso está seguro?".
- **O agente não precisa ser o 'crack' que resolve o bug.** Precisa ensinar a pessoa a reconhecer risco, a questionar o contexto certo e a corrigir por princípios — o que exige um processo próprio, e não improviso.
- **Complementa as skills existentes.** O plano de estudos, o destravar de desafio e a explicação de conceito continuam. A análise de segurança ganha um fluxo definido, fundado na tríade CIA, na triagem de risco e nas classes OWASP/CWE/MITRE.
- **Gera respostas verificáveis.** A skill de pesquisa na web (You.com) garante fontes citadas para o que muda com o tempo, e a skill de análise de vulnerabilidades mantém o estudante no controle do que aprender.

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um Harness

O harness é o programa que dá vida ao agente. Recomendamos o **Google Antigravity**, que tem limites de uso mais generosos para quem está começando. Mas qualquer harness moderno funciona.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://docs.claude.com/en/docs/claude-code |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

Escolha um e siga o passo a passo da documentação oficial dele. Cada documentação já traz tudo certo para o seu sistema, então a instalação é tranquila.

### 2️⃣ Configure o DIO Agent

Agora você vai baixar este repositório para o seu computador. Escolha a forma mais simples para você:

**Opção A: com Git** (se você já usa Git)

```bash
git clone https://github.com/digitalinnovationone/dio-agent.git
```

**Opção B: baixando o .zip** (se você não usa Git)

Na página do repositório no GitHub, clique no botão verde **Code** e depois em **Download ZIP**. Em seguida, extraia a pasta em um lugar fácil de encontrar.

Com o repositório baixado, abra a pasta `dio-agent` no harness que você instalou. Cada harness tem o seu jeito de abrir uma pasta de projeto, e a documentação dele mostra como fazer isso.

E é só isso! O harness lê automaticamente o arquivo `AGENTS.md` e o agente já sabe quem é: o seu mentor de estudos da DIO.

> 🔄 **Fique de olho nas atualizações.** Não importa se você usou o Git ou o .zip: o repositório do DIO Agent evolui com o tempo. De tempos em tempos, vale voltar aqui e pegar a versão mais recente. Quem usou Git pode rodar `git pull` (ou pedir pro próprio DIO Agent rodar); quem baixou o .zip pode baixar de novo. Assim o seu mentor está sempre com o melhor que a gente tem a oferecer.

### 3️⃣ Hands On!

Agora é só conversar. Você pode falar naturalmente, com as suas palavras. Mas, principalmente nas primeiras vezes, vale usar um modelo de prompt pronto: é só copiar e preencher os campos entre colchetes. Quanto mais contexto você dá, melhor o agente ajuda.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos (se possível, com materiais complementares).
- Meu objetivo: [ex: aprender mais sobre IA, ser dev back-end, concluir um bootcamp]
- Experiência ou carreira da DIO: [URL ou nome do bootcamp/formação, ou de uma carreira da DIO]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou descreva]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código atual: [cole aqui, se for Desafio de Código]
- Link do repositório base: [copie aqui, se for Desafio de Projeto]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
- Onde apareceu: [ex: no curso X de um bootcamp] (opcional)
```

**🛡️ Análise de vulnerabilidades** (a especialização)

```
Estou com um algoritmo de login, um formulário ou um endpoint e quero saber se está seguro.
- O que é o sistema: [stack, ambiente, o que está protegido]
- O que pode acontecer se os dados vazarem: [credenciais, PII, funcionalidade]
- Tenho autorização para analisar: [sim/não, e quem é o dono/responsável]
- O que eu já sei sobre segurança: [iniciante, intermediário, avançado]
Me orienta a classificar o risco e a corrigir por princípios, sem entregar payloads prontos.
```

Não precisa de comando especial nem de formato perfeito: o agente conduz a conversa a partir daí e pede mais detalhes se precisar.

---

## 🧩 As skills do agente

Uma **skill** é uma habilidade do agente, descrita em um guia passo a passo. O DIO Agent vem com cinco:

| Skill | Para que serve | Exemplo de pedido do estudante |
|-------|----------------|--------------------------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo | "Por onde começo?" |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz até a solução de um desafio, sem dar a resposta | "Travei no desafio" |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma didática | "Não entendi o que é uma API" |
| [Pesquisa na web](skills/web-search/SKILL.md) | Fundamenta respostas com busca atual e fontes citadas | "Qual a versão estável do Node hoje?" |
| [Análise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md) | Orientação de segurança: impacto × probabilidade × severidade | "Esse login está seguro?" |

Você não precisa "chamar" uma skill. O agente percebe o que você precisa e usa a skill certa sozinho.

---

## 🗂️ Estrutura do repositório

```text
dio-agent/
├── README.md                        Este guia
├── AGENTS.md                        Definição do agente (lida por qualquer harness)
├── CLAUDE.md                        Atalho para o Claude Code
│
├── agent/
│   ├── persona.md                   A personalidade e o tom do agente
│   └── knowledge/
│       ├── dio-platform.md          O que é a DIO
│       ├── learning-experiences.md  Os formatos de aprendizado da DIO
│       └── security-basics.md       Conceitos de segurança (para a skill de análise)
│
├── skills/
│   ├── README.md                    O que são skills e como elas funcionam
│   ├── study-plan/                  Skill: plano de estudos
│   ├── unblock-challenge/           Skill: destravar desafio
│   ├── explain-concept/             Skill: explicar conceito
│   ├── web-search/                  Skill: pesquisa na web (You.com)
│   └── vulnerability-analysis/      Skill: análise de vulnerabilidades (AppSec)
│
├── docs/
│   ├── glossary.md                  Glossário de termos
│   └── demo-app.py                  Exemplo didático de login com SQL Injection
│
└── .gitignore
```

> 🔍 **Por que funciona em qualquer harness?** O coração do projeto é o arquivo `AGENTS.md`, um padrão aberto que harnesses modernos sabem ler. O `CLAUDE.md` apenas aponta para ele, então você pode usar o harness que preferir.

---

## 📁 Arquivos criados ou alterados

Para dar vida à especialização, foram criados e/ou ajustados estes arquivos:

| Arquivo | Tipo | O que faz |
|---------|------|-----------|
| `skills/vulnerability-analysis/SKILL.md` | **Skill criada** | Guia de análise de segurança: fluxo por impacto (confidencialidade, integridade, disponibilidade) × probabilidade × severidade. |
| `agent/knowledge/security-basics.md` | **Conhecimento criado** | Conceitos de segurança da informação (vulnerabilidade, ameaça, risco, tríade CIA) que fundamentam a resposta. |
| `agent/persona.md` | **Persona alterada** | Ajustada com a seção "O que o DIO Agent faz com segurança", orientando a ativação da skill e as regras de contexto antes de sugerir qualquer análise. |
| `AGENTS.md` | **Definição alterada** | Registra a nova skill e o arquivo de conhecimento, indicando quando usá-los durante a conversa. |
| `skills/web-search/SKILL.md` | **Skill criada** | Pesquisa na web com You.com, com fontes citadas, para respostas atualizadas (versões, lançamentos, mercado). |
| `docs/demo-app.py` | **Exemplo criado** | Aplicativo de login didático com SQL Injection, usado para ensinar o princípio da vulnerabilidade e a correção por consulta parametrizada. |

A tabela de skills (`skills/README.md`) e o `AGENTS.md` também foram atualizados para refletir os dois novos adicionados ao repositório.

---

## 📖 Glossário rápido

Termos como *agente*, *harness*, *skill*, *prompt* e *superfície de ataque* estão explicados com analogias simples no **[Glossário completo](docs/glossary.md)**. Se algum termo soar estranho, comece por lá.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você desde o início dos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀
