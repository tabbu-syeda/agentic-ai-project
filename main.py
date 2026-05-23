from app.services.llmservice import ask_llm


if __name__ == "__main__":
    response = ask_llm(
        "Explain AI agents in simple words."
    )

    print("\n")
    print(response)