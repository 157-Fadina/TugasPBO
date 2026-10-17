teman_sekelas = {"Alice", "Bob", "Charlie", "David", "Eva"}
teman_dekat = {"Alice", "Charlie", "Frank", "Grace", "Ivy"}

teman_sekelas.add("Andi Timtan")
teman_dekat.add("Ridho Dendeng")

print(teman_sekelas)
print(teman_dekat)

irisan = teman_sekelas.intersection(teman_dekat)

perbedaan = teman_sekelas.difference(teman_dekat)

print("\nIrisan:", irisan)
print("Perbedaan:", perbedaan)