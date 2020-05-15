from THG.View.Interpreter.THGInterpreter import ThgInterpreter


class THG(ThgInterpreter):
    def run(self):
        self.cmdloop()


if __name__ == '__main__':
    app = THG()
    app.run()
