-- Dados para criar a tabela no banco de dados SQL Server
CREATE TABLE CLIENTES (
    [ID] [int] IDENTITY(1,1) NOT NULL,
	[cliNome] [varchar](50) NULL,
	[cliIdade] [int] NULL,
	[cliProfissao] [varchar](50) NULL,
)