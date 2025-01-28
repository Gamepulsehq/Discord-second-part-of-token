import aiosonic
import codecs
import time
import datetime
import asyncio
import base64

class SecondPiece():
    def __init__(self, token: str, bot: bool = False) -> None:
        self.api = "https://discord.com/api/v10/"
        self.headers = {"Authorization": token if not bot else "Bot %s" % token}
        self.loop = asyncio.get_event_loop()

    async def id_to_second_piece(self, id: str) -> str:
        # Fetch user data from Discord API
        x = await aiosonic.HTTPClient().get(f"{self.api}users/{id}", headers=self.headers)
        y = await x.json()

        # Convert user ID to Unix timestamp
        bi = str(bin(int(id))).replace("0b", "")
        m = 0x40 - len(bi)
        unixbin = bi[:0x2a - m]
        unix = int(unixbin, 2) + 0x14aa2cab000
        unixfortoken = (unix - 0x14aa2cab000) + 0x4d1e6e80

        # Get the date time for the Unix timestamp
        user_datetime = datetime.datetime.utcfromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S")

        # Encode Unix timestamp to base64 (simplified)
        b64unix = base64.urlsafe_b64encode(unix.to_bytes((unix.bit_length() + 7) // 8, 'big')).decode().rstrip("=")

        # Print the output
        print(f"""
User: {y['username']}#{y['discriminator']}
Unix: {unix}
Second Piece of Token: {b64unix}
Date/Time: {user_datetime}
""")

    def between_callback(self, id):
        return self.loop.run_until_complete(self.id_to_second_piece(id))

# Main program to use the class
if __name__ == "__main__":
    uwu = SecondPiece(input("Token > "))
    import os
    os.system("cls" if os.name == "nt" else "clear")  # No DeprecationWarning
    uwu.between_callback(input("User ID > "))
