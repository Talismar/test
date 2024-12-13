import os


def main():
    message = os.getenv("INPUT_MESSAGE", "Olá, mundo!")
    print(f"Mensagem recebida: {message}")


if __name__ == "__main__":
    main()
