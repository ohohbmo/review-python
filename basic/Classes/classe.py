class Task():
    def __init__(self, id='001', tipo='base'):
        self.id=id
        self.tipo=tipo
        self.dic_obj={
            #'id':[relacao, local]
        }
    def print_nome(self):
        print(self.nome)

class TaskRecurrent(Task):
    def loop(self):
        for x in [1,2, 3, self.nome]:
            print(x)



tarefa_001 = Task('111')
tarefa_001.print_nome()

tarefa_002 = TaskRecurrent('222')
tarefa_002.print_nome()
tarefa_002.loop()

