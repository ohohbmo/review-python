class Task():
    def __init__(self, id='001', sujeito='manual'):
        self.id = id
        self.sujeito = sujeito
        self.raiz = raiz
        self.dic_ = {
            # 'id':[relacao, local]
        }

    def get_id(self):
        return self.id

    def print_id(self):
        print(self.get_id())


class TaskRecurrent(Task):
    def loop(self):
        for x in [1, 2, 3, self.nome]:
            print(x)
