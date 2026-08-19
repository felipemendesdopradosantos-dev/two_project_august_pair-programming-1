💵 Projeto Banco digital 💵

Esse projeto apresenta um banco digital, funcionamentos principais: depósito do valor, saque e extrato.

Felipe Mendes e Sarah Santos.

🏹 Objetivos🏹

lógica: O código implementa uma aplicação gráfica de Simulador Bancário em Python utilizando a biblioteca Tkinter. A estrutura segue o modelo de Programação Orientada a Objetos (POO).

Estrutura de Dados e Estado
self.saldo: Armazena o valor atual disponível na conta (inicia em 0.0). self.extrato: Uma lista de strings que guarda o histórico de todas as transações realizadas com data e hora. self.modo_escuro: Um booleano (True/False) que controla o tema visual da interface.

Interface Gráfica (GUI)
Janela Principal: Define o tamanho fixo (450x400) e o título. Header: Contém o título do aplicativo e o botão para alternar entre Modo Claro e Escuro. Abas (ttk.Notebook)**: Dividido em duas telas principais: Aba 1 (Início) : Exibe o saldo atual, o campo de entrada para digitação do valor e os botões de Depositar e sacar Aba 2 (Extrato): Contém uma Listbox com barra de rolagem para listar o histórico de operações.

Lógica das Operações Bancárias
Validação de Entrada (_obter_valor_valido)

Captura o texto digitado, substitui vírgula por ponto (para aceitar centavos no formato brasileiro) e remove espaços.
Tenta converter para número decimal (float).
Se a conversão falhar ou o valor for menor/igual a zero, exibe uma mensagem de erro (messagebox) e interrompe o processo.
Depósito (depositar)

Obtém o valor validado.
Adiciona o valor ao self.saldo.
Registra a data/hora atual e formata a mensagem no histórico (self.extrato).
Atualiza a tela e exibe confirmação.
Saque (sacar)

Obtém o valor validado.
Verifica se o valor solicitado é maior que o saldo atual:
Sim: Exibe alerta de saldo insuficiente e cancela a operação.
Não: Subtrai o valor do self.saldo, registra no extrato com a data/hora, atualiza a interface e exibe confirmação.
Atualização e Temas Visual
_atualizar_interface: Atualiza o texto do saldo na tela, limpa o campo de entrada e recarrega a lista do extrato. alternar_tema e _aplicar_tema: Alternam as cores dos componentes de acordo com o estado de self.modo_escuro, modificando as propriedades dos estilos ttk e das cores de fundo/texto da Listbox e janela principal.

🚀 Projetos Incluídos

📜 Linha do Tempo: Eufrásia Teixeira Leite (historia_financas_with_eufrasia_seunome.py) Uma interface interativa sobre Eufrásia Teixeira Leite (1850–1930), a primeira investidora global do Brasil.
Destaques: Download e exibição de imagem via requisição HTTP (requests e Pillow). Tratamento de falhas de conexão para manter a aplicação funcional mesmo offline. Botões interativos para exibição de fatos históricos.

💵 Simulador de Aportes (financas_aportes_bankb3_sarahsantos.py) Uma calculadora de fluxo de caixa simplificada para ensinar operações de depósito e saque.

Destaques: Controle de saldo em tempo real. Validação para impedir saques maiores do que o saldo disponível. Atualização dinâmica dos rótulos e campos de texto.

📊 Dashboard Financeiro - Padrão B3 (financas_dashboard_bankb3_sarahsantos.py) Um painel completo simulando o ambiente da Bolsa de Valores brasileira (B3).

Destaques: Uso de abas interativas (ttk.Notebook) para navegar entre Conta Corrente, Criptoativos e Extrato. Simulação de compra de frações de Bitcoin (BTC). Histórico de transações em tempo real utilizando tk.Listbox.
