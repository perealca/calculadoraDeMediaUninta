ap1 = float(input("Digite a nota da AP1: "))
ap1a = float(input("Digite a nota da AP1A: "))

ap2 = float(input("Digite a nota da AP2: "))
ap2a = float(input("Digite a nota da AP2A: "))

ap3 = float(input("Digite a nota da AP3: "))
ap3d = float(input("Digite a nota da AP3D: "))

media_final = (
    (ap1 * 0.1) +
    (ap1a * 0.1) +
    (ap2 * 0.1) +
    (ap2a * 0.1) +
    (ap3 * 0.4) +
    (ap3d * 0.2)
)

print(f"Média final: {media_final:.2f}")
