import argparse
import os
import discord


from article_generator import ArticleGeneratorAI21, ArticleGeneratorOpenAI


class Config:
    discord_bot_token = os.environ.get("DISCORD_BOT_TOKEN_AMAGA")
    main_commands = ["Is it true that ", "is it true that "]


class Client(discord.Client):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.config = Config()

    async def on_ready(self):
        print(f"Discord client started and logged on as {self.user}!")

    async def on_message(self, message):
        # Don't respond to her own messages
        if message.author == self.user:
            return

        # Don't respond if not called by a main_command
        for main_command in self.config.main_commands:
            if message.content.startswith(main_command):
                text = message.content[len(main_command) :].strip()
                command = main_command
                break
        else:
            return

        text = text.replace("?", "").strip()

        if command == "Is it true that ":
            refute = False
        elif command == "is it true that ":
            refute = True
        else:
            return

        ag = ArticleGeneratorAI21()
        article = ag.generate_article("j1-jumbo", text, refute)

        response = "From an article of the Internet: \n"
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


def main():
    client = Client(intents=get_intents())
    client.run(client.config.discord_bot_token)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AMAGA bot for discord.")
    args = parser.parse_args()
    main(**vars(args))
