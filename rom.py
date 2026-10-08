from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes
from worlds.AutoWorld import World
import os
import hashlib
from settings import get_settings
import struct
import Utils

BubBobHash = [ "9f08eff58f4727d0d172ca008d3894e2", ]

PlayerNameAddress = 0x1BEE0

APidentifierAddress = 0x01BED0
APidentifier = ( 0x42, 0x55, 0x42, 0x42, 0x4F, 0x42, 0x41, 0x50, )

BounceBlockAddress1 = 0x01BF40
BounceBlockAddress2 = 0x017f40
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

    for j, b in enumerate(world.playerName):
        patch.write_token(APTokenTypes.WRITE, PlayerNameAddress + j, struct.pack("<B", b))
    for j, b in enumerate(APidentifier):
        patch.write_token(APTokenTypes.WRITE, APidentifierAddress + j, struct.pack("<B", b))
    for j, b in enumerate(BounceBlockCode):
        patch.write_token(APTokenTypes.WRITE, BounceBlockAddress1 + j, struct.pack("<B", b))
        patch.write_token(APTokenTypes.WRITE, BounceBlockAddress2 + j, struct.pack("<B", b))
    for j, b in enumerate(BounceBlockJumpCode):
        patch.write_token(APTokenTypes.WRITE, BounceBlockJump + j, struct.pack("<B", b))
    for j, b in enumerate(LastLevelCode):
        patch.write_token(APTokenTypes.WRITE, LastLevelAddress + j, struct.pack("<B", b))
    for j, b in enumerate(LastLevelJumpCode):
        patch.write_token(APTokenTypes.WRITE, LastLevelJump + j, struct.pack("<B", b))
    for j, b in enumerate(StartingLivesCode):
        patch.write_token(APTokenTypes.WRITE, StartingLivesAddress + j, struct.pack("<B", b))
    for j, b in enumerate(StartingLivesJumpCode):
        patch.write_token(APTokenTypes.WRITE, StartingLivesJump1 + j, struct.pack("<B", b))
        patch.write_token(APTokenTypes.WRITE, StartingLivesJump2 + j, struct.pack("<B", b))

    patch.write_file("token_data.bin", patch.get_token_binary())

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