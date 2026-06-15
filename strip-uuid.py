import sys


def zero_macho_uuid(filepath):
    print(f"Nettoyage de l'UUID pour : {filepath}")
    with open(filepath, "rb") as f:
        data = bytearray(f.read())

    # Pattern magique de LC_UUID en little-endian (arm64)
    # cmd (0x1b) sur 4 octets + cmdsize (24 octets) sur 4 octets
    pattern = b"\x1b\x00\x00\x00\x18\x00\x00\x00"

    idx = data.find(pattern)
    if idx != -1:
        uuid_offset = idx + 8
        # On remplace les 16 octets de l'UUID par des zéros
        data[uuid_offset : uuid_offset + 16] = b"\x00" * 16

        with open(filepath, "wb") as f:
            f.write(data)
        print("-> LC_UUID mis à zéro avec succès.")
    else:
        print("-> Alerte : Aucun bloc LC_UUID trouvé dans ce binaire.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 strip-uuid.py <chemin_du_binaire>")
    else:
        zero_macho_uuid(sys.argv[1])
