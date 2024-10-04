import discord
from discord.ext import commands
from discord.ui import Button, View
class WelcomeView(View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Ver serviços", style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Obtenha o canal onde o botão foi clicado
        channel = interaction.channel

        # Verifique se o usuário já tem um canal privado
        existing_channel = discord.utils.get(channel.guild.text_channels, name=f'boost-{interaction.user.name.lower()}')
        if existing_channel:
            await interaction.response.send_message("Você já tem um canal privado.", ephemeral=True)
            return

        # Obtém os cargos Staff e Administrador
        staff_role = discord.utils.get(interaction.guild.roles, name="CEO")
        admin_role = discord.utils.get(interaction.guild.roles, name="Comercial")
        coach_role = discord.utils.get(interaction.guild.roles, name="Bot")

        # Crie um novo canal apenas para o usuário
        category = channel.category
        new_channel = await channel.guild.create_text_channel(
            name=f'teste-{interaction.user.name.lower()}',
            category=category,
            overwrites={
                interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                staff_role: discord.PermissionOverwrite(read_messages=True, send_messages=True) if staff_role else discord.PermissionOverwrite(),
                admin_role: discord.PermissionOverwrite(read_messages=True, send_messages=True) if admin_role else discord.PermissionOverwrite(),
                coach_role: discord.PermissionOverwrite(read_messages=True, send_messages=True) if coach_role else discord.PermissionOverwrite()
            }
        )

        messages = "BOT EM DESENVOLVIMENTO"

        await new_channel.send(messages)

        await interaction.response.send_message(f"Seu canal foi criado! Acesse ele para ter mais informações: {new_channel.mention}", ephemeral=True)