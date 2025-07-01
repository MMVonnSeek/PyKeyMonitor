# PyKeyMonitor Educacional

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
### Instale as dependências
Abra o terminal na pasta do projeto e instale a biblioteca necessária com:

pip install pynput

A biblioteca tkinter já vem embutida no Python padrão (Windows/Linux/macOS), então não precisa instalá-la separadamente.

---
## Demonstração Visual

### 1 Janela Inicial
Rode o script principal em seu terminal ou diretamente no VS Code:
keymonitor.py
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
