import argparse
import os
import discord


from article_generator import ArticleGeneratorAI21, ArticleGeneratorOpenAI


class Config:
    discord_bot_token = os.environ.get("DISCORD_BOT_TOKEN_AMAGA")
    main_commands = [
        "is it true that",
        "tell me if",
        "amaga:",
        "amaga :",
        "can you confirm that",
    ]


class Client(discord.Client):
    def __init__(self, company, model, *args, **kw):
        super().__init__(*args, **kw)
        self.config = Config()
        self.config.company = company
        self.config.model = model

    async def on_ready(self):
        print(f"Discord client started and logged on as {self.user}!")

    async def on_message(self, message):
        # Don't respond to her own messages
        if message.author == self.user:
            return

        # Don't respond if not called by a main_command
        for main_command in self.config.main_commands:
            if message.content.lower().strip().startswith(main_command):
                text = message.content[len(main_command) :].strip()
                command = main_command
                refute = message.content.strip()[0].islower()
                break
        else:
            return

        text = text.replace("?", "").strip()

        if self.config.company == "openai":
            ag = ArticleGeneratorOpenAI()
        elif self.config.company == "ai21":
            ag = ArticleGeneratorAI21()

        article = ag.generate_article(self.config.model, text, refute)

        response = (
            f"To answer {message.author}, here is an article from the Internet: \n"
        )
        response += "> " + "\n> ".join(article.split("\n"))
        await message.channel.send(response)
        return


def get_intents():
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False
    intents.messages = True
    intents.guilds = True
    intents.reactions = True
    return intents


def main(company, model):
    client = Client(company, model, intents=get_intents())
    client.run(client.config.discord_bot_token)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AMAGA bot for discord.")
    parser.add_argument(
        "--company",
        "-c",
        type=str,
        help="Company",
        choices=["openai", "ai21"],
        default="openai",
    )
    parser.add_argument(
        "--model",
        "-m",
        type=str,
        help="Model",
    )
    args = parser.parse_args()
    main(**vars(args))
