# PyKeyMonitor Educacional

![Autor](https://img.shields.io/badge/Autor-Max_Müller-blue?style=for-the-badge&logo=github)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Ethical](https://img.shields.io/badge/Ethical_Use-Apenas_Com_Consentimento-red?style=for-the-badge&logo=security)
![Cyber Education](https://img.shields.io/badge/Educação-Simulação_Cibersegurança-blueviolet?style=for-the-badge&logo=hackaday)


**PyKeyMonitor Educacional** é um projeto desenvolvido com fins **exclusivamente didáticos**, voltado para a demonstração ética de técnicas de captura de teclas (keylogging) em ambientes controlados, com consentimento explícito do usuário.

### Objetivos do projeto

- Demonstrar o funcionamento de bibliotecas como `pynput` e `tkinter`.
- Simular ferramentas de monitoramento para fins educacionais, auditoria de acessibilidade e pesquisa em usabilidade.
- Reforçar a importância da ética e da transparência no desenvolvimento de softwares de segurança.

### O que o projeto ensina

- Captura de eventos de teclado com `pynput`.
- Criação de interfaces gráficas modernas com `tkinter`.
- Registro de logs em arquivos de forma organizada.
- Implementação de mecanismos de consentimento e boas práticas de segurança.
- Design ético e transparente de ferramentas de monitoramento.

### Funcionalidades

- Interface gráfica e botões acessíveis.
- Solicitação de consentimento antes do início do monitoramento.
- Logs salvos localmente com separação por sessões.
- Compatível com sistemas Windows, Linux e macOS.

### Aviso Ético

> Este projeto **não deve ser utilizado para fins maliciosos ou espionagem não autorizada**.  
> É um recurso de aprendizado e demonstração para fins pedagógicos, voltado ao ensino de cibersegurança, programação defensiva e design responsável de software.

---

## Como Executar

1. Faça um Fork do Repositório:
Antes de tudo, crie sua própria cópia deste projeto:

- Clique no botão Fork no canto superior direito do GitHub.

- Isso criará uma versão do repositório na sua conta.

2. Clone o Seu Repositório Forkado:

```
git clone https://github.com/SEU-USUARIO/PyKeyMonitor.git
cd PyKeyMonitor
```
###### Substitua SEU-USUARIO pelo nome do seu GitHub.

3. Instale as dependências:
pip install pynput


4. Execute o projeto:

A biblioteca tkinter já vem embutida no Python padrão (Windows/Linux/macOS), então não precisa instalá-la separadamente.

---
## Demonstração Visual

### 1 Janela Inicial
Rode o script principal em seu terminal ou diretamente no VS Code:
- keymonitor.py

A janela inicial será exibida com a identidade visual do projeto.

![1](https://github.com/user-attachments/assets/d47809ef-f04d-4e5a-b0fb-d55fa6a9245e)



---

### 2 Termo de Consentimento
Antes de iniciar o monitoramento, o programa solicitará consentimento explícito do usuário. Nenhuma tecla será registrada até que a permissão seja concedida.

![2](https://github.com/user-attachments/assets/ad04337e-90d5-4096-88e9-d28f11fc302c)



---

### 3 Encerramento Seguro
Ao fechar a janela ou clicar em "Cancelar", o programa salva o log e informa o fim da sessão de forma segura.
![2 3](https://github.com/user-attachments/assets/0aad409f-eb7a-45b5-b984-3d8635231a55)

O arquivo log_01.txt será gerado automaticamente na pasta exemplo_logs/ com o registro das teclas pressionadas durante a sessão.

![3](https://github.com/user-attachments/assets/bb959219-b446-4ca1-bc8e-a5063d9961fe)


## Autor
Professor: Max Müller

Se este projeto ajudou você a evoluir, deixe uma ⭐ e compartilhe o conhecimento. Obrigado por usar este repositório!
