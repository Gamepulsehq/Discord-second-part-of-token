import aiosonic; import codecs; import time; import datetime; import asyncio;

# Note, this doesn't work if somebody has changed their passwords once

class SecondPiece():
    def __init__(self, token:str, bot:bool=False) -> None:
        self.api = "https://discord.com/api/v10/";
        self.headers = {"Authorization": token if not bot else "Bot %s" % token};
        self.loop = asyncio.get_event_loop();
        pass;
    async def id_to_second_piece(self, id:str) -> str:
        x = await aiosonic.HTTPClient().get("%susers/%s" % (self.api, id), headers=self.headers); y = await x.json();
        bi = str(bin(int(id))).replace("0b", ""); m = 0x40-len(bi); unixbin = bi[0x0:0x2a-m];
        unix = int(unixbin, 2)+0x14aa2cab000; unixfortoken = (unix-0x14aa2cab000)+0x4d1e6e80;
        #datetime.utcfromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S");
        b64unix = str(codecs.encode(codecs.decode(str(hex((int(str(unix)[0:10])))).replace("0x", ""), "hex"), "base64").decode()).replace("==", "");
        print("""
User: %s
Unix: %s
Second Piece of Token: %s
""" % (y['username']+y['discriminator'], unix, b64unix));
    def between_callback(self, id):
        return self.loop.run_until_complete(self.id_to_second_piece(id));

uwu = SecondPiece(input("Token > "));
import os; os.system("cls" if os.name == "nt" else "clear"); # No DeprecationWarning
uwu.between_callback(input("User ID > "));
