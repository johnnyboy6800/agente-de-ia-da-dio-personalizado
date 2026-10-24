# Segurança Básica para o Estudante da DIO

Contexto de segurança da informação para o DIO Agent fundamentar respostas sobre
vulnerabilidades, ameaças, risco e boas práticas.

## O que é segurança da informação

Proteger sistemas, redes e dados contra acessos não autorizados, ataques, danos e
interrupções de serviço. O objetivo não é eliminar todos os riscos (o que é
impossível), mas **reduzir o risco** a um nível aceitável, com medidas balanceadas
entre segurança, usabilidade e custo.

## A tríade CIA

O modelo básico de segurança da informação:

- **Confidencialidade**: garantir que apenas pessoas autorizadas conseguem ler os
  dados. Garantido, por exemplo, com criptografia, controle de acesso e senhas
  **criptografadas**.
- **Integridade**: garantir que os dados não foram alterados sem autorização. Garantido
  com checksums, assinatura digital, controles de acesso e validação de entrada.
- **Disponibilidade**: garantir que os sistemas e dados estejam acessíveis quando
  autorizados. Garantido com redundância, backup, monitoramento e manutenção.

Uma boa segurança atenta aos três: reforçar apenas o dacesso a dados sem garantir
disponibilidade deixaria o sistema inacessível; garantir disponibilidade sem
integridade permitiria alteração de dados.

## Vulnerabilidade

Fraqueza em um sistema (código, configuração, processo ou política). Um atacante pode
explorar uma vulnerabilidade para comprometer confidencialidade, integridade ou
disponibilidade. Exemplos: entrada de dados não validada, senha forte em texto
puro, acesso a um banco de dados sem validação, serviço exposto sem autenticação.

Importante: **toda vulnerabilidade não é explotável**. A probabilidade de exploração
depende da superfície de ataque, da habilidade do atacante e das regressões do
ambiente.

## Ameaça

Um agente ou evento capaz de explorar uma vulnerabilidade. Pode ser:

- **Humana**: atacante externo, phishing, insider malicioso.
- **Automação**: scripts que procuram falhas conhecidas.
- **Falha ambiental**: falta de backup, desligamento inesperado de serviço.

Uma ameaça só vira risco quando encontra uma vulnerabilidade e uma superfície de
ataque.

## Risco

A probabilidade de uma ameaça se concretizar em uma vulnerabilidade, multiplicada pelo
seu impacto. Definição prática:

> Risco = probabilidade de exploração × impacto da consequência

Classificação prática:

| Severidade | Impacto | Probabilidade | Ação |
|------------|---------|---------------|------|
| **Alto** | Dados sensíveis vazam, sistema parado, credenciais roubadas | Exploração fácil, até automática | Corrigir antes de continuar |
| **Moderado** | Algum dado acessado, mas sem grande impacto | Requer habilidade ou acesso específico | Corrigir em escopo de prioridade |
| **Baixo** | Impacto pequeno ou difícil de explorar | Muito difícil ou improvável | Agendar, monitorar |

## Como analisar um sistema

1. Mapeie a superfície de ataque (o que o atacante pode enviar ou acessar).
2. Liste os ativos protegidos (dados, funcionalidades).
3. Para cada ativo, pesquise: o que pode acontecer, quem poderia fazer, com que
   probabilidade.
4. Classifique a severidade e priorize as correções.
5. Valide: repita a análise após as correções.

## Boas práticas

- **Validação de entrada**: trate toda entrada como suspeita. Valide tipos, tamanhos,
  formatos e valores permitidos. NÃO confie apenas em filtrar caracteres maliciosos
  (ex.: remover apenas aspas) — esse tipo de filtro é preenchido facilmente.
- **Consultas parametrizadas**: use consultas parametrizadas no lugar de montar SQL
  com concatenação de strings. Isso impede a injeção de SQL.
- **Criptografia de senhas**: armazene senhas com algoritmos de hashing com
  adicional (salt) e lentidão (ex.: bcrypt, argon2). Nunca armazene senha em texto
  puro.
- **HTTPS**: transporte de dados criptografado entre o cliente e o servidor.
- **Princípio do menor privilégio**: cada componente só tem acesso ao que precisa.
  Ex.: o aplicativo não precisa de admin do banco; o servidor web não precisa de
  acesso a senhas de produção.
- **Gestão de segredos**: não coloque chaves, tokens ou credenciais em código ou em
  arquivos fáceis de ler. Use varredores e gestores de segredos.
- **Logging e monitoramento**: registre eventos de segurança (falhas de login,
  acessos indevidos) sem expor dados sensíveis. Monitore padrões suspeitos.
- **Atualização de dependências**: manter libs e frameworks atualizados para fechar
  pássaros conhecidos.
- **Erro controlado**: não expose detalhes de stack trace, conexão ou configuração em
  respostas. O feedback de erro deve ser amigável, sem revelar estrutura interna.
- **Autenticação e autorização**: valide quem está acessando, não apenas o que está
  sendo acessado. Verifique permissões em cada requisição.

## Considerações legais e éticas

- Só analise sistemas que você administra ou tem autorização explícita para analisar.
- Nunca submeta intencionalmente uma falha conhecida a sistemas de terceiros.
- Se o estudante "precisar testar", pergunte a autorização e o escopo antes de
  avançar.
- O objetivo da análise é melhorar a segurança, não explorar.

## Como estudar

- Comece por `skills/explain-concept` para entender termos.
- Leia a `OWASP Top 10` para as falhas mais comuns.
- Leia a detecção de falhas conhecidas no `MITRE ATT&CK` para mapear técnicas.
- Pratique em laboratórios seguros (ambientes próprios ou governados) antes de
  tocar em sistemas de terceiros.
