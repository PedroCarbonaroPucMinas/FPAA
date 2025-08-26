# Instruções para Visualizar o Grafo de Fluxo - VERSÃO MELHORADA

## 🎨 Novo Design Profissional

O diagrama foi completamente redesenhado com foco em:
- ✅ **Simetria e organização visual**
- ✅ **Cores profissionais e hierarquia visual**
- ✅ **Layout limpo e moderno**
- ✅ **Numeração clara dos nós**
- ✅ **Legenda organizada e completa**

## Como abrir o arquivo draw.io

### Opção 1: Online (Recomendado)
1. Acesse [https://app.diagrams.net/](https://app.diagrams.net/)
2. Clique em "Open Existing Diagram"
3. Selecione o arquivo `grafo_fluxo_karatsuba.drawio`
4. O diagrama será carregado automaticamente

### Opção 2: VS Code Extension
1. Instale a extensão "Draw.io Integration" no VS Code
2. Abra o arquivo `grafo_fluxo_karatsuba.drawio` diretamente no VS Code
3. O diagrama será renderizado na própria interface

### Opção 3: Desktop Application
1. Baixe o draw.io desktop em [https://github.com/jgraph/drawio-desktop/releases](https://github.com/jgraph/drawio-desktop/releases)
2. Instale e abra o aplicativo
3. Abra o arquivo `grafo_fluxo_karatsuba.drawio`

## Elementos do Diagrama

## Elementos do Diagrama

### Novo Layout Simétrico
- **Fluxo Central**: Coluna principal com o fluxo do algoritmo
- **Divisão Clara**: Caso base à esquerda, caso recursivo à direita
- **Três Recursões**: Organizadas simetricamente em linha
- **Numeração Visual**: Círculos amarelos numerando cada nó

### Esquema de Cores Profissional
- **Verde**: Início, fim e combinação final
- **Amarelo/Laranja**: Decisão principal  
- **Vermelho**: Caso base (parada)
- **Azul**: Processos de preparação e divisão
- **Roxo**: Chamadas recursivas
- **Cinza**: Fluxo principal das arestas

### Cores e Formas
- **Elipses Roxas**: Pontos de entrada e saída
- **Losango Amarelo**: Nó de decisão (if/else)
- **Retângulos Azuis**: Processos e cálculos
- **Retângulos Vermelhos**: Chamadas recursivas
- **Retângulo Verde**: Caso base (retorno direto)

### Tipos de Arestas
- **Setas Sólidas Cinzas**: Fluxo normal do programa
- **Seta Verde**: Caminho TRUE da decisão
- **Seta Vermelha**: Caminho FALSE da decisão
- **Setas Tracejadas Roxas**: Chamadas recursivas implícitas

### Legendas Incluídas
- **Caixa Cinza**: Legenda completa com explicação dos elementos
- **Caixa Amarela**: Análise de complexidade ciclomática detalhada
- **Caixa Verde**: Caminhos independentes identificados

## Análise do Diagrama

### Estrutura do Grafo
- **10 Nós**: Representam as operações principais
- **10 Arestas**: Conexões entre as operações
- **1 Componente Conexo**: Grafo totalmente conectado

### Complexidade Ciclomática
- **Fórmula**: m = e - n + 2p
- **Cálculo**: m = 10 - 10 + 2(1) = 2
- **Interpretação**: Baixa complexidade, fácil de testar

### Caminhos de Teste
Para garantir 100% de cobertura, execute:
1. **Teste do Caso Base**: Números pequenos (< 10)
2. **Teste Recursivo**: Números grandes (≥ 10)

## Editando o Diagrama

Se precisar modificar o diagrama:
1. Abra no draw.io
2. Selecione elementos para editar propriedades
3. Use a barra lateral direita para modificar cores, textos, etc.
4. Salve o arquivo modificado

## Exportando o Diagrama

Para criar imagens do diagrama:
1. No draw.io, vá em File → Export as
2. Escolha o formato desejado (PNG, PDF, SVG, etc.)
3. Configure a resolução e qualidade
4. Baixe o arquivo exportado

## Troubleshooting

### Arquivo não abre
- Verifique se a extensão é `.drawio`
- Tente renomear para `.xml` temporariamente
- Use a opção "Import" no draw.io se necessário

### Diagrama aparece cortado
- Use o zoom para ajustar a visualização
- Vá em View → Fit para ajustar automaticamente
- Verifique as configurações de página

### Elementos não aparecem
- Verifique se todas as camadas estão visíveis
- Use Ctrl+A para selecionar todos os elementos
- Recarregue o arquivo se necessário
