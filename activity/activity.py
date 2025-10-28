import ifcopenshell
ifc_file = ifcopenshell.open("AC20-FZK-Haus.ifc")
print("IFC file loaded:", ifc_file.schema)

stairs = ifc_file.by_type("IFCStair")
print(f"Number of stairs: {len(stairs)}")
for stair in stairs:
    print(stair.Name, stair.GlobalId)

slabs = ifc_file.by_type("IFCSlab")
print(f"Number of slabs: {len(slabs)}")
for slab in slabs:
    print(slab.Name, slab.GlobalId)

slabs = ifc_file.by_type("IFCSlab")
for i, slab in enumerate(slabs, 1):
    slab.Name = f"Renamed_Slab_{i}"
    print(f"Updated slab: {slab.GlobalId} → {slab.Name}")

project = ifc_file.by_type("IfcProject")[0]
for site in project.IsDecomposedBy[0].RelatedObjects:
    for building in site.IsDecomposedBy[0].RelatedObjects:
        for storey in building.IsDecomposedBy[0].RelatedObjects:
            print("Storey", storey.Name, "Elevation", storey.Elevation)


types = set(el.is_a() for el in ifc_file)
types = set(el.is_a() for el in ifc_file)
print("Object types in file:", types)


ifc_file.write("AC20-FZK-Haus_renamed.ifc")