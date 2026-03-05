from .agent import agent


def main():
    print("欢迎使用智能旅游助手！\n")
    print("Welcome to Intelligent Travel Assistant!\n")

    while True:
        user_input = input("请输入您的问题（输入'退出'结束）：")
        if user_input.lower() in ["退出", "exit", "quit"]:
            print("感谢使用智能旅游助手，再见！")
            print("Thank you for using Intelligent Travel Assistant, goodbye!")
            break

        try:
            response = agent.run(user_input)
            print(f"助手回答：{response}\n")
        except Exception as e:
            print(f"Error: {str(e)}\n")


if __name__ == "__main__":
    main()
