import services.database as db
import models.Cliente as cliente


def incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO CLIENTES (cliNome, cliIdade, cliProfissao) VALUES (?,?,?)""",
    cliente.nome, cliente.idade, cliente.profissao).rowcount
    db.cnxn.commit()
    print(f'Dados Inseridos com Sucesso: {str(count)}')


def excluir(id):
    db.cursor.execute("""
    DELETE FROM CLIENTES WHERE ID = ? """,
    id).rowcount
    db.cnxn.commit()
    # print(f'{id}: Cliente Deletado com Sucesso: {str(count)}')


# Mostrar dados de todos os clientes dentro do banco.
def selecionar_todos():
    db.cursor.execute("SELECT * FROM CLIENTES")
    costumer_list = []

    for row in db.cursor.fetchall():
        costumer_list.append(cliente.Cliente(row[0], row[1], row[2], row[3]))

    return costumer_list    