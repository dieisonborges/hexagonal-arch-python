
# Order Calculator: Comparando Arquiteturas

Este repositório demonstra a diferença entre uma aplicação construída com e sem a **Arquitetura Hexagonal**. O objetivo é destacar como o design pode impactar na separação de responsabilidades, flexibilidade, manutenibilidade e testabilidade do código.

# Order Calculator

O sistema "Order Calculator" é uma aplicação simples que calcula o total de pedidos com base em uma lista de itens (preço e quantidade). Ele foi desenvolvido com o objetivo de demonstrar as diferenças práticas entre um design tradicional, onde a lógica de negócios está diretamente acoplada a detalhes técnicos, e a Arquitetura Hexagonal, que promove a separação de responsabilidades, flexibilidade e facilidade de manutenção, isolando o núcleo do sistema das dependências externas, como banco de dados e interface.

---

## Estrutura do Repositório

```plaintext
.
├── hexagonal/            # Exemplo utilizando Arquitetura Hexagonal
│   ├── domain/           # Núcleo da aplicação (lógica de negócio)
│   │   └── order_calculator.py
│   ├── ports/            # Interfaces (contratos de comunicação)
│   │   └── order_repository.py
│   ├── adapters/         # Implementações concretas para banco e interface
│   │   ├── sqlite_order_repository.py
│   │   └── console_interface.py
│   └── main.py           # Arquivo principal que conecta tudo
│
├── non-hexagonal/        # Exemplo sem Arquitetura Hexagonal
│   ├── orders_service.py # Lógica diretamente integrada com banco
│   └── interface.py      # Interação com o usuário final
│
└── README.md             # Este arquivo
```

---

## Hexagonal Architecture (`hexagonal/`)

### [domain/order_calculator.py](hexagonal/domain/order_calculator.py)
Este arquivo contém a **lógica principal do negócio**, responsável por calcular o total de um pedido a partir de uma lista de itens (preço e quantidade). Esta lógica é completamente independente de detalhes técnicos, como banco de dados ou interface.

---

### [ports/order_repository.py](hexagonal/ports/order_repository.py)
Define a interface para buscar itens de um pedido. Este contrato é implementado pelos adaptadores externos, garantindo que o domínio nunca dependa diretamente da lógica de acesso a dados.

---

### [adapters/sqlite_order_repository.py](hexagonal/adapters/sqlite_order_repository.py)
Adaptador que implementa a interface definida em `order_repository.py`. Ele conecta-se ao banco de dados SQLite para buscar os itens de um pedido.

---

### [adapters/console_interface.py](hexagonal/adapters/console_interface.py)
Adaptador que conecta o domínio ao usuário final. Este arquivo exibe o total do pedido no terminal, usando a lógica de negócio e o adaptador de banco.

---

### [main.py](hexagonal/main.py)
Arquivo principal que **conecta todas as partes** da aplicação. Ele configura o adaptador do banco de dados e chama a interface para exibir o total do pedido. É aqui que o sistema é iniciado.

---

## Non-Hexagonal Architecture (`non-hexagonal/`)

### [orders_service.py](non-hexagonal/orders_service.py)
Este arquivo combina a lógica de negócios com o acesso ao banco de dados. Ele calcula o total do pedido diretamente, mas está fortemente acoplado ao SQLite, dificultando a manutenção e os testes.

---

### [interface.py](non-hexagonal/interface.py)
Arquivo que conecta a lógica de negócios ao usuário final. Ele chama diretamente o `orders_service.py` para calcular o total e exibe o resultado no terminal.

---

## Como Executar

### Pré-requisitos
- Python 3.8+
- SQLite3

### Configurando o Banco de Dados
Antes de rodar os exemplos, crie um banco de dados SQLite com os seguintes comandos:

1. Crie um arquivo SQL (`create_db.sql`) com o seguinte conteúdo:
   ```sql
   CREATE TABLE order_items (
       id INTEGER PRIMARY KEY,
       order_id INTEGER,
       price REAL,
       quantity INTEGER
   );

   INSERT INTO order_items (order_id, price, quantity) VALUES
   (1, 10.0, 2),
   (1, 15.0, 1),
   (2, 20.0, 3);
   ```

2. Execute o script para criar o banco:
   ```bash
   sqlite3 orders.db < create_db.sql
   ```

### Rodando o Exemplo com Arquitetura Hexagonal
1. Navegue para a pasta `hexagonal/`:
   ```bash
   cd hexagonal
   ```
2. Execute o arquivo principal:
   ```bash
   python main.py
   ```

### Rodando o Exemplo Sem Arquitetura Hexagonal
1. Navegue para a pasta `non-hexagonal/`:
   ```bash
   cd non-hexagonal
   ```
2. Execute o arquivo da interface:
   ```bash
   python interface.py
   ```

---

## Contribuindo

Fique à vontade para abrir issues ou enviar pull requests. Este repositório é um ponto de partida para quem quer entender e aplicar a Arquitetura Hexagonal.

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.