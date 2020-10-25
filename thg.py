from THG.View.Interpreter.THGInterpreter import ThgInterpreter


class THG(ThgInterpreter):
    """
    ponto de entrada para iniciar o thg

    """

    def run(self):
        self.cmdloop()


if __name__ == '__main__':
    app = THG()
    app.run()
