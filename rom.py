from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes
from worlds.AutoWorld import World
import os
import hashlib
from settings import get_settings
import struct
import Utils

BubBobHash = [ "B220CB06A7E23C55A982FD75B32554D0BF511B7B", ]

PlayerNameAddress = 0x1BEE0

APidentifierAddress = 0x1800
APidentifier = ( 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, )

BounceBlockAddress = 0x01BF40
BounceBlockCode = (	0x8d, 0xd2, 0x01, 0xad, 0xd1, 0x01, 0xf0, 0x07, 0xad, 0xd2, 0x01, 0x20, 0x6b, 0xd3, 0x60, 0xad, 0xd2, 0x01, 0x60, )

BounceBlockJump = 0x01D35A
BounceBlockJumpCode = ( 0x20, 0x30, 0xbf, )

LastLevelAddress = 0x01BFA0
LastLevelCode = ( 0x8d, 0x00, 0x04, 0xad, 0x01, 0x04, 0x8d, 0xd3, 0x01, 0xad, 0x00, 0x04, 0x60, )

LastLevelJump = 0x01CB3E
LastLevelJumpCode = ( 0x20, 0x90, 0xbf, )

StartingLivesAddress = 0x01FFC6
StartingLivesCode = ( 0xae, 0xd0, 0x01, 0xad, 0x02, 0x04, 0x60, )

StartingLivesJump1 = 0x1CA47
StartingLivesJump2 = 0x1432E
StartingLivesJumpCode = ( 0x20, 0xb6, 0xff, 0xea, 0xea, )

class BubbleBobbleProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Bubble Bobble"
    hash = BubBobHash
    patch_file_ending = ".apbubbob"
    result_file_ending = ".nes"

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()

def write_tokens(world:World, patch:BubbleBobbleProcedurePatch):
    AllChanges = [
        [ APidentifierAddress, APidentifier, ],
        [ PlayerNameAddress, world.playerName, ],
        [ BounceBlockAddress, BounceBlockCode, ],
        [ BounceBlockJump, BounceBlockCode, ],
        [ LastLevelAddress, LastLevelCode, ],
        [ LastLevelJump, LastLevelJumpCode, ],
        [ StartingLivesAddress, StartingLivesCode, ],
        [ StartingLivesJump1, StartingLivesJumpCode, ],
        [ StartingLivesJump2, StartingLivesJumpCode, ],
    ]
    for x, y in AllChanges:
        for j, b in enumerate(y):
            patch.write_token(APTokenTypes.WRITE, x + j, struct.pack("<B", b))

def get_base_rom_bytes(file_name: str ="") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path(file_name)
        base_rom_bytes = bytes(Utils.read_snes_rom(open(file_name, "rb"), False))
        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        md5hash = basemd5.hexdigest()
        if md5hash not in BubBobHash:
            raise Exception("ROM is not US version of Bubble Bobble")
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes

def get_base_rom_path(file_name: str="")-> str:
    if not file_name:
        file_name = get_settings().bubble_bobble_settings.rom_file
    if not os.path.exists(file_name):
        file_name= Utils.user_path(file_name)
    return file_name