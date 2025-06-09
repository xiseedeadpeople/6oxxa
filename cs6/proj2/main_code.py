class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Server:
    __ip_counter = 1

    def __init__(self):
        self.ip = Server.__ip_counter
        Server.__ip_counter += 1
        self.buffer = []
        self.router = None

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        received = self.buffer[:]
        self.buffer.clear()
        return received

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers[server.get_ip()] = server
        server.router = self

    def unlink(self, server):
        ip = server.get_ip()
        if ip in self.servers:
            del self.servers[ip]
        server.router = None

    def send_data(self):
        for data in self.buffer:
            if data.ip in self.servers:
                self.servers[data.ip].buffer.append(data)
        self.buffer.clear()


# тест тз
router = Router()
sv_from = Server()
sv_from2 = Server()

router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())

sv_to = Server()
router.link(sv_to)

sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))

router.send_data()

msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"
assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"
assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"
assert hasattr(router, 'buffer') and hasattr(sv_to, 'buffer'), "в объектах Router и/или Server отсутствует атрибут buffer"

router.unlink(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
msg_lst_to = sv_to.get_data()

assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"
